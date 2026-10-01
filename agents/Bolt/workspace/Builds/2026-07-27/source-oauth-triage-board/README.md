# Source & OAuth Triage Board — 2026-07-27

Local v0 dashboard that groups recent reliability blockers from Obsidian/shared cron notes.

## Open
Open `index.html` in a browser.

## Files
- `index.html` — phone-readable dashboard
- `data.json` — extracted blocker hits and counts
- `build_source_oauth_triage.py` — repeatable local generator

## Safety
File-only local build. No cron edits, sends, deploys, deletes, or credential reads.
