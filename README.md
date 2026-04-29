# Limitless AI Team OS

A private, student-cloneable operating system for building a multi-agent AI team with Hermes Agent, Telegram bots, Obsidian memory, scheduled jobs, and platform integrations.

This repository is a **sanitized mirror** of Jet/Jedi Trinupab's agent setup. It includes agent roles, profile templates, configuration examples, installation instructions, and automation scripts — but **never real API keys or secrets**.

> Thai version: [README.th.md](README.th.md)

## What this system gives you

- A Chief-of-Staff agent: **Kelly / Hermes**
- A research agent: **Signal**
- A content agent: **Blaze**
- A Thai voice agent: **Kaijeaw**
- A taste/gadgets scout: **Zegna**
- An app/site builder: **Bolt**
- A local/private model worker: **Qwen**
- A newsletter/Beehiiv agent: **Protocol**
- Shared Obsidian memory folders for transparent handoffs
- Telegram gateway setup for each bot
- Cron/scheduled job patterns
- Safe config examples students can copy and fill with their own keys

## Repository map

```text
agents/                 Agent SOUL files + Obsidian workspace docs
configs/                Sanitized Hermes config templates
examples/               .env examples and setup templates
docs/                   Architecture, API key guide, operations manual
scripts/                Export/update helpers and validation scripts
.github/workflows/      Optional GitHub Actions checks
```

## Quick start

```bash
git clone git@github.com:jetlauncher/limitless-ai-team-os.git
cd limitless-ai-team-os
bash scripts/install-hermes.sh
cp examples/env/root.env.example ~/.hermes/.env
# Fill in your own API keys.
```

Then follow: [INSTALL.md](INSTALL.md)

## Safety model

This repo intentionally excludes:

- Real `.env` files
- API keys and OAuth tokens
- Bot tokens
- Local auth/session databases
- Logs
- Message/session transcripts
- Customer/student data
- Payment/revenue records

Every committed config is either sanitized or an example.

## Daily update automation

Jet's live machine runs a scheduled job that refreshes this repo daily from the local agent workspaces using:

```bash
scripts/export_sanitized_agent_system.py
scripts/validate_no_secrets.py
git commit && git push
```

Students should not run the daily mirror job unless they understand what paths it reads and have reviewed the sanitizer.

## License

Private educational/internal use unless Jet changes the repo visibility or licensing.
