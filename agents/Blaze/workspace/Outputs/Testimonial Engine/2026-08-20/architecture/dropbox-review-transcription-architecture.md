# Resumable Dropbox Review-Video Transcription Architecture

## 1. Outcomes and non-negotiable invariants

Build a single-host macOS worker that can enumerate a large Dropbox Business corpus, process it in bounded batches, survive crashes/reboots/rate limits, and resume without duplicating accepted work.

Hard invariants:

1. **Dropbox is read-only.** The worker may `lsjson`, `hash`, `cat`, `copyto`, or mount the configured source. It never runs `delete`, `move`, `sync`, `purge`, or writes to the source remote.
2. **One durable identity per source revision.** A changed Dropbox object becomes a new revision; it never silently overwrites an old transcript.
3. **At most one full source video is local per worker** (default concurrency `download=1`, `extract=1`). At most one or two audio chunks are staged per transcription worker.
4. **No local source media deletion before transcript verification and durable artifact commit.** Chunk audio may be deleted earlier only after that chunk's raw response and normalized transcript have both passed chunk QA and been committed.
5. **Raw evidence is immutable.** Provider responses, model/config metadata, source identity, timestamps, and checksums are retained. Reviewed/normalized text is a separate derivative.
6. **No invented quotes.** An ad quote must map to a verified time range and exact text in a retained transcript artifact; rewriting or translating it creates “copy,” not a customer quote.
7. **Every transition is transactional and replayable.** SQLite is the current state; append-only JSONL is the audit trail.

## 2. Recommended architecture

### Control plane

Use a small Python 3 CLI/daemon (`review-transcriber`) with:

- SQLite in WAL mode for assets, revisions, chunks, attempts, leases, artifacts, QA, and cleanup records.
- An append-only JSONL event log for operator-readable traceability.
- `rclone` subprocesses for Dropbox discovery/download.
- `ffprobe`/`ffmpeg` subprocesses for validation and audio extraction.
- Pluggable transcription adapters:
  - `whisper_cpp` for an Apple-Silicon/Metal local baseline.
  - `faster_whisper` where its installed backend benchmarks well on the target Mac.
  - `openai_transcription` (or another API adapter) for high-accuracy/overflow processing.
- A launchd job or manual CLI invocation; duplicate instances are safe because claims use DB leases.

Do not use filenames as primary keys. Use the remote revision identity.

### Data plane

Default reliable path:

1. Inventory remote metadata only.
2. Claim one source revision.
3. Download that one source to `spool/incoming/<asset_id>.partial`.
4. Verify it, then atomically rename to `spool/source/<asset_id>.<ext>`.
5. Probe once and create a deterministic chunk plan.
6. Extract, transcribe, validate, and delete one audio chunk at a time.
7. Assemble and QA the transcript.
8. Commit immutable artifacts.
9. Move local source to a contained trash directory and delete it via the cleanup janitor.

Optional low-disk fast path: `rclone cat remote:path | ffmpeg -i pipe:0 ...`. Use it only after a canary proves the container is streamable. Some MP4/MOV files require seeking (for example when metadata is at the end); pipe failure must automatically fall back to the one-file spool path. Never make stdin streaming the only path.

Optional mount path: an `rclone mount` with a tightly bounded VFS cache can avoid an explicitly managed full file, but the cache may still grow to the source size. Treat the VFS cache as spool media subject to the same containment and cleanup policy; do not assume it is “zero disk.”

## 3. Filesystem layout

All paths are configurable; a safe default under a dedicated volume is:

```text
transcription-workspace/
  state/
    corpus.sqlite3
    events-YYYY-MM.jsonl
    locks/
  manifests/
    inventory-<run_id>.jsonl
    inventory-<run_id>.summary.json
  spool/
    incoming/                 # only *.partial downloads
    source/                   # verified local source; max one per download worker
    chunks/<asset_id>/        # one or two temporary audio chunks
    quarantine/               # failed/corrupt media; never auto-delete immediately
    trash/                    # verified media pending safe unlink
  artifacts/<asset_id>/<revision_id>/
    source.json
    probe.json
    chunk-plan.json
    attempts.jsonl
    raw/<chunk_id>/<attempt_id>.json
    chunks/<chunk_id>.json
    transcript.raw.json
    transcript.raw.txt
    transcript.reviewed.json  # optional, never replaces raw
    transcript.reviewed.txt
    captions.vtt
    qa.json
    provenance.json
    COMPLETE                  # final commit marker, written last
  reports/
    run-<run_id>.json
    exceptions.csv
    quote-ledger.csv
  logs/
```

