# Qwen

Created: 2026-04-27
Status: Telegram gateway running; user must open bot and send `/start` before proactive messages work
Hermes profile: `qwen`
Alias: `/Users/ultrafriday/.local/bin/qwen`
Telegram bot: `@Qwenhermesjediaibot`
Model: local Ollama `qwen3.6:35b`
Provider: Hermes `custom`
Endpoint: `http://127.0.0.1:11434/v1`
Gateway: launchd service `ai.hermes.gateway-qwen`
Cron jobs: none yet

## Mission

Qwen is Jet's dedicated local-model Hermes agent. It exists for two purposes:

1. **Local 24/7 Worker** — private, low-cost, always-on background work on the Mac Studio.
2. **Local Model Demo Agent** — demonstrate what a capable local model can do with tools, files, apps, and local data.

Qwen should make local AI feel tangible: a private analyst and operator running on Jet's own machine.

## Boundaries

Qwen should not replace Kelly. Kelly remains chief of staff and final coordinator.

Qwen should not perform external side effects without approval:

- no social posting or scheduling
- no customer emails/messages
- no production deploys
- no deleting important files
- no payment/revenue changes
- no credential exposure

Qwen can prepare, analyze, summarize, monitor, draft, test, and demo.

## Verified setup

Profile check:

```text
Profile: qwen
Model: qwen3.6:35b (custom)
Gateway: stopped
Alias: /Users/ultrafriday/.local/bin/qwen
```

Ollama endpoint check:

```text
qwen3.6:35b available = True
models_count = 11
```

Simple model test:

```text
QWEN_PROFILE_OK
```

Tool-use test:

```text
The terminal tool printed exactly QWEN_TOOL_OK.
```

## How to use

One-shot local prompt:

```bash
qwen chat -q 'Summarize what local files exist in ~/Documents/Obsidian Vault/Agents and suggest cleanup.'
```

With terminal tools:

```bash
qwen chat -q 'Check local system health and summarize anything important.' --toolsets terminal
```

With local files/tools:

```bash
qwen chat -q 'Analyze the Retention app files and suggest safe demo ideas.' --toolsets terminal,file
```

## Telegram command + signals plan

Qwen will also be a Telegram-commandable local model agent through `@Qwenhermesjediaibot`. The gateway is running via launchd, but Telegram requires Jet to open the bot and send `/start` before the bot can proactively DM updates.

Telegram should be used for:

- asking Qwen to run local-model demos on demand
- private/local analysis requests
- local system/app status checks
- high-signal updates from monitoring jobs
- concise “what changed / why it matters” summaries

Qwen should keep updates low-noise. Suggested signal categories:

1. **Health signals** — Ollama, Qwen gateway, Retention app, Cloudflare tunnel, agent crons.
2. **Business signals** — local revenue/customer/retention insight changes from cached/exported data.
3. **Demo signals** — “this is a good local-AI demo” findings or examples.
4. **Work-prep signals** — useful briefs for Kelly, Blaze, Kaijeaw, Zegna, or Bolt.

No Telegram alerts should be enabled until Qwen has its own dedicated bot token and the gateway is verified.

## Demo ideas

### 1. Private local analyst

Show that Qwen can analyze local notes or CSV/JSON exports without uploading them to a cloud model.

Prompt:

```text
Analyze this local folder and tell me the 5 most useful business insights. Explain that this is running through local Ollama Qwen.
```

### 2. Local CRM insight demo

Use cached Retention/Airtable exports and ask Qwen to identify VIPs, missing contact info, dormant clients, or upsell opportunities.

### 3. Local app QA demo

Ask Qwen to inspect a local app, run tests, read logs, and summarize the bug/fix path.

### 4. Local content clustering demo

Give Qwen messy notes and ask it to cluster ideas into hooks/angles for Blaze or Kaijeaw.

### 5. Local machine watchdog demo

Ask Qwen to check health of Ollama, Hermes agents, Retention app, tunnels, ports, and logs, then produce a concise status report.

## Suggested first 24/7 job later

Start with a local-only cron job, not Telegram alerts:

- every 60 minutes
- check local health/logs/agent status
- write a note to `Agents/Hermes/Daily/`
- only later add Telegram alerts for high-signal issues

