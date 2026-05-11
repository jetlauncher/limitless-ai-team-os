# 2026-05-11 Automation Trim

Timestamp: 2026-05-11 16:12:11 +07

## Changes applied

### Zegna
- Profile model changed from `gpt-5.5` / `openai-codex` to local Ollama-compatible `qwen3.6:35b` via `http://127.0.0.1:11434/v1`.
- `Zegna style + cool-stuff scout → Notion archive` reduced from 4x/day (`9,13,17,21`) to 2x/day (`9,17`).
- Daily curation page refresh remains active, local delivery only.

### Signal
Kept max 4 user-facing updates/day:
- `signal-daily-x-bookmarks-research-5am` — 05:00
- `signal-ai-morning-brief` — 08:30
- `signal-high-signal-ai-watch` — changed from every 120m to 14:00 daily
- `signal-daily-ai-intel-report-9pm` — 21:00

Paused:
- `signal-ai-evening-brief`
- `signal-x-twitter-high-alert-scan`
- `signal-daily-x-posts-to-notion-9pm`
- `Signal daily Notion work wrap`

### Blaze
- Paused `all-day-content-research-momentum` every-2h job.
- Kept only the main content generators:
  - `daily-content-engine-best-pick` — 09:00
  - `midday-content-burst` — 13:00
- Added a prompt hard cap to both active Blaze content jobs: max ~10 publishable pieces/day across scheduled Blaze output.
- `daily-scheduled-content-platform-update` remains active but changed to local delivery only.

## Durable preference saved
- Zegna local model.
- Signal ≤4 user-facing updates/day.
- Blaze ≤10 publishable pieces/day.