Keep `state/`, `manifests/`, `artifacts/`, and `reports/` in Time Machine and/or a second durable destination. Media spool is explicitly excluded from backup. Do not store API keys in this tree; read them from Keychain/environment at runtime and redact subprocess output.

## 4. Remote inventory and stable identity

### Discovery

Run metadata-only discovery with `rclone lsjson` recursively, requesting hashes when the Dropbox backend exposes them. Filter a case-insensitive allowlist such as:

```text
.mp4 .mov .m4v .mkv .avi .webm .mts .m2ts .3gp
```

Record all entries, including excluded files and exclusion reasons. Preserve both raw remote path and a display-safe path; never normalize the raw path destructively.

Conceptual discovery command (flags must be verified against the installed rclone version):

```bash
rclone lsjson 'dropbox-business:Limitless Club/Reviews' \
  --recursive --files-only --hash \
  --metadata > inventory.partial.json
```

Rename the inventory atomically only after the command exits zero and the JSON parses. For huge listings, prefer line-oriented ingestion from rclone's supported output/API rather than loading the full list into RAM.

### Revision identity

Persist:

- remote name and root
- raw relative path
- size
- modification time with timezone
- Dropbox content hash (when available)
- remote object ID/revision metadata (when exposed)
- inventory run ID and observed timestamp

Compute:

```text
asset_key   = SHA-256(remote_name + NUL + raw_relative_path)
revision_id = SHA-256(asset_key + NUL + best_revision_token)
```

`best_revision_token` priority:

1. Dropbox revision/object token if stable and exposed;
2. Dropbox content hash + size;
3. size + exact modtime (marked `weak_identity=true`).

If a path's revision identity changes, insert a new revision and mark the old one `SUPERSEDED`; keep old transcript artifacts. A rename may look like a new asset unless Dropbox provides a stable object ID; optional dedupe can link identical content hashes, but do not collapse records destructively.

Before download, re-stat the object. After download, re-stat it again. If the remote size/revision changed during transfer, discard/quarantine the partial file and requeue the new revision.

## 5. SQLite state model

Minimum tables:

```text
assets(asset_key PK, remote, path_raw, first_seen_at, last_seen_at)
revisions(revision_id PK, asset_key FK, size, modtime, remote_hash,
          remote_revision, identity_strength, state, priority, discovered_at)
media_probe(revision_id FK, duration_ms, audio_streams_json, format_json, probe_sha256)
chunks(chunk_id PK, revision_id FK, idx, start_ms, end_ms,
       overlap_before_ms, state, accepted_attempt_id, transcript_sha256)
attempts(attempt_id PK, chunk_id FK, engine, model, model_revision,
         config_json, prompt_sha256, started_at, ended_at, outcome,
         error_class, error_redacted, raw_artifact_path, raw_sha256,
         metrics_json)
artifacts(artifact_id PK, revision_id FK, kind, path, sha256, size, created_at)
qa_checks(check_id PK, target_type, target_id, check_name, status,
          metrics_json, reviewer, reviewed_at)
leases(target_type, target_id, worker_id, expires_at, heartbeat_at, PK(...))
cleanup(cleanup_id PK, revision_id FK, original_path, trash_path,
        required_artifact_sha256, requested_at, moved_at, deleted_at,
        outcome, error_redacted)
runs(run_id PK, command, config_sha256, code_version, host_fingerprint,
     started_at, ended_at, outcome, counts_json)
```

Use foreign keys, transactions, WAL mode, and `busy_timeout`. State changes and the corresponding event-log append should share a durable event ID; on restart, reconcile missing JSONL events from the DB outbox table.

### Revision state machine

```text
DISCOVERED -> CLAIMED -> SOURCE_READY -> PROBED -> CHUNKS_PLANNED
-> TRANSCRIBING -> ASSEMBLED -> QA_PENDING -> VERIFIED -> CLEANED
```

Side states:

```text
FAILED_RETRYABLE, BLOCKED_PERMANENT, QUARANTINED, SUPERSEDED
```

A lease contains an expiration and heartbeat. A crashed worker's expired lease may be reclaimed. Reclaiming never resets accepted chunks; it resumes at the first non-accepted chunk.

