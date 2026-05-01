# OpenAI Usage Audit — 2026-05-01

## Executive summary
- Screenshot showed OpenAI Platform spend spike: **$30.08 on May 1 UTC**, total spend **$40.47**, May spend **$30.08 / $100**.
- Dashboard showed **Responses and Chat Completions** as the dominant category: **287 requests** and **14,012,879 input tokens**.
- Dashboard showed **Images** only **1 request / 1 image** for the visible filtered view, so the $30 spike was primarily not image generation in that project view.
- Local Hermes logs across profiles showed **283 logged API calls on May 1**, matching **98.6%** of the dashboard request count.
- Average input tokens/request from screenshot: **~48,825 tokens/request**.

## Main source breakdown from local Hermes logs
- Kelly/default profile: **129 calls** (~45.6%)
- Kaijeaw profile: **93 calls** (~32.9%)
- Signal profile: **41 calls** (~14.5%)
- Blaze profile: **11 calls**
- Bolt profile: **9 calls**
- Total logged: **283 calls** vs screenshot **287 requests**

## High-call workflows found
### Kelly/default
- 00:08 — background creative/video process completion handling: **32 calls**
- 06:21–06:28 — Fire social profile setup: **22 calls**
- 06:47–06:51 — Fire handle audit: **11 calls**
- 06:52–06:58 — switch to Quiet Founder: **16 calls**
- 14:39–14:50 — system infographic generation/QA: **16 calls**

### Kaijeaw
- Thai Threads setup/research sequence: **93 calls** total
- Biggest single run: “research best practices of Threads”: **43 calls**

### Signal
- Report storage/backfill/session: **41 calls** total
- One long run around 10:13–10:52 used **19 calls**

## Direct OpenAI image generation found
Guarded scripts found/modified:
- `/Users/ultrafriday/.hermes/fire_social/generate_fire_logo.py`
- `/Users/ultrafriday/.hermes/fire_social/generate_fire_banner.py`
- `/Users/ultrafriday/Documents/Obsidian Vault/Agents/Hermes/Creative/The Quiet Founder/generate_quiet_founder_avatars.py`
- `/Users/ultrafriday/Documents/Obsidian Vault/Agents/Hermes/Creative/The Quiet Founder/generate_quiet_founder_image_set.py`

Known generated image assets around the spike window:
- Fire logo: 2026-05-01 06:26, `gpt-image-2`, 1024x1024 high
- Fire banner: 2026-05-01 06:28, `gpt-image-2`, 1536x1024 high
- Quiet Founder avatar concepts: 2 images around 2026-04-30 22:51–22:54
- Quiet Founder image set: 5 images around 2026-04-30 23:57–2026-05-01 00:07

Interpretation: these image scripts did cause some spend, but the screenshot’s visible project view shows the $30 spike was overwhelmingly **Responses/Chat Completions token usage**, not Images.

## Cron inventory notes
Enabled cron jobs on default profile include:
- `limitless-payment-alerts` every 15m
- `notion-to-obsidian-content-clone` every 15m
- `important-email-alert-filter` every 30m
- revenue/X monitor/social/briefing/repo jobs

May 1 cron output volume:
- `important-email-alert-filter`: 30 files, ~532 KB output
- `limitless-payment-alerts`: 56 files, ~82 KB output; many timed out
- `notion-to-obsidian-content-clone`: 53 files, ~80 KB output; many timed out

These cron jobs add baseline model calls and should be optimized, but local profile logs indicate the major spike was mostly interactive multi-agent work plus large context/tool loops.

## Guardrails added
- Added `ALLOW_OPENAI_IMAGE_SPEND=1` approval gate to all known direct OpenAI image scripts.
- Verified the scripts now block by default.

## Recommended next actions
1. Switch non-critical profiles / cron model from `gpt-5.5` to cheaper/lower-context model where possible.
2. Reduce loaded skills/context for scheduled jobs; they currently include large prompt blocks.
3. Add spend-aware routing: image generation and long research require explicit spend approval.
4. Fix timed-out cron scripts so they stop generating failed LLM report runs every 15 minutes.
5. In OpenAI Platform, use API Keys/Services breakdown to confirm which key/service is labeled “Kelly AI”; current local key lacks `api.usage.read`, so API usage details could not be queried programmatically.
