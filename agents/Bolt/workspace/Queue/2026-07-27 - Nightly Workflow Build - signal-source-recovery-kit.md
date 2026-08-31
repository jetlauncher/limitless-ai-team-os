# Nightly Workflow Build — Signal Source Recovery Kit

## Why this helps Jet
Signal/X intel is a recurring upstream blocker. This gives Jet/Kelly a one-screen recovery checklist instead of burying the issue in daily notes.

## Built
- `index.html` — local visual triage card.
- `data.json` — machine-readable blockers/checklist.
- `README.md` — use and safety notes.

## Open/use
Open: `/Users/ultrafriday/Documents/Limitless OS/Agents/Bolt/Builds/2026-07-27/signal-source-recovery-kit/index.html`

## Acceptance criteria
- HTML opens locally and contains the current blockers.
- README explains safe recovery flow.
- No external side effects, billing changes, deploys, cron edits, or secrets exposure.

## Suggested Bolt next step
Turn this static card into a small reader that auto-loads source status from Shared Memory daily notes and highlights whether Signal is green/yellow/red.
