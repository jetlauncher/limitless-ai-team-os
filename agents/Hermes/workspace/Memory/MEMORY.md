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
- 2026-05-10: Limitless Mission Control repo is `/Users/ultrafriday/Projects/limitless-mission-control`; local dashboard normally runs at `127.0.0.1:8765`, with the access key stored in `~/.hermes/limitless/mission_control_key.txt` and never pasted into notes or chat.
- 2026-05-11: Automation-noise preferences: Zegna should use local `qwen3.6:35b` via Ollama-compatible `http://127.0.0.1:11434/v1`; Signal user-facing scheduled updates should stay at ≤4/day; Blaze scheduled publishable content should stay at ≤10 pieces/day.
- 2026-05-16: All active agents should follow the shared always-write memory protocol at `Agents/Shared Memory/Protocols/always-write-memory.md`: daily note after meaningful work, durable facts only in each agent's `Memory/MEMORY.md`, cross-agent handoffs in Shared Memory, no secrets/raw transcripts. Qwen/local `qwen3.6:35b` owns low-cost memory hygiene checks; all-agent memory sync script includes Pixel.

- Qwen Hermes profile fix: local Ollama `qwen3.6:35b` must keep `model.context_length: 131072` in `~/.hermes/profiles/qwen/config.yaml`; Hermes rejects the profile if it falls back to 8192. Qwen no-agent scripts resolve under `~/.hermes/profiles/qwen/scripts/`, not only `~/.hermes/scripts/`.

- 2026-05-17: Jet Brain v0 installed: Shared Memory protocol/evals/templates under `Agents/Shared Memory/`; Hermes skill `jet-brain-retrieval`; GBrain CLI 0.35.1.1 via Bun at `~/.bun/bin/gbrain` from `~/gbrain`. Do not import broad vaults or secrets; sidecar is optional until GBrain health/source boundaries are cleaned.

- Oracle Telegram: bot username `@oraclejedihermesbot`; token lives in `~/.hermes/profiles/oracle/.env`; gateway service `ai.hermes.gateway-oracle`.

- Cua Driver installed for local macOS GUI control: `/Applications/CuaDriver.app`, CLI `~/.local/bin/cua-driver`, Hermes MCP server `cua-driver` in default config. Needs Accessibility permission if not already granted.
