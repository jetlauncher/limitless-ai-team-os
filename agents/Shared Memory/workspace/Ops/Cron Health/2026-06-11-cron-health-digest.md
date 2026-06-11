# Hermes Cron Health Digest — 2026-06-11

Generated: 2026-06-11 08:10:38 +07

Scanned **74** jobs across default + profiles; **63** active.

## Issues

### 1. default / important-email-alert-filter

- Job ID: `1cb288572dbf`
- Status: `ok`
- Last run: `2026-06-11T07:56:23.322066+07:00`
- Config: `/Users/ultrafriday/.hermes/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/cron/output/1cb288572dbf/2026-06-11_07-56-23.md`
- Findings:
  - latest output contains revoked/expired token

### 2. default / daily-evening-shutdown-briefing

- Job ID: `2bc4f618a2c1`
- Status: `ok`
- Last run: `2026-06-10T21:32:18.156534+07:00`
- Config: `/Users/ultrafriday/.hermes/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/cron/output/2bc4f618a2c1/2026-06-10_21-32-16.md`
- Findings:
  - latest output contains 401 unauthorized

### 3. default / weekly-ceo-review

- Job ID: `73d4312bcf3f`
- Status: `ok`
- Last run: `2026-06-07T20:03:33.294190+07:00`
- Config: `/Users/ultrafriday/.hermes/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/cron/output/73d4312bcf3f/2026-06-07_20-03-31.md`
- Findings:
  - stale last_run ≈ 84h ago
  - latest output contains 401 unauthorized

### 4. default / two-account-gmail-inbox-zero

- Job ID: `d1e3eedb44c2`
- Status: `error`
- Last run: `2026-06-11T08:00:37.174114+07:00`
- Config: `/Users/ultrafriday/.hermes/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/cron/output/d1e3eedb44c2/2026-06-11_08-00-37.md`
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

### 6. default / kelly-proactive-ops-radar-daily

- Job ID: `05f1e5bb26c6`
- Status: `ok`
- Last run: `2026-06-10T08:18:31.616671+07:00`
- Config: `/Users/ultrafriday/.hermes/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/cron/output/05f1e5bb26c6/2026-06-10_08-18-30.md`
- Findings:
  - latest output contains revoked/expired token

### 7. default / hermes-cron-health-digest

- Job ID: `655dd227f390`
- Status: `ok`
- Last run: `2026-06-10T08:10:53.682637+07:00`
- Config: `/Users/ultrafriday/.hermes/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/cron/output/655dd227f390/2026-06-10_08-10-35.md`
- Findings:
  - delivery error: delivery error: Telegram send failed: Timed out
  - latest output contains 401 unauthorized
  - latest output contains revoked/expired token
  - latest output contains traceback/error

### 8. default / google-youtube-oauth-token-health-check

- Job ID: `0439294d9bdf`
- Status: `ok`
- Last run: `2026-06-09T14:13:11.432704+07:00`
- Config: `/Users/ultrafriday/.hermes/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/cron/output/0439294d9bdf/2026-06-09_14-13-11.md`
- Findings:
  - latest output contains traceback/error

### 9. default / kelly-daily-next-7-calendar-time-block-scan

- Job ID: `8fcc64022fb5`
- Status: `ok`
- Last run: `2026-06-10T08:33:25.040741+07:00`
- Config: `/Users/ultrafriday/.hermes/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/cron/output/8fcc64022fb5/2026-06-10_08-33-23.md`
- Findings:
  - latest output contains revoked/expired token

### 10. default / limitless-daily-youtube-report

- Job ID: `8539c3349272`
- Status: `error`
- Last run: `2026-06-11T08:00:38.834291+07:00`
- Config: `/Users/ultrafriday/.hermes/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/cron/output/8539c3349272/2026-06-11_08-00-38.md`
- Findings:
  - last_status=error
  - latest output contains traceback/error

### 11. blaze / Jedi AI Creative Director Daily Pipeline

- Job ID: `255e748b82b1`
- Status: `ok`
- Last run: `2026-06-11T08:06:28.165419+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/blaze/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/blaze/cron/output/255e748b82b1/2026-06-11_08-06-26.md`
- Findings:
  - latest output contains traceback/error

### 12. bolt / Daily YouTube to Blog Check

- Job ID: `2aae2b04d926`
- Status: `ok`
- Last run: `2026-06-11T08:01:43.607494+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/bolt/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/bolt/cron/output/2aae2b04d926/2026-06-11_08-01-43.md`
- Findings:
  - latest output contains iCloud/resource deadlock

