# Signal Work Log Index

Last updated: 2026-05-01 10:10 +07

This is the human-readable index for Signal’s work outputs. It was created after Jet noticed that reports were not consistently stored in Obsidian or a proper Notion database.

## Start here

- [[2026-05-01 Signal Backlog and Output Audit]] — storage audit + backfilled artifact index
- [[2026-05-01 X Bookmarks + Signal Research]] — latest 5am bookmark research run
- [[2026-04-30 X Bookmarks Sweep]] — manual X bookmark sweep from local browser

## Structured daily intel reports

- [[2026-04-30 - Signal Daily AI Intel Report]]
- [[2026-04-29 - Signal Daily AI Intel Report]]
- [[2026-04-28 - Signal Daily AI Intel Report]]
- [[2026-04-27 - Signal Daily AI Intel Report]]
- [[2026-04-26 - Signal Daily AI Intel Report]]

These live in:

`~/Documents/Obsidian Vault/Agents/Shared Memory/Intel/`

## Raw cron archive

Raw scheduled run logs live in:

`~/.hermes/profiles/signal/cron/output/{job_id}/YYYY-MM-DD_HH-MM-SS.md`

This is useful for audit/recovery, but it is not clean workspace memory.

## Local JSON backup

Machine-readable backups live in:

`~/.hermes/limitless/`

Examples:

- `daily_ai_intel_YYYY-MM-DD.json`
- `x_signal_posts_YYYY-MM-DD.json`

## Current gap

Signal reports now have a canonical Notion database:

- **Name:** `Signal Reports Database`
- **Database ID:** `353d076c-9ad3-81cd-aff3-e054bd10e43b`
- **URL:** https://app.notion.com/p/353d076c9ad381cdaff3e054bd10e43b
- **Backfill:** 906 artifacts indexed, 0 failures on 2026-05-01.

Future cron jobs have been updated so every new run writes or syncs a DB row automatically via `/Users/ultrafriday/.hermes/profiles/signal/scripts/signal_reports_db_backfill.py`.
