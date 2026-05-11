# Todoist Integration Setup Needed

**Date created:** 2026-05-12  
**Script:** `~/.hermes/scripts/qwen_todoist_fetch.py`  
**Status:** `TODOIST_NOT_CONFIGURED`

## What's missing
The Qwen Todoist fetcher needs an API token to query tasks.

## How to fix
Set the Todoist API token in one of these locations:

1. **Config file (recommended):**  
   Write the token to: `~/.config/todoist/api_key`

2. **Environment variable:**  
   Set: `export TODOIST_API_TOKEN=[REDACTED]

3. **Verify it works:**  
   ```bash
   python3 ~/.hermes/scripts/qwen_todoist_fetch.py
   ```

## Selection rule
- Tasks with labels: `qwen`, `ai`, `agent`, or `delegate`
- Tasks starting with: `Qwen:`, `AI:`, or `Agent:`
- To also scan Inbox candidates: set `TODOIST_QWEN_INCLUDE_INBOX=1`

## Notes
- Qwen does **not** complete, modify, or delete Todoist tasks — only reads them.
- The fetcher script itself exists and runs correctly at `~/.hermes/scripts/qwen_todoist_fetch.py`.
