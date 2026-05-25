# Hermes Cron Health Digest — 2026-05-24

Generated: 2026-05-24 11:55:09 +07

Scanned **55** jobs across default + profiles; **48** active.

## Issues

### 1. default / limitless-hourly-airtable-snapshot

- Job ID: `b22b3ce9203e`
- Status: `ok`
- Last run: `2026-05-24T11:54:38.424662+07:00`
- Config: `/Users/ultrafriday/.hermes/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/cron/output/b22b3ce9203e/2026-05-24_11-54-37.md`
- Findings:
  - latest output contains 401 unauthorized
  - latest output contains revoked/expired token
  - latest output contains zero-record data

### 2. default / limitless-x-to-obsidian-hourly

- Job ID: `9a5c42413ac6`
- Status: `ok`
- Last run: `2026-05-24T10:32:51.960732+07:00`
- Config: `/Users/ultrafriday/.hermes/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/cron/output/9a5c42413ac6/2026-05-24_10-32-51.md`
- Findings:
  - latest output contains zero-record data

### 3. default / limitless-x-daily-report

- Job ID: `3e00a7f3524f`
- Status: `ok`
- Last run: `2026-05-23T18:15:58.947311+07:00`
- Config: `/Users/ultrafriday/.hermes/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/cron/output/3e00a7f3524f/2026-05-23_18-15-57.md`
- Findings:
  - delivery error: delivery error: Telegram send failed: Unknown error in HTTP implementation: RuntimeError('cannot schedule new futures after interpreter shutdown')
  - latest output contains iCloud/resource deadlock
  - latest output contains traceback/error

### 4. default / important-email-alert-filter

- Job ID: `1cb288572dbf`
- Status: `ok`
- Last run: `2026-05-24T11:49:39.238410+07:00`
- Config: `/Users/ultrafriday/.hermes/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/cron/output/1cb288572dbf/2026-05-24_11-49-37.md`
- Findings:
  - latest output contains revoked/expired token

### 5. default / weekly-ceo-review

- Job ID: `73d4312bcf3f`
- Status: `ok`
- Last run: `2026-05-17T20:16:52.613846+07:00`
- Config: `/Users/ultrafriday/.hermes/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/cron/output/73d4312bcf3f/2026-05-17_20-16-51.md`
- Findings:
  - stale last_run ≈ 160h ago

### 6. default / daily-limitless-ai-team-os-repo-refresh

- Job ID: `b54b00ce6f12`
- Status: `ok`
- Last run: `2026-05-24T03:33:35.953208+07:00`
- Config: `/Users/ultrafriday/.hermes/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/cron/output/b54b00ce6f12/2026-05-24_03-33-35.md`
- Findings:
  - latest output contains iCloud/resource deadlock

### 7. default / two-account-gmail-inbox-zero

- Job ID: `d1e3eedb44c2`
- Status: `error`
- Last run: `2026-05-24T10:00:48.874548+07:00`
- Config: `/Users/ultrafriday/.hermes/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/cron/output/d1e3eedb44c2/2026-05-24_10-00-48.md`
- Findings:
  - last_status=error
  - latest output contains revoked/expired token
  - latest output contains traceback/error

### 8. default / limitless-visibility-weekly-gsc-gap-report

- Job ID: `6a2606b41e59`
- Status: `error`
- Last run: `2026-05-18T09:11:45.226983+07:00`
- Config: `/Users/ultrafriday/.hermes/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/cron/output/6a2606b41e59/2026-05-18_09-11-44.md`
- Findings:
  - last_status=error
  - latest output contains revoked/expired token
  - latest output contains traceback/error

### 9. default / kelly-proactive-ops-radar-daily

- Job ID: `05f1e5bb26c6`
- Status: `ok`
- Last run: `2026-05-24T08:17:01.723861+07:00`
- Config: `/Users/ultrafriday/.hermes/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/cron/output/05f1e5bb26c6/2026-05-24_08-17-01.md`
- Findings:
  - latest output contains revoked/expired token
  - latest output contains iCloud/resource deadlock

### 10. default / jet-workspace-digest-scan-nightly

- Job ID: `07cfbc10c14b`
- Status: `error`
- Last run: `2026-05-24T06:46:35.829909+07:00`
- Config: `/Users/ultrafriday/.hermes/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/cron/output/07cfbc10c14b/2026-05-24_06-46-35.md`
- Findings:
  - last_status=error
  - latest output contains iCloud/resource deadlock
  - latest output contains traceback/error

### 11. default / jet-personal-artifacts-scan-daily

