# Nightly Workflow Build — Agent Write-Access Safety Gate

**Date:** 2026-07-29 02:00 BKK  
**Owner:** Kelly → Bolt optional polish  
**Status:** v0 built locally and verified

## Why this helps Jet

Signal's latest radar made one risk teachable: powerful agents can self-manage, game evaluations, or misbehave when they get too much autonomy. Jet needs a simple classroom/founder checklist before giving agents real write access.

## What was built

A local, printable, single-page HTML tool plus markdown worksheet:

- `Agents/Bolt/Builds/2026-07-29/agent-write-access-safety-gate/index.html`
- `Agents/Bolt/Builds/2026-07-29/agent-write-access-safety-gate/worksheet.md`
- `Agents/Bolt/Builds/2026-07-29/agent-write-access-safety-gate/data.json`
- `Agents/Bolt/Builds/2026-07-29/agent-write-access-safety-gate/README.md`

## How to open/use

Open `index.html` in a browser. For each proposed AI-agent workflow, check:

1. Permission Boundary
2. Independent Verification
3. Kill Switch + Audit Trail

If score is below 3/3, keep the workflow draft-only or add a verifier/rollback path.

## Acceptance criteria

- [x] Usable local HTML exists and contains valid `<html>` structure.
- [x] Markdown worksheet exists with the three gates and decision rule.
- [x] No external messages, posts, deploys, cron edits, payments, or deletes.
- [x] Build has README + source data + verification.

## Suggested Bolt next step

Optional: add localStorage saved scenarios and a one-click JSON export so students can compare before/after workflow designs.
