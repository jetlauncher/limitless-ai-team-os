# Hermes Cron Health Digest — 2026-06-26

Generated: 2026-06-26 10:54:17 +07

Scanned **76** jobs across default + profiles; **57** active.

## Issues

### 1. default / limitless-x-to-obsidian-hourly

- Job ID: `9a5c42413ac6`
- Status: `ok`
- Last run: `2026-06-26T07:33:32.807623+07:00`
- Config: `/Users/ultrafriday/.hermes/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/cron/output/9a5c42413ac6/2026-06-26_07-33-32.md`
- Findings:
  - latest output contains zero-record data

### 2. default / weekly-ceo-review

- Job ID: `73d4312bcf3f`
- Status: `ok`
- Last run: `2026-06-21T20:05:51.250932+07:00`
- Config: `/Users/ultrafriday/.hermes/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/cron/output/73d4312bcf3f/2026-06-21_20-05-50.md`
- Findings:
  - stale last_run ≈ 111h ago

### 3. default / hermes-cron-health-digest

- Job ID: `655dd227f390`
- Status: `ok`
- Last run: `2026-06-25T08:10:47.267122+07:00`
- Config: `/Users/ultrafriday/.hermes/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/cron/output/655dd227f390/2026-06-25_08-10-47.md`
- Findings:
  - latest output contains 401 unauthorized
  - latest output contains revoked/expired token
  - latest output contains traceback/error

### 4. default / google-youtube-oauth-token-health-check

- Job ID: `0439294d9bdf`
- Status: `ok`
- Last run: `2026-06-25T14:14:41.735711+07:00`
- Config: `/Users/ultrafriday/.hermes/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/cron/output/0439294d9bdf/2026-06-25_14-14-41.md`
- Findings:
  - latest output contains traceback/error

### 5. bolt / Jedi website production watchdog

- Job ID: `8cf265b1a8e6`
- Status: `error`
- Last run: `2026-06-25T09:02:41.286910+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/bolt/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/bolt/cron/output/8cf265b1a8e6/2026-06-25_09-02-40.md`
- Findings:
  - last_status=error

### 6. kaijeaw / kaijeaw-calendar-aware-workshop-content-pipeline

- Job ID: `2f06fffea29b`
- Status: `ok`
- Last run: `2026-06-26T07:20:29.864079+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/kaijeaw/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/kaijeaw/cron/output/2f06fffea29b/2026-06-26_07-20-27.md`
- Findings:
  - latest output contains revoked/expired token

### 7. kaijeaw / prepare-5-saturday-themes-for-jet

- Job ID: `91c2f104af0f`
- Status: `ok`
- Last run: `2026-06-13T08:01:50.785092+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/kaijeaw/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/kaijeaw/cron/output/91c2f104af0f/2026-06-13_08-01-49.md`
- Findings:
  - stale last_run ≈ 315h ago

### 8. kaijeaw / sunday-thai-faith-carousel-checkin

- Job ID: `a111b6f60774`
- Status: `ok`
- Last run: `2026-06-21T09:01:16.119080+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/kaijeaw/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/kaijeaw/cron/output/a111b6f60774/2026-06-21_09-01-14.md`
- Findings:
  - stale last_run ≈ 122h ago

## Noisy output volumes

- default: 4705 cron output files this week, 7.2 MB
- bolt: 1412 cron output files this week, 0.3 MB
- oracle: 158 cron output files this week, 3.4 MB
- qwen: 314 cron output files this week, 3.1 MB

## Recommended next actions

1. Fix token/OAuth jobs before rerunning dependent workflows.
2. Move mutable scanner state out of iCloud/Obsidian paths.
3. Fix profile cron delivery targets where `last_delivery_error` is present.
4. Convert high-volume unchanged sync jobs to silent/no-agent outputs.

_Secrets are redacted by this script; inspect referenced files locally if needed._
