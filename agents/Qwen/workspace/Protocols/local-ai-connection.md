# Qwen Local AI Connection

Updated: 2026-05-16

## Endpoint

- Runtime: Ollama / local OpenAI-compatible API.
- Base URL: `http://127.0.0.1:11434/v1`
- Native Ollama URL: `http://127.0.0.1:11434`
- Model: `qwen3.6:35b`
- API key: not required locally; use placeholder `no-key-required` when a client expects a token.

## Hermes profile

- Profile: `qwen`
- Path: `/Users/ultrafriday/.hermes/profiles/qwen/`
- Alias: `qwen`
- Gateway launchd label: `ai.hermes.gateway-qwen`
- Telegram gateway: connected.

## Configuration

`~/.hermes/profiles/qwen/config.yaml`:

- provider: `custom`
- model: `qwen3.6:35b`
- base_url: `http://127.0.0.1:11434/v1`
- api_mode: `chat_completions`
- context_length: `8192`

The model advertises a much larger context, but local runtime should default to a smaller working context for reliability and speed. Use larger context only for explicit long-document work.

## OpenClaw model registry

OpenClaw already has an Ollama provider with `ollama/qwen3.6:35b` available in `~/.openclaw/openclaw.json`.

## Operational note

Only one Ollama server should own port `127.0.0.1:11434`. Duplicate Homebrew + GUI Ollama servers can make generation calls hang. Current target is the Homebrew service `homebrew.mxcl.ollama`.
