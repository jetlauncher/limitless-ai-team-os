# Todoist API Configuration Needed

**Status:** Not configured  
**Detected:** 2026-05-19  

## What's needed

Qwen's automated Todoist fetch script (`qwen_todoist_fetch.py`) cannot read tasks because no API token is configured.

## Setup steps

1. Get a Todoist Personal Access Token:  
   [REDACTED] → Generate new token (scopes: `write:tasks`, `read:tasks`)

2. Store the token securely:

```bash
mkdir -p ~/.config/todoist
# Token goes here — never print or share it
echo '<YOUR_TOKEN>' > ~/.config/todoist/api_key
chmod 600 ~/.config/todoist/api_key
```

3. Export the environment variable for automated runs:

```bash
export TODOIST_API_TOKEN='<YOUR_TOKEN>'
```

4. Optionally include Inbox candidates:

```bash
export TODOIST_QWEN_INCLUDE_INBOX=1
```

## Selection rule (already configured)

Qwen picks up tasks matching:
- Label: `qwen`, `ai`, `agent`, `delegate`  
- OR Title prefix: `Qwen:`, `AI:`, `Agent:`

## Next time this triggers

Once configured, the fetch script will return a JSON payload of selected tasks. Qwen will then process safe local/draft/summarization tasks and write outputs under `Agents/Qwen/Outputs/Todoist/`.
