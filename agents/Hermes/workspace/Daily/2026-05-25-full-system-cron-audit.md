# Full System Cron / Agent Audit — 2026-05-25 22:56 ICT

## Executive summary
- All primary Hermes gateways are running: default/Kelly, Blaze, Signal, Zegna, Kaijeaw, Bolt, Qwen, Oracle.
- Blaze is active and did create content today. The issue was delivery visibility: Blaze jobs were set to `deliver=discord`, but the Blaze profile has Discord delivery unresolved, so the runs succeeded locally but did not reach Jet.
- Safe fix applied: Blaze's three core content jobs now deliver to `origin` (Jet Telegram origin) so tomorrow's outputs should reach Jet.
- The old default/Kelly content jobs are paused intentionally because they were consolidated into Blaze's dedicated content workflow. They are not the current source of truth.
- Wider fleet issue: several non-default profiles still have cron jobs set to `deliver=discord` while profile-level Discord is unresolved. This affects Signal, Zegna, Kaijeaw, Bolt, Qwen, and one Oracle job. They are running, but many reports are not being delivered.

## Fixes already applied
- Updated Blaze job `c20a2a2db954` — `daily-scheduled-content-platform-update` — deliver `discord` → `origin`.
- Updated Blaze job `255e748b82b1` — `Jedi AI Creative Director Daily Pipeline` — deliver `discord` → `origin`.
- Updated Blaze job `929b8a33a119` — `Daily LinkedIn + X Scheduled Draft Queue` — deliver `discord` → `origin`.

## Blaze audit
- Gateway: running, PID 8306.
- Model: gpt-5.5 via OpenAI Codex.
- Smoke test: passed (`BLAZE_OK`).
- Active jobs: 4.
- Core content jobs:
  - `daily-scheduled-content-platform-update`: active; last run OK; delivery previously failed due Discord target; now fixed to origin.
  - `Jedi AI Creative Director Daily Pipeline`: active; last run OK; delivery previously failed due Discord target; now fixed to origin.
  - `Daily LinkedIn + X Scheduled Draft Queue`: active; last run OK; delivery previously failed due Discord target; now fixed to origin.
- Today's Blaze output exists at `~/Documents/Obsidian Vault/Agents/Blaze/Daily/creative_director_2026-05-25.md`.
- Today's queue verification: `~/.hermes/limitless/content_approval_queue.json` contains 4 ready-for-review drafts for 2026-05-25: 3 X/Twitter + 1 LinkedIn.
- One non-core Blaze job failed: `Meta IG boost performance check` timed out after 300s.

## Paused content crons
Default/Kelly paused content jobs found:
- `daily-content-engine-best-pick` — paused, old default content flow.
- `all-day-content-research-momentum` — paused, old default content flow.
- `midday-content-burst` — paused, old default content flow.
- `quiet-founder-social-daily-draft-engine` — paused.

Assessment: do not blindly resume these because they likely duplicate Blaze's consolidated workflow. If Jet wants more volume, create/adjust Blaze jobs instead.

## Gateway / model health
- default/Kelly: running, gpt-5.5/OpenAI Codex, Discord + Telegram configured.
- Blaze: running, gpt-5.5/OpenAI Codex, Telegram configured, Discord unresolved.
- Signal: running, gpt-5.5/OpenAI Codex, smoke test passed.
- Zegna: running, gpt-5.5/OpenAI Codex, smoke test passed.
- Kaijeaw: running, gpt-5.5/OpenAI Codex, smoke test passed after slower retry.
- Bolt: running, gpt-5.5/OpenAI Codex, smoke test passed after slower retry.
- Oracle: running, gpt-5.5/OpenAI Codex, smoke test passed.
- Qwen: running, local `qwen3.6:35b`, smoke test passed.
- Pixel: running but no scheduled jobs.
- Protocol: running but no scheduled jobs.

## Other fleet issues found
- Default job `limitless-visibility-weekly-gsc-gap-report`: failing due Google Search Console OAuth refresh token expired/revoked.
- Default jobs `jet-workspace-digest-scan-nightly` and `jet-personal-artifacts-scan-daily`: failing with `OSError: [Errno 11] Resource deadlock avoided` while writing state into Obsidian/Shared Memory digest files.
- Qwen job `qwen-comet-x-radar-hourly`: timed out after 120s.
- Non-default profile cron delivery failures due `deliver=discord` with unresolved profile Discord target:
  - Signal: morning brief, high-signal watch, daily AI intel report, etc.
  - Zegna: both daily scout/curation jobs.
  - Kaijeaw: both Thai content jobs.
  - Bolt: both jobs.
  - Qwen: multiple jobs.
  - Oracle: daily idea seed scan.

## Recommended next fixes
1. Keep Blaze as content owner; do not resume old default content jobs unless intentional duplication is desired.
2. Decide fleet delivery policy:
   - Option A: Change non-default jobs to `origin`/Telegram for guaranteed delivery.
   - Option B: properly wire profile-level Discord delivery without creating duplicate Discord bot listeners.
   - Option C: route only summaries to Telegram and keep high-frequency monitors local.
3. Repair Google Search Console OAuth for the weekly visibility report.
4. Patch the digest scan scripts to write state files safely outside the iCloud/Obsidian deadlock path or with atomic retry logic.
5. Increase/optimize Qwen Comet radar timeout or make it silent/local-only when slow.

## Audit commands used
- `hermes cron list --all` and profile alias cron lists.
- `hermes profile list`.
- `<profile> cron status`.
- `<profile> status --all` and gateway status.
- No-tool profile smoke tests for Blaze, Signal, Zegna, Kaijeaw, Bolt, Oracle, Qwen.
- Inspection of Blaze cron outputs and today's Blaze daily content file.
