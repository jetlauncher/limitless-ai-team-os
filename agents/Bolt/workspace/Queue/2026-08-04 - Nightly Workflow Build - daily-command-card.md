# Nightly Workflow Build — Daily Command Card

## Why this helps Jet
Jet gets a phone-readable, one-screen daily command card instead of opening multiple agent notes after the 2:00 AM sync.

## What was built
- Local HTML dashboard: `Agents/Bolt/Builds/2026-08-04/daily-command-card/index.html`
- Extracted data: `Agents/Bolt/Builds/2026-08-04/daily-command-card/data.json`
- Generator: `Agents/Bolt/Builds/2026-08-04/daily-command-card/generate_daily_command_card.py`
- README: `Agents/Bolt/Builds/2026-08-04/daily-command-card/README.md`

## How to open/use
Open `index.html` locally in a browser. Re-run the generator after new daily notes land.

## Acceptance criteria
- `index.html` exists and contains `<html`.
- `data.json` is valid JSON and includes email, calendar/revenue, AI signal, ops attention, and agent sync sections.
- Shared daily note links to this artifact.

## Safety constraints
No Telegram/email/posts/deploys/purchases/destructive deletes/cron edits/external state changes.

## Suggested Bolt next step
Turn this v0 into a reusable daily generator with a stable `latest.html` symlink and optional print/PDF styling.
