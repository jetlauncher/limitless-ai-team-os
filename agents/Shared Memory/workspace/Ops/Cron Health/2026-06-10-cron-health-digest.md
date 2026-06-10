# Hermes Cron Health Digest — 2026-06-10

Generated: 2026-06-10 08:10:33 +07

Scanned **74** jobs across default + profiles; **63** active.

## Issues

### 1. default / daily-good-morning-briefing

- Job ID: `83f630e1147b`
- Status: `ok`
- Last run: `2026-06-10T08:03:33.401467+07:00`
- Config: `/Users/ultrafriday/.hermes/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/cron/output/83f630e1147b/2026-06-10_08-03-32.md`
- Findings:
  - latest output contains 401 unauthorized

### 2. default / important-email-alert-filter

- Job ID: `1cb288572dbf`
- Status: `ok`
- Last run: `2026-06-10T07:52:40.645023+07:00`
- Config: `/Users/ultrafriday/.hermes/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/cron/output/1cb288572dbf/2026-06-10_07-52-40.md`
- Findings:
  - latest output contains revoked/expired token

### 3. default / weekly-ceo-review

- Job ID: `73d4312bcf3f`
- Status: `ok`
- Last run: `2026-06-07T20:03:33.294190+07:00`
- Config: `/Users/ultrafriday/.hermes/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/cron/output/73d4312bcf3f/2026-06-07_20-03-31.md`
- Findings:
  - stale last_run ≈ 60h ago
  - latest output contains 401 unauthorized

### 4. default / two-account-gmail-inbox-zero

- Job ID: `d1e3eedb44c2`
- Status: `error`
- Last run: `2026-06-10T08:00:32.429377+07:00`
- Config: `/Users/ultrafriday/.hermes/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/cron/output/d1e3eedb44c2/2026-06-10_08-00-32.md`
- Findings:
  - last_status=error

### 5. default / limitless-visibility-weekly-gsc-gap-report

- Job ID: `6a2606b41e59`
- Status: `error`
- Last run: `2026-06-08T09:00:20.698706+07:00`
- Config: `/Users/ultrafriday/.hermes/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/cron/output/6a2606b41e59/2026-06-08_09-00-20.md`
- Findings:
  - last_status=error
  - latest output contains revoked/expired token
  - latest output contains traceback/error

### 6. default / hermes-cron-health-digest

- Job ID: `655dd227f390`
- Status: `ok`
- Last run: `2026-06-09T08:10:24.074312+07:00`
- Config: `/Users/ultrafriday/.hermes/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/cron/output/655dd227f390/2026-06-09_08-10-22.md`
- Findings:
  - latest output contains 401 unauthorized
  - latest output contains revoked/expired token
  - latest output contains traceback/error

### 7. default / google-youtube-oauth-token-health-check

- Job ID: `0439294d9bdf`
- Status: `ok`
- Last run: `2026-06-09T14:13:11.432704+07:00`
- Config: `/Users/ultrafriday/.hermes/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/cron/output/0439294d9bdf/2026-06-09_14-13-11.md`
- Findings:
  - latest output contains traceback/error

### 8. default / kelly-daily-next-7-calendar-time-block-scan

- Job ID: `8fcc64022fb5`
- Status: `ok`
- Last run: `2026-06-09T08:33:48.598877+07:00`
- Config: `/Users/ultrafriday/.hermes/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/cron/output/8fcc64022fb5/2026-06-09_08-33-47.md`
- Findings:
  - latest output contains 401 unauthorized

### 9. default / limitless-daily-youtube-report

- Job ID: `8539c3349272`
- Status: `error`
- Last run: `2026-06-10T08:00:34.550821+07:00`
- Config: `/Users/ultrafriday/.hermes/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/cron/output/8539c3349272/2026-06-10_08-00-33.md`
- Findings:
  - last_status=error
  - latest output contains traceback/error

### 10. blaze / Jedi AI Creative Director Daily Pipeline

- Job ID: `255e748b82b1`
- Status: `ok`
- Last run: `2026-06-10T08:08:52.891147+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/blaze/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/blaze/cron/output/255e748b82b1/2026-06-10_08-08-51.md`
- Findings:
  - latest output contains traceback/error

### 11. bolt / Daily YouTube to Blog Check

- Job ID: `2aae2b04d926`
- Status: `ok`
- Last run: `2026-06-10T08:02:07.861469+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/bolt/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/bolt/cron/output/2aae2b04d926/2026-06-10_08-02-07.md`
- Findings:
  - latest output contains iCloud/resource deadlock

