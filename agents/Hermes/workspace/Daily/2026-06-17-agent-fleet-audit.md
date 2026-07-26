# Agent Fleet Audit — 2026-06-17 19:22–19:28 Bangkok

## What was checked
- `hermes --version`: Hermes Agent v0.16.0, upstream c6b0eb4d.
- `hermes profile list`: default + blaze/bolt/jekjack/kaijeaw/muse/oracle/pixel/protocol/qwen/signal/tiff/unclechris/zegna all show gateway `running`.
- Cron lists across profiles.
- Recent gateway logs and cron output folders.
- No-tool smoke tests: blaze, signal, bolt, qwen, oracle, kaijeaw, zegna all returned expected sentinels.
- Terminal-tool smoke tests: blaze, signal, bolt, qwen, oracle all returned expected sentinels.

## High-level diagnosis
The fleet is not dead. Core model/tool execution is healthy for representative agents. The perceived quietness is mostly from routing/design:
- Many agents intentionally deliver to `local`, not Telegram/Discord.
- Signal has only 1 active job and 7 paused jobs.
- Pixel, Protocol, Tiff, Jekjack have no cron jobs.
- Qwen and Oracle are active but fully local-only.

## Active cron visibility snapshot
- default/Kelly: 30 active, 16 local, 14 origin, 4 paused.
- Blaze: 4 active, 3 origin, 1 local.
- Signal: 1 active origin, 7 paused.
- Zegna: 2 active, 1 origin, 1 local.
- Kaijeaw: 4 active origin.
- Bolt: 5 active, 2 origin, 3 local.
- Qwen: 6 active local-only.
- Oracle: 4 active local-only.
- Pixel/Protocol/Tiff/Jekjack: no scheduled jobs.
- UncleChris: 7 active, several failures/delivery config issues; likely outside Jet core fleet.

## Problems found
1. Named profile launchd plists are stale after Hermes update (`Run: hermes gateway start` shown for almost all named profiles). Gateways are loaded/running, but plist refresh is needed.
2. API server conflict: all/most profiles try to reconnect API Server on port 8642; PID 2539 (`tiff`) owns it. Logs spam `Port 8642 already in use`. Does not stop Telegram/cron but creates noise and likely breaks API-server access for other profiles.
3. Kanban DB corruption/index issue: logs repeatedly say `~/.hermes/kanban.db is not a valid SQLite database`; `sqlite3 PRAGMA integrity_check` reports `wrong # of entries in index idx_events_task` and missing index rows. This causes repeated gateway log errors across profiles.
4. Default cron failures:
   - `limitless-visibility-weekly-gsc-gap-report` fails with Google Search Console `invalid_grant` refresh error.
   - `limitless-daily-youtube-report` fails with YouTube/Data API HTTP 400 Bad Request.
   - `daily-evening-shutdown-briefing` has an old delivery error `python-telegram-bot not installed`, but Hermes venv currently imports `telegram` v22.6, so this may already be resolved pending next run.
5. Bolt cron failure:
   - `Jedi website production watchdog` timed out after 120s.
6. UncleChris profile failures:
   - one prompt blocked by `deception_hide`, two old Telegram delivery errors, one finance monitor script code 1.

## Verified healthy
- Representative model calls: Blaze, Signal, Bolt, Qwen, Oracle, Kaijeaw, Zegna.
- Representative terminal tool calls: Blaze, Signal, Bolt, Qwen, Oracle.
- Default Telegram is working (this audit delivered via Kelly).

## Recommended next fixes
1. Visibility/product decision: decide which local-only agents should send visible daily/weekly summaries. Likely: Oracle daily idea digest and Qwen daily local-worker digest should be `origin` or summarized by Kelly.
2. Restore Signal volume: unpause/replace Signal morning/evening briefs if Jet wants research chatter again.
3. Repair noisy infra:
   - Refresh named profile launchd plists with `profile gateway start` or launchctl pattern outside the active Kelly session.
   - Disable API server on non-owner profiles or assign unique ports; keep only one owner for :8642.
   - Reindex/rebuild Kanban DB indexes or re-init the board after backup.
4. Fix cron failures:
   - Reauth Google Search Console credentials for weekly visibility report.
   - Inspect/fix YouTube report API 400 request payload/credentials.
   - Increase or optimize Bolt website watchdog timeout.
5. Add/restore cron jobs for Pixel/Protocol if those agents are expected to proactively produce work.