### 13. bolt / Jedi website production watchdog

- Job ID: `8cf265b1a8e6`
- Status: `error`
- Last run: `2026-06-10T09:02:50.181955+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/bolt/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/bolt/cron/output/8cf265b1a8e6/2026-06-10_09-02-49.md`
- Findings:
  - last_status=error

### 14. kaijeaw / kaijeaw-calendar-aware-workshop-content-pipeline

- Job ID: `2f06fffea29b`
- Status: `ok`
- Last run: `2026-06-11T07:23:09.483886+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/kaijeaw/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/kaijeaw/cron/output/2f06fffea29b/2026-06-11_07-23-08.md`
- Findings:
  - latest output contains 401 unauthorized
  - latest output contains revoked/expired token

### 15. kaijeaw / prepare-5-saturday-themes-for-jet

- Job ID: `91c2f104af0f`
- Status: `ok`
- Last run: `2026-06-06T08:01:58.470305+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/kaijeaw/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/kaijeaw/cron/output/91c2f104af0f/2026-06-06_08-01-57.md`
- Findings:
  - stale last_run ≈ 120h ago

### 16. kaijeaw / sunday-thai-faith-carousel-checkin

- Job ID: `a111b6f60774`
- Status: `ok`
- Last run: `2026-06-07T09:01:32.449104+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/kaijeaw/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/kaijeaw/cron/output/a111b6f60774/2026-06-07_09-01-31.md`
- Findings:
  - stale last_run ≈ 95h ago

### 17. qwen / qwen-morning-prep-for-kelly

- Job ID: `2ecf236f6cca`
- Status: `ok`
- Last run: `2026-06-11T07:17:59.293003+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/qwen/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/qwen/cron/output/2ecf236f6cca/2026-06-11_07-17-59.md`
- Findings:
  - latest output contains iCloud/resource deadlock

### 18. qwen / qwen-nightly-obsidian-hygiene

- Job ID: `b160922c0931`
- Status: `ok`
- Last run: `2026-06-10T23:37:12.210689+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/qwen/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/qwen/cron/output/b160922c0931/2026-06-10_23-37-12.md`
- Findings:
  - latest output contains iCloud/resource deadlock

### 19. qwen / qwen-todoist-worker

- Job ID: `1213c21e5430`
- Status: `ok`
- Last run: `2026-06-11T07:58:36.014876+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/qwen/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/qwen/cron/output/1213c21e5430/2026-06-11_07-58-36.md`
- Findings:
  - latest output contains iCloud/resource deadlock

### 20. qwen / qwen-comet-x-radar-hourly

- Job ID: `44f5881a93f9`
- Status: `error`
- Last run: `2026-06-11T07:52:38.312551+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/qwen/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/qwen/cron/output/44f5881a93f9/2026-06-11_07-52-38.md`
- Findings:
  - last_status=error

### 21. qwen / qwen-agent-memory-guardian

- Job ID: `f4d9899e9bfc`
- Status: `ok`
- Last run: `2026-06-11T07:57:21.110617+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/qwen/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/qwen/cron/output/f4d9899e9bfc/2026-06-11_07-57-21.md`
- Findings:
  - latest output contains iCloud/resource deadlock

### 22. unclechris / uncle-chris-portfolio-opportunity-check-5pm

- Job ID: `621654a5c632`
- Status: `error`
- Last run: `2026-06-10T17:00:11.399786+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/unclechris/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/unclechris/cron/output/621654a5c632/2026-06-10_17-00-10.md`
- Findings:
  - last_status=error

### 23. unclechris / Thai portfolio low-noise movement monitor

- Job ID: `a4ae310dc534`
- Status: `error`
- Last run: `2026-06-10T16:15:59.609685+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/unclechris/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/unclechris/cron/output/a4ae310dc534/2026-06-10_16-15-58.md`
- Findings:
  - last_status=error
  - latest output contains traceback/error

## Noisy output volumes

- default: 2991 cron output files this week, 8.6 MB
- bolt: 1762 cron output files this week, 0.5 MB
- oracle: 182 cron output files this week, 4.2 MB
- qwen: 369 cron output files this week, 2.8 MB
- signal: 116 cron output files this week, 23.6 MB

## Recommended next actions

1. Fix token/OAuth jobs before rerunning dependent workflows.
2. Move mutable scanner state out of iCloud/Obsidian paths.
3. Fix profile cron delivery targets where `last_delivery_error` is present.
4. Convert high-volume unchanged sync jobs to silent/no-agent outputs.

_Secrets are redacted by this script; inspect referenced files locally if needed._
