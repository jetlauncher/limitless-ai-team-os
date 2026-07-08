# Hermes Cron Health Digest — 2026-07-07

Generated: 2026-07-07 08:10:15 +07

Scanned **82** jobs across default + profiles; **64** active.

## Issues

### 1. default / limitless-x-to-obsidian-hourly

- Job ID: `9a5c42413ac6`
- Status: `ok`
- Last run: `2026-07-07T07:12:41.663094+07:00`
- Config: `/Users/ultrafriday/.hermes/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/cron/output/9a5c42413ac6/2026-07-07_07-12-41.md`
- Findings:
  - latest output contains zero-record data

### 2. default / hermes-cron-health-digest

- Job ID: `655dd227f390`
- Status: `ok`
- Last run: `2026-07-06T08:10:04.583060+07:00`
- Config: `/Users/ultrafriday/.hermes/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/cron/output/655dd227f390/2026-07-06_08-10-04.md`
- Findings:
  - latest output contains 401 unauthorized
  - latest output contains revoked/expired token
  - latest output contains traceback/error

### 3. default / google-youtube-oauth-token-health-check

- Job ID: `0439294d9bdf`
- Status: `ok`
- Last run: `2026-07-03T14:16:01.150562+07:00`
- Config: `/Users/ultrafriday/.hermes/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/cron/output/0439294d9bdf/2026-07-03_14-16-01.md`
- Findings:
  - stale last_run ≈ 90h ago

### 4. default / limitless-daily-youtube-report

- Job ID: `8539c3349272`
- Status: `error`
- Last run: `2026-07-07T08:00:16.054981+07:00`
- Config: `/Users/ultrafriday/.hermes/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/cron/output/8539c3349272/2026-07-07_08-00-14.md`
- Findings:
  - last_status=error
  - latest output contains traceback/error

### 5. default / weekly-hermes-janitor

- Job ID: `a930198fa9cb`
- Status: `ok`
- Last run: `2026-07-05T03:00:43.971941+07:00`
- Config: `/Users/ultrafriday/.hermes/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/cron/output/a930198fa9cb/2026-07-05_03-00-42.md`
- Findings:
  - stale last_run ≈ 53h ago
  - latest output contains traceback/error

### 6. bolt / Daily YouTube to Blog Check

- Job ID: `2aae2b04d926`
- Status: `ok`
- Last run: `2026-07-07T08:04:28.011807+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/bolt/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/bolt/cron/output/2aae2b04d926/2026-07-07_08-04-28.md`
- Findings:
  - latest output contains revoked/expired token

### 7. kaijeaw / kaijeaw-calendar-aware-workshop-content-pipeline

- Job ID: `2f06fffea29b`
- Status: `ok`
- Last run: `2026-07-07T07:16:47.717998+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/kaijeaw/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/kaijeaw/cron/output/2f06fffea29b/2026-07-07_07-16-46.md`
- Findings:
  - latest output contains revoked/expired token

### 8. kaijeaw / prepare-5-saturday-themes-for-jet

- Job ID: `91c2f104af0f`
- Status: `ok`
- Last run: `2026-07-04T08:01:26.543508+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/kaijeaw/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/kaijeaw/cron/output/91c2f104af0f/2026-07-04_08-01-25.md`
- Findings:
  - stale last_run ≈ 72h ago

### 9. qwen / qwen-morning-prep-for-kelly

- Job ID: `2ecf236f6cca`
- Status: `ok`
- Last run: `2026-07-07T07:16:36.306065+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/qwen/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/qwen/cron/output/2ecf236f6cca/2026-07-07_07-16-36.md`
- Findings:
  - latest output contains iCloud/resource deadlock

### 10. qwen / qwen-nightly-obsidian-hygiene

- Job ID: `b160922c0931`
- Status: `ok`
- Last run: `2026-07-06T23:33:12.300005+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/qwen/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/qwen/cron/output/b160922c0931/2026-07-06_23-33-12.md`
- Findings:
  - latest output contains iCloud/resource deadlock

### 11. qwen / qwen-agent-memory-guardian

- Job ID: `f4d9899e9bfc`
- Status: `ok`
- Last run: `2026-07-07T06:59:38.935895+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/qwen/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/qwen/cron/output/f4d9899e9bfc/2026-07-07_06-59-38.md`
- Findings:
  - latest output contains iCloud/resource deadlock

## Noisy output volumes

- default: 700 cron output files this week, 3.1 MB
- bolt: 1710 cron output files this week, 0.5 MB
- oracle: 189 cron output files this week, 4.0 MB
- qwen: 382 cron output files this week, 4.8 MB
- signal: 42 cron output files this week, 7.6 MB

## Recommended next actions

1. Fix token/OAuth jobs before rerunning dependent workflows.
2. Move mutable scanner state out of iCloud/Obsidian paths.
3. Fix profile cron delivery targets where `last_delivery_error` is present.
4. Convert high-volume unchanged sync jobs to silent/no-agent outputs.

_Secrets are redacted by this script; inspect referenced files locally if needed._
