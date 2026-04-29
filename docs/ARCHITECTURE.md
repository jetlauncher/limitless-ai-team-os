# Architecture

## Agent roster

| Agent | Role | Main workspace |
|---|---|---|
| Kelly / Hermes | Chief of staff, ops, dashboards, approvals | `Agents/Hermes/` |
| Signal | AI research/search and high-signal alerts | `Agents/Signal/` |
| Blaze | Content generation and repurposing | `Agents/Blaze/` |
| Kaijeaw | Thai voice/content assistant | `Agents/Kaijeaw/` |
| Zegna | Taste, gadgets, brands, premium discovery | `Agents/Zegna/` |
| Bolt | Apps, websites, landing pages | `Agents/Bolt/` |
| Qwen | Local/private Ollama worker | `Agents/Qwen/` |
| Protocol | Newsletter/Beehiiv editor | `Agents/Protocol/` |

## Memory layers

1. Built-in Hermes profile memory.
2. Human-readable Obsidian workspaces under `Agents/<Agent>/`.
3. Shared memory and daily handoffs under `Agents/Shared Memory/`.

## Control principle

Agents may draft, analyze, and prepare. Publishing, emailing, posting, deploying, deleting, or charging money requires explicit approval unless the owner has intentionally changed that rule.
