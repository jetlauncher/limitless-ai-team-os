# Agent Team Recovery Index

Updated: 2026-05-16
Owner: Friday / OpenClaw
Status: Recovery map from local system inspection

## Current Obsidian connection

- Active vault path: `/Users/ultrafriday/Documents/Obsidian Vault`
- `obsidian-cli` is installed at `/opt/homebrew/bin/obsidian-cli`.
- CLI default vault has been set to `/Users/ultrafriday/Documents/Obsidian Vault`.
- Agent memory source of truth lives under `Agents/`.
- Friday memory lives under `Friday/Memory/`.

## Current active agent system

The currently active Hermes/OpenClaw agent fleet appears to be:

- Kelly / Hermes: primary ops, automation, dashboards, config, monitoring, troubleshooting.
- Blaze: content creation, hooks, posts, scripts, carousels, launch copy, course content.
- Signal: AI research, model/product launches, agent workflow intelligence.
- Zegna: tastemaker, cool brands, gadgets, product recommendations.
- Kaijeaw: Thai-language Hermes profile.
- Bolt: apps/sites building profile.
- Qwen: local Ollama worker/demo profile.
- Uncle Chris: restored as `unclechris` Hermes profile for investment news, stock checkers, market briefs, and finance/revenue research.
- Protocol: publishing/analytics/research workflows.
- Pixel: visual/generation profile.
- OpenClaw / Friday: runtime, tools, channels, local workspace, legacy recovery.

Related Obsidian workspaces:

- `Agents/Hermes/`
- `Agents/Blaze/`
- `Agents/Signal/`
- `Agents/Zegna/`
- `Agents/Kaijeaw/`
- `Agents/Bolt/`
- `Agents/Qwen/`
- `Agents/Uncle Chris/`
- `Agents/Protocol/`
- `Agents/Pixel/`
- `Agents/OpenClaw/`
- `Agents/Shared Memory/`

## Older named agent team recovered from local docs

Recovered from `/Users/ultrafriday/clawd/second-brain-imac/docs/`:

- Friday: executive assistant.
- Nova: chief of staff / morning briefings / task tracking.
- Blaze: creative director / Instagram carousels / design.
- Jamerson: research and AI coach.
- Uncle Chris: finance / expenses / revenue reports.
- Coach Marc: sales coach / objection handling / follow-ups.
- Pastor David: spiritual advisor.
- Forge: app builder.
- Venice: special ops / automation / browser control / scraping.

Old restored agent list also included:

- `main`
- `friday-ea`
- `coach-marc`
- `pastor-david`
- `uncle-chris`
- `jamerson`
- `blaze`

## Old app/control-room artifacts

- Old second-brain path: `/Users/ultrafriday/clawd/second-brain-imac/`
- Old AI dev team path: `/Users/ultrafriday/clawd/builds/ai-dev-team/`
- Mission Control app path: `/Users/ultrafriday/clawd/mission-control/`
- Current Mission Control local app responds on `http://127.0.0.1:3001` and redirects to login.
- Legacy docs mention routes:
  - `/mc/team`
  - `/mc/approvals`
  - `/mc/api/mc/team-status`
  - `/mc/api/mc/tasks`

## Working public links verified on 2026-05-16

- https://agent-workshop-review-page.vercel.app/
- https://carousel-showcase.vercel.app/
- https://ai-audit-architect.vercel.app/
- https://ai-appointment-setter-two.vercel.app/
- https://ai-followup-generator.vercel.app/
- https://asethjeti-clinic-landing.vercel.app/
- https://ai-employee-builder.vercel.app/
- https://aiexpertbyjedi-itikdbb.gamma.site/

## Carousel / creative memory

Default carousel style recovered from the OpenClaw handoff:

- Theme: Midnight Luxe Editorial.
- Palette: black, charcoal, graphite, white, silver.
- Feel: luxury founder-media, editorial, premium but direct.
- Typical header: `Limitless Club`.
- CTA: `@jeditrinupab`.
- Showcase: https://carousel-showcase.vercel.app/

## Stripe capability

Stripe live connectivity was verified read-only on 2026-05-16. Friday/OpenClaw can create Stripe payment links, but creating live payment links is an external money action and requires explicit Jet approval with:

- product name
- price
- currency
- one-time or subscription
- live or test mode

Do not write Stripe keys or secret values into Obsidian.

## Recovery notes

- The OpenClaw gateway incident on 2026-05-16 was caused by an updater script repeatedly stopping the gateway, then failing due to stale binary/npm paths.
- The unsafe updater was preserved as `/Users/ultrafriday/.openclaw/tmp/update-openclaw-20260515.sh.disabled-backup`.
- The active updater script was replaced with a no-op guard to stop the restart loop.
- Gateway health after remediation: `{"ok":true,"status":"live"}`.

## Next useful step

Turn this recovery map into a live Obsidian control room:

- update `Agent Registry.md` with the older named-agent roles,
- add current live/dead status per agent,
- add local/public links,
- add runbooks for gateway health, Stripe link creation, carousel generation, and agent routing.