- Job ID: `3177ae5a9725`
- Status: `error`
- Last run: `2026-05-24T06:50:46.298456+07:00`
- Config: `/Users/ultrafriday/.hermes/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/cron/output/3177ae5a9725/2026-05-24_06-50-45.md`
- Findings:
  - last_status=error
  - latest output contains iCloud/resource deadlock
  - latest output contains traceback/error

### 12. default / signal-x-ai-training-insight-radar

- Job ID: `8cdfac21faf2`
- Status: `ok`
- Last run: `2026-05-24T08:06:07.693972+07:00`
- Config: `/Users/ultrafriday/.hermes/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/cron/output/8cdfac21faf2/2026-05-24_08-06-07.md`
- Findings:
  - latest output contains 401 unauthorized

### 13. blaze / daily-scheduled-content-platform-update

- Job ID: `c20a2a2db954`
- Status: `ok`
- Last run: `2026-05-24T10:00:44.599733+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/blaze/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/blaze/cron/output/c20a2a2db954/2026-05-24_10-00-44.md`
- Findings:
  - delivery error: no delivery target resolved for deliver=discord

### 14. blaze / Jedi AI Creative Director Daily Pipeline

- Job ID: `255e748b82b1`
- Status: `ok`
- Last run: `2026-05-24T08:07:54.353066+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/blaze/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/blaze/cron/output/255e748b82b1/2026-05-24_08-07-54.md`
- Findings:
  - delivery error: no delivery target resolved for deliver=discord

### 15. blaze / Daily LinkedIn + X Scheduled Draft Queue

- Job ID: `929b8a33a119`
- Status: `ok`
- Last run: `2026-05-24T08:19:32.770306+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/blaze/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/blaze/cron/output/929b8a33a119/2026-05-24_08-19-32.md`
- Findings:
  - delivery error: no delivery target resolved for deliver=discord

### 16. bolt / Daily YouTube to Blog Check

- Job ID: `2aae2b04d926`
- Status: `ok`
- Last run: `2026-05-24T08:06:22.104983+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/bolt/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/bolt/cron/output/2aae2b04d926/2026-05-24_08-06-22.md`
- Findings:
  - delivery error: no delivery target resolved for deliver=discord
  - latest output contains iCloud/resource deadlock

### 17. bolt / daily-canva-carousel-intake

- Job ID: `6f3c73339f2b`
- Status: `ok`
- Last run: `2026-05-24T09:00:39.595804+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/bolt/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/bolt/cron/output/6f3c73339f2b/2026-05-24_09-00-39.md`
- Findings:
  - delivery error: no delivery target resolved for deliver=discord

### 18. kaijeaw / kaijeaw-daily-thai-threads-post

- Job ID: `a8b932969f00`
- Status: `ok`
- Last run: `2026-05-24T08:33:13.448643+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/kaijeaw/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/kaijeaw/cron/output/a8b932969f00/2026-05-24_08-33-13.md`
- Findings:
  - delivery error: no delivery target resolved for deliver=discord

### 19. kaijeaw / kaijeaw-calendar-aware-workshop-content-pipeline

- Job ID: `2f06fffea29b`
- Status: `ok`
- Last run: `2026-05-24T07:21:11.266007+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/kaijeaw/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/kaijeaw/cron/output/2f06fffea29b/2026-05-24_07-21-11.md`
- Findings:
  - delivery error: no delivery target resolved for deliver=discord
  - latest output contains revoked/expired token
  - latest output contains iCloud/resource deadlock

### 20. oracle / oracle-daily-idea-seed-scan

- Job ID: `13d10d4b7229`
- Status: `ok`
- Last run: `2026-05-24T07:20:46.495926+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/oracle/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/oracle/cron/output/13d10d4b7229/2026-05-24_07-20-46.md`
- Findings:
  - delivery error: no delivery target resolved for deliver=discord

### 21. qwen / qwen-morning-prep-for-kelly

- Job ID: `2ecf236f6cca`
- Status: `ok`
- Last run: `2026-05-24T07:23:41.231894+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/qwen/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/qwen/cron/output/2ecf236f6cca/2026-05-24_07-23-41.md`
- Findings:
  - delivery error: no delivery target resolved for deliver=discord

### 22. qwen / qwen-nightly-obsidian-hygiene

- Job ID: `b160922c0931`
- Status: `ok`
- Last run: `2026-05-23T23:41:14.271469+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/qwen/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/qwen/cron/output/b160922c0931/2026-05-23_23-41-14.md`
- Findings:
  - delivery error: no delivery target resolved for deliver=discord

