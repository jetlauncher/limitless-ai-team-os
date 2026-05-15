# Qwen Comet X Radar Workflow

## Purpose

Qwen runs a local, low-cost high-signal AI/Agent radar for Jet using:

- Jet's logged-in local Comet browser session for X search pages
- local Ollama model `qwen3.6:35b` for ranking/summarization
- local Obsidian output files under `Agents/Qwen/Outputs/X-Radar/`

This avoids X API credit spend for routine scans while keeping the output private/local.

## Cron

- Profile: `qwen`
- Job name: `qwen-comet-x-radar-hourly`
- Job ID: `44f5881a93f9`
- Schedule: `every 60m`
- Mode: `--no-agent`
- Delivery: `local`
- Script: `~/.hermes/scripts/qwen_comet_x_radar_hourly.py`

Command used:

```bash
qwen cron create 'every 1h' \
  'Run the local Comet + Qwen X radar script for high-signal AI/agent posts. Script writes the full report to Obsidian. No posting or external side effects.' \
  --name qwen-comet-x-radar-hourly \
  --deliver local \
  --script qwen_comet_x_radar_hourly.py \
  --no-agent
```

## Source queries

The script scans three curated X searches in Comet:

1. Major AI labs: OpenAI, Anthropic, Google DeepMind, xAI, Meta AI, Mistral, Perplexity.
2. Agent products: Cursor, Cognition, LangChain, crewAI, Browserbase, Vercel, Manus, Ollama.
3. Big AI people: Sam Altman, Karpathy, Andrew Ng, swyx, Aidan McLaughlin, Jeremy Howard, Ethan Mollick.

Topics filtered for:

- AI agents
- coding agents
- computer use
- Codex
- Cursor/cloud agents
- agent infrastructure
- browser/computer automation
- agent security

## Output

Reports are saved to:

```text
~/Documents/Obsidian Vault/Agents/Qwen/Outputs/X-Radar/
```

Example verified output:

```text
2026-05-15-2216-qwen-comet-x-radar.md
```

## Safety and noise rules

- No social posting.
- No likes, replies, reposts, DMs, follows, or other X write actions.
- No X API calls required for this cron.
- Default delivery is `local` to avoid hourly Telegram spam.
- If Jet wants alerts, send only a compact Telegram digest when there is a genuinely important signal.

## Known limitations

- The script uses the active Comet tab and restores the original URL afterward; it may briefly touch the browser session during each hourly scan.
- X page text does not always include exact post URLs/IDs, so Qwen should not invent links.
- Comet must remain scriptable: View → Developer → Allow JavaScript from Apple Events.
- If the active browser session is logged out of X, outputs may degrade.
