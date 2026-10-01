# Nightly Workflow Build — Agent Ops Preflight

## Why this helps Jet
Recurring agent-memory and cron reliability issues are easier to act on when the morning check is one openable dashboard instead of scattered daily notes.

## What was built
A local single-file HTML dashboard plus JSON summary and README. It verifies active agent daily notes, flags stopped gateways/failure phrases, and gives a morning triage checklist.

## Files created
- `Agents/Bolt/Builds/2026-08-03/agent-ops-preflight/index.html`
- `Agents/Bolt/Builds/2026-08-03/agent-ops-preflight/sync-summary.json`
- `Agents/Bolt/Builds/2026-08-03/agent-ops-preflight/README.md`

## How to open/use
Open `index.html` locally in a browser, then scan stopped/review rows first.

## Acceptance criteria
- HTML contains valid `<html>` structure.
- Summary JSON exists and includes every discovered matching agent.
- Shared daily note links to the artifact.
- No external side effects beyond local Obsidian/build files.

## Safety constraints
No cron edits, deploys, credential changes, emails, social posts, purchases, or deletes.

## Suggested Bolt next step
If useful, turn the static dashboard into a tiny local app that can refresh from Obsidian notes and filter by blocker/owner.
