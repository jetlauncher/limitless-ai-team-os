# Hermes Cron Health Digest — 2026-06-21

Generated: 2026-06-21 08:10:04 +07

Scanned **76** jobs across default + profiles; **55** active.

## Issues

### 1. default / limitless-x-to-obsidian-hourly

- Job ID: `9a5c42413ac6`
- Status: `ok`
- Last run: `2026-06-21T07:21:35.592180+07:00`
- Config: `/Users/ultrafriday/.hermes/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/cron/output/9a5c42413ac6/2026-06-21_07-21-35.md`
- Findings:
  - latest output contains zero-record data

### 2. default / limitless-x-daily-report

- Job ID: `3e00a7f3524f`
- Status: `ok`
- Last run: `2026-06-17T18:01:18.241408+07:00`
- Config: `/Users/ultrafriday/.hermes/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/cron/output/3e00a7f3524f/2026-06-17_18-01-18.md`
- Findings:
  - stale last_run ≈ 86h ago

### 3. default / weekly-ceo-review

- Job ID: `73d4312bcf3f`
- Status: `ok`
- Last run: `2026-06-14T20:06:06.561365+07:00`
- Config: `/Users/ultrafriday/.hermes/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/cron/output/73d4312bcf3f/2026-06-14_20-06-05.md`
- Findings:
  - stale last_run ≈ 156h ago

### 4. default / hermes-cron-health-digest

- Job ID: `655dd227f390`
- Status: `ok`
- Last run: `2026-06-19T08:10:07.321014+07:00`
- Config: `/Users/ultrafriday/.hermes/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/cron/output/655dd227f390/2026-06-19_08-10-07.md`
- Findings:
  - latest output contains revoked/expired token
  - latest output contains traceback/error

### 5. default / google-youtube-oauth-token-health-check

- Job ID: `0439294d9bdf`
- Status: `ok`
- Last run: `2026-06-17T14:14:02.624833+07:00`
- Config: `/Users/ultrafriday/.hermes/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/cron/output/0439294d9bdf/2026-06-17_14-14-02.md`
- Findings:
  - stale last_run ≈ 90h ago
  - latest output contains traceback/error

### 6. bolt / Jedi website production watchdog

- Job ID: `8cf265b1a8e6`
- Status: `error`
- Last run: `2026-06-19T09:02:52.397368+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/bolt/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/bolt/cron/output/8cf265b1a8e6/2026-06-19_09-02-51.md`
- Findings:
  - last_status=error

### 7. kaijeaw / kaijeaw-calendar-aware-workshop-content-pipeline

- Job ID: `2f06fffea29b`
- Status: `ok`
- Last run: `2026-06-21T07:21:36.487807+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/kaijeaw/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/kaijeaw/cron/output/2f06fffea29b/2026-06-21_07-21-35.md`
- Findings:
  - latest output contains revoked/expired token

### 8. kaijeaw / prepare-5-saturday-themes-for-jet

- Job ID: `91c2f104af0f`
- Status: `ok`
- Last run: `2026-06-13T08:01:50.785092+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/kaijeaw/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/kaijeaw/cron/output/91c2f104af0f/2026-06-13_08-01-49.md`
- Findings:
  - stale last_run ≈ 192h ago

### 9. kaijeaw / sunday-thai-faith-carousel-checkin

- Job ID: `a111b6f60774`
- Status: `ok`
- Last run: `2026-06-14T09:01:38.778780+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/kaijeaw/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/kaijeaw/cron/output/a111b6f60774/2026-06-14_09-01-37.md`
- Findings:
  - stale last_run ≈ 167h ago

## Noisy output volumes

- default: 3239 cron output files this week, 6.0 MB
- bolt: 1238 cron output files this week, 0.3 MB
- oracle: 133 cron output files this week, 3.0 MB
- qwen: 268 cron output files this week, 2.2 MB

## Recommended next actions

1. Fix token/OAuth jobs before rerunning dependent workflows.
2. Move mutable scanner state out of iCloud/Obsidian paths.
3. Fix profile cron delivery targets where `last_delivery_error` is present.
4. Convert high-volume unchanged sync jobs to silent/no-agent outputs.

_Secrets are redacted by this script; inspect referenced files locally if needed._
