# Nightly Workflow Build — Agent Sync Dashboard v0

## Why this helps Jet
Jet can open one local page to see which agents wrote memory today, what changed, and which durable MEMORY.md files need review.

## Built
- Static dashboard: `/Users/ultrafriday/Documents/Limitless OS/Agents/Bolt/Builds/2026-07-20/nightly-agent-sync-dashboard/index.html`
- Machine-readable snapshot: `/Users/ultrafriday/Documents/Limitless OS/Agents/Bolt/Builds/2026-07-20/nightly-agent-sync-dashboard/data.json`
- Generator/sync script: `/Users/ultrafriday/Documents/Limitless OS/Agents/Bolt/Builds/2026-07-20/nightly-agent-sync-dashboard/generate_dashboard.py`
- README: `/Users/ultrafriday/Documents/Limitless OS/Agents/Bolt/Builds/2026-07-20/nightly-agent-sync-dashboard/README.md`

## How to use
Open `index.html` in a browser after the nightly cron. Re-run with:

```bash
python3 '/Users/ultrafriday/Documents/Limitless OS/Agents/Bolt/Builds/2026-07-20/nightly-agent-sync-dashboard/generate_dashboard.py'
```

## Acceptance criteria
- HTML contains valid `<html>` structure.
- `data.json` contains all active/present profile-folder mappings.
- Each mapped agent daily note for 2026-07-20 exists and is non-empty.
- Shared daily note links this build.

## Safety constraints
Local file edits only under `Agents/`; no cron edits, deletes, deploys, messages, payments, or external API writes.

## Suggested Bolt next step
Turn this static v0 into a reusable `nightly-agent-sync-dashboard` CLI that can generate any date and optionally export a PNG/PDF summary for Telegram.