## 6. Download and media verification

### Download

Use a destination filename derived only from `asset_id`, never a remote basename. A conceptual command is:

```bash
rclone copyto 'dropbox-business:<raw path>' \
  'spool/incoming/<asset_id>.partial' \
  --retries 5 --low-level-retries 10 --retries-sleep 10s
```

Pass paths as an argument vector from Python, not through `shell=True`; this avoids shell injection and quoting failures. Capture rclone version, exit code, redacted stderr, elapsed time, and bytes.

A restart may need to redownload a partial Dropbox object; resumability is guaranteed at source/chunk level, not promised at byte range. Delete a stale `.partial` only when it is inside the exact incoming root, belongs to an expired/failed attempt, and cannot be mistaken for a verified source.

### Verify source

Gate `SOURCE_READY` on all of:

- rclone exit code zero;
- local regular file, not symlink;
- local size equals post-transfer remote size;
- available remote content hash verifies, preferably via rclone's backend-aware hash/check command; otherwise record hash as unavailable and compute local SHA-256 for traceability;
- `ffprobe` exits zero and reports at least one decodable audio stream;
- duration is positive and within configured sanity bounds.

Atomically rename `.partial` only after these checks. Store the full ffprobe JSON and checksum.

## 7. Deterministic audio chunking

### Audio format

For accuracy-first Thai transcription, extract mono 16 kHz lossless FLAC by default:

```bash
ffmpeg -nostdin -hide_banner -loglevel error \
  -ss <start_seconds> -i '<source>' -t <duration_seconds> \
  -map 0:a:0 -vn -ac 1 -ar 16000 -c:a flac \
  '<chunk>.partial.flac'
```

Then probe the chunk and atomically rename it. If an API/file-size constraint requires smaller payloads, reduce chunk duration. Do not silently switch to aggressively lossy audio. A carefully benchmarked speech codec can be an explicit space-saving profile, not the default accuracy profile.

If the first audio stream is not the desired stream, flag multi-audio media for policy/human review or transcribe each relevant stream separately; never silently merge unrelated tracks.

### Plan

- Default target: 8–12 minute chunks.
- Add 2–5 seconds of deterministic overlap on both sides except at media boundaries.
- Store millisecond integer boundaries in `chunk-plan.json`; never recompute boundaries from floating-point progress after a restart.
- Ensure the encoded chunk stays below the configured API upload ceiling with a safety margin. The ceiling is a provider configuration discovered from current provider docs/tests, not a hard-coded historical constant.
- Use a short canary chunk first for each new engine/model/config combination.

For lowest disk, create one chunk, transcribe it, commit its raw/normalized artifacts, then delete that chunk before extracting the next. For two concurrent API requests, cap staged chunks at two and enforce a workspace byte budget.

### Boundary merge

Keep provider segment/word timestamps when available. Convert chunk-local times to source-global times, then merge overlaps by:

1. timestamp overlap;
2. normalized token-sequence similarity;
3. retaining both versions with a conflict flag if confidence is insufficient.

Never delete text merely because strings are similar. Boundary conflicts go to QA. Preserve the unmerged chunk artifacts permanently.

## 8. Thai/English transcription strategy

### Engine policy

Run a 10–20 video calibration set spanning:

- clean Thai speech;
- Thai/English code-switching;
- noisy phone recordings;
- background music;
- multiple speakers;
- dialects and brand/product names.

Compare at minimum:

1. local high-accuracy Whisper-family model (prefer a `large-v3` class model if the Mac has sufficient memory);
2. a current high-accuracy transcription API;
3. optionally a faster local model for triage.

A Thai-speaking reviewer scores literal accuracy, names/numbers, code-switching, punctuation/readability, and quote usability. Choose the production default from evidence. Do not assume the cheapest or largest model wins on this corpus.

### Language handling

- Start calibration with automatic language detection and with Thai-biased decoding; evaluate both on mixed-language material.
- A forced `th` setting can improve Thai consistency but may damage English names/code-switching. Select per corpus evidence, not globally by intuition.
- Store detected language and confidence per chunk where available.
- Maintain a versioned glossary of known Thai names, English brand terms, products, campaign phrases, and uncommon spellings. Hash the exact prompt/glossary used per attempt.
- Prompts provide spelling/context only. They must not contain desired testimonials or marketing claims, because that can bias generation.
- Use deterministic/low-temperature decoding for the primary evidence transcript. Any second-pass cleanup must be a derivative and cannot overwrite raw text.

