# Agent Memory Repair Triage Dashboard v0

Generated: 2026-08-08 02:04:17 UTC+07:00

## Why this exists
The nightly all-agent sync now produces a lot of file-only notes. This dashboard turns those notes into a practical repair queue so Kelly can see which agents need attention before Jet starts a new session.

## Open/use
Open `index.html` in a browser. Use the filter buttons for `Needs attention`, `Needs review`, `Watch`, and `OK`.

## Files
- `index.html` — static local dashboard, no network calls.
- `data.json` — generated local snapshot from Obsidian and the latest sync log.
- `generate_dashboard.py` — rebuild script.

## Safety
Local-only. No Telegram, email, posts, deploys, cron edits, destructive deletes, payments, purchases, or secret reads.

## Suggested next step
Have Bolt turn this into a reusable `agent-memory-triage` local command after Kelly confirms the triage rules are useful.
