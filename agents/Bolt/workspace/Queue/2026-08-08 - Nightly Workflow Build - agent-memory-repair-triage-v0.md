# Nightly Workflow Build — Agent Memory Repair Triage Dashboard v0

Date: 2026-08-08
Owner: Kelly → Bolt
Status: v0 built and locally verified

## Why this helps Jet
The nightly all-agent memory sync is working, but it creates many notes. This dashboard turns the sync into a practical repair queue so Kelly/Jet can see which agents need attention before starting the next session.

## What was built
A static local HTML dashboard that reads the latest file-only sync snapshot and ranks agents by:
- known blockers in daily/shared notes,
- stopped gateways,
- missing/tiny/stale durable `Memory/MEMORY.md`,
- daily note presence and size.

## Files created
- `Agents/Bolt/Builds/2026-08-08/agent-memory-repair-triage-v0/index.html`
- `Agents/Bolt/Builds/2026-08-08/agent-memory-repair-triage-v0/data.json`
- `Agents/Bolt/Builds/2026-08-08/agent-memory-repair-triage-v0/README.md`
- `Agents/Bolt/Builds/2026-08-08/agent-memory-repair-triage-v0/generate_dashboard.py`

## How to open/use
Open `index.html` locally in a browser. Use filter pills for `Needs attention`, `Needs review`, `Watch`, and `OK`.

## Acceptance criteria verified
- `generate_dashboard.py` compiles with `python3 -m py_compile`.
- `index.html` contains valid `<html` structure and is non-empty.
- `data.json` parses and includes 13 synced agents.
- Local verification output: `agents_synced=13`, `needs_attention=3`, `needs_review=6`.

## Safety constraints
Local-only. No Telegram, email, posts, deploys, cron edits, destructive deletes, payments, purchases, or secret reads.

## Suggested Bolt next step
If Jet likes the v0, package `generate_dashboard.py` as a reusable local command such as `agent-memory-triage` and add optional trend history from previous nightly sync logs.
