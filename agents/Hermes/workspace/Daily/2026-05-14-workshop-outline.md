# Limitless AI Team OS — 2-Day Workshop
**Goal:** Every participant leaves with a working personal Hermes agent installed, connected to Telegram, with 2+ skills and 1 cron job running.

---

## DAY 1 — Foundations & Your First Agent

### Block 1 — The Mental Model (60 min)
- Why an AI Team OS beats a single chatbot
- The 4 layers: **Agents → Skills → Connectors → Memory**
- Tour of Jet's live system (Kelly, Signal, Blaze, Zegna, Kaijeaw, Bolt, Protocol)
- What "one brain, many faces" actually means

### Block 2 — Install Day (90 min) 🛠️
- Prereqs: Python, Node, Homebrew (Mac) / WSL (Win)
- Install Hermes core
- API keys checklist: OpenAI, Anthropic, OpenRouter (one is enough to start)
- First boot: `hermes setup`
- Verify: `hermes config` + send first message in CLI
- **Checkpoint:** everyone gets a "hello" back from their agent

☕ Break

### Block 3 — Connect Telegram (60 min)
- BotFather → token → wire it up
- Home channel concept
- Topic threads & multi-chat routing
- **Checkpoint:** every student texts their agent from their phone

### Block 4 — Personas & Multi-Agent Setup (75 min)
- Persona files: what makes Kelly ≠ Blaze
- Create your own primary assistant (name, mission, tone)
- When to spawn a second agent vs. a skill
- Memory vs. user-profile: what to save where

### Block 5 — Day 1 Lab (60 min)
- Each student: install + Telegram + custom persona working
- Office hours / debugging
- Homework: bring 3 real tasks you want to automate tomorrow

---

## DAY 2 — Connectors, Skills & Shipping

### Block 6 — Skills System (90 min)
- What is a skill, when to write one
- Anatomy of a SKILL.md (frontmatter, triggers, steps, pitfalls)
- Live demo: write a skill together (e.g., "daily news brief")
- `skill_view`, `skill_manage` walkthrough
- **Lab:** each student writes 1 skill for one of their homework tasks

### Block 7 — Connector Buffet (90 min)
Pick 3 to install live based on the room:
- **Notion** — exec mirror / control room
- **Obsidian** — operating source of truth
- **Airtable** — revenue / CRM
- **Google Workspace** — Gmail, Calendar, Drive
- **Apple** — iMessage, Notes, Reminders (Mac only)
- **Discord / Slack / iMessage** — extra channels
- **Higgsfield / OpenAI Images** — visual generation
- **Blotato** — social posting with approval

☕ Lunch

### Block 8 — Cron Jobs & Automation (75 min)
- The cron tool: scheduled prompts vs. scheduled scripts
- `notify_on_complete` for long tasks
- Approval-gated workflows (Mission Control pattern)
- Live build: "every morning 7am, brief me on X"
- **Lab:** each student ships 1 cron running on their machine

### Block 9 — Real Use Cases Showcase (60 min)
- **Revenue monitoring:** Airtable → Telegram alerts
- **Content engine:** research → draft → approve → post
- **Chief of Staff briefings:** daily roll-up
- **Newsletter agent:** Protocol-style
- Pick one to clone into your stack

### Block 10 — Ship & Sustain (45 min)
- Backup your `~/.hermes` and Obsidian vault
- Cost control: which models for which jobs (GPT-5.5 default, Sonnet for hard problems)
- How to debug when something breaks (logs, `hermes config`, session_search)
- When to use sub-agents / Claude Code / Codex
- Community + ongoing support

### Block 11 — Graduation Demos (45 min)
- Each student demos their agent live in the room
- Awards: Most Useful, Most Creative, Most Likely to Replace a Cofounder
- Certificate + Discord invite

---

## What Every Student Leaves With
✅ Hermes installed and persistent
✅ Telegram-connected primary agent with custom persona
✅ 2+ working skills
✅ 1 cron job running on schedule
✅ 3+ connectors wired up
✅ A roadmap of 5 next automations to build

---

## Instructor Prep Checklist
- [ ] Pre-made API key bundles for students who need them
- [ ] Backup install USB / offline installer for bad wifi
- [ ] Slide deck for Blocks 1, 6, 9
- [ ] Live demo agent on projector
- [ ] TA for debug support during labs
- [ ] Welcome kit: cheat sheet PDF + Discord link + post-workshop calendar
