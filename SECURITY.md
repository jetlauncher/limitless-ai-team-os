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

The sanitizer is conservative, but humans should still review diffs before making a public/student-facing version.

## Credential storage pattern

Use local files or env vars:

```text
~/.hermes/.env
~/.hermes/profiles/<profile>/.env
~/.config/<service>/api_key
```

Repo files should only show placeholders like `[REDACTED]`, `your-api-key-here`, or empty env vars.
