---
title: "AI Agent Team Platform Security Review — Nick from Orgo Podcast"
source_video: "https://youtu.be/BI-MNjm1tTQ"
transcript_note: "[[2026-05-13 - Nick from Orgo - One Person AI Agent Business Playbook]]"
date: 2026-05-13
tags: [ai-agents, client-agent-teams, security, orgo, hermes, client-delivery]
status: draft-reviewed
---

# AI Agent Team Platform Security Review — Nick from Orgo Podcast

## Executive verdict

The podcast playbook is directionally strong for Jet's market: businesses do not want to buy tokens, models, or infrastructure; they want a reliable **AI employee / AI team** that knows their business and improves every week.

But for client delivery, the stack must be treated as **managed IT + security**, not just "cool agents." The safe version is:

1. **One client = one isolated workspace / VM / vault / credentials boundary.**
2. **Agents get least-privilege access only.**
3. **Every external tool connection uses OAuth or scoped service accounts, never shared passwords in chat.**
4. **Human approval gates for destructive/high-risk actions.**
5. **Observability + watchdogs + incident alerting from day one.**
6. **No healthcare/finance/legal production data until contracts, DPA, access control, logging, and platform trust docs are complete.**

My recommendation: use this playbook for **marketing agencies, real estate, education, creators, consultants, internal ops, and non-regulated SMBs first**. Avoid regulated/high-liability workflows until the security package is mature.

---

## Transcript storage

Saved transcript files:

- Raw text: `/Users/ultrafriday/clawd/youtube-transcripts/2026-05-13 - Nick from Orgo - One Person AI Agent Business Playbook.txt`
- Obsidian note: `/Users/ultrafriday/clawd/youtube-transcripts/2026-05-13 - Nick from Orgo - One Person AI Agent Business Playbook.md`
- Visible in Limitless OS through: `Inbox/YouTube Transcripts/`

Video metadata extracted:

- Video ID: `BI-MNjm1tTQ`
- Duration: `47:56`
- Transcript segments: `1,145`
- Transcript length: `42,307` chars

---

## Podcast playbook extracted

### Offer

- Sell an **AI employee**, not an AI agent.
- Keep offer simple: unlimited agents, usage, monitoring, support, security, ongoing changes.
- In reality most clients need 1–3 useful agents, not 100.
- Price point mentioned: about **$5k/month per customer**.
- Avoid talking about tokens/credits; sell business outcomes.
- First working agent should be live within ~48 hours.
- Ongoing onboarding/playbook target: ~30 days.

### Best early markets mentioned

Better starting markets:

- Marketing agencies
- Law firms, with caution and scoping
- Insurance agencies
- Manufacturers
- Wholesalers
- Real estate agencies

Avoid or delay:

- Healthcare
- Finance

Reason: regulatory burden, compliance, privacy, data sensitivity.

### Core customer problems

Executives have:

- Too many emails
- Too many meetings
- Too many follow-ups
- Too many open loops
- Too much context scattered across people/projects/tools

The first agent should usually solve an executive-level workflow, then expand vertically.

---

## Platforms/tools mentioned

### Customer-facing / delivery ops

- Granola — meeting notes, MCP/context
- Trello — customer-facing Kanban board / request queue
- Loom — async customer updates
- Calendly — booking link/funnel
- Superhuman — high-volume email workflow
- Asana — internal task management

### Agent harness / build tools

- Hermes Agent
- OpenClaw
- Claude Code
- OpenAI Codex

### Compute / place for agents to live

- Orgo
- Hostinger / VPS as alternative
- Local computers/Mac minis discussed and discouraged for scale

### Agent tools/context layer

- Composio
- AgentMail
- Obsidian
- Perplexity MCP
- Exa AI
- Context7 MCP
- Firecrawl
- X/Twitter MCP

### Models mentioned

- GPT 5.5 — podcast claim, not independently verified as public official model at time of review
- GLM 5.1 / Z.ai
- Kimi / Moonshot
- Opus 4.7 — podcast claim, not independently verified as public official model at time of review

---

# Platform security notes

## 1. Orgo

Official sources checked:

- https://www.orgo.ai/
- https://docs.orgo.ai/
- https://docs.orgo.ai/llms-full.txt
- https://www.orgo.ai/privacy
- https://www.orgo.ai/terms
- https://www.orgo.ai/security — checked, returned 404

What it does:

