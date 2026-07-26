# X Radar Intake Validator — Nightly Workflow Build

## Why this helps Jet
Tonight's Qwen X radar output had no usable signal because the input contained X search URLs and UI boilerplate with empty `TITLE` / `TEXT` fields. This v0 catches that before an agent spends a run analyzing empty source material.

## What was built
A local, single-file HTML validator that:
- Accepts pasted X/Twitter scrape/export text.
- Scores whether the source is ready for Qwen.
- Detects empty `TITLE:` and `TEXT:` fields, low real-text density, and X UI boilerplate.
- Produces a Qwen-ready handoff prompt when the source passes.
- Produces a corrective checklist when the source is not usable.

## Files created
- `/Users/ultrafriday/Documents/Limitless OS/Agents/Bolt/Builds/2026-07-11/x-radar-intake-validator/index.html`

## How to open/use
Open the HTML file locally in a browser:

```bash
open "/Users/ultrafriday/Documents/Limitless OS/Agents/Bolt/Builds/2026-07-11/x-radar-intake-validator/index.html"
```

Then paste raw X source text, click **Validate intake**, and copy the Qwen handoff if score is 70+.

## Acceptance criteria
- [x] Local artifact exists under the nightly build folder.
- [x] HTML file is non-empty and contains valid `<!doctype html>` / `<html>` structure.
- [x] Includes a failure sample matching tonight's empty-source Qwen issue.
- [x] Generates actionable next steps without external network calls.
- [x] No credentials, secrets, production deploy, or external side effects.

## Safety constraints
- Local-only.
- Paste-only; no scraping, login, posting, messaging, payments, deploys, deletes, or credential access.

## Suggested Bolt next step
If Jet likes the validator, Bolt can fold it into the Layer 1 portal as a small “Agent Source QA” utility and add a drag/drop `.txt` import plus saved validation history.
