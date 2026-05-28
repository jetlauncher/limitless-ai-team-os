# 2026-05-28 X Bookmarks + Signal Research

- Timestamp: 2026-05-28 05:00:51 +07 (Bangkok)
- Agent/profile: Signal
- Source method: `xurl --app jet-x whoami` succeeded for `@jeditrinupab`; `xurl --app jet-x bookmarks -n 50` returned `CreditsDepleted`, so live bookmark extraction used the logged-in Chrome DevTools session on port `9223` at `https://x.com/i/bookmarks`.
- Live capture result: 4 visible bookmark cards extracted from X via CDP.
- Raw capture JSON: `/Users/ultrafriday/.hermes/limitless/x_bookmarks_live_cdp_2026-05-28_raw.json`
- Structured JSON: `/Users/ultrafriday/.hermes/limitless/x_bookmarks_signal_research_2026-05-28.json`
- Canonical Notion database: Signal Reports Database (`353d076c-9ad3-81cd-aff3-e054bd10e43b`)
- Notion indexing status: completed via canonical backfill (`ok=true`, `created=3`, `updated=1719`, `failed=0`, `total_artifacts=1722`).

## Bookmark/post links captured

1. Ole Lehmann / Claude buyer simulation skill
   - X: https://x.com/itsolelehmann/status/2059538995269279912
   - Captured text: Claude skill simulates five buyer personas browsing a page to expose why landing pages/emails/ads fail to convert.
2. Runway MCP
   - X: https://x.com/runwayml/status/2059636517283176479
   - Official source: https://runwayml.com/mcp
   - Captured text: Runway MCP connects Runway into Claude, ChatGPT, Cursor, Replit and other compatible agents for image/video generation.
3. Claude for finance / investment analyst workflow
   - X: https://x.com/Av1dlive/status/2059273095970738264
   - Official source: https://www.anthropic.com/events/claude-for-financial-services
   - Captured text: Anthropic Claude for finance lecture plus a quoted article on setting up Claude Code as an investment research analyst.
4. Hermes Agent MCP Catalog
   - X: https://x.com/NousResearch/status/2059638198075109769
   - Official docs: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp/
   - Captured text: Hermes Agent now has a built-in MCP Catalog.

## Clusters/themes

### 1. MCP is becoming the operator distribution layer

- Runway has an official MCP page that says Runway can generate high-quality images/videos from Claude, ChatGPT, Cursor and compatible agents, with models such as Gen-4.5 and other image/video generators available from the conversation surface.
- Nous/Hermes bookmark points to the same platform direction: agent tools are being packaged as discoverable connectors/catalog entries, not one-off scripts.
- Hermes docs position MCP as an integration path for connecting servers/tools to the agent.

### 2. Skills/procedures are moving from coding into revenue workflows

- The Ole Lehmann bookmark is not a lab release, but it is high-signal operator behavior: reusable Claude skills are being applied to conversion diagnostics, buyer-persona simulation, and sales-page critique.
- Claude Code docs confirm skills are first-class procedural extensions: `SKILL.md` instructions become reusable capabilities, invoked when relevant or directly.
- This is the same mechanic Limitless can use for repeatable business audits: buyer simulation, offer critique, ad/message diagnosis, workshop recap, sales-call follow-up.

### 3. Finance/research agents are becoming a serious vertical workflow

- Anthropic's official event page describes Claude for Financial Services as an event for senior executives shaping AI in financial services.
- The bookmarked social post frames Claude Code as an investment research analyst; this is a credible operator pattern even if the detailed article itself remains social-source-led.
- Adjacent primary docs matter: Claude Code skills, permissions, and hooks show the rails needed for analyst workflows that touch files, models, web data, and repeatable reports.

### 4. Governed agent operating systems remain the strongest thesis

- The strongest cluster is not one launch. It is the convergence of: MCP connectors, skill catalogs, permissions, hooks, and vertical operator procedures.
- Primary-source support:
  - Claude Code skills: https://code.claude.com/docs/en/skills.md
  - Claude Code hooks: https://code.claude.com/docs/en/hooks.md
  - Claude Code permissions: https://code.claude.com/docs/en/permissions.md
  - OpenAI Codex cloud: https://developers.openai.com/codex/cloud.md
  - Runway MCP: https://runwayml.com/mcp
  - Hermes MCP docs: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp/

## Strongest thesis

AI leverage is moving from prompt-craft into governed, reusable agent operating layers: MCP connectors bring tools into the agent surface; skills encode repeatable operating procedures; hooks/permissions create control rails; vertical workflows convert the stack into business outcomes.

## Why it matters

- Limitless Club: This is a curriculum and productization signal. Teach members to build reusable operator skills and MCP-enabled workflows, not just better prompts.
- Founders: Distribution is shifting toward agent-native connectors. Products need MCP/API surfaces and clear use cases inside Claude, ChatGPT, Cursor, Replit and similar environments.
- Operators: The winning workflow is reusable diagnosis and execution: conversion audits, campaign asset generation, finance research, customer ops, and reporting with approvals and logs.
- Educators: The teachable unit is now a procedure pack: context, tool permissions, checklist, examples, verification, and handoff artifacts.

## Recommended actions/angles

1. Build a Limitless mini-workshop: "From prompt to operator skill" using the buyer-simulation bookmark as the concrete example.
2. Create an internal MCP/agent-tool inventory: which tools in Jet's stack should be callable from Claude/Codex/Hermes, with what permissions and audit logs?
3. Package 3 reusable business skills for members: landing-page buyer simulation, offer critique, and research analyst report.
4. For creator/operator content, frame Runway MCP as the practical proof: media generation is entering the same agent workspace as research/coding/writing, reducing context switching.
5. Watch finance-agent workflows carefully, but require strong source verification before making claims about performance, compliance, or investment outcomes.

## Source links

- X bookmark: Ole Lehmann Claude buyer simulation skill: https://x.com/itsolelehmann/status/2059538995269279912
- X bookmark: Runway MCP: https://x.com/runwayml/status/2059636517283176479
- Runway MCP official page: https://runwayml.com/mcp
- X bookmark: Claude for finance / investment analyst workflow: https://x.com/Av1dlive/status/2059273095970738264
- Anthropic Claude for Financial Services event: https://www.anthropic.com/events/claude-for-financial-services
- X bookmark: Nous/Hermes MCP Catalog: https://x.com/NousResearch/status/2059638198075109769
- Hermes MCP docs: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp/
- Claude Code skills docs: https://code.claude.com/docs/en/skills.md
- Claude Code hooks docs: https://code.claude.com/docs/en/hooks.md
- Claude Code permissions docs: https://code.claude.com/docs/en/permissions.md
- OpenAI Codex cloud docs: https://developers.openai.com/codex/cloud.md

## Caveats / assumptions

- X API bookmarks endpoint is currently unavailable because the X API account has `CreditsDepleted`; CDP was used instead.
- CDP extraction captures visible bookmark cards only, not a complete historical bookmark archive.
- The buyer-simulation and investment-analyst details are social-bookmark signals; primary-source verification supports the underlying workflow mechanics, not every social claim.
