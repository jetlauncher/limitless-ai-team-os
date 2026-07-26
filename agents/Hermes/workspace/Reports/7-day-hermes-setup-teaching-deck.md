# The 7-Day Hermes Setup — Teaching Deck

**Source inspiration:** @zaimiri X Article — “The 7-day Hermes setup (full guide)”  
**Source URL:** https://x.com/zaimiri/article/2066117404392890835  
**Prepared for:** Jet / Limitless class  
**Prepared by:** Kelly  
**Purpose:** Turn the article’s 7-day Hermes setup framework into a practical teaching deck for founders, operators, and students building their first AI operator.

---

## Deck Positioning

This deck is not “how to install another AI tool.”

It teaches students how to build an AI assistant like an operating system:

- Start with a reliable foundation
- Give the agent identity and boundaries
- Add only durable memory
- Move the agent into a daily interface
- Convert repeated work into skills
- Add quiet scheduled automations
- Split profiles only when isolation is needed

The core lesson:

> A useful AI agent is not built by adding everything at once. It is built by layering identity, memory, skills, tools, interface, cron, and profiles in the right order.

---

# Slide 1 — Title

## The 7-Day Hermes Setup

### Build your first personal AI operator without creating chaos

**Subtitle:** A practical class for turning Hermes from “another chatbot” into a reliable assistant with memory, tools, skills, and workflows.

**Speaker notes:**
Most people try to build their AI setup in one chaotic weekend. They install tools, connect APIs, paste a giant system prompt, create automations, and then wonder why the whole thing feels unreliable. This class gives them a slower, layered approach.

---

# Slide 2 — The Problem

## Most AI setups fail because they are built backwards

People usually start with:

- 10 tools
- 5 APIs
- Random automations
- Giant system prompts
- No boundaries
- No memory discipline
- No verification loop

Then the system becomes:

- Noisy
- Fragile
- Hard to debug
- Hard to trust
- Easy to abandon

**Speaker notes:**
The problem is not that the tools are bad. The problem is sequencing. If you add tools, memory, automation, and agents before identity and reliability, every failure becomes confusing.

---

# Slide 3 — The Core Reframe

## Don’t build an AI pile. Build an AI operator.

A pile of automations:

- Does random things
- Interrupts too often
- Has no clear boundaries
- Breaks silently
- Creates more management work

An AI operator:

- Knows the house rules
- Remembers what matters
- Uses the right tools
- Verifies important work
- Improves after real tasks

**Speaker notes:**
This is the language students should remember. We’re not building “a bunch of prompts.” We’re building an operator: a role with context, procedures, tools, and accountability.

---

# Slide 4 — The Stack

## The Hermes setup has 7 layers

1. **Foundation** — install and verify the basics
2. **Identity** — define role, tone, boundaries, and approval rules
3. **Memory** — save only durable, high-signal facts
4. **Interface** — put Hermes where you actually communicate
5. **Skills** — turn repeated workflows into procedural memory
6. **Cron** — add quiet scheduled jobs
7. **Profiles** — split agents only when isolation is needed

**Speaker notes:**
This is the spine of the class. Every day adds one layer. The order matters. If students remember the order, they can build a system that compounds.

---

# Slide 5 — The 7-Day Map

## One layer per day

**Day 1:** Install Hermes and verify basics  
**Day 2:** Give the agent an identity  
**Day 3:** Add only high-signal memory  
**Day 4:** Move Hermes into your daily interface  
**Day 5:** Create your first skill from a real repeated task  
**Day 6:** Add one quiet cron  
**Day 7:** Split your first profile, only if needed

**Speaker notes:**
This is intentionally paced. The goal is not to impress students with complexity. The goal is to get them to a setup they can trust and actually use.

---

# Slide 6 — Day 1: Foundation

## Install Hermes and prove the basics work

Before adding memory, skills, or automations, verify that the foundation is healthy.

Core checks:

- Install Hermes
- Run setup
- Choose model/provider
- Run doctor checks
- Send a basic chat
- Test simple tool use
- Confirm it can read the environment safely

**Command examples:**

```bash
hermes setup
hermes model
hermes doctor
hermes chat -q "Return exactly: HERMES_OK"
```

**Speaker notes:**
Day 1 is not about building a complex assistant. It is about proving that the engine turns on, the model responds, and the environment is sane.

---

# Slide 7 — Day 1 Teaching Point

## Reliability beats impressiveness

A good Day 1 result is boring:

- The agent answers reliably
- Tools are available
- Config is healthy
- No credential confusion
- No mystery errors

A bad Day 1 result:

- Many tools installed
- Many keys pasted
- No verification
- No clear model route
- No idea what is broken

**Speaker notes:**
Students often want to skip to automations. Don’t let them. A boring verified foundation is what makes every later layer easier.

---

# Slide 8 — Day 1 Lab

## Lab: Foundation Smoke Test

Ask students to verify:

1. Which model/provider is active?
2. Does Hermes answer a simple prompt?
3. Can it run one harmless tool call?
4. Can it read/write a small test file?
5. Does `hermes doctor` report major problems?

**Expected output:**

A short setup receipt:

```markdown
## Hermes Foundation Check
- Model/provider:
- Doctor status:
- Tool test:
- File test:
- Blockers:
```

**Speaker notes:**
This creates the first habit: never say “it works” unless you have a receipt.

---

# Slide 9 — Day 2: Identity

## Give the agent a clear identity

Identity defines how the agent behaves before it touches tools or memory.

A strong identity includes:

- Role and mission
- Tone and style
- Output preferences
- Tool-use rules
- Safety boundaries
- Approval gates
- When to push back
- What never to do without permission

**Speaker notes:**
Identity is not decoration. It is the operating policy. Without it, the agent will optimize for being helpful in the moment instead of being reliable over time.

---

# Slide 10 — Day 2 Starter Identity

## A simple starter identity

```markdown
You are my practical AI operator.

Default behavior:
- Be concise and direct.
- Use tools for facts instead of guessing.
- Prefer small verified actions over big unverified plans.
- Ask before risky writes, purchases, deletions, posts, or messages.
- When work repeats, offer to save the procedure as a skill.
- Report blockers honestly instead of inventing results.
```

**Speaker notes:**
This is a minimal identity students can adapt. The key is not to make a giant persona. The key is to encode operating principles.

---

# Slide 11 — Day 2 Teaching Point

## Identity prevents chaos later

Once memory and tools are added, the agent becomes more powerful.

Without identity, more power creates:

- More accidental actions
- More vague outputs
- More tool misuse
- More trust issues

With identity, more power creates:

- Better delegation
- Safer execution
- Clearer handoffs
- Higher trust

**Speaker notes:**
Identity is the constitution. Tools are the hands. Memory is the brain. Don’t give the agent hands and memory before you give it house rules.

---

# Slide 12 — Day 3: Memory

## Add only high-signal memory

Memory should reduce repeated steering.

Save facts that will still matter in a month:

- User preferences
- Stable project conventions
- Important environment details
- Repeated corrections
- Durable workflow quirks
- Safety boundaries

Do **not** save:

- Temporary task status
- Random links
- One-off notes
- Stale numbers
- “Task completed” logs
- Anything likely to expire quickly

**Speaker notes:**
The memory mistake is trying to remember everything. That turns memory into noise. The purpose of memory is not archiving. It is future usefulness.

---

# Slide 13 — Memory Examples

## Good memory vs bad memory

**Good memory:**

- “User prefers concise, evidence-backed answers.”
- “Project uses pnpm, not npm.”
- “Revenue source of truth is Airtable table X.”
- “Never post externally without explicit approval.”

**Bad memory:**

- “Finished PR #123.”
- “User asked about a random article today.”
- “Temporary blocker from last week.”
- “Need to send a message tomorrow.”

**Speaker notes:**
Students need concrete examples because memory feels abstract. The key filter: will this reduce future friction, or will it just pollute context?

---

# Slide 14 — Day 3 Lab

## Lab: Write a Memory Policy

Students write two lists:

### Save to memory
- Preferences
- Corrections
- Stable project facts
- Tool quirks
- Safety boundaries

### Do not save to memory
- Temporary tasks
- Stale outputs
- Private secrets
- One-off links
- Completed work logs

**Output:**

```markdown
## My Hermes Memory Policy
Hermes should remember:
1.
2.
3.

Hermes should not remember:
1.
2.
3.
```

**Speaker notes:**
This turns memory from “magic” into governance.

---

# Slide 15 — Day 4: Interface

## Move Hermes into your daily communication channel

The best AI operator is the one you actually use.

For many users, that means Telegram:

```bash
hermes gateway setup
hermes gateway start
```

Interface options include:

- CLI
- Telegram
- Discord
- Slack
- WhatsApp
- Email
- Webhooks
- API server

