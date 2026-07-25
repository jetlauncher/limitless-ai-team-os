# Limitless Knowledge Wiki — Audit & Roadmap
**Date:** 2026-06-15
**Auditor:** Kelly
**URL:** https://limitless-knowledge-wiki.vercel.app/
**Status of audit:** Phase 1 complete (live-site observation). Phase 2 (deeper) and Phase 3 (OS Brain spec) not started.

---

## TL;DR

The wiki is a **healthy, source-backed teaching brain** for Limitless Academy. 162/162 transcripts distilled, 336 assets, 40 topics, daily refresh loop, 7-area taxonomy. It does its current job well. It is **not** a "company brain" because it intentionally doesn't try to be: it has no view into the Limitless OS (the 15+ agent fleet, cron jobs, business numbers, decisions log, system health). To become a true company brain, **don't dilute this wiki — build a parallel private OS Brain and cross-link them**.

---

## Phase 1 — Live Site Audit (this session)

### What's in there
- **162 transcript sources** (83 drive, 34 YouTube, 20 program, 7 workshop, 11 local, 7 inbox)
- **162 distilled** (100% coverage) — **0 pending**
- **336 wiki assets** across 6 layers (181 distillation, 50 lead-magnet, 25 guide, 23 atom, 42 topic, 12 meta)
- **40 canonical topics** in 5 kinds:
  - 10 frameworks (`10-80-10 Rule`, `3-AI Team Pattern`, `3-Tier Memory Model`, `Aaha Teaching Framework`, `Agent Ladder`, `Golden Triangle`, `Knowledge Loop`, `KOI Prompting Method`, `Mission Control Pattern`, `Reverse Engineering Loop`)
  - 10 articles (Agent OS, Agent Team Starter Kit, Tool Map, Content Studio, Creative Studio, Curator Agent, AI Efficiency for Thai SMEs, Hermes Setup, CEO Deploy & QA, YouTube-to-Website)
  - 6 thoughts (AI Is Team Management, Automate Before Hiring, Context Beats Tool Choice, Human Judgment Boundary, One Person Ten-Person Output, Tool Category Before Brand)
  - 7 ideas, 7 workflows
