# Hermes Cron Health Digest — 2026-06-23

Generated: 2026-06-23 08:10:37 +07

Scanned **76** jobs across default + profiles; **55** active.

## Issues

### 1. default / two-account-gmail-inbox-zero

- Job ID: `d1e3eedb44c2`
- Status: `ok`
- Last run: `2026-06-23T08:00:41.851318+07:00`
- Config: `/Users/ultrafriday/.hermes/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/cron/output/d1e3eedb44c2/2026-06-23_08-00-41.md`
- Findings:
  - latest output contains revoked/expired token

### 2. default / hermes-cron-health-digest

- Job ID: `655dd227f390`
- Status: `ok`
- Last run: `2026-06-22T08:10:09.647018+07:00`
- Config: `/Users/ultrafriday/.hermes/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/cron/output/655dd227f390/2026-06-22_08-10-09.md`
- Findings:
  - latest output contains revoked/expired token
  - latest output contains traceback/error

### 3. default / google-youtube-oauth-token-health-check

- Job ID: `0439294d9bdf`
- Status: `ok`
- Last run: `2026-06-21T14:14:10.265556+07:00`
- Config: `/Users/ultrafriday/.hermes/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/cron/output/0439294d9bdf/2026-06-21_14-14-10.md`
- Findings:
  - latest output contains traceback/error

### 4. bolt / Daily YouTube to Blog Check

- Job ID: `2aae2b04d926`
- Status: `ok`
- Last run: `2026-06-22T08:15:04.998579+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/bolt/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/bolt/cron/output/2aae2b04d926/2026-06-22_08-15-04.md`
- Findings:
  - latest output contains 401 unauthorized
  - latest output contains revoked/expired token

### 5. bolt / Jedi website production watchdog

- Job ID: `8cf265b1a8e6`
- Status: `error`
- Last run: `2026-06-22T09:02:17.869383+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/bolt/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/bolt/cron/output/8cf265b1a8e6/2026-06-22_09-02-16.md`
- Findings:
  - last_status=error

### 6. kaijeaw / kaijeaw-calendar-aware-workshop-content-pipeline

- Job ID: `2f06fffea29b`
- Status: `ok`
- Last run: `2026-06-23T07:21:01.295623+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/kaijeaw/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/kaijeaw/cron/output/2f06fffea29b/2026-06-23_07-21-00.md`
- Findings:
  - latest output contains revoked/expired token

### 7. kaijeaw / prepare-5-saturday-themes-for-jet

- Job ID: `91c2f104af0f`
- Status: `ok`
- Last run: `2026-06-13T08:01:50.785092+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/kaijeaw/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/kaijeaw/cron/output/91c2f104af0f/2026-06-13_08-01-49.md`
- Findings:
  - stale last_run ≈ 240h ago

## Noisy output volumes

- default: 3818 cron output files this week, 6.2 MB
- bolt: 1236 cron output files this week, 0.3 MB
- oracle: 136 cron output files this week, 3.0 MB
- qwen: 271 cron output files this week, 2.4 MB

## Recommended next actions

1. Fix token/OAuth jobs before rerunning dependent workflows.
2. Move mutable scanner state out of iCloud/Obsidian paths.
3. Fix profile cron delivery targets where `last_delivery_error` is present.
4. Convert high-volume unchanged sync jobs to silent/no-agent outputs.

_Secrets are redacted by this script; inspect referenced files locally if needed._
