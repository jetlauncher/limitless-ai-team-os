# Nightly Workflow Build — Nightly Agent Sync Dashboard

## Why this helps Jet
The nightly sync previously produced notes/logs but no fast visual control-room. This v0 gives Jet/Kelly/Bolt one local HTML page to confirm agent memory coverage and spot missing/partial notes.

## Built
- `Builds/2026-07-01/nightly-agent-sync-dashboard/index.html`
- `Builds/2026-07-01/nightly-agent-sync-dashboard/build_summary.json`
- `Builds/2026-07-01/nightly-agent-sync-dashboard/README.md`

## How to open/use
Open `index.html` in a browser, then review any yellow `needs_review` rows and follow the daily-note file paths into Obsidian.

## Acceptance criteria
- HTML file exists and contains a valid `<html>` structure.
- JSON contains agent records for all present profile workspaces.
- Shared daily note links to the artifact.
- No external side effects were used.

## Safety constraints
Do not add cron jobs, send Telegram/email/social messages, deploy, delete, purchase, or contact customers from this build.

## Suggested Bolt next step
If Jet likes it, convert this static HTML into a small local app that regenerates from Obsidian daily notes and highlights stale MEMORY.md files automatically.