**Speaker notes:**
A terminal-only agent is powerful but easy to forget. A messaging agent becomes part of daily operations.

---

# Slide 16 — Day 4 Teaching Point

## Interface changes behavior

When Hermes lives in chat, it becomes useful for:

- Quick capture
- Voice notes
- Follow-up tasks
- Alerts
- Receipts
- Remote work
- Daily operating rhythm

But it also needs stronger rules:

- Who can message it?
- Where does it deliver outputs?
- What requires approval?
- What should stay local only?

**Speaker notes:**
The interface layer is where the agent becomes operational. That is also when safety and routing matter more.

---

# Slide 17 — Day 5: Skills

## Turn repeated tasks into skills

A skill is procedural memory.

It tells Hermes:

- When to use the workflow
- What steps to follow
- What commands or tools to use
- What pitfalls to avoid
- How to verify success
- What output format the user expects

**Speaker notes:**
Skills are what make Hermes compound. Memory remembers facts. Skills remember procedures.

---

# Slide 18 — Don’t Invent Fake Skills

## The best skills come from real repeated work

Bad skill creation:

- “Maybe I’ll need this someday.”
- “Let’s write a giant skill for every possible thing.”
- “Let’s copy a random workflow from the internet.”

Good skill creation:

- Do a real task
- Notice repetition
- Capture the successful workflow
- Include pitfalls and verification
- Use it next time
- Patch it when it breaks

**Speaker notes:**
Skills should be earned by real work. Otherwise the skill library becomes bloated and stale.

---

# Slide 19 — Skill Examples

## Example first skills

Good beginner skills:

- Turn a link into an X post draft
- Process a voice memo into notes
- Review a pull request
- Build a weekly research brief
- Convert a transcript into a lesson deck
- Audit a landing page
- Summarize customer feedback

Each skill should include:

- Trigger
- Inputs
- Step-by-step process
- Verification
- Output format
- Known pitfalls

**Speaker notes:**
Students should leave with at least one candidate skill from their real life.

---

# Slide 20 — Day 5 Lab

## Lab: Identify Your First Skill

Ask students:

1. What task do you repeat every week?
2. What inputs does it need?
3. What output do you expect?
4. What mistakes happen often?
5. How do you verify it worked?

**Output:**

```markdown
## First Hermes Skill Candidate
Task:
Trigger:
Inputs:
Steps:
Pitfalls:
Verification:
Output format:
```

**Speaker notes:**
This lab makes the class immediately practical. They are not learning abstract “agent architecture”; they are turning one real workflow into a repeatable operating procedure.

---

# Slide 21 — Day 6: Cron

## Add one quiet scheduled job

A cron is a scheduled agent run.

Start with one narrow job:

- Daily research brief
- Morning inbox filter
- Source monitor
- Weekly content sweep
- Revenue check
- System health check

The rule:

> A good cron stays quiet unless there is real signal.

**Speaker notes:**
This is where many AI systems become annoying. The goal is not more notifications. The goal is useful interruption.

---

# Slide 22 — Quiet Cron Design

## Design crons like trusted assistants

Bad cron:

- Runs too often
- Sends generic summaries
- Repeats known information
- Alerts on everything
- Has no threshold

Good cron:

- Has a clear purpose
- Knows what “signal” means
- Saves detailed output locally
- Sends concise alerts only when useful
- Includes source links and receipts

**Speaker notes:**
A cron that trains the user to ignore it is worse than no cron.

---

# Slide 23 — Day 6 Lab

## Lab: Design One Quiet Cron

Students choose one scheduled workflow.

Template:

```markdown
## My First Quiet Cron
Name:
Schedule:
Purpose:
Sources to check:
What counts as signal:
What should be ignored:
Where full output is saved:
When to notify me:
```

Example:

```markdown
Name: Daily AI Operator Brief
Schedule: 8:30 AM daily
Signal: One new tool/workflow that can save founders time this week
Ignore: generic model launches with no practical workflow impact
Notify: Telegram, only if high-signal
```

**Speaker notes:**
This lab teaches students that automation is editorial judgment, not just scheduling.

---

# Slide 24 — Day 7: Profiles

## Split profiles only when isolation is needed

Profiles create separate agent contexts.

Use profiles when you need isolation of:

- Memory
- Identity
- Tools
- Credentials
- Audience
- Delivery channel
- Risk boundaries

Do **not** create profiles just because it feels cool.

