# Hermes Weekly Agent Audit

**Week audited:** 2026-05-18 → 2026-05-24  
**Prepared for:** Jet / Limitless Club  
**Scope:** Obsidian agent daily logs, Shared Memory, Hermes runtime logs, profile cron jobs, selected output artifacts, and skill coverage.

## Executive Take

This week proves the Hermes fleet has moved beyond “chatbot helpers” into a real multi-agent operating system. The strongest work was not one artifact; it was the emergence of a repeatable loop:

**Signal finds intelligence → Blaze/Kaijeaw turn it into content → Bolt ships systems/sites → Qwen audits memory/health → Hermes coordinates operations → Shared Memory preserves the truth.**

The biggest gap is no longer “we need more agents.” The gap is **workflow integration, health monitoring, and cleanup automation**. The system creates a lot of valuable output, but several flows still depend on Kelly manually rescuing auth, iCloud, Notion, delivery, and queue hygiene.

## Top 10 Improvement Priorities

1. **Cron health digest:** Daily scan of all main/profile cron jobs for failures, delivery errors, stale jobs, and “green-but-broken” outputs.
2. **Credential/OAuth preflight:** Gmail, GSC, Airtable, YouTube, Todoist, Ahrefs checks before dependent jobs run.
3. **Obsidian/iCloud resilience:** Move mutable scanner state out of iCloud-backed vaults; add retry/materialize wrappers for `Resource deadlock avoided`.
4. **Profile delivery audit:** Many profile jobs succeed but fail delivery because `deliver=discord` is unresolved in profile contexts.
5. **Agent handoff system:** Formalize Signal → Blaze → Mission Control → Blotato/Notion/Obsidian with schemas, dedupe, freshness gates, and owner status.
6. **Approval queue cleanup:** Mission Control should stop accumulating drafts without review/reject/schedule reconciliation.
7. **Qwen fleet SLA dashboard:** Turn Qwen hygiene into a dashboard: active agents, stale memory, missing daily notes, broken outputs, and next owner.
8. **Notion/Iris direct fallback skill:** Blaze/Kaijeaw repeatedly used direct Notion REST because the generic skill was unavailable in some contexts.
9. **YouTube OAuth/upload ops skill:** Google Drive → local video → private YouTube upload is important enough to become a dedicated skill.
10. **Weekly audit automation:** This report should become a scheduled artifact, generated automatically from Shared Memory + agent dailies + cron logs.

## This Week by Agent

### Hermes — Command Center / Ops Coordinator

**What happened**
- Coordinated daily briefings, email scans, revenue checks, X monitor reports, evening shutdown notes, and profile operations.
- Created/managed hybrid autoresearch workflow for Qwen/Oracle.
- Created Team Hermes/Nova profile work on NJJ iMac, including Telegram gateway isolation and remote setup notes.
- Worked on OpenClaw legacy inspection/import planning.
- Created Shortcut to AI Expert workshop outline and related presentation/workshop artifacts.
- Prepared a Google Drive video for YouTube upload; upload remains blocked by YouTube OAuth approval.

**Blockers**
- Repeated Obsidian/iCloud `Resource deadlock avoided` during daily note and scan writes.
- Google/Gmail/GSC token revocation broke some dependent jobs.
- Browser automation could not safely click through Google OAuth because the window rendered blank to automation.
- NJJ iMac disk is tight; avoid heavy migrations/model downloads there.

**Automate next**
- Profile bootstrap checklist for new Hermes instances.
- Safe Obsidian append/materializer wrapper.
- OAuth/token health preflight before ops workflows.

### Signal — AI Intelligence / Research Radar

**What happened**
- Ran AI morning briefs, high-signal watches, X high-alert scans, X bookmarks/research, and AI Training Radar.
- Produced daily AI intel reports into Shared Memory.
- Generated Blaze handoffs for high-signal AI/business content.
- Produced AI Week / business-owner podcast docket.

**Blockers**
- X search credits depleted or blocked in some scans.
- Cloudflare blocked/truncated some official sources.
- Notion/Obsidian appends sometimes failed because of iCloud deadlocks.

**Automate next**
- Source-confidence labels: official verified, RSS-only, X-only, Cloudflare-blocked, pending manual confirmation.
- X fallback stack: xurl/app → Grok OAuth → saved captures → Nitter/RSS → official blog/GitHub/HN.
- Auto-generate Blaze handoff cards with hook, implication, source, urgency, and content format.

### Blaze — Creative Production / Social Assets

