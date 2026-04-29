# Installation Guide — Limitless AI Team OS

This guide helps a student clone the system and replace Jet's credentials with their own.

## 1. Requirements

- macOS or Linux
- Git
- Python 3.11+
- Telegram account
- GitHub account
- Optional: Ollama for local models

## 2. Install Hermes Agent

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
hermes doctor
```

## 3. Clone this repository

```bash
git clone git@github.com:jetlauncher/limitless-ai-team-os.git
cd limitless-ai-team-os
```

If you do not have SSH set up, use HTTPS instead.

## 4. Create your root Hermes config

```bash
mkdir -p ~/.hermes
cp examples/env/root.env.example ~/.hermes/.env
cp configs/root/config.example.yaml ~/.hermes/config.yaml
chmod 600 ~/.hermes/.env
```

Then edit:

```bash
nano ~/.hermes/.env
```

## 5. Required API keys

Minimum working setup:

| Platform | Why | Env var / file |
|---|---|---|
| OpenRouter or OpenAI/Anthropic | Main model provider | `OPENROUTER_API_KEY`, `OPENAI_API_KEY`, or `ANTHROPIC_API_KEY` |
| Telegram BotFather | Chat interface for each agent | `TELEGRAM_BOT_TOKEN` per profile |
| GitHub | Repo sync and code tasks | `GITHUB_TOKEN` or `gh auth login` |

Recommended full setup:

| Platform | Why | Suggested storage |
|---|---|---|
| Notion | Archive content / control-room mirror | `~/.config/notion/api_key` |
| Beehiiv | Newsletter drafts | `~/.config/beehiiv/api_key` |
| Airtable | Sales/revenue reporting | `~/.config/airtable/api_key` |
| Google Workspace | Gmail/Calendar/Drive | OAuth token path from your setup |
| OpenAI Images | Premium carousel generation | `~/.config/openai/api_key` |
| Higgsfield | Image/video generation MCP | `HIGGSFIELD_MCP_TOKEN` |
| Blotato | Social approval posting | `~/.config/blotato/api_key` |
| Ollama | Local model worker | Local server at `127.0.0.1:11434` |

## 6. Create Telegram bots

In Telegram, open `@BotFather` and create one bot per agent:

- Kelly / Hermes
- Signal
- Blaze
- Kaijeaw
- Zegna
- Bolt
- Qwen
- Protocol

For each profile:

```bash
hermes profile create signal --clone-all
hermes profile alias signal --name signal
mkdir -p ~/.hermes/profiles/signal
cp examples/env/profile.env.example ~/.hermes/profiles/signal/.env
nano ~/.hermes/profiles/signal/.env
signal gateway start
signal gateway status
```

Use the matching SOUL file from `agents/<AgentName>/SOUL.md`.

## 7. Set up Obsidian memory

```bash
mkdir -p "$HOME/Documents/Obsidian Vault/Agents"
cp -R agents/* "$HOME/Documents/Obsidian Vault/Agents/"
```

## 8. Start gateways

```bash
hermes gateway start
signal gateway start
blaze gateway start
kaijeaw gateway start
zegna gateway start
bolt gateway start
protocol gateway start
```

Start Qwen only after Ollama is installed and a local model is available.

## 9. Verify

```bash
hermes profile list
hermes gateway status
signal gateway status
protocol gateway status
```

Open each Telegram bot and send `/start` then `/status`.

## 10. Daily repo update job

Jet's repo uses a Hermes cron job to run `scripts/export_sanitized_agent_system.py` and push changes daily. If you want the same behavior, edit the paths in the script first, then create your own cron job.
