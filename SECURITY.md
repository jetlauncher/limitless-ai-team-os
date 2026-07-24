# Security Policy

## Never commit secrets

Do not commit:

- `.env`
- API keys
- OAuth tokens
- Telegram bot tokens
- GitHub tokens
- Session databases
- Logs
- Customer/student/payment data

## Validate before push

Run:

```bash
python3 scripts/validate_no_secrets.py
```

It scans the working tree for provider keys, bot/OAuth tokens, private key blocks,
committed `.env` files and credential-looking assignments, and exits non-zero on a hit.
The sanitizer is conservative, but humans should still review diffs before making a
public/student-facing version.

## Hardening the example configs

`scripts/sanitize_lib.py` is the shared redaction layer used by the export scripts. On
every export it also hardens the config templates so a live setup cannot leak unsafe
settings into the mirror:

- credential fields (`api_key`, `token`, `password`, MCP `Authorization` headers, MCP
  `env` secrets) are emptied or replaced with `${ENV_VAR}` placeholders
- private workspace identifiers (Telegram chat IDs, Discord/Slack channel and guild IDs)
  are cleared
- `command_allowlist` is emptied, `approvals.mode` is forced to `manual` and
  `security.tirith_fail_open` to `false`

Re-harden the committed templates at any time with:

```bash
python3 scripts/sanitize_lib.py configs
```

## Agent authorization

Before starting a gateway:

- set `telegram.allowed_chats` (and the Discord/Slack/Matrix equivalents) to your own IDs;
  an empty allowlist means anyone who finds the bot can drive your agent
- keep `command_allowlist` empty unless you truly want a command auto-approved without a
  prompt — entries such as `recursive delete`, `delete in root path`, `sudo with
  combined-flag privilege escalation` or `SQL DROP` disable the approval prompt for
  destructive actions
- keep `security.tirith_fail_open: false` so a failing policy check blocks instead of
  silently allowing the action

## Credential storage pattern

Use local files or env vars:

```text
~/.hermes/.env
~/.hermes/profiles/<profile>/.env
~/.config/<service>/api_key
```

Repo files should only show placeholders like `[REDACTED]`, `your-api-key-here`, or empty env vars.
