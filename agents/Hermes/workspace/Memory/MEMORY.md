# Kelly / Hermes — Durable Memory

Use this file for durable, agent-specific memory that should remain useful across sessions.

## Stable identity
- Agent: Kelly / Hermes
- Role: Primary assistant for Jet: general ops, automation, configuration, dashboards, revenue monitoring, and coordination.
- Profile: default Hermes profile at ~/.hermes

## Memory rules
- Store only stable facts, preferences, conventions, source-of-truth paths, and reusable context.
- Do not store secrets, raw API keys, passwords, or temporary task progress.
- Put temporary context in `Daily/` or `Scratchpad/`, not here.
- Promote repeated workflows into `Protocols/`.

## Durable notes
- Created/verified on 2026-04-26.
- Jet is considering a lightweight portable MacBook (“MacBook Neo” as transcribed) instead of an iPad because he wants a carry-around device that can code/build properly. Treat as active consideration; clarify exact model/specs before purchase advice.
- 2026-05-10: Claude Code for Hermes agents uses Jet’s Claude Max / Claude.ai OAuth login, not Anthropic Console API billing. `ANTHROPIC_API_KEY` should remain unset unless Jet explicitly requests API-billed usage. See [[Claude Code OAuth Access - 2026-05-10]].
- 2026-05-10: Bolt was explicitly verified through its own Hermes profile with Claude Code OAuth; smoke test returned `BOLT_CLAUDE_OAUTH_OK`. Bolt may use Claude Code for app/site/landing-page builds, then must independently verify files, tests/builds, screenshots, and outputs.
- 2026-05-10: All-agent memory sync orchestration script lives at `~/.hermes/scripts/run_all_agent_memory_sync.sh`; logs/summaries are written under `~/.hermes/agent-memory-sync/`. Keep these syncs file-only unless Jet explicitly authorizes external messages or posts.
