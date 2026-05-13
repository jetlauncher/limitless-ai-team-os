---
title: "Orgo Pricing and Client Use Brief"
date: 2026-05-13
source:
  - https://www.orgo.ai/pricing
  - https://docs.orgo.ai/quickstart
  - https://docs.orgo.ai/introduction
  - https://docs.orgo.ai/guides/models#use-any-model
  - https://docs.orgo.ai/guides/instance-types
  - https://docs.orgo.ai/guides/auto-stop
  - https://www.orgo.ai/privacy
tags: [orgo, ai-agents, client-delivery, pricing, security]
---

# Orgo Pricing and Client Use Brief

## What Orgo is

Orgo is cloud desktop infrastructure for AI agents. It launches Linux cloud computers that agents can control via screenshots, click/type/key/scroll, bash, Python exec, and an OpenAI-compatible chat completion endpoint.

Core positioning: **computers for AI agents** / **desktop infrastructure for AI agents**.

## Official pricing checked May 13, 2026

Monthly billing:

- Hacker: $39/month
  - 5 persistent computers
  - 1 vCPU / 4GB RAM
  - $5/month AI credits
  - 40GB storage
  - 1Gbps network
  - Snapshots
  - Static IP
  - Team features

- Team: $149/month
  - 20 persistent computers
  - 2 vCPU / 8GB RAM
  - $25/month AI credits
  - 160GB storage
  - 1Gbps network
  - 5 snapshots
  - 1 static IP
  - Team workspace

- Scale: $299/month
  - 50 persistent computers
  - 4 vCPU / 16GB RAM
  - $100/month AI credits
  - 400GB storage
  - 1Gbps network
  - 20 snapshots
  - 3 static IPs
  - Team workspace

Yearly billing, with 3 months free:

- Hacker: $29/month, $351 billed yearly
- Team: $112/month, $1,341 billed yearly
- Scale: $224/month, $2,691 billed yearly

Dedicated clusters, tenant isolation, or SLAs: contact `spencer@orgo.ai` or book a call.

## Instance types

- Standard: 4GB RAM, API identifier `orgo-computer-small`
- Medium: 8GB RAM, API identifier `orgo-computer-medium`
- Large: 16GB RAM, API identifier `orgo-computer-large`
- XL: 32GB RAM, API identifier `orgo-computer-xl`

All include Linux OS, API access, and default 1280x720 resolution.

## How it works

Quickstart flow:

1. Create account and get API key from `orgo.ai/start` / `orgo.ai/workspaces`.
2. Create workspace.
3. Create computer inside workspace.
4. Control computer through API: screenshot, click, type, key, scroll, bash, Python exec.
5. Let an AI model drive it via `/api/v1/chat/completions` with `computer_id`.
6. Stop/start/restart/delete computers via API.

Orgo supports raw HTTP, Python SDK, and TypeScript SDK. SDK install: `pip install orgo`.

## Models

Docs say Orgo can work with Claude, OpenAI GPT/computer-use, Gemini, OpenClaw, or any model that can drive computer actions. Orgo provides the computer; the operator chooses the model.

## Auto-stop

- Free-tier computers auto-stop after 15 minutes.
- Paid plans have auto-stop disabled by default.
- Paid plans can configure `auto_stop_minutes` per computer to reduce waste.
- Orgo preserves desktop/files/process state when suspended and can restart later.

## Security notes from public docs

Privacy policy says Orgo collects:

- Email
- Usage data
- VM activity logs

Shared with:

- Cloud infrastructure providers
- Payment processors
- Minimal analytics

Security statement says:

- Industry-standard encryption
- Isolated VMs
- Regular security audits

Important gap:

- Public `/security` page returned 404 in prior review.
- Need private/vendor docs before regulated or sensitive client use: DPA, SOC2/security report, subprocessors, retention, tenant isolation details, admin/audit logs, breach process.

## Client-use recommendation

Use Orgo as the **cloud computer layer**, not the whole AI team product.

Recommended client deployment:

- One Orgo workspace per client.
- One computer per agent or risky workflow.
- Install Hermes/OpenClaw/Claude Code/Codex inside the Orgo computer if needed.
- Connect only approved tools/scopes.
- Maintain client memory in a separate Obsidian vault/folder.
- Use watchdogs and alerts for failures.
- Record a Loom demo showing the agent operating its own cloud computer.

Best first customer use cases:

- Executive assistant agent
- Research/browser automation
- Website/admin dashboard tasks
- Content operations
- CRM cleanup/checking
- Internal reporting
- Lead enrichment using public data

Avoid first:

- Finance operations
- Healthcare data
- Legal privileged documents
- Anything requiring strong enterprise audit/SLA until Orgo provides dedicated tenant/security docs.

## Jet packaging idea

For clients, pitch:

> We give your AI employee its own secure cloud computer, company memory, approved tools, and weekly monitoring — so it can do real work without touching your personal laptop or sharing credentials in chat.

Recommended pricing economics:

- If charging clients $2k–$5k/month, Orgo infra at $39–$299/month is financially workable.
- For first pilots, use Hacker or Team.
- For many clients, do not mix clients inside one general workspace unless tenant boundaries are clear; prefer one workspace per client and move to dedicated clusters if needed.