- Cloud computer / desktop infrastructure for AI agents.
- Gives agents a computer to operate visually/remotely.
- Supports workspace/project/computer concepts.
- Useful for demos, browser automation, isolated cloud desktops, and managing many customer agent machines from one place.

Security posture:

- Privacy docs mention usage data, VM activity logs, cloud infrastructure providers, payment processors, analytics.
- Public docs mention isolated VMs / encryption / audits, but I did **not** find detailed public trust docs, SOC 2 report page, DPA, subprocessor list, retention policy, or architectural isolation details.

Jet verdict:

- **Promising but needs vendor diligence before serious client data.**
- Good for demos and lower-risk client workflows.
- For paid client deployments, request from Orgo:
  - DPA
  - SOC 2 / security report
  - Subprocessors
  - VM isolation architecture
  - Logging/retention policy
  - Admin/audit logs
  - Breach notification terms
  - How VNC/shell/API access is secured

Guardrail:

- One Orgo workspace per client.
- Separate computers per agent/function.
- No shared credentials between clients.
- Avoid regulated data until vendor documentation is complete.

---

## 2. Hermes Agent

Official sources checked:

- https://hermes-agent.nousresearch.com/docs
- https://hermes-agent.nousresearch.com/docs/llms-full.txt
- https://github.com/NousResearch/hermes-agent

What it does:

- Local/self-hosted agent gateway + tool system.
- Supports model/provider switching.
- Supports tools, skills, cron jobs, messaging gateways, terminal/file/browser workflows.

Security posture:

- Secrets separated from config: `~/.hermes/.env` vs `~/.hermes/config.yaml`.
- Supports Docker/SSH terminal backends for safer execution.
- Has command scanning, secret redaction, blocklists, and gateway-level PII redaction features.
- Security depends heavily on operator configuration.

Jet verdict:

- **Best fit for Jet's own AI Team OS because we can control and harden it.**
- For clients, use separate deployments per client/trust boundary.

Guardrail:

- One client = one VM/container/OS user + separate Hermes config + separate secrets.
- Enable secret redaction.
- Use Docker/SSH backend where possible.
- Restrict tools per client.
- Add approval gates for email sending, posting, payments, deleting files, code deploys.

---

## 3. OpenClaw

Official sources checked:

- https://openclaw.ai/
- https://docs.openclaw.ai/
- https://github.com/openclaw/openclaw
- https://docs.openclaw.ai/gateway/security.md
- https://docs.openclaw.ai/gateway/sandboxing.md
- https://docs.openclaw.ai/tools/exec-approvals.md
- https://docs.openclaw.ai/gateway/secrets.md

Security posture:

- OpenClaw docs explicitly describe a personal-assistant trust model.
- It is **not** a hostile multi-tenant security boundary by itself.
- Sandboxing and secret refs exist but are optional/operator-controlled.

Jet verdict:

- **Useful but risky if deployed casually.**
- Good for single-client/single-trust-boundary setups.
- Do not run many unrelated clients through one shared OpenClaw gateway.

Guardrail:

- Separate gateway/VM/credentials per client.
- Run security audit commands.
- Use sandboxing and exec approvals.
- Keep messaging integrations tightly allowlisted.

---

## 4. Claude Code

Official sources checked:

- https://code.claude.com/docs/en/security.md
- https://code.claude.com/docs/en/settings.md
- https://code.claude.com/docs/en/admin-setup.md
- https://code.claude.com/docs/en/data-usage.md
- https://trust.anthropic.com

Security posture:

- Read-only by default, explicit permissions for edits/commands.
- Supports sandboxing and admin-managed settings.
- Enterprise/admin controls can govern tools, commands, MCP servers, and network destinations.
- Commercial terms differ from consumer plan data settings.

Jet verdict:

- **Strong for coding/build tasks, especially under Team/Enterprise/API terms.**
- Not the thing to sell directly to clients as their assistant, but excellent as a builder/operator behind the scenes.

Guardrail:

- Use managed settings for team/client work.
- Avoid consumer accounts for client-sensitive code/data.
- Keep approvals on for shell/network/destructive operations.

---

## 5. OpenAI Codex

Official sources checked:

- https://developers.openai.com/codex
- https://developers.openai.com/codex/agent-approvals-security.md
- https://developers.openai.com/codex/concepts/sandboxing.md
- https://developers.openai.com/codex/cloud.md
- https://developers.openai.com/codex/cloud/environments.md
- https://developers.openai.com/codex/cloud/internet-access.md
- https://developers.openai.com/codex/enterprise/governance.md
- https://trust.openai.com/

