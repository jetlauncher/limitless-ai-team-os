# AI Team OS Build Spec — From “How I’m Using AI to Build a One-Person Business”

Date: 2026-05-24
Source transcript: `/Users/ultrafriday/.hermes/cache/documents/doc_635d77c8993d_youtube_i2RLC_transcript.txt`
Video: `https://youtu.be/i2RLCtNa1C8`
Owner: Jet + Kelly

## Core Thesis

The transcript gives a clean 3-level ladder for Jet's Limitless AI Team OS:

1. **AI builds custom internal tools** instead of buying fragmented SaaS.
2. **AI agents become a lean operating team** that executes specialized workflows in series.
3. **The agent system becomes the product** students/clients can use without Jet doing every step manually.

This maps almost perfectly to Jet's current Hermes fleet and Limitless Club business.

## Jet Version of the 3 Levels

### Level 1 — Replace fragmented SaaS with internal operating tools

Goal: reduce overhead tax and centralize business data.

Current Jet assets:

- Airtable sales source of truth: `Limitless Sales` → `1. transactions` → `ยอดโอน`.
- Mission Control: `https://limitless-mission-control.vercel.app`.
- Obsidian Agents workspace: `~/Documents/Obsidian Vault/Agents/`.
- Hermes scripts/crons for revenue, sales, content, X radar, Notion sync.

Build targets:

- Unified Revenue + Student dashboard.
- Lead/source tracker for Telegram, YouTube, workshops, ads, referrals.
- Course/workshop asset library.
- Single “today’s command center” view.

### Level 2 — AI agents as lean team

Goal: Jet stops being the bottleneck for research, ideation, packaging, drafts, QA, and reporting.

Current Jet agents:

- Kelly: chief of staff / ops / coordination.
- Signal: AI research radar.
- Blaze: English content.
- Kaijeaw: Thai content.
- Pixel: visual design/assets.
- Bolt: apps/sites/tools.
- Qwen: local/private worker + hygiene.
- Oracle: knowledge-network idea surfacing.
- Zegna: taste/brands/gadgets.
- Protocol: newsletter / protocol content.
- Nova-NJJ: remote NJJ iMac agent profile.

Build targets:

- Agent handoff inbox: Signal → Blaze/Kaijeaw → Mission Control → Blotato/Notion/Obsidian.
- Shared Memory digest so agents inherit what the others found.
- Approval dashboard for Jet.
- Daily auto-generated content package with source links and freshness labels.

### Level 3 — The AI system becomes the product

Goal: sell/deploy an AI Team OS students can copy/adapt, not just teach concepts.

Product direction:

- “AI Team OS for Thai Business Owners”
- Includes agents, prompts, operating rhythms, dashboards, templates, scripts, and approval loops.
- Students get a working system, not only a course.

Package components:

1. Founder Command Center.
2. Sales/Revenue Monitor.
3. Content Team Agents.
4. Workshop/Transcript Repurposing Factory.
5. Approval + Posting Pipeline.
6. Local Knowledge Brain.
7. Weekly CEO Review.

## MVP We Should Build First

### MVP Name

**Limitless AI Team OS — Founder Command Center v0**

### Promise

A Thai founder can see revenue, leads, content pipeline, agent outputs, and next actions in one place — with AI agents doing the prep work and the founder only approving decisions.

### MVP Modules

#### 1. Revenue Truth Panel

- Source: Airtable `Limitless Sales` / `1. transactions` / `ยอดโอน`.
- Show: today, yesterday, 7-day, month-to-date, top sources if available.
- Alert: meaningful revenue events, failed syncs, suspicious zeros.

#### 2. Student / Customer Panel

- Source: Airtable `จำนวนนักเรียน` and related tables.
- Show: total students, new students by cohort/date, likely incomplete records.

#### 3. Agent Inbox Panel

- Pull from Shared Memory + agent inbox folders.
- Show: new Signal insights, Blaze drafts, Kaijeaw Thai drafts, Pixel assets, Bolt builds, Qwen issues.
- Status: new / needs Jet approval / scheduled / published / blocked.

#### 4. Content Pipeline Panel

- Source: Mission Control + Blotato/Notion/Obsidian local archives.
- Show: ideas, drafts, approved posts, scheduled posts, stale items.

#### 5. System Health Panel

- Source: cron health digest.
- Show: broken jobs, token issues, delivery failures, noisy profiles.

## Build Order

### Sprint 1 — Source map and dashboard skeleton

- Confirm canonical sources and credential paths.
- Build a local static HTML dashboard that reads generated JSON snapshots.
- Add panels for revenue, students, cron health, and agent inbox.
- No external writes.

### Sprint 2 — Agent handoff pipeline

- Standardize handoff notes.
- Add status fields and duplicate checks.
- Connect Signal → Blaze/Kaijeaw → Mission Control.

### Sprint 3 — Approval and publish loop

- Mission Control approval queue becomes the central human-in-the-loop layer.
- Blotato posts only after approval.
- Archive final URLs back to Obsidian/Notion.

### Sprint 4 — Productize for students

- Turn the system into templates/checklists.
- Create install/setup scripts or copyable Notion/Obsidian templates.
- Make a Thai workshop/demo deck and PDF.

## Immediate Next Action

Correction from Jet: we already have the Command Center. Do **not** create a separate `Founder Command Center v0` app.

Improve the existing Mission Control repo instead:

- Repo: `/Users/ultrafriday/Projects/limitless-mission-control`
- Production: `https://limitless-mission-control.vercel.app`
- Existing unified endpoint: `/api/command-center`
- New upgrade plan: `2026-05-24-mission-control-upgrade-plan.md`

Next implementation should wire the transcript-inspired AI Team OS layer into Mission Control: cron health, real automation status, student-count truth, agent inbox lanes, and a sharper priority-action strip.

## Human-Owned Decisions

Jet should own:

- Final dashboard taste/brand.
- Which panels matter most.
- What can be shown to students vs private internal data.
- Approval before any posting or customer-facing automation.

## Notes from the Transcript to Preserve

- “Overhead tax”: fragmented software slows the founder down.
- “One thing rule”: many SaaS tools are used for only one thing.
- “AI creates tools”: use AI as tool-builder, not just chatbot.
- “Specific workflow agents”: each agent owns a narrow task.
- “Founder remains creative judge”: agents draft/execute; Jet approves/tastes.
- “The system is the product”: the AI operating system can become the offer.
