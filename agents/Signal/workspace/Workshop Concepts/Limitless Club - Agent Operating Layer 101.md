# Limitless Club — Agent Operating Layer 101

Date drafted: 2026-05-18
Owner: Signal
Status: Draft session architecture

## Big idea

Most people teach “how to prompt an AI.” This session teaches the operating layer that makes AI useful inside a real business: context, reusable skills, source data, approval rules, mobile supervision, and audit logs.

## Session promise

By the end, participants understand how to design an Agent Operating Layer and can run a 28-hour AI Operator Sprint where each team ships one reusable workflow with measurable business value and governance.

## Target audience

- Founders who want AI to save real operating hours, not just create demos
- Operators and team leads building repeatable workflows
- Educators/consultants packaging AI delivery systems
- Limitless Club members ready to move from prompts to operating infrastructure

## Core framing

### From prompts to operating layer

- Prompt = one-time instruction
- Workflow = repeated process
- Agent Operating Layer = the rules, memory, tools, approvals, supervision, and logs that make workflows safe enough for a team

### Six building blocks

1. **Context folder**
   - The agent’s working memory and business brain
   - Includes company overview, offers, ICP, SOPs, brand voice, product docs, examples, constraints, and past decisions
   - Rule: if a teammate would need it to do the work, the agent needs it too

2. **Reusable skills**
   - Packaged procedures the agent can run repeatedly
   - Examples: qualify lead, draft proposal, summarize sales call, create campaign brief, reconcile payment proof, generate onboarding checklist
   - Good skill = trigger, inputs, step-by-step process, tool access, quality bar, failure cases, output format

3. **Source data connectors**
   - Trusted systems the agent reads/writes from
   - Examples: Airtable, Notion, Google Drive, Gmail, Stripe, CRM, form submissions, analytics, Slack/Telegram
   - Principle: connect to the source of truth before asking AI to guess

4. **Approval rules**
   - Defines what the agent can do autonomously vs what requires human review
   - Examples:
     - Draft-only: external emails, invoices, refunds, public posts
     - Auto-run: internal summaries, tagging, data cleanup under threshold
     - Escalate: legal, pricing exceptions, VIP customers, ambiguous complaints

5. **Mobile supervision**
   - Human-in-the-loop from Telegram/LINE/mobile dashboard
   - The operator can approve, reject, ask for revision, or pause workflow without opening a laptop
   - This is how busy founders stay in control without becoming the bottleneck

6. **Audit log**
   - Record of what the agent saw, decided, produced, sent, changed, and who approved it
   - Required for debugging, trust, training, compliance, and team adoption
   - Minimum fields: timestamp, workflow, input source, action taken, output link, approval status, human reviewer, error/exception

## 90-minute teaching session

### 0–10 min — Hook: why prompt libraries are not enough

- Show contrast:
  - Prompt user: asks AI every time
  - AI operator: designs workflows that run repeatedly
- Key line: “The future advantage is not who has better prompts. It is who has better operating layers.”

### 10–25 min — Agent Operating Layer map

Teach the six-layer map:

1. Context folder
2. Reusable skills
3. Source data connectors
4. Approval rules
5. Mobile supervision
6. Audit log

Mini activity:
- Ask members to pick one recurring task they hate doing every week
- Map which of the six layers it would need

### 25–45 min — Workflow anatomy

Use one example workflow:

**Example: Lead-to-Proposal Assistant**

- Source data: Typeform / CRM / Airtable lead record
- Context: offer docs, pricing rules, case studies, objection handling
- Skill: qualify lead and draft proposal
- Approval: founder approves before sending
- Mobile supervision: Telegram approval card
- Audit log: proposal generated, approved by whom, sent when, outcome

Breakdown template:

- Trigger: what starts it?
- Inputs: what data does it need?
- Context: what knowledge does it need?
- Decision rules: what can it decide?
- Output: what does it produce?
- Approval: what needs human sign-off?
- Log: what must be recorded?

### 45–65 min — Governance without killing speed

Teach 3 levels of autonomy:

- **Level 1 — Copilot:** drafts, summarizes, suggests
- **Level 2 — Operator:** executes internal actions with boundaries
- **Level 3 — Agent:** performs external/customer-facing actions with approval gates and logs

Approval rule examples:

- Money movement: always approve
- Customer-facing message: approve until quality proven
- Internal tagging/summarization: can auto-run
- High-value customer or negative sentiment: escalate
- Low-confidence result: ask human

### 65–80 min — Sprint briefing

Introduce the 28-hour AI Operator Sprint.

Sprint goal:
- Each team builds one reusable workflow that saves time, creates revenue leverage, can be reused, and includes governance.

Team output:
- Working or semi-working workflow
- Context folder
- Reusable skill spec
- Connector map
- Approval rules
- Mobile supervision mockup or live flow
- Audit log sample
- 3-minute demo

### 80–90 min — Team formation + workflow selection

Teams choose one workflow from:

- Sales lead qualification
- Proposal / quotation generation
- Content repurposing with approval
- Customer onboarding
- Payment proof reconciliation
- Event follow-up
- Course/community support assistant
- Weekly founder dashboard
- Recruiting shortlist assistant
- Finance/admin document collector

## 28-hour AI Operator Sprint

### Sprint structure

**Hour 0–1: Kickoff**

- Explain judging criteria
- Teams pick workflow and business owner
- Define target metric: hours saved or revenue impact

**Hour 1–3: Workflow mapping**

Deliverables:
- Current manual process map
- Pain point and bottleneck
- Trigger/input/output
- Human approval moments
- Success metric

**Hour 3–6: Context folder build**

Deliverables:
- Business facts
- SOPs/examples
- Brand/tone/quality rules
- Edge cases
- Output examples

**Hour 6–10: Skill design**

Deliverables:
- Skill name
- Trigger
- Required inputs
- Step-by-step instructions
- Output format
- Quality checklist
- Failure/escalation rules

**Hour 10–15: Connector setup or mock connector**

Deliverables:
- Source of truth identified
- Data fields mapped
- Read/write permissions defined
- Sample input records
- If no live API: CSV/Airtable/Google Sheet mock

**Hour 15–19: Workflow build**

Deliverables:
- Prototype in chosen stack: ChatGPT project, Claude project, Make/Zapier, Airtable automation, Notion, custom script, OpenClaw/Hermes, etc.
- Test on 3 sample cases

**Hour 19–22: Approval + mobile supervision**

Deliverables:
- Approval card format
- Approve/reject/revise options
- Escalation rules
- Mobile demo or Figma/Notion mock

**Hour 22–24: Audit log**

Deliverables:
- Log schema
- 3 sample logged runs
- Error/exception field
- Reviewer field

**Hour 24–26: Business case**

Deliverables:
- Estimated hours saved/month
- Revenue impact or risk reduction
- Reuse potential across team/customers
- Governance risk addressed

**Hour 26–28: Demo + judging**

Demo format:
- Problem: 30 sec
- Workflow: 60 sec
- Live run / mock run: 60 sec
- Metrics + governance: 45 sec
- What they would improve next: 15 sec

## Judging rubric: 100 points

### 1. Hours saved — 30 pts

- 0–10: vague or one-time benefit
- 11–20: clear recurring time saving
- 21–30: quantified, high-frequency, owner-validated saving

### 2. Revenue impact — 25 pts

- 0–8: no clear revenue link
- 9–17: improves sales, retention, conversion, speed, or capacity
- 18–25: directly tied to revenue metric or monetizable workflow

### 3. Reuse — 25 pts

- 0–8: custom one-off demo
- 9–17: reusable within one team/process
- 18–25: packaged skill/template usable across teams or clients

### 4. Governance — 20 pts

- 0–6: unsafe/unclear autonomy
- 7–14: approval rules and basic logging included
- 15–20: clear approval tiers, escalation, source-of-truth discipline, and audit log

## Required team artifacts

1. Workflow one-pager
2. Context folder
3. Reusable skill spec
4. Connector map
5. Approval rules
6. Mobile supervision card
7. Audit log sample
8. Demo script
9. Business impact estimate

## Templates

### Workflow one-pager

- Workflow name:
- Business owner:
- Problem:
- Current manual process:
- Trigger:
- Inputs:
- Source of truth:
- Agent actions:
- Human approvals:
- Output:
- Audit log fields:
- Success metric:
- Estimated hours saved/month:
- Revenue impact:

### Reusable skill spec

- Skill name:
- When to use:
- Required inputs:
- Context needed:
- Steps:
- Tools/connectors:
- Output format:
- Quality checklist:
- Escalation rules:
- Example run:

### Approval rule template

- Action:
- Autonomy level: auto / draft-only / approval required / forbidden
- Threshold:
- Escalation condition:
- Reviewer:
- Audit requirement:

### Audit log schema

- Timestamp
- Workflow name
- Run ID
- Input source
- Input record link
- Agent action
- Output link
- Confidence / status
- Approval status
- Reviewer
- Final action taken
- Error or exception

## Recommended positioning

Title options:

- Agent Operating Layer 101: From Prompts to AI Operators
- Build Your First AI Operating Layer
- The 28-Hour AI Operator Sprint
- Stop Prompting. Start Operating.

Best headline:

**Agent Operating Layer 101: Build reusable AI workflows your team can actually trust**

## Founder/operator takeaways

- AI adoption fails when knowledge, approvals, and logs are missing
- Reusable workflows beat isolated prompts
- Source-of-truth connectors reduce hallucination and manual copy-paste
- Governance is not bureaucracy; it is what allows more autonomy
- Mobile supervision makes AI practical for busy founders

## Content angles for Limitless Club

- “Your AI does not need another prompt. It needs an operating layer.”
- “If there is no source of truth, your AI is guessing.”
- “The approval button is the bridge between demo and deployment.”
- “Audit logs are how founders trust AI enough to delegate.”
- “The best AI workflow is not the flashiest. It is the one your team reuses every week.”