### 12. bolt / Jedi website production watchdog

- Job ID: `8cf265b1a8e6`
- Status: `error`
- Last run: `2026-06-09T09:02:50.173287+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/bolt/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/bolt/cron/output/8cf265b1a8e6/2026-06-09_09-02-49.md`
- Findings:
  - last_status=error

### 13. kaijeaw / kaijeaw-calendar-aware-workshop-content-pipeline

- Job ID: `2f06fffea29b`
- Status: `ok`
- Last run: `2026-06-10T07:23:17.344441+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/kaijeaw/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/kaijeaw/cron/output/2f06fffea29b/2026-06-10_07-23-16.md`
- Findings:
  - latest output contains revoked/expired token

### 14. kaijeaw / prepare-5-saturday-themes-for-jet

- Job ID: `91c2f104af0f`
- Status: `ok`
- Last run: `2026-06-06T08:01:58.470305+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/kaijeaw/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/kaijeaw/cron/output/91c2f104af0f/2026-06-06_08-01-57.md`
- Findings:
  - stale last_run ≈ 96h ago

### 15. kaijeaw / sunday-thai-faith-carousel-checkin

- Job ID: `a111b6f60774`
- Status: `ok`
- Last run: `2026-06-07T09:01:32.449104+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/kaijeaw/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/kaijeaw/cron/output/a111b6f60774/2026-06-07_09-01-31.md`
- Findings:
  - stale last_run ≈ 71h ago

### 16. qwen / qwen-morning-prep-for-kelly

- Job ID: `2ecf236f6cca`
- Status: `ok`
- Last run: `2026-06-10T07:17:52.326854+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/qwen/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/qwen/cron/output/2ecf236f6cca/2026-06-10_07-17-52.md`
- Findings:
  - latest output contains iCloud/resource deadlock

### 17. qwen / qwen-nightly-obsidian-hygiene

- Job ID: `b160922c0931`
- Status: `ok`
- Last run: `2026-06-09T23:35:04.474973+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/qwen/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/qwen/cron/output/b160922c0931/2026-06-09_23-35-04.md`
- Findings:
  - latest output contains iCloud/resource deadlock

### 18. qwen / qwen-todoist-worker

- Job ID: `1213c21e5430`
- Status: `ok`
- Last run: `2026-06-10T07:25:48.369648+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/qwen/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/qwen/cron/output/1213c21e5430/2026-06-10_07-25-48.md`
- Findings:
  - latest output contains iCloud/resource deadlock

### 19. qwen / qwen-comet-x-radar-hourly

- Job ID: `44f5881a93f9`
- Status: `error`
- Last run: `2026-06-10T08:03:46.202377+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/qwen/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/qwen/cron/output/44f5881a93f9/2026-06-10_08-03-46.md`
- Findings:
  - last_status=error

### 20. qwen / qwen-agent-memory-guardian

- Job ID: `f4d9899e9bfc`
- Status: `ok`
- Last run: `2026-06-10T06:51:31.084973+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/qwen/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/qwen/cron/output/f4d9899e9bfc/2026-06-10_06-51-31.md`
- Findings:
  - latest output contains iCloud/resource deadlock

### 21. unclechris / uncle-chris-portfolio-opportunity-check-5pm

- Job ID: `621654a5c632`
- Status: `error`
- Last run: `2026-06-09T17:00:13.697560+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/unclechris/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/unclechris/cron/output/621654a5c632/2026-06-09_17-00-12.md`
- Findings:
  - last_status=error

### 22. unclechris / Thai portfolio low-noise movement monitor

- Job ID: `a4ae310dc534`
- Status: `error`
- Last run: `2026-06-09T16:15:01.288245+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/unclechris/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/unclechris/cron/output/a4ae310dc534/2026-06-09_16-15-00.md`
- Findings:
  - last_status=error
  - latest output contains traceback/error

## Noisy output volumes

- default: 2786 cron output files this week, 9.4 MB
- bolt: 1802 cron output files this week, 0.5 MB
- oracle: 183 cron output files this week, 4.4 MB
- qwen: 366 cron output files this week, 2.8 MB
- signal: 132 cron output files this week, 26.9 MB

## Recommended next actions

1. Fix token/OAuth jobs before rerunning dependent workflows.
2. Move mutable scanner state out of iCloud/Obsidian paths.
3. Fix profile cron delivery targets where `last_delivery_error` is present.
4. Convert high-volume unchanged sync jobs to silent/no-agent outputs.

_Secrets are redacted by this script; inspect referenced files locally if needed._
