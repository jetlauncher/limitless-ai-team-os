# Signal Memory

Durable human-readable memory for Signal. Do not store secrets here.
- 2026-05-16: `xurl` official X API CLI is configured for Signal's X bookmark workflow via the `jet-x` OAuth app for `@jeditrinupab`; daily bookmark research should use `xurl --app jet-x bookmarks -n 50` because the built-in `default` xurl profile currently has no OAuth2 credentials. Continue to follow secret-safety rules: never read or expose `~/.xurl`, tokens, or OAuth credential files.
- 2026-05-17 X scan: xAI official post `2055745332919808181` says X Premium subscriptions work in Hermes Agent and Hermes can search X posts; treat as duplicate of May 16 Grok/Hermes subscription-as-auth unless new implementation docs or reliability tests appear.


## AI Signals Notion database
- Source of truth for future AI Signal entries: Notion database `AI Signals` — `363d076c-9ad3-8099-bbd9-e9f1d3cd23cf` / https://www.notion.so/363d076c9ad38099bbd9e9f1d3cd23cf
- Schema: `Name` title; `Date` date; `Top Theme` select (`OpenAI`, `Anthropic`, `Google / DeepMind`, `Meta`, `AI Agents`, `SMB AI Tools`, `Industry / Other`); `Content Bet` rich_text; `Status` select (`🆕 New`, `👀 Reviewed`, `✅ Content Made`, `🗄 Archived`); `Items` number.
- Existing template style: quote intro; numbered H2 items; paragraph summary; bullets for `Why you care`, `Teach/try`/`Apply now`, `Sources`; divider; final `🎯 This week's content bet`.
## 2026-05-19 - Anthropic acquires Stainless signal
- X high-alert scan selected Anthropic acquiring Stainless as high-signal: SDK, CLI, and MCP-server generation is moving into Claude Platform as core agent-connectivity infrastructure.
- Official source: https://www.anthropic.com/news/anthropic-acquires-stainless; X source: https://x.com/AnthropicAI/status/2056419620643541012.
- Dedupe guidance: repeat only if Anthropic adds concrete Stainless product integration details, connector marketplace changes, MCP governance/security controls, pricing/availability, or migration requirements.


- 2026-05-20 watch/dedupe: OpenAI Guaranteed Capacity verified via official X + sitemap (`/business/guaranteed-capacity/`, `/form/guaranteed-capacity/` lastmod 2026-05-19) and Sam Altman stated discounted tokens for 1-3 year commits. Future repeats should add terms/eligibility/pricing/body details before re-alerting.
- 2026-05-20 watch/dedupe: Google I/O follow-up verified Managed Agents API on Google Cloud blog and @GoogleAIStudio: Google-hosted secure agent environments, Markdown instructions/skills/tools, Antigravity through Agent Platform, Antigravity 2.0 desktop app, and CLI. Future repeats need docs/API pricing/security/logging details before re-alerting.


- 2026-05-21: `signal_reports_db_backfill.py` can fail on Obsidian/iCloud transient file locks with `OSError: [Errno 11] Resource deadlock avoided` during `collect_obsidian()`. Current script was patched to `try/except OSError` around markdown `read_text`, log `skip unreadable obsidian file ...`, continue, and then complete backfill successfully.
- 2026-05-22: X API `xurl --app jet-x bookmarks -n 50` and search can return `CreditsDepleted` even though `whoami` works. For bookmark cron runs, fall back to newest durable bookmark JSON under `~/.hermes/limitless/`, label the live-bookmark limitation, refresh via official sources, and still write Obsidian/JSON plus run Signal Reports DB backfill.


- 2026-05-23 watch note: Hugging Face feed surfaced NVIDIA Nemotron-Labs Diffusion (`https://huggingface.co/blog/nvidia/nemotron-labs-diffusion`) as a fresh official-source model/runtime item: 3B/8B/14B text diffusion models under NVIDIA Nemotron Open Model License, AR/diffusion/self-spec generation modes, self-spec reported ~865 tok/s on B200 (~4x AR baseline). Useful future framing: inference throughput/model-architecture option for operator cost/latency, not generic benchmark hype.
- 2026-05-23 watch note: Databricks feed surfaced `Observability for any agent, anywhere` and open-source-model prompt caching; useful under-covered agent-ops sources when same-day briefs are saturated with Google/OpenAI/AWS.
