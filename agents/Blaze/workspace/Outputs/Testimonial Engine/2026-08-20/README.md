# Limitless Club Testimonial Engine

**Prepared by:** Blaze  
**Source:** `dropbox-jedienterprise:Limitless Club/All Reviews`  
**Inventory:** 230 videos · 76.12 GiB · largest file 12.29 GiB

## Mission

Create a complete, traceable testimonial corpus and turn verified customer proof into new ad and sales assets without filling the Mac’s disk or inventing claims.

## Canonical transcription workflow

1. Read source metadata from `inventory.csv` / `inventory.json`.
2. Download one Dropbox video into `spool/`.
3. Extract 16 kHz mono FLAC with ffmpeg.
4. Delete the temporary local video after audio extraction succeeds.
5. Transcribe locally with `mlx-community/whisper-large-v3-mlx`.
6. Save `transcript.json`, `.txt`, `.srt`, `.vtt`, and `source.json`.
7. Validate text, timestamps, JSON structure, and artifact hashes.
8. Write `COMPLETE.json`.
9. Revalidate checksums, then delete the temporary local FLAC.
10. Mark source complete in `pipeline.sqlite3`.

Dropbox originals are read-only and are never deleted by this pipeline.

## Commands

```bash
cd "/Users/ultrafriday/Documents/Limitless OS/Agents/Blaze/Outputs/Testimonial Engine/2026-08-20"
/usr/bin/python3 testimonial_pipeline.py status
/usr/bin/python3 testimonial_pipeline.py run
python3 build_corpus.py
python3 -m unittest -v test_testimonial_pipeline.py
```

## Output map

- `inventory.csv`, `inventory.json` — complete source manifest
- `pipeline.sqlite3` — resumable source state
- `transcripts/<source_id>/` — canonical ASR artifacts and checksum marker
- `transcripts-turbo-pilot/` — non-canonical calibration pilot
- `corpus/source_index.csv` — searchable video index
- `corpus/segments.jsonl` — timestamped segment ledger
- `corpus/proof_candidates.jsonl` — heuristic review queue
- `corpus/low_content.json` — empty/non-testimonial candidates
- `corpus/all_transcripts.md` — combined corpus
- `proof-system/` — taxonomy, claim schema, and ad-asset templates
- `mining/` — semantic claim extraction batches
- `architecture/` — implementation and QA architecture

## Publication gates

Machine transcripts are discovery artifacts, not final legal proof. Before any public ad:

- Human-check the exact video/audio against the quote and timecode.
- Confirm customer identity and paid-ad usage permission.
- Preserve qualifiers, negation, numbers, and context.
- Review quantified, financial, or atypical results.
- Get Jet’s approval before publishing or scheduling.

## Model calibration

The cached turbo model was fast but made avoidable Thai substitutions. Full MLX `large-v3` materially improved Thai transcription and is the canonical model. Names and ambiguous phrases still require human verification.
