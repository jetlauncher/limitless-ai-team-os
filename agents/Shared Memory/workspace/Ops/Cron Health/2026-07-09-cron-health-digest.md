# Hermes Cron Health Digest — 2026-07-09

Generated: 2026-07-09 08:10:29 +07

Scanned **82** jobs across default + profiles; **59** active.

## Issues

### 1. default / weekly-ceo-review

- Job ID: `73d4312bcf3f`
- Status: `ok`
- Last run: `2026-07-05T20:04:11.444704+07:00`
- Config: `/Users/ultrafriday/.hermes/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/cron/output/73d4312bcf3f/2026-07-05_20-04-10.md`
- Findings:
  - stale last_run ≈ 84h ago

### 2. default / hermes-cron-health-digest

- Job ID: `655dd227f390`
- Status: `ok`
- Last run: `2026-07-08T08:10:21.739612+07:00`
- Config: `/Users/ultrafriday/.hermes/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/cron/output/655dd227f390/2026-07-08_08-10-21.md`
- Findings:
  - latest output contains 401 unauthorized
  - latest output contains revoked/expired token
  - latest output contains traceback/error

### 3. default / google-youtube-oauth-token-health-check

- Job ID: `0439294d9bdf`
- Status: `ok`
- Last run: `2026-07-07T14:16:13.346003+07:00`
- Config: `/Users/ultrafriday/.hermes/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/cron/output/0439294d9bdf/2026-07-07_14-16-13.md`
- Findings:
  - latest output contains traceback/error

### 4. default / limitless-daily-youtube-report

- Job ID: `8539c3349272`
- Status: `error`
- Last run: `2026-07-09T08:00:29.036935+07:00`
- Config: `/Users/ultrafriday/.hermes/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/cron/output/8539c3349272/2026-07-09_08-00-27.md`
- Findings:
  - last_status=error
  - latest output contains traceback/error

### 5. default / class-roster-intelligence-day-before

- Job ID: `c315042fec3f`
- Status: `error`
- Last run: `2026-07-08T18:00:59.836835+07:00`
- Config: `/Users/ultrafriday/.hermes/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/cron/output/c315042fec3f/2026-07-08_18-00-58.md`
- Findings:
  - last_status=error
  - latest output contains traceback/error

### 6. default / weekly-hermes-janitor

- Job ID: `a930198fa9cb`
- Status: `ok`
- Last run: `2026-07-05T03:00:43.971941+07:00`
- Config: `/Users/ultrafriday/.hermes/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/cron/output/a930198fa9cb/2026-07-05_03-00-42.md`
- Findings:
  - stale last_run ≈ 101h ago
  - latest output contains traceback/error

### 7. bolt / Daily YouTube to Blog Check

- Job ID: `2aae2b04d926`
- Status: `ok`
- Last run: `2026-07-09T08:09:22.617331+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/bolt/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/bolt/cron/output/2aae2b04d926/2026-07-09_08-09-22.md`
- Findings:
  - latest output contains revoked/expired token

### 8. bolt / Jedi website production watchdog

- Job ID: `8cf265b1a8e6`
- Status: `ok`
- Last run: `2026-07-08T11:12:04.524156+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/bolt/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/bolt/cron/output/8cf265b1a8e6/2026-07-08_11-12-03.md`
- Findings:
  - latest output contains 401 unauthorized

### 9. bolt / Daily Hermes update monitor

- Job ID: `0027fbd483ea`
- Status: `ok`
- Last run: `2026-07-07T10:08:04.229108+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/bolt/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/bolt/cron/output/0027fbd483ea/2026-07-07_10-08-02.md`
- Findings:
  - latest output contains 401 unauthorized

### 10. kaijeaw / kaijeaw-calendar-aware-workshop-content-pipeline

- Job ID: `2f06fffea29b`
- Status: `ok`
- Last run: `2026-07-09T07:17:20.275713+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/kaijeaw/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/kaijeaw/cron/output/2f06fffea29b/2026-07-09_07-17-19.md`
- Findings:
  - latest output contains revoked/expired token

### 11. kaijeaw / prepare-5-saturday-themes-for-jet

- Job ID: `91c2f104af0f`
- Status: `ok`
- Last run: `2026-07-04T08:01:26.543508+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/kaijeaw/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/kaijeaw/cron/output/91c2f104af0f/2026-07-04_08-01-25.md`
- Findings:
  - stale last_run ≈ 120h ago

### 12. kaijeaw / sunday-thai-faith-carousel-checkin

- Job ID: `a111b6f60774`
- Status: `ok`
- Last run: `2026-07-05T09:03:53.009053+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/kaijeaw/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/kaijeaw/cron/output/a111b6f60774/2026-07-05_09-03-51.md`
- Findings:
  - stale last_run ≈ 95h ago

### 13. qwen / qwen-morning-prep-for-kelly

- Job ID: `2ecf236f6cca`
- Status: `ok`
- Last run: `2026-07-09T07:17:43.905967+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/qwen/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/qwen/cron/output/2ecf236f6cca/2026-07-09_07-17-43.md`
- Findings:
  - latest output contains iCloud/resource deadlock

### 14. qwen / qwen-nightly-obsidian-hygiene

- Job ID: `b160922c0931`
- Status: `ok`
- Last run: `2026-07-08T23:33:16.119347+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/qwen/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/qwen/cron/output/b160922c0931/2026-07-08_23-33-16.md`
- Findings:
  - latest output contains iCloud/resource deadlock

### 15. qwen / qwen-todoist-worker

- Job ID: `1213c21e5430`
- Status: `ok`
- Last run: `2026-07-09T07:56:06.448883+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/qwen/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/qwen/cron/output/1213c21e5430/2026-07-09_07-56-06.md`
- Findings:
  - latest output contains iCloud/resource deadlock

### 16. signal / signal-ai-morning-brief

- Job ID: `d194c1c29c42`
- Status: `error`
- Last run: `2026-07-08T09:29:02.833443+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/signal/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/signal/cron/output/d194c1c29c42/2026-07-08_09-29-01.md`
- Findings:
  - last_status=error

## Noisy output volumes

- default: 701 cron output files this week, 3.2 MB
- qwen: 206 cron output files this week, 3.6 MB
- signal: 41 cron output files this week, 7.4 MB

## Recommended next actions

1. Fix token/OAuth jobs before rerunning dependent workflows.
2. Move mutable scanner state out of iCloud/Obsidian paths.
3. Fix profile cron delivery targets where `last_delivery_error` is present.
4. Convert high-volume unchanged sync jobs to silent/no-agent outputs.

_Secrets are redacted by this script; inspect referenced files locally if needed._
