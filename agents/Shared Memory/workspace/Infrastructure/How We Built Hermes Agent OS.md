# How We Built a Personal AI Agent Operating System on Hermes

*By Jedi Trinupab Jiratraitharn / Limitless Club*  
*Drafted with Kelly on Hermes — 2026-04-26*

## The simple idea

Most people use AI as a chat box.

We wanted something different: a small AI team that actually helps run the business.

Not one assistant. Not one prompt. Not one automation.

A working agent infrastructure.

The goal was to create a system where different AI agents have clear roles, shared memory, reliable workflows, and enough structure to support real business operations: content creation, research, automation, revenue monitoring, troubleshooting, and daily decision-making.

That system is now built around Hermes.

Hermes is the operating layer. It gives us persistent agents, tools, memory, scheduled jobs, file access, Notion access, Obsidian access, Telegram delivery, browser control, and local command execution. Instead of treating AI as a temporary conversation, Hermes lets us treat AI as a team with responsibilities.

## Why we built it

The original problem was not “how do we use AI?”

The real problem was operational leverage.

Limitless Club has many moving parts:

- content ideas
- research signals
- carousels and creative assets
- social posting workflows
- sales and revenue monitoring
- Notion databases
- Obsidian notes
- Telegram alerts
- local tools and gateways
- recurring automations
- founder-level decisions that need context

A normal AI chat can help with one task at a time. But it forgets context, cannot coordinate across tools, and usually does not know where things live.

So we built a system with three principles:

1. **Agents need roles.**  
   Each agent should know what it owns.

2. **Agents need memory.**  
   Important context should not disappear after one chat.

3. **Agents need infrastructure.**  
   If the system matters, it needs folders, runbooks, dashboards, logs, and source-of-truth documents.

## The agent team

We currently use a small team model.

### Kelly — operations and coordination

Kelly is the primary Hermes assistant.

Kelly owns:

- general assistant work
- operations
- automations
- dashboards
- configuration
- troubleshooting
- revenue and system monitoring
- cross-agent coordination

Kelly is the default “operator” of the system. If something breaks, needs to be connected, needs to be checked, or needs to be documented, Kelly handles it.

### Blaze — content and creative production

Blaze owns content creation.

Blaze is responsible for:

- content strategy
- copywriting
- carousel drafts
- creative production
- graphics workflows
- Notion content archives
- social-media-ready assets

This matters because content creation has a very different mindset from operations. Blaze can focus on taste, voice, structure, creative quality, and production speed.

### Signal — AI research and intelligence

Signal owns research and search.

Signal is responsible for:

- AI news
- trend monitoring
- research sweeps
- market intelligence
- finding useful signals for future content
- feeding research into Blaze and Kelly

This turns research into a repeatable function instead of a random activity.

### OpenClaw — gateway and runtime layer

OpenClaw is not a “creative agent” in the same way. It is part of the local infrastructure.

It supports:

- gateway/runtime behavior
- model routing
- browser/tool access
- local channels
- plugin/runtime dependencies

When OpenClaw works, the agent system has more hands. When it breaks, Kelly treats it like infrastructure and troubleshoots it.

## The memory architecture

We decided not to rely only on hidden AI memory.

Hidden memory is useful, but it is not enough for a real operating system. The founder should be able to open the system, inspect it, edit it, and understand how it works.

So we use two human-readable memory layers.

### Obsidian is the operating source of truth

Obsidian stores the detailed version of the system.

It is local, fast, readable, and easy to restructure.

Our main workspace is:

`~/Documents/Obsidian Vault/Agents/`

Inside that, each agent has its own workspace:

- `Agents/Hermes/`
- `Agents/Blaze/`
- `Agents/Signal/`
- `Agents/OpenClaw/`
- `Agents/Shared Memory/`

The most important infrastructure notes are now stored at:

- `Agents/Shared Memory/Infrastructure/Agent Infrastructure OS.md`
- `Agents/Shared Memory/Infrastructure/Agent Registry.md`
- `Agents/Shared Memory/Infrastructure/Notion Mirror Spec.md`

This makes Obsidian the place where the system can be understood and maintained.

### Notion is the executive mirror

Notion is used differently.

