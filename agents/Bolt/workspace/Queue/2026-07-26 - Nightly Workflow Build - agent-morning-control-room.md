# Nightly Workflow Build — Agent Morning Control Room

## Why this helps Jet
Jet gets a single local page to start the morning after the all-agent memory sync, instead of opening many daily notes manually.

## Built
- `index.html` — usable static dashboard.
- `agents.json` — machine-readable sync card data.
- `README.md` — open/use instructions.

## Open/use
Open: `/Users/ultrafriday/Documents/Limitless OS/Agents/Bolt/Builds/2026-07-26/agent-morning-control-room/index.html`

## Acceptance criteria
- Dashboard opens locally in a browser.
- Shows active/present agent workspaces discovered during the cron run.
- Links/paths point to daily notes and shared daily coordination.

## Safety constraints
Local files only. No Telegram/email/posts/deploys/deletes/cron edits/production changes.

## Suggested Bolt next step
Turn `agents.json` into a tiny live reader that highlights new blockers from the last 72 hours and adds a one-click copyable morning brief.
