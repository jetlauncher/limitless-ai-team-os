# Hermes Cron Health Digest — 2026-07-06

Generated: 2026-07-06 08:10:02 +07

Scanned **82** jobs across default + profiles; **64** active.

## Issues

### 1. default / limitless-x-to-obsidian-hourly

- Job ID: `9a5c42413ac6`
- Status: `ok`
- Last run: `2026-07-06T08:01:20.536734+07:00`
- Config: `/Users/ultrafriday/.hermes/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/cron/output/9a5c42413ac6/2026-07-06_08-01-20.md`
- Findings:
  - latest output contains zero-record data

### 2. default / signal-x-ai-training-insight-radar

- Job ID: `8cdfac21faf2`
- Status: `ok`
- Last run: `2026-07-06T08:02:23.466406+07:00`
- Config: `/Users/ultrafriday/.hermes/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/cron/output/8cdfac21faf2/2026-07-06_08-02-23.md`
- Findings:
  - latest output contains zero-record data

### 3. default / hermes-cron-health-digest

- Job ID: `655dd227f390`
- Status: `ok`
- Last run: `2026-07-05T08:10:29.280123+07:00`
- Config: `/Users/ultrafriday/.hermes/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/cron/output/655dd227f390/2026-07-05_08-10-29.md`
- Findings:
  - latest output contains 401 unauthorized
  - latest output contains revoked/expired token
  - latest output contains traceback/error

### 4. default / google-youtube-oauth-token-health-check

- Job ID: `0439294d9bdf`
- Status: `ok`
- Last run: `2026-07-03T14:16:01.150562+07:00`
- Config: `/Users/ultrafriday/.hermes/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/cron/output/0439294d9bdf/2026-07-03_14-16-01.md`
- Findings:
  - stale last_run ≈ 66h ago

### 5. default / weekly-hermes-janitor

- Job ID: `a930198fa9cb`
- Status: `ok`
- Last run: `2026-07-05T03:00:43.971941+07:00`
- Config: `/Users/ultrafriday/.hermes/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/cron/output/a930198fa9cb/2026-07-05_03-00-42.md`
- Findings:
  - latest output contains traceback/error

### 6. bolt / Jedi website production watchdog

- Job ID: `8cf265b1a8e6`
- Status: `ok`
- Last run: `2026-07-05T09:02:14.006905+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/bolt/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/bolt/cron/output/8cf265b1a8e6/2026-07-05_09-02-12.md`
- Findings:
  - latest output contains 401 unauthorized

### 7. kaijeaw / kaijeaw-calendar-aware-workshop-content-pipeline

- Job ID: `2f06fffea29b`
- Status: `ok`
- Last run: `2026-07-06T07:18:10.516499+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/kaijeaw/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/kaijeaw/cron/output/2f06fffea29b/2026-07-06_07-18-09.md`
- Findings:
  - latest output contains revoked/expired token

### 8. kaijeaw / prepare-5-saturday-themes-for-jet

- Job ID: `91c2f104af0f`
- Status: `ok`
- Last run: `2026-07-04T08:01:26.543508+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/kaijeaw/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/kaijeaw/cron/output/91c2f104af0f/2026-07-04_08-01-25.md`
- Findings:
  - stale last_run ≈ 48h ago

### 9. qwen / qwen-morning-prep-for-kelly

- Job ID: `2ecf236f6cca`
- Status: `ok`
- Last run: `2026-07-06T07:16:57.406668+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/qwen/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/qwen/cron/output/2ecf236f6cca/2026-07-06_07-16-57.md`
- Findings:
  - latest output contains iCloud/resource deadlock

### 10. qwen / qwen-nightly-obsidian-hygiene

- Job ID: `b160922c0931`
- Status: `ok`
- Last run: `2026-07-05T23:33:44.197289+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/qwen/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/qwen/cron/output/b160922c0931/2026-07-05_23-33-44.md`
- Findings:
  - latest output contains iCloud/resource deadlock

### 11. qwen / qwen-todoist-worker

- Job ID: `1213c21e5430`
- Status: `ok`
- Last run: `2026-07-06T06:16:08.420054+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/qwen/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/qwen/cron/output/1213c21e5430/2026-07-06_06-16-08.md`
- Findings:
  - latest output contains iCloud/resource deadlock

### 12. qwen / qwen-agent-memory-guardian

- Job ID: `f4d9899e9bfc`
- Status: `ok`
- Last run: `2026-07-06T06:17:50.276876+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/qwen/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/qwen/cron/output/f4d9899e9bfc/2026-07-06_06-17-50.md`
- Findings:
  - latest output contains iCloud/resource deadlock

## Noisy output volumes

- default: 700 cron output files this week, 3.1 MB
- bolt: 1709 cron output files this week, 0.4 MB
- oracle: 189 cron output files this week, 4.0 MB
- qwen: 382 cron output files this week, 4.7 MB
- signal: 42 cron output files this week, 7.6 MB

## Recommended next actions

1. Fix token/OAuth jobs before rerunning dependent workflows.
2. Move mutable scanner state out of iCloud/Obsidian paths.
3. Fix profile cron delivery targets where `last_delivery_error` is present.
4. Convert high-volume unchanged sync jobs to silent/no-agent outputs.

_Secrets are redacted by this script; inspect referenced files locally if needed._
