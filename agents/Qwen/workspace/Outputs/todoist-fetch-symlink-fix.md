# Todoist Fetch Script — Symlink Fix

**Date:** 2026-05-12  
**Status:** Fixed, needs cron re-run

## Problem
Qwen's cron job failed with:
```
Blocked: script path resolves outside the scripts directory
('/Users/ultrafriday/.hermes/profiles/qwen/scripts'): 'qwen_todoist_fetch.py'
```

## Root cause
`~/.hermes/profiles/qwen/scripts/qwen_todoist_fetch.py` was a **symlink** pointing to:
```
-> /Users/ultrafriday/.hermes/scripts/qwen_todoist_fetch.py
```
The symlink target lives in `~/.hermes/scripts/` which is outside the allowed Qwen profile scripts directory (`~/.hermes/profiles/qwen/scripts/`). The cron sandbox blocked it for resolving outside the scripts directory.

## Fix applied
- Removed the symlink (`rm ~/.hermes/profiles/qwen/scripts/qwen_todoist_fetch.py`)
- Copy-replaced it with a real file (`cp ~/.hermes/scripts/qwen_todoist_fetch.py ~/.hermes/profiles/qwen/scripts/qwen_todoist_fetch.py`)
- Verified permissions: `-rwxr-xr-x`

## Verification
- File size: 4773 bytes (was 56 bytes as symlink — now a real file)
- File command: "Python script text executable, ASCII text" (not a symlink)
- The file is now genuinely inside the Qwen profile scripts directory

## Next step
Re-run the cron job for `qwen_todoist_fetch.py`. It should pass the path check now.

## Recommendation
**Audit all agent scripts for similar symlinks.** Any cross-directory symlinks will hit the same sandbox block. Check `find ~/.hermes/profiles/ -type l` for other offenders.
