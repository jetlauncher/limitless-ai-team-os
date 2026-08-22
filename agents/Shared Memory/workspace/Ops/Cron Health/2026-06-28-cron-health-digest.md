# Hermes Cron Health Digest — 2026-06-28

Generated: 2026-06-28 08:10:11 +07

Scanned **77** jobs across default + profiles; **58** active.

## Issues

### 1. default / limitless-x-to-obsidian-hourly

- Job ID: `9a5c42413ac6`
- Status: `ok`
- Last run: `2026-06-28T08:06:40.006519+07:00`
- Config: `/Users/ultrafriday/.hermes/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/cron/output/9a5c42413ac6/2026-06-28_08-06-40.md`
- Findings:
  - latest output contains zero-record data

### 2. default / weekly-ceo-review

- Job ID: `73d4312bcf3f`
- Status: `ok`
- Last run: `2026-06-21T20:05:51.250932+07:00`
- Config: `/Users/ultrafriday/.hermes/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/cron/output/73d4312bcf3f/2026-06-21_20-05-50.md`
- Findings:
  - stale last_run ≈ 156h ago

### 3. default / hermes-cron-health-digest

- Job ID: `655dd227f390`
- Status: `ok`
- Last run: `2026-06-27T08:10:44.164927+07:00`
- Config: `/Users/ultrafriday/.hermes/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/cron/output/655dd227f390/2026-06-27_08-10-44.md`
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
  - stale last_run ≈ 66h ago
  - latest output contains traceback/error

### 5. blaze / Daily Signal-Informed X Post Ideas for Jet Selection

- Job ID: `929b8a33a119`
- Status: `ok`
- Last run: `2026-06-27T08:16:18.131262+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/blaze/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/blaze/cron/output/929b8a33a119/2026-06-27_08-16-14.md`
- Findings:
  - latest output contains revoked/expired token

### 6. kaijeaw / kaijeaw-calendar-aware-workshop-content-pipeline

- Job ID: `2f06fffea29b`
- Status: `ok`
- Last run: `2026-06-28T07:20:16.194795+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/kaijeaw/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/kaijeaw/cron/output/2f06fffea29b/2026-06-28_07-20-15.md`
- Findings:
  - latest output contains revoked/expired token

### 7. kaijeaw / sunday-thai-faith-carousel-checkin

- Job ID: `a111b6f60774`
- Status: `ok`
- Last run: `2026-06-21T09:01:16.119080+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/kaijeaw/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/kaijeaw/cron/output/a111b6f60774/2026-06-21_09-01-14.md`
- Findings:
  - stale last_run ≈ 167h ago

### 8. qwen / qwen-morning-prep-for-kelly

- Job ID: `2ecf236f6cca`
- Status: `ok`
- Last run: `2026-06-28T07:16:52.081740+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/qwen/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/qwen/cron/output/2ecf236f6cca/2026-06-28_07-16-52.md`
- Findings:
  - latest output contains iCloud/resource deadlock

### 9. qwen / qwen-nightly-obsidian-hygiene

- Job ID: `b160922c0931`
- Status: `ok`
- Last run: `2026-06-27T23:32:26.043913+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/qwen/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/qwen/cron/output/b160922c0931/2026-06-27_23-32-26.md`
- Findings:
  - latest output contains iCloud/resource deadlock

### 10. qwen / qwen-todoist-worker

- Job ID: `1213c21e5430`
- Status: `ok`
- Last run: `2026-06-28T07:43:33.207809+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/qwen/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/qwen/cron/output/1213c21e5430/2026-06-28_07-43-33.md`
- Findings:
  - latest output contains iCloud/resource deadlock

### 11. qwen / qwen-agent-memory-guardian

- Job ID: `f4d9899e9bfc`
- Status: `ok`
- Last run: `2026-06-28T07:34:12.483315+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/qwen/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/qwen/cron/output/f4d9899e9bfc/2026-06-28_07-34-12.md`
- Findings:
  - latest output contains iCloud/resource deadlock

## Noisy output volumes

- default: 5586 cron output files this week, 8.8 MB
- bolt: 1676 cron output files this week, 0.4 MB
- oracle: 187 cron output files this week, 4.0 MB
- qwen: 380 cron output files this week, 3.9 MB
- signal: 36 cron output files this week, 6.3 MB

## Recommended next actions

1. Fix token/OAuth jobs before rerunning dependent workflows.
2. Move mutable scanner state out of iCloud/Obsidian paths.
3. Fix profile cron delivery targets where `last_delivery_error` is present.
4. Convert high-volume unchanged sync jobs to silent/no-agent outputs.

_Secrets are redacted by this script; inspect referenced files locally if needed._
