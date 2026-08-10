# Agent Fleet Safe Prune — 2026-06-17 22:43 Bangkok

## Scope
Jet asked Kelly to audit and prune anything not needed after fleet felt quiet. I applied only reversible/no-data-loss cleanup: pause broken recurring jobs and repair noisy indexes. I did not delete profiles, secrets, cron definitions, or user data.

## Actions taken

### Repaired Kanban DB index noise
- Backed up `~/.hermes/kanban.db` to `~/.hermes/backups/kanban.db.before-reindex-20260617-224336.bak`.
- Ran `sqlite3 ~/.hermes/kanban.db 'REINDEX; PRAGMA integrity_check;'`.
- Verification: `PRAGMA integrity_check` returned `ok`.

### Paused broken active cron jobs
Paused these reversible jobs so they stop failing/retrying until fixed:

| Profile | Job ID | Job | Reason |
|---|---|---|---|
| default | `6a2606b41e59` | `limitless-visibility-weekly-gsc-gap-report` | Google Search Console OAuth `invalid_grant`; not Gmail |
| default | `8539c3349272` | `limitless-daily-youtube-report` | HTTP 400 from YouTube/Data API request |
| bolt | `8cf265b1a8e6` | `Jedi website production watchdog` | Script timed out after 120s |
| unclechris | `621654a5c632` | `uncle-chris-portfolio-opportunity-check-5pm` | Prompt blocked by threat pattern `deception_hide` |
| unclechris | `a4ae310dc534` | `Thai portfolio low-noise movement monitor` | Missing Python dependency `pandas` |

## Left untouched intentionally
- Existing paused old content/Signal jobs: kept paused for recoverability rather than deleting.
- Profiles with no cron jobs (Pixel, Protocol, Tiff, Jekjack): left as on-call agents; no deletion without explicit owner decision.
- API server port conflict on `:8642`: still present. Current owner appears to be Tiff gateway PID 2539, while default and Muse envs also enable API server. Needs a deliberate owner/port decision before changing gateway env/restarting profiles.
- Named gateway stale plist warnings: left for a separate maintenance window because refreshing profile launchd plists can restart profile gateways.

## Current known remaining issues
1. API Server conflict: repeated `Port 8642 already in use` log noise.
2. Named profile launchd plists stale after Hermes update.
3. Google Search Console and YouTube reporting jobs are paused, pending repair.
4. Fleet quietness remains partly by design: Qwen/Oracle are local-only; Signal has only one active job; Pixel/Protocol/Tiff/Jekjack have no scheduled work.

## Verification
- Paused jobs show `[paused]` in their profile cron list.
- Kanban DB integrity check: `ok`.
