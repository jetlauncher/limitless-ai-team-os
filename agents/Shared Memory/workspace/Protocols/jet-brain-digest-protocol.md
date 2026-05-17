# Jet Brain Digest Protocol

Purpose: make Jet's full Hermes/Obsidian/Limitless workspace usable every day without forcing him to inspect folders.

## Inputs

1. Nightly workspace scan output:
   - `Agents/Shared Memory/Projects/Digests/workspace-digest-scan-YYYY-MM-DD.md`
   - `Agents/Shared Memory/Projects/Digests/workspace-classification-YYYY-MM-DD.csv`
2. Agent daily notes:
   - `Agents/{Hermes,Signal,Blaze,Bolt,Kaijeaw,Pixel,Protocol,Qwen,Zegna}/Daily/YYYY-MM-DD.md`
3. Shared daily handoff:
   - `Agents/Shared Memory/Daily/YYYY-MM-DD.md`
4. Business truth sources when relevant:
   - Airtable `Limitless Sales` → table `1. transactions` → field `ยอดโอน`
   - Gmail/Calendar/Drive only for explicit ops briefings
5. Live app truth:
   - `~/Documents/Limitless OS/Live Vercel Project Links.md`

## Daily Telegram digest format

Keep under 10 bullets unless urgent.

```markdown
## Jet Brain Digest — YYYY-MM-DD

**Command center**
- [1 active dashboard/link/task]
- [2]
- [3]

**Revenue/Ops**
- [Airtable revenue/payment/register/email signal]

**Agent fleet**
- [cron failures/stuck jobs/noisy agents/missing memory notes]

**Jet source signals**
- Plaud: [1 key idea / decision if new]
- YouTube: [1 reusable teaching/content insight if new]
- Brain dump: [1 open loop or project seed if new]
- Apple Notes: [1 promoted note if any]

**Content + research**
- [top 1]
- [top 2]
- [top 3]

**Teaching/Product**
- [new/changed asset]

**Needs Jet decision**
- [Decision] — recommended default: [default]

**Sources**
- `path/or/url`
- `path/or/url`
```

## Weekly attachment format

Create Markdown and optional PDF:

- Wins
- Open loops
- Dashboard/app health
- Revenue trend
- Content produced
- Teaching assets
- Project drift
- Cleanup recommendations
- Next week priorities
- Source links

## Rules

- Digest changes since the last scan, not the entire vault.
- Cite source paths/URLs.
- Use Airtable for revenue truth; local notes are supporting context.
- Do not include secrets, tokens, auth files, hidden credential data, or raw logs.
- GBrain remains read-only sidecar until retrieval benchmark beats Jet Brain v0.
- If uncertain, label `Needs Kelly review` rather than inventing facts.
