# Hermes: The 7-Day Clean Setup

**A teaching deck for building a reliable personal AI operator**

---

## The Problem Most People Face

Most people try to build their AI setup in one chaotic weekend.

They install ten tools, connect five APIs, create a few automations, add a giant system prompt… then wonder why it feels messy two days later.

**Result:** A noisy assistant with too much access and not enough judgment.

---

## The Better Approach

**Hermes is better if you build it slower.**

The setup is not the hard part.

The hard part is keeping the layers clean:

**Identity → Memory → Skills → Tools → Telegram → Crons → Profiles**

If you stack those in the wrong order, you get noise.

If you stack them in the right order, you get something that starts to compound.

---

## The 7-Day Setup Philosophy

- Don't start with automations
- Prove the base agent works first
- Fix personality *before* giving it more power
- Memory should reduce repeated steering, not archive your entire life
- The best system is the one you actually touch every day
- Turn real repeated tasks into skills
- Only add crons when there's real signal
- Create new profiles only when boundaries require it

---

## Day 1: Install & Verify the Basics

**Goal:** Confirm Hermes can run, call tools, read the environment, and respond reliably.

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
hermes setup
hermes model
hermes doctor
hermes chat
```

Shaky foundation = painful debugging later.

---

## Day 2: Give the Agent an Identity

Most people skip this and jump to tools. That’s backwards.

Define:
- Tone and voice
- Risk boundaries
- When to push back
- When to use tools
- What it should never do without approval

**Example starter identity:**
> You are my practical AI operator. Be concise. Use tools when facts matter. Do not guess file contents, current dates, system state, or live facts. Ask before risky writes. Prefer small verified actions over big plans. If a workflow becomes repeatable, offer to save it as a skill.

A strong identity prevents future mess.

---

## Day 3: Add Only High-Signal Memory

Memory is where most setups die. Don’t make it remember everything.

**Good memory (durable, matters in a month):**
- Preferred answer length
- Your role and main projects
- Writing preferences
- Common tools & conventions
- Mistakes it should not repeat

**Bad memory (avoid):**
- Temporary task progress
- Random links
- One-day reminders
- Stale project status

The goal of memory is to reduce repeated steering.

---

## Day 4: Move Hermes Into Your Daily Interface

Terminal agents are powerful until you forget to open them.

Set up the Telegram gateway:

```bash
hermes gateway setup
hermes gateway start
```

When the agent lives where you already chat, usage changes dramatically.

The best system isn’t the one with the most features — it’s the one you actually touch every day.

---

## Day 5: Create Your First Real Skill

Don’t invent ten theoretical skills.

Wait until you do something real with Hermes, then turn that working path into a **skill** (procedural memory).

**Good skill examples:**
- Draft a Zaimiri-style X post from a link
- Process a voice memo
- Review a GitHub PR
- Turn a Telegram link into a wiki note

A good skill has: clear triggers, boundaries, workflow, common errors, verification steps, and expected output format.

This is where Hermes stops being a chatbot and starts becoming a personal operator.

---

## Day 6: Add One Quiet Cron

Only now — after it has identity, memory, and skills.

Start with **one** narrow, quiet recurring job:
- Daily research brief
- Weekly repo cleanup
- Morning inbox digest
- Content radar

**Rule:** If there’s no real signal, it should say *nothing*.

Noisy crons become background radiation you learn to ignore.

---

## Day 7: Split Your First Profile (Only If Needed)

Don’t create multiple agents just because it’s cool.

Only make a new profile when you need different:
- Memory
- Identity
- Tools/permissions/credentials
- Audience or delivery channel

**Examples:**
- Personal operator
- Content agent
- Research agent
- Coding agent
- Client agent

---

## What Success Looks Like After 7 Days

You don’t have a giant AI empire.

You have a clean operating chain:

**Telegram → Hermes → Memory → Skill → Tool call → Verified output → Short receipt**

Plus one quiet scheduled watcher that only alerts when there’s real value.

That’s enough to start compounding.

---

## The Beginner Mistake

Trying to make Hermes impressive immediately.

**The better move:** Make it **reliable** first.

One clean memory.
One real skill.
One useful Telegram lane.
One quiet cron.
Profiles only when boundaries require it.

---

## Your Hermes Setup Should Feel Like...

A person who:
- Knows the house rules
- Remembers what matters
- Uses the right tools
- Gets a little better after every real task

Not a pile of automations.

---

## Next Steps

1. Start Day 1 today (install + verify)
2. Document your identity on Day 2
3. Audit your current memory — keep only what compounds
4. Identify one repeated task worth turning into a skill
5. Join the Hermes community for support

**Your setup compounds when the layers are clean.**

---

## Limitless Club · @jeditrinupab · jeditrinupab.com

*Hermes Agent by Nous Research*