- **7 areas**: agent-os (10), business-automation (9), content-creative (9), knowledge-memory (6), tool-selection (3), prompting (2), education (1)
- **33 YouTube videos** with `apify-imported: 1 | queued-apify: 17 | transcript-fetched: 15`
- **Lead Magnet Library** with 50 entries (mostly "Lead Magnet Brief" drafts per the wiki's own description)
- **Guide Index** with 25 student guides (Thai + English, including a 5-part foundational series)

### What's solid
- Source-backed, every claim has provenance
- Daily refresh loop visible (Corpus Update Log, Distillation Queue)
- Five-bucket topic model is a clean schema
- Navigation is dense but not chaotic
- Knowledge Gap Report exists and is generating topics
- Search is a real search (not a placeholder)

### What's wrong (polish list, ordered by impact)

1. **Search is below the fold.** A new visitor lands, sees the H1, the intro paragraph, the Contents list — *then* the search box. Should be persistent in the header or right at the top.
2. **Knowledge Gap Report is hidden.** I see it in the asset list and as a search result, but it's not in the main nav. If it's the engine that drives what's distilled next, it deserves top-nav status.
3. **404s on subpages.** `/topics`, `/topic-index`, `/source-index`, `/asset-index` all 404. Only the SPA root + `#anchor` work. The wiki should either (a) generate static pages for each route, or (b) drop the broken links from the nav.
4. **YouTube Monitor status is ops-looking, not wiki-looking.** `apify-imported: 1 | queued-apify: 17 | transcript-fetched: 15` is a build-pipeline counter, not a reader-facing fact. Move raw counters to a separate ops dashboard; keep a reader-facing "Latest YouTube additions" page.
5. **No "last reviewed" dates on topic pages** from observation. A reader can't tell if a topic was curated yesterday or six months ago.
6. **No health indicator on the Corpus Snapshot.** A wiki with 100% distillation coverage, 0 pending, daily refresh is *green* — make it visually obvious (green dot or status pill).
7. **Lead magnets corpus (50 entries) is suspicious.** The wiki's own description says "Primarily Lead Magnet Brief drafts" — that's 50 briefs, not 50 shipped lead magnets. Either the count is misleading, or the lead-magnet pipeline is stuck at the brief stage.
8. **The "Ecosystem Map" link points to a page that's effectively a meta overview, not a navigable map.** It is a table of contents, but the title oversells. Consider renaming "Ecosystem Map" → "Knowledge Pipeline" or add a real graph/diagram.
9. **No on-page search highlight when you click a search result.** A search-and-jump that doesn't anchor the match is friction.

### What's missing to become a "company brain"

The wiki has the **teaching** layer. The actual *company* runs on a second system that I (Kelly) live in every day, but the wiki doesn't see:

**Layer A: The Agent Fleet (Limitless OS)**
- 15+ agent profiles: Kelly, Blaze, Signal, Oracle, Qwen, Protocol, Tiff, Uncle Chris, Friday, Muse, Bolt, Pixel, Zegna, Jekjack, Kaijeaw
- Each has a SOUL, a skill set, a memory location
- Cron inventory: daily schedules, owners, what each one does, the time-of-day rhythm
- Routing rules: who handles what (Signal=research, Blaze=content, Oracle=cron, Kelly=ops, Qwen=memory, Tiff=LINE bot, Muse=creative, Bolt=engineering)
- Approval gates: Mission Control, Blotato, human-in-the-loop rules
- Recurring failures / lessons learned (like the LinkedIn+X cron issue we just caught)

**Layer B: Business & Revenue Truth**
- Airtable revenue, Stripe, Limitless Club+ → ฿100M architecture (the *teaching* about it is in the wiki; the *actual* financial state is not)
- ฿100-120K Oct 2026 cohort, ~30 seats, ~6 days of Jet's time
- Customer/prospect layer: Skool members, DM inquiries, sales pipeline
- Decisions log: "We chose Airtable over Notion for transactions because…"

**Layer C: People & Roles**
- Jet: voice, preferences, decision patterns, time/health constraints
- Family: Ning, Jamie (ICS school)
- Team: contractors, named students who buy cohorts
- External collaborators: tech partners, accountants

**Layer D: Operating Memory**
- Open loops (Jet owes X, blocked by Y)
- Calendar awareness (next cohort, next workshop, deadlines)
- Recurring problems (the LinkedIn+X cron, recurring Telegram delivery issues, etc.)
- Lessons learned across agents

**Layer E: System Health**
- Wiki health (pending distillations, age of last refresh)
- OS health (cron liveness, agent failures, API spend, queue depth)
- Revenue pulse (daily/weekly)

---

## Phase 2 — Deeper Audit (to do)

Needs access to the wiki build source. I don't have the repo URL or the local build directory in this session. To do this phase I need:
- Wiki repo URL (GitHub?) or local build path
- The SCHEMA.md and any taxonomy files
- A sample of 5-10 topic pages for content quality check
- The Knowledge Gap Report content
- The Distillation Queue contents
- The Corpus Update Log (last 30 days)

Without these I can only do observation-based polish recommendations, not content-level quality work.

## Phase 3 — OS Brain Proposal (to do)

Architecture spec for a private, separate wiki (or section) that holds the missing Layers A-E. Decisions to make with Jet:
- **Where**: new Vercel project, sub-route on existing wiki, or subdomain?
- **Auth**: Vercel Password Protection, Cloudflare Access in front, or own auth (Clerk/Auth0)?
- **Schema**: separate from Academy wiki, or share the same five-bucket topic model?
- **Source of truth**: who writes to it? Cron jobs auto-publish health? Jet edits directly? Agent fleet writes daily?
- **Cross-link strategy**: Academy pages link to "how we do this in our OS", OS pages link back to "the teaching behind this rule"

**My recommendation:** Two-tier brain, each with a clear job.
- Public: Limitless Academy Brain (what's there now — keep it)
- Private: Limitless OS Brain (Layers A-E, with auth)
- Cross-link them at the topic level, not the asset level

---

## Phase 1 Deliverables — Polish I can do TODAY if I get build access

Given the wiki's source on disk / GitHub, the polish list is implementable as 1-2 day work:
- Move search to top
- Add Knowledge Gap Report to main nav
- Fix 404s (drop links or generate static pages)
- Hide raw YouTube Monitor counters, add "Latest YouTube additions" page
- Add `last_reviewed` field to topic pages
- Add a green/yellow/red health pill to the Corpus Snapshot
- Audit the 50 "Lead Magnet Brief" entries — are they shipped or drafts?
- Add highlight-on-jump for search results

**None of these touch the wiki's data model.** They're template + nav + presentation changes. Low risk.

---

## What I need from Jet to proceed

1. **Wiki repo / build path** — to do Phase 2 and the actual polish implementation
2. **Decision on OS Brain auth approach** — for Phase 3 spec
3. **Decision on lead magnets** — are the 50 "briefs" actually shipped? If not, that's a stuck pipeline worth fixing

— Kelly