### Local options

- **whisper.cpp + Metal:** strong macOS deployment choice; benchmark a pinned build and model checksum. Record CLI flags and model SHA-256.
- **faster-whisper:** useful if it performs well on the target CPU/backend; pin package/model revisions and benchmark real-time factor and memory.
- **smaller model:** only for triage, language detection, or temporary fallback. Do not silently accept it as equivalent to the accuracy model.

### API option

The adapter must:

- query/configure current accepted formats, maximum upload size, response schema, and timestamp support;
- retain the exact raw response and provider request ID;
- record provider/model identifier, request parameters, latency, and usage;
- redact authorization headers and secrets;
- use idempotency keys if the provider supports them;
- treat an ambiguous timeout as “unknown outcome,” then safely retry without accepting two different outputs silently.

If provider timestamps are unavailable, keep chunk-level source times and mark timestamp granularity accordingly. Never synthesize word-level timings.

## 9. Retry, fallback, and backpressure

Classify errors rather than applying one retry loop to everything:

| Class | Examples | Action |
|---|---|---|
| transient remote | timeout, connection reset, 429, 5xx | exponential backoff with full jitter; bounded attempts |
| authentication/config | 401/403, missing remote, invalid model | stop queue; operator action; do not hammer |
| invalid payload | unsupported codec, too large, malformed request | re-extract smaller/compatible chunk once, then block |
| corrupt source | ffprobe/decode failure | one clean redownload, then quarantine |
| local resource | OOM, disk pressure, thermal overload | release lease safely; lower concurrency; retry later |
| low-quality transcript | empty speech despite voiced audio, repetition, timestamp failure | alternate engine/config; then human QA |
| permanent content | no audio stream, zero duration | mark blocked with explicit reason |

Suggested bounds:

- download/API transient attempts: 5 with exponential full-jitter backoff capped at several minutes;
- local engine crash: 2, then alternate configured engine;
- corrupt download: one full redownload;
- QA fallback: one alternate high-accuracy engine, not an unlimited model loop.

After the cap, move to an exception queue. Never mark failed media complete and never delete its source automatically.

Backpressure gates:

- refuse new downloads below `min_free_bytes`;
- workspace hard cap checked before every extraction/download;
- API requests obey provider concurrency/rate headers;
- local concurrency defaults to one high-accuracy model instance;
- a circuit breaker pauses a provider after repeated systemic failures.

## 10. QA gates

### Chunk acceptance gate

All required before deleting chunk audio:

- process/API success and parseable raw response;
- raw response written, flushed, checksummed, and registered in DB;
- normalized chunk JSON written, flushed, checksummed, and registered;
- timestamps monotonic, finite, and within chunk bounds where timestamps exist;
- no empty transcript when audio analysis indicates meaningful voiced content;
- no severe repetition/hallucination heuristic (for example repeated phrase loops);
- detected duration close to planned duration;
- language/script metrics recorded, not necessarily auto-rejected.

On failure, retain the chunk until retry/fallback resolution or move it to quarantine under disk-pressure policy.

### Revision verification gate

All required before `VERIFIED`:

- every planned chunk accepted exactly once;
- merged transcript covers the expected timeline, accounting for overlap and known silence;
- overlap conflicts resolved or explicitly flagged;
- transcript JSON schema validates;
- transcript text is nonempty unless a human confirms “no intelligible speech”;
- source/probe/chunk plan/model config/attempts/QA provenance exists;
- artifact SHA-256 values recompute correctly;
- `COMPLETE` commit marker written last and contains the final provenance manifest checksum;
- no unresolved high-severity QA flags.

### Corpus QA

- Human-review all initial calibration items.
- After launch, review 100% of flagged items plus a random sample from every batch/engine/language/noise stratum.
- Track Thai reviewer corrections, name/number error rate, empty rate, retry rate, real-time factor, cost/minute, and transcript yield.
- If sampled accuracy falls below the agreed threshold, stop cleanup for the affected batch and reprocess; do not merely adjust future batches.

## 11. Quote provenance and ad-asset gate

Create `quote-ledger.csv`/DB records with:

```text
quote_id, revision_id, artifact_sha256, start_ms, end_ms,
verbatim_text, language, speaker_label_if_verified,
review_status, reviewer, reviewed_at, source_remote_path
```

