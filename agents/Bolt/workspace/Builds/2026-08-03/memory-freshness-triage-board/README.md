# Memory Freshness Triage Board — 2026-08-03

Local v0 dashboard for nightly all-agent memory sync.

## Open
- `index.html`

## Regenerate
```bash
cd '/Users/ultrafriday/Documents/Limitless OS/Agents/Bolt/Builds/2026-08-03/memory-freshness-triage-board'
python3 generate_memory_freshness_board.py
```

## What it checks
- Active Hermes profiles from `hermes profile list`
- Matching Obsidian agent folders
- Today's Daily note existence/non-empty status
- Durable `Memory/MEMORY.md` freshness and size
- Latest non-sync local note signal where available
- File-only blocker / next owner per agent

Safety: no network calls, no external messages, no deploys, no cron changes.