**What happened**
- Produced daily creative director packages: Thai long-form video ideas, Shorts, LinkedIn/X drafts, Notion pages, and backups.
- Generated approval queue content and scheduled at least one LinkedIn post via Blotato.
- Created Higgsfield UGC product videos and Baoyu comic/infographic visual experiments.
- Started using a fresher “news gate” before content creation.

**Blockers**
- Notion skill unavailable in scheduler contexts; direct API fallback needed.
- Some source backups unreadable via iCloud, creating stale draft risk.
- Approval queue backlog can grow faster than Jet can review.
- Model-cost routing needed for GPT Image vs Nano Banana Pro.

**Automate next**
- Fresh-news gate skill.
- Approval queue de-duplicator and stale-draft sweeper.
- Asset-cost router and Notion block-count verifier.

### Qwen — Memory Hygiene / Fleet Auditor

**What happened**
- Ran repeated memory hygiene audits.
- Produced morning prep and X-Radar outputs.
- Flagged stale/missing agents, empty memory files, missing daily coverage, and output-folder health.
- Checked Todoist queue after token setup, but strict routing found no matching tasks.

**Blockers**
- Todoist routing criteria too strict; likely tasks are missed if not labeled/prefixed correctly.
- Many Qwen outputs accumulate quickly.
- Several agent memory files hit iCloud deadlock.

**Automate next**
- Fleet SLA dashboard.
- Todoist routing recommender: suggest relabeling likely agent tasks.
- Weekly Qwen archive digest that compresses X-Radar + hygiene outputs.

### Bolt — Builder / Deployments / Web Systems

**What happened**
- Built AccRevo pilot simulator, LINE webhook, OCR/adapters, Airtable integration, and approval/audit flows.
- Deployed/verified systems on Vercel.
- Fixed Ahrefs-critical SEO issues on Limitless Club site: sitemap/canonical/metadata/JSON-LD/crawlable fallback content.
- Set up Canva carousel daily intake cron and patched Ahrefs MCP timeout behavior.

**Blockers**
- iCloud-backed repos caused git/object read issues; clean clone workaround needed.
- OAuth flows like Ahrefs need longer timeout and explicit Jet approval.
- Some credentials/API scopes required multiple setup passes.

**Automate next**
- Clean-clone deploy wrapper for iCloud-backed repos.
- OAuth long-timeout MCP helper.
- Reusable webhook QA harness.
- Ahrefs/site-audit repair pipeline.

### Zegna — Taste / Style Curation

**What happened**
- Ran daily curation refreshes with hundreds of style items.
- Archived runs to Notion via direct API when skill unavailable.
- Captured taste signals around heritage utility, refined founder travel, warm architecture, and minimal workspace systems.

**Blockers**
- Several RSS feeds repeatedly fail with 403/404/XML issues.
- Notion direct API fallback is still needed.

**Automate next**
- Feed-health replacement list.
- Weekly taste-memory distiller.
- Notion archive wrapper.

### Kaijeaw — Thai Content / Workshop Extraction

**What happened**
- Ran calendar-aware workshop/Plaud content pipeline in draft-only mode.
- Created Thai threads, carousel outlines, captions, longform drafts, and design copy from transcripts/YouTube/Noiz notes.
- Scheduled Thai Threads posts via Blotato and archived/verified in Notion.
- Created workflow notes for Plaud/Iris fallback.

**Blockers**
- Notion skill unavailable.
- Local iCloud `.docx` copies can be invalid/not zip; fresh rclone copy works better.
- Some visual output still failed Jet’s taste standard.

**Automate next**
- Plaud materializer: rclone copy, validate docx zip, normalize transcript, record freshness.
- Thai style evaluator based on successful Carousel Studio examples.
- Calendar-to-content mapper for missing transcript detection.

### Oracle — Idea Synthesis

**What happened**
- Scanned cross-agent notes and generated idea seed reports.
- Produced ideas such as Founder Knowledge Flywheel, Student Agent OS Idea Lab, Agent Fleet Taste Council, and Opportunity Radar.

**Blockers**
- Ideas remain seeds unless selected and routed.
- Some reads hit iCloud deadlock.

**Automate next**
- Oracle-to-task router with owner, source, and next action.
- Idea lineage/dedupe so recurring ideas evolve instead of resetting.
- Weekly “top 5 ideas worth building.”

### Uncle Chris — Finance / Market Intelligence

**What happened**
- Produced finance/revenue reports and depa/Tax200 application pack.
- Built AI infrastructure market intelligence and financial data source stack.
- Created MRVL/MU stock checker and under-the-radar AI infrastructure screens.
- Restored partial Airtable revenue visibility with local API config.

