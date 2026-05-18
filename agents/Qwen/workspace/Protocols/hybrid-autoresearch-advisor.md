# Hybrid Autoresearch Advisor Workflow

> Local Qwen does the main research. GPT-5.5 is a periodic advisor, not the primary worker.

## Purpose

This implements the Tobi Lütke-style pattern Jet shared: run autoresearch mostly on a local Qwen model, then periodically ask a stronger hosted model for strategic ideas, blind spots, and better next moves.

## Installed files

- Main script: `~/.hermes/scripts/hybrid_autoresearch.py`
- Qwen profile copy: `~/.hermes/profiles/qwen/scripts/hybrid_autoresearch.py`
- CLI wrapper: `~/.local/bin/qwen-autoresearch`
- Output folder: `~/Documents/Obsidian Vault/Agents/Qwen/Outputs/Autoresearch/`
- Oracle idea copy: `~/Documents/Obsidian Vault/Agents/Oracle/Ideas/`

## Basic usage

```bash
qwen-autoresearch "What are the best opportunities for local AI agents in Thai SMB education?"
```

Fast path without GPT advisor:

```bash
qwen-autoresearch "Local AI agent business opportunities" --cycles 1 --no-advisor
```

Seed with a URL:

```bash
qwen-autoresearch "NotebookLM as an agent memory layer" \
  --seed-source https://example.com/article \
  --cycles 2 --advisor-every 1
```

Dry-run install check:

```bash
qwen-autoresearch "install check" --dry-run
```

## Architecture

```text
Research topic
  ↓
Local Qwen plan generation via Ollama OpenAI endpoint
  ↓
Best-effort public web search + source fetch
  ↓
Local Qwen cycle memo
  ↓ every N cycles
GPT-5.5 advisor through Hermes openai-codex
  ↓
Local Qwen incorporates critique and continues
  ↓
Final report saved to Qwen outputs and Oracle ideas
```

## Safety and cost controls

- Local Qwen does the majority of the work.
- GPT-5.5 is only called when `--advisor-every` triggers and `--no-advisor` is not set.
- No posting, messaging, deploying, or deleting.
- Public web reads only; no private files are sent to GPT unless intentionally included in the topic/seed content.
- Reports are local Markdown files.

## Recommended defaults

For a useful but not too slow run:

```bash
qwen-autoresearch "TOPIC" --cycles 2 --advisor-every 1
```

For quick local-only ideation:

```bash
qwen-autoresearch "TOPIC" --cycles 1 --no-advisor
```

For deeper research:

```bash
qwen-autoresearch "TOPIC" --cycles 3 --advisor-every 2 --queries-per-cycle 4
```

## Telegram command

Kelly/default Telegram now has a gateway hook for:

```text
/research <topic>
/research --local <topic>
/research --quick <topic>
/research --deep <topic>
```

Modes:
- `balanced` default: 2 cycles, GPT-5.5 advisor every cycle.
- `--quick`: 1 shorter hybrid cycle.
- `--local`: 1 local-only Qwen cycle, no GPT advisor.
- `--deep`: 3 cycles, advisor every 2 cycles.

The command returns immediately with a start message, runs the worker in the background, then sends a completion brief plus the Markdown report path back to Telegram.

## Known limitations

- Web search uses no-key DuckDuckGo HTML and can be blocked or sparse.
- Source fetching uses Jina Reader when available, then falls back to direct HTML/text fetch.
- Local Qwen speed depends on Ollama/model load.
- GPT advisor uses Hermes `openai-codex` and should be treated as a premium call.

## Next upgrades

1. Add a Telegram command wrapper, e.g. `/autoresearch topic`.
2. Add Mission Control dashboard panel for recent reports.
3. Add source connectors: Obsidian folders, X radar output, Todoist tasks, Airtable customer notes.
4. Add a scoring step that turns reports into Oracle idea cards.
5. Add a scheduled local-only daily idea miner with advisor calls only for high-signal topics.
