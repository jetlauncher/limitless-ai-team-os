# Hermes Weekly Audit Improvements — Phase 1 Build Plan

Date: 2026-05-24
Owner: Kelly / Hermes

## What is live now

### 1. Cron health digest script

- Script: `~/.hermes/scripts/hermes_cron_health_digest.py`
- State: `~/.hermes/state/cron_health/latest.json`
- Reports: `~/Documents/Obsidian Vault/Agents/Shared Memory/Ops/Cron Health/YYYY-MM-DD-cron-health-digest.md`
- Scheduled job: `655dd227f390` / `hermes-cron-health-digest`
- Schedule: `10 8 * * *`
- Delivery: origin, no-agent. It prints a concise alert only when issues/noisy profiles are found.

First verified run on 2026-05-24:

- Scanned 55 jobs.
- Active jobs: 48.
- Issue jobs found: 32.
- Noisy output profiles: 4.
- Report path: `~/Documents/Obsidian Vault/Agents/Shared Memory/Ops/Cron Health/2026-05-24-cron-health-digest.md`

### 2. P0 skills created

- `youtube-oauth-upload-ops`
- `agent-handoff-and-inbox-system`
- `qwen-memory-hygiene-and-archive`
- `notion-iris-content-pipeline`

## Next build queue

### P0 fixes

1. Fix Airtable hourly snapshot so HTTP 401 exits nonzero instead of producing green-but-broken output.
2. Move workspace/personal artifact scanner state JSON out of Obsidian/iCloud paths and into `~/.hermes/state/`.
3. Audit and fix profile cron delivery targets where `deliver=discord` is unresolved.
4. Create OAuth/token preflight script for Gmail, GSC, Airtable, Todoist, YouTube, and Ahrefs.

### P1 builds

1. Build Signal X Radar Ops skill and source fallback script.
2. Build OpenClaw Legacy Migration skill from the 2026-05-24 triage notes.
3. Build Jet Workshop Deck Factory skill for transcript/research → deck/PDF/archive.
4. Add Qwen fleet SLA dashboard from memory hygiene outputs.

## Operating principle

The next layer is not more content generation. It is making Hermes self-auditing: health digest, handoff standard, approval queue cleanup, skill debt review, and stable source-of-truth reports.
