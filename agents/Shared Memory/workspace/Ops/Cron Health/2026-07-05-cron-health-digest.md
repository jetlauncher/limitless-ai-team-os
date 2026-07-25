# Hermes Cron Health Digest — 2026-07-05

Generated: 2026-07-05 08:10:28 +07

Scanned **82** jobs across default + profiles; **64** active.

## Issues

### 1. default / limitless-x-to-obsidian-hourly

- Job ID: `9a5c42413ac6`
- Status: `ok`
- Last run: `2026-07-05T08:06:54.855384+07:00`
- Config: `/Users/ultrafriday/.hermes/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/cron/output/9a5c42413ac6/2026-07-05_08-06-54.md`
- Findings:
  - latest output contains zero-record data

### 2. default / weekly-ceo-review

- Job ID: `73d4312bcf3f`
- Status: `ok`
- Last run: `2026-06-28T20:01:51.798992+07:00`
- Config: `/Users/ultrafriday/.hermes/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/cron/output/73d4312bcf3f/2026-06-28_20-01-50.md`
- Findings:
  - stale last_run ≈ 156h ago

### 3. default / signal-x-ai-training-insight-radar

- Job ID: `8cdfac21faf2`
- Status: `ok`
- Last run: `2026-07-05T08:01:31.567439+07:00`
- Config: `/Users/ultrafriday/.hermes/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/cron/output/8cdfac21faf2/2026-07-05_08-01-31.md`
- Findings:
  - latest output contains zero-record data

### 4. default / hermes-cron-health-digest

- Job ID: `655dd227f390`
- Status: `ok`
- Last run: `2026-07-04T08:10:08.060162+07:00`
- Config: `/Users/ultrafriday/.hermes/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/cron/output/655dd227f390/2026-07-04_08-10-08.md`
- Findings:
  - latest output contains 401 unauthorized
  - latest output contains revoked/expired token

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
- Status: `error`
- Last run: `2026-07-04T09:02:45.024636+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/bolt/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/bolt/cron/output/8cf265b1a8e6/2026-07-04_09-02-43.md`
- Findings:
  - last_status=error

### 7. kaijeaw / kaijeaw-calendar-aware-workshop-content-pipeline

- Job ID: `2f06fffea29b`
- Status: `ok`
- Last run: `2026-07-05T07:21:05.935613+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/kaijeaw/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/kaijeaw/cron/output/2f06fffea29b/2026-07-05_07-21-04.md`
- Findings:
  - latest output contains revoked/expired token

### 8. kaijeaw / sunday-thai-faith-carousel-checkin

- Job ID: `a111b6f60774`
- Status: `ok`
- Last run: `2026-06-28T09:01:43.876226+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/kaijeaw/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/kaijeaw/cron/output/a111b6f60774/2026-06-28_09-01-42.md`
- Findings:
  - stale last_run ≈ 167h ago

### 9. qwen / qwen-morning-prep-for-kelly

- Job ID: `2ecf236f6cca`
- Status: `ok`
- Last run: `2026-07-05T07:20:17.682241+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/qwen/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/qwen/cron/output/2ecf236f6cca/2026-07-05_07-20-17.md`
- Findings:
  - latest output contains iCloud/resource deadlock

### 10. qwen / qwen-nightly-obsidian-hygiene

- Job ID: `b160922c0931`
- Status: `ok`
- Last run: `2026-07-04T23:33:25.528701+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/qwen/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/qwen/cron/output/b160922c0931/2026-07-04_23-33-25.md`
- Findings:
  - latest output contains iCloud/resource deadlock

### 11. qwen / qwen-todoist-worker

- Job ID: `1213c21e5430`
- Status: `ok`
- Last run: `2026-07-05T07:59:04.461188+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/qwen/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/qwen/cron/output/1213c21e5430/2026-07-05_07-59-04.md`
- Findings:
  - latest output contains iCloud/resource deadlock

### 12. qwen / qwen-agent-memory-guardian

- Job ID: `f4d9899e9bfc`
- Status: `ok`
- Last run: `2026-07-05T05:56:13.984152+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/qwen/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/qwen/cron/output/f4d9899e9bfc/2026-07-05_05-56-13.md`
- Findings:
  - latest output contains iCloud/resource deadlock

## Noisy output volumes

- default: 696 cron output files this week, 3.1 MB
- bolt: 1708 cron output files this week, 0.4 MB
- oracle: 189 cron output files this week, 4.0 MB
- qwen: 382 cron output files this week, 4.7 MB
- signal: 42 cron output files this week, 7.6 MB

## Recommended next actions

1. Fix token/OAuth jobs before rerunning dependent workflows.
2. Move mutable scanner state out of iCloud/Obsidian paths.
3. Fix profile cron delivery targets where `last_delivery_error` is present.
4. Convert high-volume unchanged sync jobs to silent/no-agent outputs.

_Secrets are redacted by this script; inspect referenced files locally if needed._