Notion is not the deepest operating layer. It is the executive control-room view.

It is better for:

- dashboards
- high-level status
- databases
- task lists
- review pages
- founder visibility

So the rule is:

**Obsidian is where the system lives. Notion is where the system is reviewed.**

We created a Notion page called:

**Agent Infrastructure OS**

That page mirrors the core infrastructure decision, agent roles, key Obsidian paths, and the secrets policy.

## The secrets rule

A serious agent system needs a serious secrets policy.

The rule is simple:

**Never store raw secrets in Obsidian or Notion.**

That means no:

- API keys
- bot tokens
- passwords
- session cookies
- private connection strings

Instead, we store only credential file paths and ownership notes.

If a secret is referenced, it should be written as:

`[REDACTED]`

This lets the system remain useful without turning the notes into a security risk.

## What the system can already do

This is not just a diagram. The system is already doing real work.

Examples include:

- generating content packages
- creating Instagram carousel drafts
- producing carousel graphics
- using browser-based rendering for proper Thai typography
- sending Telegram updates
- syncing or mirroring Notion content into Obsidian
- monitoring AI/business content ideas
- coordinating different agent responsibilities
- checking local API credential presence without exposing values
- troubleshooting OpenClaw runtime issues
- documenting infrastructure decisions as they happen

The important shift is that AI is not only answering questions. It is becoming an operating layer.

## Why this is different from normal automation

Traditional automation is usually brittle.

It follows a fixed path. If something changes, it breaks.

AI agents are more flexible, but without structure they become chaotic.

The Hermes system combines both:

- automation for repeatable execution
- agents for reasoning and adaptation
- Obsidian for durable operating memory
- Notion for visibility
- Telegram for low-friction communication
- local tools for real action

That combination is where the leverage appears.

## The rough value of the system

If we hired humans to cover the same functions, we would not be hiring one person.

We would likely need a small team.

A realistic replacement team might include:

1. AI/Ops Automation Specialist  
2. Content Strategist + Designer/Producer  
3. AI Research / Trend Analyst  
4. DevOps / Integration Engineer  
5. Part-time project/operator oversight

A rough Thailand-market monthly estimate:

| Role | Rough monthly cost |
|---|---:|
| AI/Ops Automation Specialist | ฿80,000–฿150,000 |
| Content Strategist + Designer/Producer | ฿50,000–฿100,000 |
| AI Research / Trend Analyst | ฿60,000–฿120,000 |
| DevOps / Integration Engineer | ฿120,000–฿250,000 |
| PM / operator overhead equivalent | ฿0–฿120,000 |

Base salary range:

**฿310,000–฿740,000 per month**

After adding a conservative 30% overhead for benefits, management time, hiring, equipment, taxes, coordination cost, and replacement risk:

**Estimated loaded cost: ฿403,000–฿962,000 per month**

Annualized:

**฿4.84M–฿11.54M per year**

In USD, using a rough ฿36/USD assumption:

**About $11.2K–$26.7K per month**  
**About $134K–$321K per year**

A leaner two-person version might be possible, but it would still likely cost around:

**฿169,000–฿325,000 per month loaded**  
**฿2.03M–฿3.90M per year loaded**

And that lean version would not have the same 24/7 availability, memory, speed, or parallel-agent behavior.

## What this does not replace

This system does not replace judgment.

It does not replace taste.

It does not replace leadership.

The founder still decides what matters.

The value of the system is that it reduces operational drag. It helps ideas move faster from thought to output. It keeps context alive. It makes the business feel less dependent on one person remembering everything.

## The biggest lesson

The biggest lesson is that AI becomes much more useful when it has a home.

A prompt is not a home.

A chat thread is not a home.

A real system needs:

- roles
- memory
- runbooks
- dashboards
- workflows
- approval gates
- shared context
- clear ownership

That is what we are building with Hermes.

## The current operating rule

From now on:

**All agent infrastructure lives in Obsidian and Notion.**

Obsidian stores the deep operating memory.  
Notion gives the founder-level view.  
Hermes coordinates the work.  
Kelly, Blaze, and Signal each own their part of the system.

This is the beginning of a personal AI operating system for Limitless Club.
