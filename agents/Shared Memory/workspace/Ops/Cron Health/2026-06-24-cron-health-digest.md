# Hermes Cron Health Digest — 2026-06-24

Generated: 2026-06-24 08:10:17 +07

Scanned **76** jobs across default + profiles; **57** active.

## Issues

### 1. default / weekly-ceo-review

- Job ID: `73d4312bcf3f`
- Status: `ok`
- Last run: `2026-06-21T20:05:51.250932+07:00`
- Config: `/Users/ultrafriday/.hermes/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/cron/output/73d4312bcf3f/2026-06-21_20-05-50.md`
- Findings:
  - stale last_run ≈ 60h ago

### 2. default / hermes-cron-health-digest

- Job ID: `655dd227f390`
- Status: `ok`
- Last run: `2026-06-23T08:10:39.155211+07:00`
- Config: `/Users/ultrafriday/.hermes/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/cron/output/655dd227f390/2026-06-23_08-10-39.md`
- Findings:
  - latest output contains 401 unauthorized
  - latest output contains revoked/expired token
  - latest output contains traceback/error

### 3. default / google-youtube-oauth-token-health-check

- Job ID: `0439294d9bdf`
- Status: `ok`
- Last run: `2026-06-21T14:14:10.265556+07:00`
- Config: `/Users/ultrafriday/.hermes/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/cron/output/0439294d9bdf/2026-06-21_14-14-10.md`
- Findings:
  - stale last_run ≈ 66h ago
  - latest output contains traceback/error

### 4. bolt / Daily YouTube to Blog Check

- Job ID: `2aae2b04d926`
- Status: `ok`
- Last run: `2026-06-24T08:04:35.668127+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/bolt/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/bolt/cron/output/2aae2b04d926/2026-06-24_08-04-35.md`
- Findings:
  - latest output contains revoked/expired token

### 5. bolt / Jedi website production watchdog

- Job ID: `8cf265b1a8e6`
- Status: `error`
- Last run: `2026-06-23T09:02:06.901350+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/bolt/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/bolt/cron/output/8cf265b1a8e6/2026-06-23_09-02-05.md`
- Findings:
  - last_status=error

### 6. kaijeaw / kaijeaw-calendar-aware-workshop-content-pipeline

- Job ID: `2f06fffea29b`
- Status: `ok`
- Last run: `2026-06-24T07:19:57.776055+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/kaijeaw/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/kaijeaw/cron/output/2f06fffea29b/2026-06-24_07-19-56.md`
- Findings:
  - latest output contains revoked/expired token

### 7. kaijeaw / prepare-5-saturday-themes-for-jet

- Job ID: `91c2f104af0f`
- Status: `ok`
- Last run: `2026-06-13T08:01:50.785092+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/kaijeaw/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/kaijeaw/cron/output/91c2f104af0f/2026-06-13_08-01-49.md`
- Findings:
  - stale last_run ≈ 264h ago

### 8. kaijeaw / sunday-thai-faith-carousel-checkin

- Job ID: `a111b6f60774`
- Status: `ok`
- Last run: `2026-06-21T09:01:16.119080+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/kaijeaw/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/kaijeaw/cron/output/a111b6f60774/2026-06-21_09-01-14.md`
- Findings:
  - stale last_run ≈ 71h ago

### 9. signal / signal-ai-morning-brief

- Job ID: `d194c1c29c42`
- Status: `ok`
- Last run: `2026-06-09T08:36:55.603739+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/signal/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/signal/cron/output/d194c1c29c42/2026-06-09_08-36-54.md`
- Findings:
  - stale last_run ≈ 360h ago

### 10. signal / signal-daily-ai-intel-report-9pm

- Job ID: `6c5ac6a19886`
- Status: `ok`
- Last run: `2026-06-08T21:04:23.951297+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/signal/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/signal/cron/output/6c5ac6a19886/2026-06-08_21-04-22.md`
- Findings:
  - stale last_run ≈ 371h ago

## Noisy output volumes

- default: 4387 cron output files this week, 6.8 MB
- bolt: 1371 cron output files this week, 0.4 MB
- oracle: 152 cron output files this week, 3.4 MB
- qwen: 302 cron output files this week, 2.8 MB

## Recommended next actions

1. Fix token/OAuth jobs before rerunning dependent workflows.
2. Move mutable scanner state out of iCloud/Obsidian paths.
3. Fix profile cron delivery targets where `last_delivery_error` is present.
4. Convert high-volume unchanged sync jobs to silent/no-agent outputs.

_Secrets are redacted by this script; inspect referenced files locally if needed._
