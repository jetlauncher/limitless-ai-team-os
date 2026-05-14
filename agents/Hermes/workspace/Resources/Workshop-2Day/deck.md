# Limitless AI Team OS
## 2-Day Workshop · Build Your Own AI Team

Instructor: Jedi Trinupab · Limitless Club

---

# Why You're Here

You will leave with a working AI agent — installed, on Telegram, with skills and a live cron.

Not a chatbot. An **operating system** for your work.

---

# The Promise

By the end of Day 2, you will have:

- Hermes installed on your machine
- A custom-named primary agent on Telegram
- 2+ working skills
- 1 live cron job running on schedule
- 3+ connectors wired up (Notion, Obsidian, Gmail, etc.)

---

# Day 1 Roadmap

1. Mental Model — the 4 layers
2. Install Day — get Hermes running
3. Connect Telegram — text your agent
4. Personas & Multi-Agent — make it yours
5. Day 1 Lab — debug + homework

---

# The 4 Layers

**Agents** — the personas (Kelly, Signal, Blaze…)
**Skills** — procedural memory, reusable workflows
**Connectors** — Notion, Telegram, Airtable, Apple, Google
**Memory** — durable facts + user profile

One brain. Many faces. Many hands.

---

# Live Tour: My Stack

- **Kelly** — ops & coordination (primary)
- **Signal** — research & search
- **Blaze** — content & writing
- **Zegna** — taste & aesthetics
- **Kaijeaw** — Thai-language ops
- **Bolt** — apps & sites
- **Protocol** — newsletter agent

---

# Block 2 — Install Day 🛠️

Prereqs:
- Python 3.11+, Node 20+
- macOS: Homebrew · Windows: WSL
- One API key (OpenAI **or** Anthropic **or** OpenRouter)

Commands:
- `hermes setup`
- `hermes config`
- `hermes` → first hello

**Checkpoint:** every student gets a reply.

---

# Block 3 — Connect Telegram

1. Talk to **@BotFather** → get a bot token
2. `hermes config set telegram.token …`
3. Define your **home channel**
4. Optional: topics for multi-channel routing

**Checkpoint:** text your agent from your phone.

---

# Block 4 — Personas

A persona file defines:
- Name, mission, tone
- Default model
- Memory store
- Allowed toolsets

**Decision rule:**
New persona = different identity / channel.
New skill = same identity, new capability.

---

# Memory vs. User Profile

**User profile** — who *you* are (name, prefs, role)
**Memory** — what the *agent* learned (env, conventions, lessons)
**Skills** — *how* to do recurring work
**Session search** — what we did last time

Save preferences and corrections. Skip task logs.

---

# Day 1 Lab

Goal: install + Telegram + custom persona working for **every** student.

Office hours. TAs floating.

**Homework:** bring 3 real tasks you want automated tomorrow.

---

# Day 2 Roadmap

6. Skills System
7. Connector Buffet
8. Cron & Automation
9. Real Use Cases
10. Ship & Sustain
11. Graduation Demos

---

# Block 6 — Skills System

A skill = SKILL.md with:
- Frontmatter (name, description, version)
- Trigger conditions ("use when…")
- Numbered steps with exact commands
- Pitfalls section
- Verification steps

Live build together. Then everyone writes one.

---

# Block 7 — Connector Buffet

Pick 3 to install live:

- **Notion** — exec mirror / control room
- **Obsidian** — operating source of truth
- **Airtable** — revenue & CRM
- **Google Workspace** — Gmail, Calendar, Drive
- **Apple** — iMessage, Notes, Reminders (Mac)
- **Discord / Slack** — extra channels
- **Higgsfield / OpenAI Images** — visuals
- **Blotato** — social posting w/ approval

---

# Block 8 — Cron & Automation

Two patterns:
- **Scheduled prompts** — agent runs a task
- **Scheduled scripts** — script feeds agent

Approval gates: Mission Control pattern.
Long tasks: `notify_on_complete`.

**Lab:** ship 1 cron live.

---

# Block 9 — Real Use Cases

- **Revenue monitor** — Airtable → Telegram alerts
- **Content engine** — research → draft → approve → post
- **Chief of Staff** — daily briefing roll-up
- **Newsletter agent** — Protocol-style weekly send

Pick one to clone into your stack.

---

# Block 10 — Ship & Sustain

- Backups: `~/.hermes` + your Obsidian vault
- Cost control: GPT-5.5 default, Sonnet for hard problems
- Debugging: logs, `hermes config`, `session_search`
- Sub-agents: Claude Code, Codex, OpenCode

---

# Block 11 — Graduation

Each student demos live.

Awards:
- Most Useful
- Most Creative
- Most Likely to Replace a Cofounder

Certificate + Discord invite.

---

# What You Leave With

✅ Hermes installed & persistent
✅ Telegram agent w/ custom persona
✅ 2+ skills · 1 cron · 3+ connectors
✅ Roadmap of 5 next automations

---

# Next 30 Days

Week 1 — Stabilize. Use it daily.
Week 2 — Add 2 more skills.
Week 3 — Add 2 more connectors.
Week 4 — Build a 2nd agent for a different role.

Stay in the Discord. Ship things. Share what breaks.

---

# Thank You

You're not learning a tool.
You're learning to **delegate to machines**.

Build the team. Reclaim the time.

— Jedi · Limitless Club