### 23. qwen / AI Digest Monitor

- Job ID: `d4c72d86b21f`
- Status: `ok`
- Last run: `2026-05-24T11:51:55.340891+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/qwen/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/qwen/cron/output/d4c72d86b21f/2026-05-24_11-51-55.md`
- Findings:
  - delivery error: no delivery target resolved for deliver=discord

### 24. qwen / qwen-comet-x-radar-hourly

- Job ID: `44f5881a93f9`
- Status: `ok`
- Last run: `2026-05-24T11:53:33.349015+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/qwen/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/qwen/cron/output/44f5881a93f9/2026-05-24_11-53-33.md`
- Findings:
  - delivery error: no delivery target resolved for deliver=discord

### 25. qwen / qwen-agent-memory-guardian

- Job ID: `f4d9899e9bfc`
- Status: `ok`
- Last run: `2026-05-24T09:58:59.707485+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/qwen/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/qwen/cron/output/f4d9899e9bfc/2026-05-24_09-58-59.md`
- Findings:
  - delivery error: no delivery target resolved for deliver=discord
  - latest output contains iCloud/resource deadlock

### 26. signal / signal-ai-morning-brief

- Job ID: `d194c1c29c42`
- Status: `ok`
- Last run: `2026-05-24T08:34:21.286078+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/signal/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/signal/cron/output/d194c1c29c42/2026-05-24_08-34-21.md`
- Findings:
  - delivery error: no delivery target resolved for deliver=discord

### 27. signal / signal-high-signal-ai-watch

- Job ID: `f64fa63e9bc7`
- Status: `ok`
- Last run: `2026-05-24T09:04:59.353077+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/signal/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/signal/cron/output/f64fa63e9bc7/2026-05-24_09-04-59.md`
- Findings:
  - delivery error: no delivery target resolved for deliver=discord

### 28. signal / signal-x-twitter-high-alert-scan

- Job ID: `88d1ac455e7b`
- Status: `ok`
- Last run: `2026-05-24T10:13:02.016240+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/signal/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/signal/cron/output/88d1ac455e7b/2026-05-24_10-13-02.md`
- Findings:
  - delivery error: no delivery target resolved for deliver=discord

### 29. signal / signal-daily-ai-intel-report-9pm

- Job ID: `6c5ac6a19886`
- Status: `ok`
- Last run: `2026-05-23T21:08:48.667430+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/signal/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/signal/cron/output/6c5ac6a19886/2026-05-23_21-08-48.md`
- Findings:
  - delivery error: no delivery target resolved for deliver=discord

### 30. signal / signal-daily-x-bookmarks-research-5am

- Job ID: `cea9aafced77`
- Status: `ok`
- Last run: `2026-05-24T05:04:45.969233+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/signal/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/signal/cron/output/cea9aafced77/2026-05-24_05-04-45.md`
- Findings:
  - delivery error: no delivery target resolved for deliver=discord

### 31. zegna / Daily Zegna curation page refresh → Notion archive

- Job ID: `bf357896fa4a`
- Status: `ok`
- Last run: `2026-05-24T08:02:01.630177+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/zegna/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/zegna/cron/output/bf357896fa4a/2026-05-24_08-02-01.md`
- Findings:
  - delivery error: no delivery target resolved for deliver=discord

### 32. zegna / Daily Zegna cool-stuff scout → Telegram + Notion archive

- Job ID: `00522937bc83`
- Status: `ok`
- Last run: `2026-05-24T09:02:42.807543+07:00`
- Config: `/Users/ultrafriday/.hermes/profiles/zegna/cron/jobs.json`
- Latest output: `/Users/ultrafriday/.hermes/profiles/zegna/cron/output/00522937bc83/2026-05-24_09-02-42.md`
- Findings:
  - delivery error: no delivery target resolved for deliver=discord

## Noisy output volumes

- default: 2111 cron output files this week, 10.6 MB
- jekjack: 626 cron output files this week, 2.9 MB
- qwen: 350 cron output files this week, 2.1 MB
- signal: 143 cron output files this week, 18.9 MB

## Recommended next actions

1. Fix token/OAuth jobs before rerunning dependent workflows.
2. Move mutable scanner state out of iCloud/Obsidian paths.
3. Fix profile cron delivery targets where `last_delivery_error` is present.
4. Convert high-volume unchanged sync jobs to silent/no-agent outputs.

_Secrets are redacted by this script; inspect referenced files locally if needed._
