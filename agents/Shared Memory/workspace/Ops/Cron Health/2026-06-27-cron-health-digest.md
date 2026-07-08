# Hermes Cron Health Digest — 2026-06-27

Generated: 2026-06-27 08:10:41 +07

Scanned **76** jobs across default + profiles; **57** active.

## Issues

### 1. default / limitless-x-to-obsidian-hourly

- Job ID: `9a5c42413ac6`
- Status: `ok`
- Last run: `2026-06-27T07:29:57.952328+07:00`
- Config: `/Users/ultrafriday/.hermes/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/cron/output/9a5c42413ac6/2026-06-27_07-29-57.md`
- Findings:
  - latest output contains zero-record data

### 2. default / weekly-ceo-review

- Job ID: `73d4312bcf3f`
- Status: `ok`
- Last run: `2026-06-21T20:05:51.250932+07:00`
- Config: `/Users/ultrafriday/.hermes/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/cron/output/73d4312bcf3f/2026-06-21_20-05-50.md`
- Findings:
  - stale last_run ≈ 132h ago

### 3. default / hermes-cron-health-digest

- Job ID: `655dd227f390`
- Status: `ok`
- Last run: `2026-06-26T10:54:23.796849+07:00`
- Config: `/Users/ultrafriday/.hermes/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/cron/output/655dd227f390/2026-06-26_10-54-23.md`
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
  - latest output contains traceback/error

### 5. kaijeaw / kaijeaw-calendar-aware-workshop-content-pipeline

- Job ID: `2f06fffea29b`
- Status: `ok`
- Last run: `2026-06-27T07:21:33.625885+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/kaijeaw/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/kaijeaw/cron/output/2f06fffea29b/2026-06-27_07-21-32.md`
- Findings:
  - latest output contains revoked/expired token

### 6. kaijeaw / sunday-thai-faith-carousel-checkin

- Job ID: `a111b6f60774`
- Status: `ok`
- Last run: `2026-06-21T09:01:16.119080+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/kaijeaw/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/kaijeaw/cron/output/a111b6f60774/2026-06-21_09-01-14.md`
- Findings:
  - stale last_run ≈ 143h ago

## Noisy output volumes

- default: 5211 cron output files this week, 8.1 MB
- bolt: 1565 cron output files this week, 0.4 MB
- oracle: 176 cron output files this week, 3.8 MB
- qwen: 352 cron output files this week, 3.5 MB
- signal: 32 cron output files this week, 5.6 MB

## Recommended next actions

1. Fix token/OAuth jobs before rerunning dependent workflows.
2. Move mutable scanner state out of iCloud/Obsidian paths.
3. Fix profile cron delivery targets where `last_delivery_error` is present.
4. Convert high-volume unchanged sync jobs to silent/no-agent outputs.

_Secrets are redacted by this script; inspect referenced files locally if needed._
