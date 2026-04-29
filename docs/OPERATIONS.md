# Operations Manual

## Common commands

```bash
hermes profile list
hermes gateway status
<agent> gateway status
<agent> cron list --all
```

## Create a new profile

```bash
hermes profile create <name> --clone-all
hermes profile alias <name> --name <name>
cp agents/<Agent>/SOUL.md ~/.hermes/profiles/<name>/SOUL.md
cp examples/env/profile.env.example ~/.hermes/profiles/<name>/.env
chmod 600 ~/.hermes/profiles/<name>/.env
```

## Start a gateway

```bash
<agent> gateway start
<agent> gateway status
```

## Scheduled jobs

Use Hermes cron for scheduled agent work:

```bash
hermes cron list --all
hermes cron create '0 8 * * *' 'Self-contained prompt...' --name my-job --deliver origin
```

## Update this mirror repo manually

```bash
cd ~/Projects/limitless-ai-team-os
python3 scripts/export_sanitized_agent_system.py
python3 scripts/validate_no_secrets.py
git add .
git commit -m "chore: refresh agent system mirror"
git push
```
