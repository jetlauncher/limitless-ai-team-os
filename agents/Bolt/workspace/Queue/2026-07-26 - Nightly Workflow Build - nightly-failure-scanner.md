# Nightly Workflow Build — Nightly Failure Scanner

## Why this helps Jet
Turns nightly sync uncertainty into a local dashboard showing agent daily-note coverage and known failure phrases.

## What was built
- Static HTML dashboard.
- `data.json` snapshot from local Obsidian/Hermes files.
- Regeneration script.

## Files created
- `/Users/ultrafriday/Documents/Limitless OS/Agents/Bolt/Builds/2026-07-26/nightly-failure-scanner/index.html`
- `/Users/ultrafriday/Documents/Limitless OS/Agents/Bolt/Builds/2026-07-26/nightly-failure-scanner/data.json`
- `/Users/ultrafriday/Documents/Limitless OS/Agents/Bolt/Builds/2026-07-26/nightly-failure-scanner/build_failure_scanner.py`
- `/Users/ultrafriday/Documents/Limitless OS/Agents/Bolt/Builds/2026-07-26/nightly-failure-scanner/README.md`

## How to open/use
Open `index.html` in a browser, or rerun: `python3 /Users/ultrafriday/Documents/Limitless OS/Agents/Bolt/Builds/2026-07-26/nightly-failure-scanner/build_failure_scanner.py`.

## Acceptance criteria
- HTML contains valid `<html` structure.
- JSON is non-empty and includes synced agents.
- Script passes Python syntax check.

## Safety constraints
Local files only. No cron edits, no external messages, no deploys, no secrets.

## Suggested Bolt next step
Add filters by agent/date and make the failure phrase list editable in the UI.
