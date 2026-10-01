# Nightly Workflow Build — Weekly Focus Picker

Date: 2026-07-30 02:03 Bangkok  
Owner: Bolt next, Kelly verified v0

## Why this helps Jet
The current fleet blocker is not lack of output; it is lack of one weekly priority. This gives Jet a phone-readable/local browser decision tool and a copy-paste routing prompt.

## What was built
A single-file HTML dashboard: **Weekly Focus Picker**.

## Files created
- `Agents/Bolt/Builds/2026-07-30/weekly-focus-picker/index.html`
- `Agents/Bolt/Builds/2026-07-30/weekly-focus-picker/README.md`

## How to open/use
Open `index.html` locally, choose one focus card, click **Insert selected focus**, then copy the generated routing prompt.

## Acceptance criteria
- HTML file exists and contains a valid `<!doctype html>` / `<html>` structure.
- Four focus options are visible.
- Copy-paste routing prompt is embedded.
- No network calls or external side effects.

## Safety constraints
No Telegram, email, social posting, deploys, purchases, payments, deletes, or cron edits. Local-only files under the Obsidian Agents workspace.

## Suggested Bolt next step
If Jet likes this, turn it into a tiny persistent dashboard that writes the selected weekly focus to `Agents/Shared Memory/Ops/current-weekly-focus.md` after explicit approval.
