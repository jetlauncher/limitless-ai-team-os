# Agent Memory Staleness Board — 2026-07-25

A local single-file dashboard for the nightly all-agent memory sync.

## Open
- `index.html` in a browser.
- `data.json` contains the generated agent rows.

## What it shows
- Which active agent daily notes were touched by the nightly file-only sync.
- Daily note line counts.
- MEMORY.md age/status to prioritize durable-memory promotion.

## Safety
Local-only. No external messages, cron edits, deploys, credentials, or destructive actions.