Security posture:

- Local sandboxing and approval policies.
- Cloud tasks run in isolated containers.
- Internet off by default in cloud agent phase.
- Docs explicitly warn about prompt injection, exfiltration, malware/dependency risk when internet is enabled.
- Enterprise governance/audit options exist.

Jet verdict:

- **Strong builder tool for code and automation.**
- Use for implementation, not necessarily as the client-facing assistant interface.

Guardrail:

- Disable internet unless required.
- Use domain allowlists.
- Review setup scripts before secrets/network access.
- Keep per-client repositories/environments isolated.

---

## 6. Hostinger / VPS

Official sources checked:

- https://www.hostinger.com/vps-hosting
- https://www.hostinger.com/legal/privacy-policy
- https://www.hostinger.com/legal/dpa
- https://developers.hostinger.com/

Security posture:

- General-purpose hosting/VPS, not agent-specific governance.
- Can be used as isolated infrastructure if hardened.
- You own OS patching, firewalling, secrets, logs, backups, incident response.

Jet verdict:

- **Acceptable as commodity infrastructure only if we manage hardening.**
- One VPS per client is safer than shared multi-client agent hosts.

---

## 7. Composio

Official sources checked:

- https://docs.composio.dev/docs
- https://composio.dev/security — checked, returned 404 during review

What it does:

- Provides 1,000+ toolkits/connectors for agents.
- Handles authentication/OAuth/API keys/tool execution for apps like Gmail, Slack, Notion, GitHub.
- Docs show concepts for users/sessions, authentication, workbench, observability, white-labeling auth, MCP/native tools.

Security posture:

- Very useful because it avoids asking clients to send usernames/passwords through chat.
- However, I did not find a public Composio security/trust page at `/security` during this review.

Jet verdict:

- **Useful but high-blast-radius. Treat as a privileged identity/connectors layer.**
- It may be safer than ad-hoc credential sharing, but it becomes a critical dependency.

Guardrail:

- Use OAuth and least-privilege scopes.
- One Composio project/account boundary per client if available.
- Review every connected app scope with the client.
- Never connect broad Gmail/Drive/Slack scopes without written approval.
- Keep a per-client connection inventory.

---

## 8. AgentMail

Official sources checked:

- https://www.agentmail.to/
- https://docs.agentmail.to/ via site link
- Homepage footer showed: SOC 2 compliant, Privacy Policy, Terms of Service, SOC 2, Subprocessors links.

What it does:

- Email inbox API for AI agents.
- Gives agents their own inboxes.
- Supports threads/replies, attachments, realtime events, custom domains, SDKs + MCP, semantic search, data extraction.

Jet verdict:

- **Good concept for agent identity and auditability.**
- Safer than letting the agent send from the founder's personal inbox.

Guardrail:

- Use per-agent/per-client addresses like `mia@clientdomain.com`.
- Keep sending limits.
- Require approval before external outbound emails until trust is proven.
- Log all sent emails.
- Do not use agent inboxes for receiving sensitive OTP/2FA unless specifically approved.

---

## 9. Granola

Official sources checked:

- https://docs.granola.ai/help-center/policies/privacy-policy
- Granola docs navigation showed DPA, vulnerability disclosure policy, and security reports/post-mortems.

Security posture from docs:

- Granola says third parties like OpenAI/Anthropic are not allowed to use Personal Data to train AI models.
- Uses de-identified data for model training with opt-out.
- Stores personal data in AWS U.S.
- Encrypts data at rest and in transit.
- Mentions AWS encrypted database systems, firewalls, VPCs, anti-virus/malware protection.

Jet verdict:

- **Good for meeting memory, but it captures sensitive conversations.**

Guardrail:

- Client consent before recording/transcribing meetings.
- Disable/opt out of model training where available.
- Avoid recording legal/HR/financial sensitive conversations unless client approves.
- Sync only relevant notes into the client vault, not every raw call forever.

---

## 10. Trello / Loom / Atlassian

Official sources checked:

- https://www.atlassian.com/legal/security-measures
- https://www.atlassian.com/trust
- Trello privacy/GDPR support docs were also checked in research.

Security posture:

- Trello and Loom are under Atlassian trust/legal security measures.
- Atlassian publishes technical/organizational security measures, access control, audit/accountability, incident response, physical/environmental security, data processing transparency, and supply chain risk management.