**Blockers**
- Airtable skill/API availability inconsistent.
- Stripe/bank transfer context still not unified.
- Yahoo quote endpoint rate-limited; fallback data is needed.

**Automate next**
- Finance access preflight.
- Market data fallback ladder with freshness labels.
- AI infra watchlist scoring cron.

### Protocol / Pixel / Codex / Cowork / Nova-NJJ

**Findings**
- Protocol appears event-based or stale; only limited weekly daily-note activity.
- Pixel/Codex/Cowork are repeatedly flagged as stale/missing by hygiene audits.
- Nova-NJJ profile was set up on the NJJ iMac, but no local Obsidian `Agents/Nova-NJJ/` folder exists yet.

**Automate next**
- Decide each agent’s status: active, paused, merged, retired, or remote-only.
- Create Nova-NJJ folder structure: Daily, Memory, Outputs, Protocols.
- Remote health cron for NJJ: gateway status, disk free, profile env, no inherited crons.

## Runtime / Cron Audit

### Active failing jobs

- **Gmail inbox-zero:** token expired/revoked. Split per-account health so one account doesn’t fail the whole job.
- **Weekly GSC gap report:** Search Console token expired/revoked. Add OAuth preflight.
- **Workspace digest scan:** iCloud `Resource deadlock avoided`. Move state JSON outside Obsidian.
- **Personal artifacts scan:** same iCloud/state problem.

### Jobs that are “green but broken”

- **Airtable hourly snapshot:** scheduler says OK, but output shows 401 Unauthorized and 0 records. Script should exit nonzero on 401/missing API key.
- **Limitless X daily report:** sometimes generates fallback content after script failure. Should report data-collection failure plainly instead of synthetic “no signals.”

### Noisy jobs

- **Important email filter:** high output volume; should be silent unless high-priority email exists.
- **Notion-to-Obsidian clone:** every 15 minutes creates many output files; should only notify on deltas/failures.
- **Airtable snapshot:** repeated 401 noise should alert once, then suppress until state changes.

### Profile delivery failures

Many profile crons report `last_status=ok` but have unresolved `deliver=discord`. This affects Blaze, Bolt, Kaijeaw, Oracle, Qwen, Signal, and Zegna profile jobs.

**Fix:** standardize delivery targets:
- `origin` for user-facing briefings.
- `local` for noisy/research jobs.
- explicit valid Discord target only when configured.

## New Skills to Build

### P0 — Build now

1. **youtube-oauth-upload-ops**
   - Drive video download, ffprobe, OAuth, private upload, safe redirect handling.

2. **agent-handoff-and-inbox-system**
   - Signal insight → Blaze package → Mission Control draft → Blotato status → Notion/Obsidian archive.

3. **qwen-memory-hygiene-and-archive**
   - Weekly digest, archive rules, stale memory policy, iCloud handling, “Needs Kelly review” tagging.

4. **notion-iris-content-pipeline**
   - Jet-specific Iris database writes, direct API fallback, draft-only rules, verification, backup URL maps.

### P1 — Build next

5. **signal-x-radar-ops**
   - Source order, X/Grok/Nitter fallback, credit depletion handling, Signal archive, Blaze handoff.

6. **openclaw-legacy-migration**
   - Safe inventory/import rules for NJJ/OpenClaw skills, scripts, profiles, content pipelines.

7. **jet-workshop-deck-factory**
   - Source/transcript/research → workshop outline → deck → PDF handout → archive.

### P2 — Later / patch instead

8. **telegram-bot-token-rotation-and-profile-livecheck**
9. **icloud-obsidian-deadlock-recovery**
10. **mission-control-queue-cleanup**

## Existing Skills to Patch

- **youtube-content:** promote upload/OAuth workflow and private defaults.
- **multi-machine-hermes-ops:** add NJJ disk-pressure warning and remote local-file roots check.
- **xurl:** add `CreditsDepleted` fallback and Signal source order.
- **grok-curated-x-monitoring:** clarify Grok OAuth vs xAI API and Signal output paths.
- **jet-daily-content-engine:** update Signal → Blaze → Mission Control flow and queue-backlog rules.
- **mission-control-approval-workflows:** add weekly queue cleanup and Blotato status reconciliation.
- **notion:** add Jet-specific Iris/Daily Video/Shorts property references and direct REST fallback.
- **obsidian / obsidian-agent-memory-workspace:** add iCloud deadlock handling and state-outside-vault rule.
- **limitless-sales-monitoring:** add weekly business ops radar: revenue, queue, OAuth, agent health.
- **workshop-recap-v2:** add rclone copy for invalid Plaud docx and mobile PDF fallback.

