# Always-Write Memory Protocol

Updated: 2026-05-16 06:06 

## Rule
Every dedicated agent should leave a human-readable Obsidian trace after meaningful work.

## Where to write
- Agent daily note: `Agents/<Agent>/Daily/YYYY-MM-DD.md` for session/task outcomes, decisions, blockers, next steps.
- Agent durable memory: `Agents/<Agent>/Memory/MEMORY.md` only for stable facts that will matter later.
- Shared daily note: `Agents/Shared Memory/Daily/YYYY-MM-DD.md` for cross-agent handoffs.

## Use local models
- Qwen/local Ollama `qwen3.6:35b` is the preferred low-cost memory hygiene worker.
- Qwen can audit agent folders for stale/missing daily notes and produce summaries under `Agents/Qwen/Outputs/Memory-Hygiene/`.
- Qwen must not invent missing facts; uncertain or risky items are marked `Needs Kelly review`.

## Safety
- No secrets, raw tokens, passwords, private session dumps, payment details, or unnecessary personal data.
- No Telegram/email/social/deploy side effects from memory hygiene jobs unless Jet explicitly approves.