Jet verdict:

- **Good for low/medium-risk client workflow tracking and Loom updates.**
- Avoid storing secrets, credentials, private client documents, or regulated data in cards/videos.

Guardrail:

- Customer-facing Trello board should contain requests/status, not credentials.
- Use private boards and role-based access.
- Loom updates should avoid showing secrets/API keys/client PII on screen.

---

## 11. Calendly

Official sources checked:

- https://calendly.com/security

Security posture:

- Calendly security page lists enterprise-grade admin/security/data governance.
- Certifications/frameworks shown: SOC 2 Type 2, SOC 3, GDPR, CCPA, CSA STAR, PCI compliant, ISO/IEC 27001.
- Features listed: SSO, SCIM, domain control, activity log, role-based permissions, global retention policies, custom terms, data deletion, audit tracking.

Jet verdict:

- **Safe enough for booking/scheduling workflows.**
- Do not expose sensitive private calendar details unnecessarily.

---

## 12. Superhuman

Official sources checked:

- https://superhuman.com/security — returned page not found
- https://superhuman.com/trust — returned page not found during review, despite footer label/link text
- Public footer included Privacy Policy, Customer Business Agreement, Legal Notices, Trust link label.

Jet verdict:

- **Useful personal productivity tool, but not core agent infrastructure.**
- I would not make Superhuman a required platform for client deployments unless the client already uses it.

Guardrail:

- Keep it as Jet/operator email productivity, not an agent permission layer.

---

## 13. Asana

Official sources checked:

- https://trustcenter.asana.com/

Security posture:

- Asana Trust Center lists trust, security, privacy, AI, infrastructure documentation.
- Compliance listed includes SOC 2 Type 2, SOC 3, ISO/IEC 27001, 27017, 27018, 27701, GDPR, HIPAA, GLBA, FERPA, VPAT, and more.
- Product security categories include audit logging, data security, integrations, access monitoring, backups, data erasure, data access, logging, password security, DPA, subprocessors, customer audits.

Jet verdict:

- **Strong internal/project management option.**
- For customer-facing boards, Trello is simpler. For internal delivery ops, Asana is stronger.

---

## 14. Obsidian

Official sources checked:

- https://obsidian.md/privacy
- https://obsidian.md/help/Obsidian+Sync/Security+and+privacy
- https://obsidian.md/security

Security posture:

- Obsidian vaults are local markdown files.
- Obsidian Sync offers end-to-end encryption option.
- Obsidian says E2EE means Obsidian cannot read data and data remains encrypted even in server breach.
- Uses AES-256; docs mention third-party security audit reports.
- Local vault itself is not encrypted by Obsidian; device/disk security matters.

Jet verdict:

- **Excellent as the memory/context layer for AI agents.**
- For clients, create a dedicated client vault or folder with clear data boundaries.

Guardrail:

- One vault/folder per client.
- No cross-client notes.
- Use git or Sync backups.
- Do not store secrets in plain markdown; store references to secret manager paths.

---

## 15. Context/research MCPs

### Perplexity MCP

Use case:

- Up-to-date web/research context for setup tasks.

Risk:

- Sending client-specific queries to third-party search/answer service.
- Potential hallucination/citation risk if not verified.

Guardrail:

- Use for public docs and general research, not private client data.
- Require source URLs.

### Exa AI

Official source checked:

- https://exa.ai/docs/ — docs available; attempted old `/reference/mcp` path returned page not found.

Use case:

- Web search/research API for agents.

Guardrail:

- Use for public web research only unless DPA/security reviewed.

### Context7 MCP

Official source checked:

- https://context7.com/docs/overview

Security posture:

- Docs include sections for data privacy, infrastructure, authentication/access control, compliance/reporting, data safety, best practices, private sources, teamspace, on-premise.

Jet verdict:

- **Good for keeping agents grounded in current library/framework docs.**
- Use it for public docs and development setup. Be careful with private sources.

### Firecrawl

Use case:

- Web crawling/scraping for agent research.

Guardrail:

- Use for public pages only.
- Respect client compliance and website terms.

### X/Twitter MCP

Use case:

- Pulling social/X context.

Guardrail:

- Treat as public internet context, not reliable truth.
- Verify important claims with primary sources.

---

## Model claims check

The podcast mentions:

- GPT 5.5
- Opus 4.7
- GLM 5.1
- Kimi

Important:

- I should treat **GPT 5.5** and **Opus 4.7** as podcast claims / future/current-session labels, not independently verified public model availability unless confirmed against official provider docs at the time of use.
- For client work, model selection should be dynamic:
  - Default: strongest reliable low-cost model for tool calls.
  - Heavy coding/reasoning: Claude/Opus/Sonnet or Codex-class model.
  - Lightweight ops: cheaper open-source/open-router models.
  - Sensitive client data: use provider/account terms that clearly state data usage and retention.

---

# Recommended Limitless client-agent stack

## Conservative production stack

For real client work:

- **Agent harness:** Hermes Agent, one deployment per client
- **Compute:** separate VM/VPS/Orgo workspace per client
- **Memory:** Obsidian vault/folder per client
- **Connectors:** Composio only after scope approval
- **Agent email:** AgentMail per agent/client
- **Client requests:** Trello board or Asana project
- **Meetings:** Granola only with consent
- **Updates:** Loom with no secrets visible
- **Research/docs:** Context7 + Perplexity/Exa for public docs only
- **Coding helper:** Claude Code / Codex behind the scenes, not as client-facing product

## Safer client architecture

```text
Client Workspace
├── Client VM / Orgo workspace
│   ├── Hermes Agent gateway
│   ├── limited toolset
│   ├── watchdog + health checks
│   └── logs/alerts
├── Client Obsidian vault/folder
│   ├── Company context
│   ├── People/projects
│   ├── SOPs
│   └── Approved prompts/skills
├── Client connector boundary
│   ├── Composio project/connections
│   ├── Google/Slack/Notion/GitHub scoped OAuth
│   └── connection inventory
└── Client control board
    ├── Backlog
    ├── Approved
    ├── Doing
    ├── Review
    └── Done
```

## Minimum security checklist before selling

For each client:

- [ ] Signed scope of work
- [ ] Data classification: what agents may/may not access
- [ ] One isolated workspace/VM/vault per client
- [ ] Separate secrets and credentials per client
- [ ] OAuth scopes reviewed and documented
- [ ] Human approval for external email/posting/payments/deletes
- [ ] Logs enabled
- [ ] Watchdog for gateway crashes
- [ ] Backup plan for vault/config
- [ ] Offboarding plan: revoke tokens, export data, delete VM, archive vault
- [ ] Incident response contact path

## Red lines

Do not allow agents to:

- Share passwords in chat
- Hold raw client credentials in Obsidian
- Use one shared Gmail/Slack/Notion admin token across clients
- Send external emails without approval during early deployment
- Access finance/health/legal privileged data without stronger contracts and controls
- Run shell commands on shared machines across clients
- Autonomously delete data or deploy code without review

---

# Client offer packaging for Jet

## Offer name idea

**Limitless AI Team Setup**

Positioning:

> We install a private AI employee/team inside your business — trained on your context, connected to approved tools, monitored every week, and improved continuously.

## Package levels

### Starter — Executive AI Assistant

- 1 agent
- Obsidian context vault
- Email/calendar/read-only workspace integrations
- Trello/Asana request board
- Weekly improvement cycle
- Best for founders/executives

### Growth — Department AI Team

- 2–3 agents
- Department-specific workflows
- Email/calendar/project/task integrations
- Agent inboxes
- Health monitoring and alerts
- Weekly Loom updates

### Premium — Managed AI Operating System

- Multi-agent workspace
- Dedicated isolated compute
- Custom skills/SOPs
- Approved automations
- Dashboard + observability
- Monthly security/access review

## First client workflow to build

Start with an executive operating agent:

1. Read meeting notes and summarize open loops.
2. Track follow-ups in Trello/Asana.
3. Draft emails but require approval before sending.
4. Maintain client/company/project context in Obsidian.
5. Produce daily/weekly founder briefings.
6. Alert when something breaks.

This is useful, low-regret, and safer than jumping directly into deep operational automation.

---

# Final recommendation

The stack is usable, but not as a copy-paste playground. For Jet's customers, package it as a **managed, secure AI team deployment** with clear boundaries.

Best immediate path:

1. Build one internal reference deployment for Limitless OS.
2. Turn that into a demo + Loom walkthrough.
3. Pilot with one friendly low-risk client.
4. Use a strict one-client/one-workspace isolation rule.
5. Create a vendor/security questionnaire before using Orgo/Composio/AgentMail on sensitive data.
6. Productize the executive assistant workflow first, then expand into vertical-specific agents.
