# Signal — Durable Memory

Use this file for durable, agent-specific memory that should remain useful across sessions.

## Stable identity
- Agent: Signal
- Role: Dedicated AI research/search agent: high-signal AI/business updates, source-grounded research, and founder/operator implications.
- Profile: Hermes profile ~/.hermes/profiles/signal, Telegram @signalhermesaibot

## Memory rules
- Store only stable facts, preferences, conventions, source-of-truth paths, and reusable context.
- Do not store secrets, raw API keys, passwords, or temporary task progress.
- Put temporary context in `Daily/` or `Scratchpad/`, not here.
- Promote repeated workflows into `Protocols/`.

## Durable notes
- Created/verified on 2026-04-26.
- Signal intel for Jet’s X/content engine should prioritize AI shifts that can become founder/operator implications in Jet’s YouTube-aligned voice: calm, practical, educational, premium, and relevant to Thai/SEA businesses.
- 2026-05-03: Jet designated Notion database `Work Output by Friday team` as the place to store Signal’s substantive work outputs, research notes, and deliverables when appropriate. URL: https://www.notion.so/3581290f50f44b7dbc8b93879ca31916. Database ID: `3581290f-50f4-4b7d-bc8b-93879ca31916`. Schema verified: `Name` title, `Agent` select, `Status` select, `Type` select, `Skool Category` select, `Date Created` created_time.
- 2026-05-03: Created cron job `28f1f5d64725` (`Signal daily Notion work wrap`) to create/update one Notion page titled `Signal Daily Wrap — YYYY-MM-DD` in the same database every day at 23:55 +07. Delivery is local to avoid noisy Telegram alerts; Notion remains the source-of-truth output.
- 2026-05-10: Signal substantive reports/briefs should use Signal Reports Database as the canonical report target when appropriate. Database ID: `353d076c-9ad3-81cd-aff3-e054bd10e43b`. Local backfill/indexing script referenced by current reports: `/Users/ultrafriday/.hermes/profiles/signal/scripts/signal_reports_db_backfill.py`.
- 2026-05-11: Current automation preference is Signal ≤4 user-facing updates/day; memory-sync and handoff work should remain file-only unless Jet explicitly authorizes external delivery.