## Missing Workflows

1. **Weekly Agent Review Ritual**
   - Inputs: all daily logs, Shared Memory, cron jobs, Qwen hygiene, Mission Control queue.
   - Output: PDF + top 10 next actions + owner assignments.

2. **Agent Status Registry**
   - Active / paused / retired / remote-only, with expected cadence and owner.

3. **Approval Queue Operating Rhythm**
   - Daily: review top 5 ready drafts.
   - Weekly: reject stale, merge duplicates, reconcile Blotato status.

4. **Auth Renewal Lane**
   - One place for Gmail/GSC/YouTube/Ahrefs/Todoist/Airtable reauth tasks.

5. **Source Artifact Promotion Lane**
   - Raw Plaud/YouTube/Brain Dump/Apple Notes → normalized note → extracted signal → promoted project/concept.

6. **Remote Machine Health Lane**
   - NJJ iMac profile status, disk, gateway, cron isolation, local file roots.

7. **Content Freshness Gate**
   - No new AI-news content without source date, URL, duplicate check, and relevance score.

8. **Skill Debt Review**
   - Weekly patch/create/prune skill list from real failure patterns, not theory.

## Recommended 7-Day Build Plan

### Day 1 — Stop silent failures
- Create cron health digest.
- Fix Airtable snapshot exit status on 401.
- Add delivery-health audit for profile cron jobs.

### Day 2 — Fix auth lane
- Reauthorize Gmail/GSC/Todoist/Ahrefs as needed.
- Build OAuth preflight script.
- Document YouTube upload token flow.

### Day 3 — Stabilize Obsidian/iCloud
- Move scanner state JSON to `~/.hermes/state/`.
- Add retry/materializer wrapper.
- Patch Obsidian skills.

### Day 4 — Clean content operations
- Mission Control approval queue sweep.
- Blotato status reconciliation.
- Add Freshness Gate to Signal/Blaze.

### Day 5 — Build P0 skills
- `youtube-oauth-upload-ops`
- `agent-handoff-and-inbox-system`

### Day 6 — Build Qwen dashboard
- Fleet SLA dashboard from memory hygiene.
- Archive X-Radar outputs into weekly digest.

### Day 7 — Remote/NJJ hardening
- Create Nova-NJJ Obsidian folder structure.
- Add remote gateway/disk health cron.
- Decide stale agents: active, paused, merged, retired.

## Source Highlights

Representative sources audited:

- `/Users/ultrafriday/Documents/Obsidian Vault/Agents/Hermes/Daily/2026-05-18.md` through `2026-05-24.md`
- `/Users/ultrafriday/Documents/Obsidian Vault/Agents/Signal/Daily/2026-05-18*` through `2026-05-24*`
- `/Users/ultrafriday/Documents/Obsidian Vault/Agents/Blaze/Daily/2026-05-18.md` through `2026-05-24.md`
- `/Users/ultrafriday/Documents/Obsidian Vault/Agents/Qwen/Daily/2026-05-18.md` through `2026-05-24.md`
- `/Users/ultrafriday/Documents/Obsidian Vault/Agents/Bolt/Daily/2026-05-18.md` through `2026-05-24.md`
- `/Users/ultrafriday/Documents/Obsidian Vault/Agents/Zegna/Daily/2026-05-18.md` through `2026-05-24.md`
- `/Users/ultrafriday/Documents/Obsidian Vault/Agents/Kaijeaw/Daily/2026-05-18.md` through `2026-05-24.md`
- `/Users/ultrafriday/Documents/Obsidian Vault/Agents/Oracle/Daily/2026-05-19.md` through `2026-05-24.md`
- `/Users/ultrafriday/Documents/Obsidian Vault/Agents/Uncle Chris/Daily/2026-05-18.md` through `2026-05-24.md`
- `/Users/ultrafriday/Documents/Obsidian Vault/Agents/Shared Memory/Daily/2026-05-18.md` through `2026-05-24.md`
- `/Users/ultrafriday/.hermes/cron/jobs.json`
- `/Users/ultrafriday/.hermes/profiles/*/cron/jobs.json`
- `/Users/ultrafriday/.hermes/logs/*`
- `/Users/ultrafriday/.hermes/profiles/*/logs/*`

## Final Recommendation

Do not add more routine content generation until the operating layer is healthier. This week’s work shows the content/research/build agents are productive. The next leverage is to make the system self-auditing:

**One dashboard, one weekly PDF, one health digest, one handoff standard, and one cleanup rhythm.**

That turns Hermes from a powerful set of agents into a dependable AI Team OS.
