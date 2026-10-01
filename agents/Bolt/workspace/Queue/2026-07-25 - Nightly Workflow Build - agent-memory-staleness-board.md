# Nightly Workflow Build — Agent Memory Staleness Board

## Why this helps Jet
Kelly's nightly sync needs a quick visual way to spot agents whose daily notes are active but durable memory is stale, without reading every log.

## What was built
A local HTML dashboard plus JSON snapshot for 12 active/present agents.

## Files created
- `/Users/ultrafriday/Documents/Limitless OS/Agents/Bolt/Builds/2026-07-25/agent-memory-staleness-board/index.html`
- `/Users/ultrafriday/Documents/Limitless OS/Agents/Bolt/Builds/2026-07-25/agent-memory-staleness-board/data.json`
- `/Users/ultrafriday/Documents/Limitless OS/Agents/Bolt/Builds/2026-07-25/agent-memory-staleness-board/README.md`

## How to open/use
Open `index.html` in a browser. Review red/amber rows first; promote durable facts only when still useful next week.

## Acceptance criteria
- HTML exists and contains a valid `<html` document.
- JSON exists and includes all present agents discovered locally.
- No external actions, production deploys, cron edits, or credential reads.

## Suggested Bolt next step
Turn this v0 into a reusable local script that diffs yesterday/today and flags missing `SYNC_DONE` only from fresh cron output folders.
