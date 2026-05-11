# Fix: Qwen Todoist Cron Script Path

## Problem
The Qwen task-fetching cron job was configured with the wrong script path:
- **Wrong:** `/Users/ultrafriday/.hermes/profiles/qwen/scripts/qwen_todoist_fetch.py` (not found)
- **Correct:** `/Users/ultrafriday/.hermes/scripts/qwen_todoist_fetch.py` (exists, 4773 bytes)

## Current Status
- The cron job has **no longer been registered** in the active cron system (`/Users/ultrafriday/.hermes/cron/jobs.json`).
- There is currently **no active Qwen todoist cron**.
- The script itself works fine at the correct location.

## Fix (when you re-add the Qwen todoist cron)
```
Script path: ~/.hermes/scripts/qwen_todoist_fetch.py
```

## Files Referenced
- Script: `/Users/ultrafriday/.hermes/scripts/qwen_todoist_fetch.py`
- Script: [valid, runs correctly, fetches Qwen todoist tasks]
- Correct script: [valid, runs correctly, fetches Qwen todoist tasks]

---
Auto-generated 2026-05-11