**Speaker notes:**
Multiple agents are powerful, but they add coordination cost. Students should understand when separation is valuable and when it is premature.

---

# Slide 25 — Profile Examples

## When profiles make sense

Examples:

- **Research agent** — monitors AI news and summarizes only high-signal items
- **Content agent** — turns ideas into posts, scripts, and carousels
- **Coding agent** — edits repos, runs tests, opens PRs
- **Client-facing agent** — has strict audience and safety constraints
- **Local/private agent** — reads files but never posts externally

Bad reason to split:

- “I want a bunch of bots.”
- “It looks impressive.”
- “I don’t know what the first agent should do.”

**Speaker notes:**
The first agent should become useful before you multiply agents. Otherwise you are multiplying confusion.

---

# Slide 26 — The End State

## What you have after 7 days

A clean operating chain:

```text
Telegram → Hermes → Memory + Skill + Tools → Verified Output + Short Receipt
```

And one scheduled watcher:

```text
Cron → Source Check → Signal Filter → Local Report → Alert only if useful
```

**Speaker notes:**
This is the picture students should aim for. It is simple, but it is already much more powerful than a chatbot.

---

# Slide 27 — The Operating Principle

## Your Hermes should feel like a trusted operator

Not:

- A pile of automations
- A giant prompt
- A random chatbot
- A noisy notification machine

But:

- A person who knows the house rules
- Remembers what matters
- Uses the right tools
- Reports honestly
- Improves after real work

**Speaker notes:**
This is the emotional anchor of the class. People don’t want more software. They want reliable help.

---

# Slide 28 — Common Failure Modes

## Why beginners get stuck

1. They add too many tools too early
2. They save too much memory
3. They create noisy crons
4. They split profiles too soon
5. They skip verification
6. They don’t define approval gates
7. They create skills from theory instead of real work

**Speaker notes:**
This slide is a checklist for debugging student setups.

---

# Slide 29 — Classroom Exercise: Diagnose the Setup

## Which setup will compound?

### Setup A
- 12 tools
- 5 automations
- 3 profiles
- No identity
- No memory policy
- No verification

### Setup B
- 1 verified install
- 1 clear identity
- 5 durable memories
- Telegram interface
- 1 real skill
- 1 quiet cron
- Profiles later

**Question:** Which one would you trust with real work?

**Speaker notes:**
Let students answer. The right answer is Setup B. It looks less impressive but is far more likely to survive.

---

# Slide 30 — 7-Day Student Assignment

## Build your first AI operator this week

### Day 1
Install and verify Hermes.

### Day 2
Write identity and safety boundaries.

### Day 3
Create a memory policy and add 3–5 durable memories.

### Day 4
Connect your daily interface.

### Day 5
Capture one repeated task as a skill.

### Day 6
Add one quiet cron.

### Day 7
Decide whether profiles are actually needed.

**Speaker notes:**
This gives the class a concrete implementation path.

---

# Slide 31 — The Founder/Operator Lens

## Why this matters for business owners

Hermes is not just a productivity toy.

It can become a lightweight operating layer for:

- Research
- Content
- Sales follow-up
- Inbox filtering
- Meeting prep
- System monitoring
- Customer insight
- Knowledge management
- Internal SOP execution

But only if the setup is trusted.

**Speaker notes:**
Tie this back to founders. The business value is not “AI novelty.” The business value is reliable delegated operations.

---

# Slide 32 — The Limitless Framing

## From personal assistant to teamless leverage

The 7-day Hermes setup is a small version of the bigger idea:

> A founder can build a teamless operating system by giving AI agents roles, memory, skills, tools, and approval gates.

The first Hermes agent is the seed.

Over time, it can expand into:

- Research agent
- Content agent
- Ops agent
- Revenue monitor
- Knowledge curator
- Builder agent
- Customer insight agent

**Speaker notes:**
This connects the article to Jet’s broader teaching: 10x leverage, AI-native operating systems, and productized/teamless offers.

---

# Slide 33 — Final Takeaway

## Build slow enough to trust it

The winning Hermes setup is not the one with the most automations.

It is the one that:

- Works every day
- Knows the rules
- Remembers the right things
- Uses tools safely
- Produces receipts
- Gets better with use

**Closing line:**

> Don’t build an impressive AI demo. Build an AI operator you can trust on a normal Tuesday.

**Speaker notes:**
End with reliability. That is the differentiator between demos and real operating systems.

---

