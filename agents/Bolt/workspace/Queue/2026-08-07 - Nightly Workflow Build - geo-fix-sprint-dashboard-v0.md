# 2026-08-07 - Nightly Workflow Build - geo-fix-sprint-dashboard-v0

## Title
Limitless GEO Fix Sprint Dashboard v0

## Why this helps Jet
The 2026-08-06 GEO / AI visibility audit showed a clear revenue/authority risk: Jet/Limitless appeared in 0/5 generic AI-answer recommendation prompts, while two P0 technical issues can dilute the official site authority. This dashboard turns that audit into a one-screen fix sprint.

## What was built
A local HTML dashboard plus structured JSON checklist for the highest-impact fix workstreams:
- P0: unknown routes must return real 404.
- P0: retire/deindex obsolete `limitlessclub.manus.space` authority leak.
- P1: add source video attribution and VideoObject schema.
- P1: clean code fences and multiple-H1 issues.
- P2: track AI-answer category authority weekly.

## Files created
- `/Users/ultrafriday/Documents/Limitless OS/Agents/Bolt/Builds/2026-08-07/geo-fix-sprint-dashboard-v0/index.html`
- `/Users/ultrafriday/Documents/Limitless OS/Agents/Bolt/Builds/2026-08-07/geo-fix-sprint-dashboard-v0/data.json`
- `/Users/ultrafriday/Documents/Limitless OS/Agents/Bolt/Builds/2026-08-07/geo-fix-sprint-dashboard-v0/README.md`

## How to open/use
Open `index.html` in a browser. Use the P0 cards as the next Bolt sprint checklist. Use `data.json` if Bolt wants to turn the checklist into issue cards or an app component.

## Acceptance criteria
- Dashboard exists locally and is non-empty.
- HTML contains a valid `<html>` structure.
- JSON parses successfully.
- P0/P1/P2 cards include owner, problem, acceptance criteria, and safe next step.
- No production deploy or external side effects happened.

## Safety constraints
Do not deploy, change DNS, deindex, redirect, delete, email, post, or modify cron without Jet approval. Keep all work local/staging until reviewed.

## Suggested Bolt next step
Create a local/staging patch plan for the two P0 items, starting with route-level 404 behavior and verification commands. Ask Jet before any production/domain-level action.
