---
title: Hermes Agent Masterclass
source: https://x.com/akshay_pachaar/status/2054564519280804028
source_author: Akshay Pachaar
fetched: 2026-05-15
verified_via:
  - https://api.fxtwitter.com/akshay_pachaar/status/2054564519280804028
  - https://r.jina.ai/http://x.com/akshay_pachaar/status/2054564519280804028
---

# Hermes Agent Masterclass — Notes

X Article by Akshay Pachaar. Core thesis: Hermes compounds through identity (`SOUL.md`), persistent memory, self-evolving skills, curator maintenance, optional GEPA optimization, multi-profile agents, Telegram gateways, and cron jobs.

## Key ideas extracted

- Hermes Agent crossed 90,000 GitHub stars in two months.
- Main differentiator: runtime skill learning + persistent multi-layer memory + optional GEPA/offline skill optimization.
- Identity layer: `SOUL.md` defines personality, tone, boundaries, and is loaded before memory/skills.
- Memory layers:
  - Tiny always-in-context memory/profile files.
  - Full-text session search over SQLite history.
  - Optional external memory providers.
- Skills are procedural memory, progressively disclosed, and should be created/updated after complex workflows or corrections.
- Curator prevents skill sprawl through stale/archive review and snapshots.
- GEPA reads execution traces and optimizes skills offline with evals and PR gates.
- Profiles allow isolated agents: designer, programmer, researcher, each with own memory, skills, SOUL, Telegram bot.
- Cron in plain English powers daily digests and autonomous routines.

## Jet/Kelly implications

- Already strong: profiles, Telegram gateways, cron, SOUL files, skills, curator.
- Main gaps to consider: GEPA not installed, xurl auth incomplete, Notion integration visibility incomplete, dedicated visual designer profile missing, cron/output pruning and evaluation/scorecards could be stronger.
