# Hermes Cron Health Digest — 2026-06-19

Generated: 2026-06-19 08:10:02 +07

Scanned **76** jobs across default + profiles; **56** active.

## Issues

### 1. default / limitless-daily-revenue-report

- Job ID: `11673b81389e`
- Status: `ok`
- Last run: `2026-06-18T09:01:48.919508+07:00`
- Config: `/Users/ultrafriday/.hermes/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/cron/output/11673b81389e/2026-06-18_09-01-47.md`
- Findings:
  - latest output contains traceback/error

### 2. default / important-email-alert-filter

- Job ID: `1cb288572dbf`
- Status: `ok`
- Last run: `2026-06-19T07:57:49.368463+07:00`
- Config: `/Users/ultrafriday/.hermes/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/cron/output/1cb288572dbf/2026-06-19_07-57-49.md`
- Findings:
  - latest output contains revoked/expired token

### 3. default / weekly-ceo-review

- Job ID: `73d4312bcf3f`
- Status: `ok`
- Last run: `2026-06-14T20:06:06.561365+07:00`
- Config: `/Users/ultrafriday/.hermes/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/cron/output/73d4312bcf3f/2026-06-14_20-06-05.md`
- Findings:
  - stale last_run ≈ 108h ago

### 4. default / hermes-cron-health-digest

- Job ID: `655dd227f390`
- Status: `ok`
- Last run: `2026-06-18T08:10:11.770219+07:00`
- Config: `/Users/ultrafriday/.hermes/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/cron/output/655dd227f390/2026-06-18_08-10-10.md`
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
  - latest output contains traceback/error

### 6. bolt / Jedi website production watchdog

- Job ID: `8cf265b1a8e6`
- Status: `error`
- Last run: `2026-06-18T09:02:48.575497+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/bolt/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/bolt/cron/output/8cf265b1a8e6/2026-06-18_09-02-47.md`
- Findings:
  - last_status=error

### 7. kaijeaw / kaijeaw-calendar-aware-workshop-content-pipeline

- Job ID: `2f06fffea29b`
- Status: `ok`
- Last run: `2026-06-19T07:28:03.262273+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/kaijeaw/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/kaijeaw/cron/output/2f06fffea29b/2026-06-19_07-28-02.md`
- Findings:
  - latest output contains revoked/expired token
  - latest output contains iCloud/resource deadlock

### 8. kaijeaw / prepare-5-saturday-themes-for-jet

- Job ID: `91c2f104af0f`
- Status: `ok`
- Last run: `2026-06-13T08:01:50.785092+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/kaijeaw/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/kaijeaw/cron/output/91c2f104af0f/2026-06-13_08-01-49.md`
- Findings:
  - stale last_run ≈ 144h ago

### 9. kaijeaw / sunday-thai-faith-carousel-checkin

- Job ID: `a111b6f60774`
- Status: `ok`
- Last run: `2026-06-14T09:01:38.778780+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/kaijeaw/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/kaijeaw/cron/output/a111b6f60774/2026-06-14_09-01-37.md`
- Findings:
  - stale last_run ≈ 119h ago

### 10. qwen / qwen-morning-prep-for-kelly

- Job ID: `2ecf236f6cca`
- Status: `ok`
- Last run: `2026-06-19T07:16:45.768385+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/qwen/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/qwen/cron/output/2ecf236f6cca/2026-06-19_07-16-45.md`
- Findings:
  - latest output contains iCloud/resource deadlock

### 11. qwen / qwen-nightly-obsidian-hygiene

- Job ID: `b160922c0931`
- Status: `ok`
- Last run: `2026-06-18T23:36:00.644546+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/qwen/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/qwen/cron/output/b160922c0931/2026-06-18_23-36-00.md`
- Findings:
  - latest output contains iCloud/resource deadlock

## Noisy output volumes

- default: 3404 cron output files this week, 6.7 MB
- bolt: 1499 cron output files this week, 0.4 MB
- oracle: 160 cron output files this week, 3.6 MB
- qwen: 328 cron output files this week, 2.6 MB

## Recommended next actions

1. Fix token/OAuth jobs before rerunning dependent workflows.
2. Move mutable scanner state out of iCloud/Obsidian paths.
3. Fix profile cron delivery targets where `last_delivery_error` is present.
4. Convert high-volume unchanged sync jobs to silent/no-agent outputs.

_Secrets are redacted by this script; inspect referenced files locally if needed._
