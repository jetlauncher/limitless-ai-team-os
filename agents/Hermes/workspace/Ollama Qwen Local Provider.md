# Ollama Qwen Local Provider

Created: 2026-04-27
Owner: Kelly / Hermes ops

## Current local state

- Ollama is installed at `/usr/local/bin/ollama`.
- Ollama is listening locally on port `11434`.
- Ollama API version checked: `0.21.2`.
- OpenAI-compatible endpoint works at: `http://127.0.0.1:11434/v1`.
- Main local model verified: `qwen3.6:35b`.
- Model details from Ollama: Qwen 36B MoE GGUF, `Q4_K_M`, around 23.9 GB.

## Verified tests

### Direct OpenAI-compatible API

Endpoint tested:

```text
http://127.0.0.1:11434/v1/chat/completions
```

Result: success. Model returned `LOCAL_OK` when given enough `max_tokens`.

Note: Qwen uses a `reasoning` field and may spend tokens thinking before producing `content`, so tiny `max_tokens` values can return empty `content`. Use a healthy token budget for short tasks too.

### Hermes temporary local-provider test

A temporary, non-production Hermes home was created at:

```text
/tmp/hermes-ollama-test
```

Minimal config that worked:

```yaml
model:
  default: qwen3.6:35b
  provider: custom
  base_url: http://127.0.0.1:11434/v1
  api_key: [REDACTED]
  api_mode: chat_completions
agent:
  max_turns: 4
memory:
  memory_enabled: false
  user_profile_enabled: false
```

Hermes test result:

```text
HERMES_OLLAMA_OK
```

Hermes tool-use test result:

```text
The result is: LOCAL_TOOL_OK
```

This confirms local Qwen through Ollama can run Hermes and call tools.

## Important Hermes routing finding

The active Kelly/default config currently routes to:

```yaml
model:
  default: gpt-5.5
  provider: openai-codex
  base_url: https://chatgpt.com/backend-api/codex
```

Because the saved provider is `openai-codex`, simply setting environment variables like `HERMES_INFERENCE_PROVIDER=custom` did not override the production config in a normal run. For local Ollama agents, use a separate Hermes profile with its own `config.yaml`, or run with an isolated `HERMES_HOME`.

## Recommended 24/7 architecture

Do **not** replace Kelly’s main model with local Qwen yet. Better pattern:

1. Keep Kelly/default on GPT-5.5 for high-stakes chief-of-staff work.
2. Create a dedicated local Hermes profile, e.g. `localqwen` or `nightwatch`.
3. Configure that profile to use:
   - provider: `custom`
   - model: `qwen3.6:35b`
   - base_url: `http://127.0.0.1:11434/v1`
   - api_key: [REDACTED]
   - api_mode: `chat_completions`
4. Give it narrow 24/7 jobs first:
   - offline inbox/news triage drafts
   - local file/Obsidian indexing and summarization
   - retention/customer insight pre-analysis
   - dashboard QA/watchdog checks
   - content idea clustering for Blaze/Kaijeaw
   - gadget/brand watch summaries for Zegna
   - landing-page screenshot/checklist audits for Bolt
5. Keep approval gates for anything external:
   - no posting
   - no emailing customers
   - no deleting/canceling/scheduling
   - no production deploys without explicit approval

## Candidate first automations

- **Local Night Watch:** every 30–60 minutes, inspect system health, logs, Retention app health, and queue anomalies; only alert Kelly/Jet when something material changes.
- **Revenue/Retention Analyst:** pull Airtable exports/cache and produce local notes about VIPs, high-potential clients, and missing-contact cleanup.
- **Content Pre-Processor:** cluster ideas and raw notes overnight, then hand structured briefs to Blaze/Kaijeaw instead of publishing.
- **Site QA Scout:** Bolt-owned local job that checks landing pages/forms/buttons/mobile screenshots and creates issues/notes.
- **Taste Radar Pre-Screener:** collect RSS/web inputs for Zegna and summarize shortlists locally before sending only the best finds.

## Next step

Create a dedicated local profile and one safe cron job with local delivery first. After a few good runs, add Telegram alerts for only high-signal events.
