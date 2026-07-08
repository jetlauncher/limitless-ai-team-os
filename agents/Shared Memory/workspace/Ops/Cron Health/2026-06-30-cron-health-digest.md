# Hermes Cron Health Digest — 2026-06-30

Generated: 2026-06-30 08:10:58 +07

Scanned **78** jobs across default + profiles; **60** active.

## Issues

### 1. default / limitless-x-to-obsidian-hourly

- Job ID: `9a5c42413ac6`
- Status: `ok`
- Last run: `2026-06-30T07:30:58.685309+07:00`
- Config: `/Users/ultrafriday/.hermes/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/cron/output/9a5c42413ac6/2026-06-30_07-30-58.md`
- Findings:
  - latest output contains zero-record data

### 2. default / hermes-cron-health-digest

- Job ID: `655dd227f390`
- Status: `ok`
- Last run: `2026-06-29T08:10:40.948879+07:00`
- Config: `/Users/ultrafriday/.hermes/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/cron/output/655dd227f390/2026-06-29_08-10-40.md`
- Findings:
  - latest output contains 401 unauthorized
  - latest output contains revoked/expired token
  - latest output contains traceback/error

### 3. kaijeaw / kaijeaw-calendar-aware-workshop-content-pipeline

- Job ID: `2f06fffea29b`
- Status: `ok`
- Last run: `2026-06-30T07:16:50.208337+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/kaijeaw/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/kaijeaw/cron/output/2f06fffea29b/2026-06-30_07-16-48.md`
- Findings:
  - latest output contains revoked/expired token

### 4. kaijeaw / prepare-5-saturday-themes-for-jet

- Job ID: `91c2f104af0f`
- Status: `ok`
- Last run: `2026-06-27T08:00:56.787621+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/kaijeaw/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/kaijeaw/cron/output/91c2f104af0f/2026-06-27_08-00-55.md`
- Findings:
  - stale last_run ≈ 72h ago

### 5. qwen / qwen-morning-prep-for-kelly

- Job ID: `2ecf236f6cca`
- Status: `ok`
- Last run: `2026-06-30T07:16:40.057606+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/qwen/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/qwen/cron/output/2ecf236f6cca/2026-06-30_07-16-40.md`
- Findings:
  - latest output contains iCloud/resource deadlock

### 6. qwen / qwen-nightly-obsidian-hygiene

- Job ID: `b160922c0931`
- Status: `ok`
- Last run: `2026-06-29T23:32:09.499720+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/qwen/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/qwen/cron/output/b160922c0931/2026-06-29_23-32-09.md`
- Findings:
  - latest output contains iCloud/resource deadlock

### 7. qwen / qwen-todoist-worker

- Job ID: `1213c21e5430`
- Status: `ok`
- Last run: `2026-06-30T06:21:39.236732+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/qwen/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/qwen/cron/output/1213c21e5430/2026-06-30_06-21-39.md`
- Findings:
  - latest output contains iCloud/resource deadlock

### 8. qwen / qwen-agent-memory-guardian

- Job ID: `f4d9899e9bfc`
- Status: `ok`
- Last run: `2026-06-30T04:22:11.346471+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/qwen/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/qwen/cron/output/f4d9899e9bfc/2026-06-30_04-22-11.md`
- Findings:
  - latest output contains iCloud/resource deadlock

## Noisy output volumes

- default: 628 cron output files this week, 2.7 MB
- bolt: 1677 cron output files this week, 0.4 MB
- oracle: 187 cron output files this week, 4.0 MB
- qwen: 378 cron output files this week, 4.0 MB
- signal: 40 cron output files this week, 7.2 MB

## Recommended next actions

1. Fix token/OAuth jobs before rerunning dependent workflows.
2. Move mutable scanner state out of iCloud/Obsidian paths.
3. Fix profile cron delivery targets where `last_delivery_error` is present.
4. Convert high-volume unchanged sync jobs to silent/no-agent outputs.

_Secrets are redacted by this script; inspect referenced files locally if needed._
