# Nightly Workflow Build — Memory Hygiene Triage Board v0

## Why this helps Jet
Qwen's memory hygiene audit flagged stale/tiny durable memories. This board turns that friction into a quick, visual triage surface for Kelly/Bolt.

## Built
- `/Users/ultrafriday/Documents/Limitless OS/Agents/Bolt/Builds/2026-06-30/memory-hygiene-triage-board-v0/dashboard.html`
- `/Users/ultrafriday/Documents/Limitless OS/Agents/Bolt/Builds/2026-06-30/memory-hygiene-triage-board-v0/sync-status.json`
- `/Users/ultrafriday/Documents/Limitless OS/Agents/Bolt/Builds/2026-06-30/memory-hygiene-triage-board-v0/README.md`

## How to open/use
Open `dashboard.html` locally. Review cards marked `Needs review`, then update the relevant agent `Memory/MEMORY.md` only with durable facts.

## Acceptance criteria
- All present active agent folders are represented.
- The dashboard is readable on phone/desktop.
- The JSON output is valid and includes agent status/flags.
- Safe scope: local files only; no external side effects.

## Suggested Bolt next step
Convert this static board into a tiny local viewer that can refresh from `sync-status.json` and add one-click filters for `Needs review`, `stale memory`, and `tiny memory`.
