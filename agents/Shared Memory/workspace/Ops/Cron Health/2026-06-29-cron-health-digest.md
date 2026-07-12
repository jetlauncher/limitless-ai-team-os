# Hermes Cron Health Digest — 2026-06-29

Generated: 2026-06-29 09:05:56 +07

Scanned **77** jobs across default + profiles; **58** active.

## Issues

### 1. default / limitless-x-to-obsidian-hourly

- Job ID: `9a5c42413ac6`
- Status: `ok`
- Last run: `2026-06-29T08:45:11.517761+07:00`
- Config: `/Users/ultrafriday/.hermes/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/cron/output/9a5c42413ac6/2026-06-29_08-45-11.md`
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

### 3. default / google-youtube-oauth-token-health-check

- Job ID: `0439294d9bdf`
- Status: `ok`
- Last run: `2026-06-25T14:14:41.735711+07:00`
- Config: `/Users/ultrafriday/.hermes/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/cron/output/0439294d9bdf/2026-06-25_14-14-41.md`
- Findings:
  - stale last_run ≈ 91h ago
  - latest output contains traceback/error

### 4. kaijeaw / kaijeaw-calendar-aware-workshop-content-pipeline

- Job ID: `2f06fffea29b`
- Status: `ok`
- Last run: `2026-06-29T07:17:37.792069+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/kaijeaw/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/kaijeaw/cron/output/2f06fffea29b/2026-06-29_07-17-36.md`
- Findings:
  - latest output contains revoked/expired token

### 5. kaijeaw / prepare-5-saturday-themes-for-jet

- Job ID: `91c2f104af0f`
- Status: `ok`
- Last run: `2026-06-27T08:00:56.787621+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/kaijeaw/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/kaijeaw/cron/output/91c2f104af0f/2026-06-27_08-00-55.md`
- Findings:
  - stale last_run ≈ 49h ago

### 6. oracle / oracle-daily-telegram-summary

- Job ID: `5bf33a5928f9`
- Status: `ok`
- Last run: `2026-06-28T22:46:35.177372+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/oracle/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/oracle/cron/output/5bf33a5928f9/2026-06-28_22-46-34.md`
- Findings:
  - latest output contains zero-record data

### 7. qwen / qwen-morning-prep-for-kelly

- Job ID: `2ecf236f6cca`
- Status: `ok`
- Last run: `2026-06-29T07:17:28.080194+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/qwen/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/qwen/cron/output/2ecf236f6cca/2026-06-29_07-17-28.md`
- Findings:
  - latest output contains iCloud/resource deadlock

### 8. qwen / qwen-nightly-obsidian-hygiene

- Job ID: `b160922c0931`
- Status: `ok`
- Last run: `2026-06-28T23:32:24.564295+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/qwen/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/qwen/cron/output/b160922c0931/2026-06-28_23-32-24.md`
- Findings:
  - latest output contains iCloud/resource deadlock

### 9. qwen / qwen-todoist-worker

- Job ID: `1213c21e5430`
- Status: `ok`
- Last run: `2026-06-29T08:00:47.800916+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/qwen/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/qwen/cron/output/1213c21e5430/2026-06-29_08-00-47.md`
- Findings:
  - latest output contains iCloud/resource deadlock

### 10. qwen / qwen-agent-memory-guardian

- Job ID: `f4d9899e9bfc`
- Status: `ok`
- Last run: `2026-06-29T07:46:28.529553+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/qwen/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/qwen/cron/output/f4d9899e9bfc/2026-06-29_07-46-28.md`
- Findings:
  - latest output contains iCloud/resource deadlock

### 11. unclechris / uncle-chris-us-brief

- Job ID: `b0acc82297d8`
- Status: `ok`
- Last run: `2026-06-28T21:31:55.095424+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/unclechris/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/unclechris/cron/output/b0acc82297d8/2026-06-28_21-31-53.md`
- Findings:
  - latest output contains 401 unauthorized

## Noisy output volumes

- default: 5581 cron output files this week, 8.8 MB
- bolt: 1676 cron output files this week, 0.4 MB
- oracle: 187 cron output files this week, 4.0 MB
- qwen: 380 cron output files this week, 4.0 MB
- signal: 39 cron output files this week, 6.9 MB

## Recommended next actions

1. Fix token/OAuth jobs before rerunning dependent workflows.
2. Move mutable scanner state out of iCloud/Obsidian paths.
3. Fix profile cron delivery targets where `last_delivery_error` is present.
4. Convert high-volume unchanged sync jobs to silent/no-agent outputs.

_Secrets are redacted by this script; inspect referenced files locally if needed._
