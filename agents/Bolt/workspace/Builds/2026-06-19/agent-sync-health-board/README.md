# Agent Sync Health Board

A read-only, single-file dashboard that shows at a glance which Limitless OS agents
have written today's daily note, how stale each `MEMORY.md` is, and whether the
nightly sync section landed.

## Why
The nightly memory-sync and morning memory-hygiene audits keep re-discovering the
same question by hand: *"who synced today and who is stale?"* This turns that into
a one-command, human-readable board.

## Files
- `generate.py` — scans `~/Documents/Limitless OS/Agents` (read-only) and writes:
  - `data.json` — machine-readable snapshot
  - `index.html` — self-contained dashboard (snapshot embedded; no server needed)

## Use
```bash
cd "~/Documents/Limitless OS/Agents/Bolt/Builds/2026-06-19/agent-sync-health-board"
python3 generate.py
open index.html
```

## What it reports per agent
- Latest daily note filename
- Days since last daily note (today / Nd ago)
- `MEMORY.md` age in days (or "missing" when empty/absent)
- Whether the latest note contains a `Nightly Memory Sync` section
- Status pill: **synced** (today), **recent** (≤1d), **stale** (>1d)

## Safety
Read-only filesystem scan. No network, no external side effects, no writes outside
this build folder.

## Snapshot at build time (2026-06-19 02:00)
Synced today: **12/12**.