# Optional Handout — The 7-Day Hermes Setup Checklist

## Day 1 — Foundation
- [ ] Install Hermes
- [ ] Run setup
- [ ] Choose model/provider
- [ ] Run doctor
- [ ] Test a simple chat
- [ ] Test one harmless tool call

## Day 2 — Identity
- [ ] Define role
- [ ] Define tone
- [ ] Define output style
- [ ] Define tool rules
- [ ] Define approval gates
- [ ] Define what never happens without permission

## Day 3 — Memory
- [ ] Write memory policy
- [ ] Add 3–5 durable facts
- [ ] Avoid temporary task notes
- [ ] Avoid secrets
- [ ] Avoid stale work logs

## Day 4 — Interface
- [ ] Choose daily interface
- [ ] Configure gateway
- [ ] Verify delivery
- [ ] Confirm allowed users/channels

## Day 5 — Skills
- [ ] Pick one repeated task
- [ ] Capture trigger
- [ ] Capture steps
- [ ] Capture pitfalls
- [ ] Capture verification
- [ ] Test the skill next time the task appears

## Day 6 — Cron
- [ ] Pick one scheduled workflow
- [ ] Define signal threshold
- [ ] Save full output locally
- [ ] Alert only when useful
- [ ] Verify one real run

## Day 7 — Profiles
- [ ] Decide whether isolation is needed
- [ ] Split only if memory/tools/credentials/audience differ
- [ ] Keep first agent useful before multiplying agents

---

# Optional Workshop Flow

## 90-Minute Class Structure

### 0–10 min — Why AI setups fail
- Show chaotic weekend setup vs layered setup
- Introduce “AI operator” concept

### 10–25 min — The 7-layer model
- Foundation
- Identity
- Memory
- Interface
- Skills
- Cron
- Profiles

### 25–40 min — Live demo: Foundation + identity
- Show model/provider check
- Show a starter identity
- Show a safe tool-use rule

### 40–55 min — Memory + skill design
- Good vs bad memory examples
- Students draft first skill candidate

### 55–70 min — Cron + profiles
- Quiet cron examples
- When to split profiles
- Failure modes

### 70–85 min — Student build plan
- Each student fills the 7-day checklist
- Identify first repeated task
- Pick one quiet cron

### 85–90 min — Closing
- “Don’t build a demo. Build an operator.”

---

# Optional Discussion Prompts

1. What task do you ask AI to help with repeatedly?
2. What rules would make you trust an AI assistant more?
3. What should your agent never do without approval?
4. What facts should your agent remember about you?
5. What repeated workflow could become your first skill?
6. What daily/weekly alert would genuinely help you?
7. When would you need a separate profile instead of one assistant?

---

# Optional Board Diagram

```text
              ┌──────────────────────┐
              │   Daily Interface     │
              │ Telegram / CLI / App  │
              └──────────┬───────────┘
                         │
                         ▼
              ┌──────────────────────┐
              │        Hermes         │
              │ Identity + Boundaries │
              └──────────┬───────────┘
                         │
       ┌─────────────────┼─────────────────┐
       ▼                 ▼                 ▼
┌─────────────┐   ┌─────────────┐   ┌─────────────┐
│   Memory    │   │   Skills    │   │    Tools    │
│ durable     │   │ workflows   │   │ actions     │
│ context     │   │ procedures  │   │ verification│
└─────────────┘   └─────────────┘   └─────────────┘
       │                 │                 │
       └─────────────────┼─────────────────┘
                         ▼
              ┌──────────────────────┐
              │  Verified Output      │
              │ + Short Receipt       │
              └──────────────────────┘

Scheduled layer:

Cron → Source Check → Signal Filter → Report / Alert
```

---

# Notes on Source Fidelity

This deck is a teaching adaptation, not a verbatim reproduction. The source article’s core framework was retrieved through xAI-powered X Search and transformed into a class-ready structure with examples, labs, speaker notes, and Limitless-specific framing.

Core source ideas preserved:

- Most AI setups fail because people build too much in one chaotic weekend
- Hermes should be layered slowly
- The 7 layers/days are foundation, identity, memory, interface, skills, cron, profiles
- Reliability matters more than immediate impressiveness
- Memory should be durable and high-signal
- Skills should come from real repeated tasks
- Crons should be quiet and signal-based
- Profiles should only be split when isolation is needed
- The desired end state is a personal operator with context, procedures, boundaries, and compounding improvement
