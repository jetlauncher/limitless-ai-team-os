# Claude Code OAuth Access — 2026-05-10

Status: verified at 2026-05-10 17:13 +07.

## What changed
- Claude Code CLI was re-authenticated with Jet’s Claude Max / Claude.ai OAuth login.
- The desired auth mode is **Claude Max account**, not Anthropic Console API billing.
- `ANTHROPIC_API_KEY` was verified as not set in the active environment.

## Verification commands
```bash
claude auth status --text
python3 - <<'PY'
import os
print('ANTHROPIC_API_KEY_set=', bool(os.environ.get('ANTHROPIC_API_KEY')))
PY
claude -p 'Return exactly: CLAUDE_MAX_OAUTH_OK' --model sonnet --max-turns 1 --no-session-persistence
```

Expected:
- `Login method: Claude Max account`
- `ANTHROPIC_API_KEY_set=False`
- `CLAUDE_MAX_OAUTH_OK`

## Agent guidance
- All Hermes profiles on this Mac can invoke the global `claude` CLI if they have terminal access.
- Before large builds, agents should verify OAuth mode first.
- Do not run `claude auth login --console` unless Jet explicitly wants Anthropic Console/API-billed usage.
- Do not print credentials or token files.

## Bolt
Bolt was explicitly smoke-tested through its own Hermes profile:

```text
Claude auth: Max account OAuth OK; ANTHROPIC_API_KEY_set=False; test prompt returned BOLT_CLAUDE_OAUTH_OK.
```

## Profiles checked
- Blaze
- Bolt
- Kaijeaw
- Protocol
- Qwen
- Signal
- Zegna

Each profile was checked for no `ANTHROPIC_API_KEY` in its `.env`, and its `SOUL.md` was updated with the rule to verify Claude Max OAuth before large Claude Code builds.

## Related notes
- [[Hermes/Memory/MEMORY]]
- [[Bolt/README]]