Rules:

1. `verbatim_text` must be an exact substring/token span of an immutable accepted transcript artifact.
2. Start/end must map to real chunk/segment timestamps; if only chunk-level timing exists, label precision as coarse.
3. Human correction is allowed only in `transcript.reviewed.*`, with an edit diff and reviewer identity. The original remains retained.
4. Translation, condensation, grammar polishing, or combined phrases are labeled `adapted_copy`, never “verbatim quote.”
5. Before ad export, verify the quote against source audio/video at the cited time and mark `human_audio_verified=true`.
6. No claim may be generated solely from a summary. Summaries point back to source spans.

This is the primary “no invented quotes” enforcement boundary.

## 12. Safe local cleanup protocol

Cleanup is a separate, least-privilege command. The transcription worker can request cleanup but cannot unlink arbitrary files.

### Preconditions

For a source media path, cleanup requires all of:

- revision state is `VERIFIED`;
- valid `COMPLETE` marker and matching final manifest checksum;
- all required transcript/provenance artifacts exist and match DB checksums;
- no unresolved high-severity QA flags;
- path resolves under the configured `spool/source` root;
- path is a regular file, not a symlink/hard-link surprise;
- filename maps to the exact revision/asset ID;
- file is not open by an active lease;
- remote operations are not part of the cleanup code path.

### Two-phase delete

1. Transactionally create a cleanup request tied to the verified artifact checksum.
2. Recheck containment using file-descriptor-safe/no-follow semantics.
3. Rename the source on the same filesystem into `spool/trash/<revision_id>.<ext>`; log inode/device, size, and time.
4. Mark revision `CLEANUP_PENDING`/trash-moved.
5. Janitor revalidates the transcript artifact and unlinks only that exact trash file.
6. Log deletion outcome and mark `CLEANED`.

Default trash grace can be 24 hours during canary operation. For low-disk production, reduce it or allow immediate janitor deletion only after the pipeline has passed canary QA. A rename does not free disk, so disk-pressure logic may purge only already-verified trash, oldest first. Never purge `incoming`, `source`, or `quarantine` merely to regain space.

Chunk cleanup uses the same containment/no-symlink checks but may occur after chunk acceptance rather than full revision verification. Failed/corrupt source media goes to quarantine with a retention policy and operator report; it is never silently deleted.

Provide dry-run output for every janitor action:

```text
revision_id | local path | bytes | verification checksum | planned action
```

## 13. Operator commands

Proposed CLI:

```bash
review-transcriber doctor
review-transcriber discover --remote dropbox-business --root 'Limitless Club/Reviews'
review-transcriber plan --batch-size 20 --max-source-gb 8
review-transcriber run --batch-size 20 --engine auto
review-transcriber resume
review-transcriber status --by-state
review-transcriber exceptions export
review-transcriber qa sample --batch <run_id>
review-transcriber cleanup --dry-run
review-transcriber cleanup --apply --grace-hours 24
review-transcriber audit --recompute-checksums
```

`doctor` verifies command versions, Dropbox read access, absence of source write actions in config, model files/checksums, API adapter connectivity (without uploading customer data unless explicitly permitted), ffmpeg codecs, SQLite integrity, workspace permissions, and free disk.

## 14. Privacy and security

- Obtain/record authorization to send customer testimonials to a third-party API. Default to local-only until policy allows API use.
- Encrypt the Mac volume (FileVault) and restrict workspace permissions.
- Do not place customer names or remote paths in provider prompts unless needed.
- Configure retention separately for media, raw provider payloads, transcripts, and logs.
- Redact API keys, access tokens, signed URLs, and sensitive headers from logs.
- Use a dedicated read-only Dropbox app/account if Business policy permits.
- Treat transcripts as customer data; durable does not mean indefinite—apply an approved retention schedule.

## 15. Implementation and rollout plan

### Phase 0 — Policy and calibration

- Confirm Dropbox source root and read-only credentials.
- Confirm whether API processing is permitted and in which region/provider.
- Select 10–20 representative, consented videos.
- Define Thai reviewer rubric and minimum acceptance threshold.

### Phase 1 — Inventory-only dry run

- Implement schema/migrations, discovery, revision identity, and reports.
- Run discovery only; compare counts/bytes/extensions against Dropbox UI.
- Verify no source-write-capable rclone command is reachable from the application.

### Phase 2 — One-video canary

- Download/probe/chunk one video.
- Run local and API candidates where permitted.
- Inspect Thai/English transcript manually.
- Crash the worker after download, after one accepted chunk, and before cleanup; confirm exact resume behavior.
- Corrupt a staged chunk and verify retry/quarantine behavior.
- Exercise cleanup dry-run only.

### Phase 3 — 20-video canary

- Process diverse media sequentially.
- Human-review all transcripts and every proposed quote.
- Test disk-pressure gating, 429/5xx simulation, expired lease recovery, duplicate worker claims, source mutation during transfer, and API timeout ambiguity.
- Apply two-phase cleanup only after artifacts pass independent checksum audit.

### Phase 4 — Production batches

- Start with batch size 20 and one local model/download worker.
- Increase API chunk concurrency cautiously; keep download/source concurrency at one unless disk budget proves safe.
- Emit a run report: discovered/new/superseded/verified/cleaned/blocked/retried, source minutes, local runtime, API usage/cost, bytes downloaded/deleted, and QA sample results.
- Stop-the-line on systematic accuracy, provenance, privacy, or cleanup failures.

## 16. Acceptance tests

1. Re-running discovery creates no duplicate revision for unchanged objects.
2. A changed object at the same path creates a new revision and retains old artifacts.
3. Killing the process at every state boundary resumes at the first incomplete idempotent step.
4. Two workers cannot accept the same chunk concurrently; expired leases recover.
5. An accepted chunk is not retranscribed after restart unless explicitly invalidated.
6. An invalid/partial raw provider response never permits chunk deletion.
7. Missing/corrupt transcript artifacts block source cleanup.
8. Cleanup refuses paths outside spool, symlinks, wrong IDs, unverified revisions, and active leases.
9. No code path invokes Dropbox delete/move/sync operations.
10. Pipe-unstreamable MOV/MP4 falls back to bounded local spooling.
11. API payload size overflow triggers smaller deterministic rechunking without losing provenance.
12. Thai/English overlap merge does not silently drop conflicting text.
13. Every exported quote resolves to artifact checksum + source time range and passes human audio verification.
14. SQLite integrity check and artifact checksum audit pass after simulated power loss.

## 17. Configuration sketch

```yaml
source:
  remote: dropbox-business
  root: "Limitless Club/Reviews"
  read_only: true
  extensions: [mp4, mov, m4v, mkv, avi, webm, mts, m2ts, 3gp]

workspace:
  root: "/Volumes/TranscriptionWork/reviews"
  min_free_bytes: 21474836480
  hard_cap_bytes: 107374182400
  download_concurrency: 1
  staged_chunk_limit: 2

chunking:
  target_seconds: 600
  overlap_seconds: 3
  sample_rate: 16000
  channels: 1
  codec: flac
  provider_upload_safety_ratio: 0.85

transcription:
  primary: whisper_cpp
  fallback: api
  language_policy: calibrate_auto_vs_th
  glossary_path: config/glossary-v1.txt
  local_model: large-v3
  temperature: 0

retry:
  transient_max_attempts: 5
  corrupt_redownloads: 1
  local_crash_attempts: 2
  max_backoff_seconds: 300

cleanup:
  source_requires_revision_verified: true
  trash_grace_hours: 24
  quarantine_grace_days: 14
  dry_run_default: true
```

Numeric disk limits are examples; set them from the actual Mac/volume capacity and largest discovered source.

## 18. Version-sensitive checks before implementation

Web retrieval was unavailable while preparing this architecture, so implementation must verify flags, limits, and response formats against the installed tools and current primary documentation rather than treating this plan's conceptual commands as copy/paste guarantees:

- rclone Dropbox backend: https://rclone.org/dropbox/
- `rclone lsjson`: https://rclone.org/commands/rclone_lsjson/
- `rclone copyto`: https://rclone.org/commands/rclone_copyto/
- OpenAI speech-to-text guide: https://platform.openai.com/docs/guides/speech-to-text
- OpenAI Whisper repository: https://github.com/openai/whisper
- FFmpeg documentation: https://ffmpeg.org/ffmpeg.html

Pin and record actual versions in every run. Run `rclone help`, `rclone backend features <remote>:`, `ffmpeg -version`, `ffprobe -version`, and each local engine's version command during `doctor`; store outputs in the run manifest.
