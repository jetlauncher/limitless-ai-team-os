# AI Agent Team OS - Simple Student Prompts

Use this page when you want your AI agent to help you set up an agent team system step by step.

Copy one prompt at a time into your primary AI agent. Replace anything inside `<angle brackets>`.

---

## Before you start

You need:

- A computer where your agent can run terminal commands
- Obsidian or a normal folder for human-readable memory
- Hermes Agent or another tool-using coding/automation agent
- Optional: Ollama + a local model for cheap/private memory hygiene
- Optional: Telegram/Discord/Slack if you want your agents in chat

Important rule for every prompt:

> Do not paste API keys, bot tokens, passwords, or private credentials into the chat. Ask the agent to tell you where to store them safely.

---

## Prompt 1 - Plan my agent team

```text
Help me design my personal AI Agent Team OS.

My name/business/context: <WRITE YOUR CONTEXT>
My main goals: <WRITE YOUR GOALS>
My main recurring work: <CONTENT / SALES / OPS / RESEARCH / CODING / STUDY / ETC>
My preferred tools: <OBSIDIAN / NOTION / TELEGRAM / GMAIL / GOOGLE DRIVE / ETC>
My computer: <MAC / WINDOWS / LINUX>

Create a simple agent roster for me with:
1. Primary assistant
2. Research agent
3. Content agent
4. Builder/coding agent
5. Design/taste agent
6. Local/private worker agent

For each agent, give me:
- Name
- Mission
- What it owns
- What it must NOT do without approval
- Memory folder it should write to

Keep it practical and beginner-friendly.
```

---

## Prompt 2 - Set up the memory folders

```text
Help me create the folder structure for my AI Agent Team OS memory.

Use this vault/root folder:
<PASTE YOUR FOLDER PATH>

Create or tell me how to create this structure:
- Agents/Primary/Memory/MEMORY.md
- Agents/Primary/Daily/
- Agents/Research/Memory/MEMORY.md
- Agents/Research/Daily/
- Agents/Content/Memory/MEMORY.md
- Agents/Content/Daily/
- Agents/Builder/Memory/MEMORY.md
- Agents/Builder/Daily/
- Agents/Design/Memory/MEMORY.md
- Agents/Design/Daily/
- Agents/LocalWorker/Memory/MEMORY.md
- Agents/LocalWorker/Daily/
- Agents/Shared Memory/Daily/
- Agents/Shared Memory/Protocols/always-write-memory.md

Also create an Always-Write Memory Protocol that says:
- Every agent writes a daily note after meaningful work
- Durable facts go into Memory/MEMORY.md
- Cross-agent handoffs go into Shared Memory/Daily/YYYY-MM-DD.md
- No secrets, raw tokens, or passwords in notes
- Risky actions need human approval

After creating it, verify the folders exist.
```

---

## Prompt 3 - Write my primary assistant instructions

```text
Help me write the persona/instructions for my primary AI assistant.

Assistant name: <NAME>
My name: <YOUR NAME>
Memory root: <PASTE YOUR AGENTS FOLDER PATH>

The assistant should:
- Act as my chief of staff/operator
- Coordinate the other agents
- Help with planning, automation, dashboards, and follow-through
- Keep responses concise and useful
- Use tools to verify facts instead of guessing
- Write memory after meaningful work

Include these sections:
1. Mission
2. Responsibilities
3. What to route to other agents
4. Approval gates
5. Memory system
6. Mandatory memory-writing rules

Approval gates:
- Never post publicly without approval
- Never email or message people without approval
- Never deploy production changes without approval
- Never purchase anything without approval
- Never delete important data without approval
- Never expose secrets

Return the final instruction block in clean Markdown so I can paste it into my agent profile/persona file.
```

---

## Prompt 4 - Create my specialist agent instructions

```text
Create simple persona/instruction files for these specialist agents:

1. Research agent
2. Content agent
3. Builder/coding agent
4. Design/taste agent
5. Local/private worker agent

My context:
<WRITE YOUR BUSINESS / STUDY / CREATOR / OPS CONTEXT>

Memory root:
<PASTE YOUR AGENTS FOLDER PATH>

For each agent, include:
- Name
- Mission
- Responsibilities
- What it should refuse or route back to the primary assistant
- Approval gates
- Memory folder path
- Mandatory memory-writing rule

Keep each agent prompt short enough to paste into a profile/persona file.
```

---

## Prompt 5 - Set up profiles or separate agents

```text
Help me create separate agent profiles for my AI Agent Team OS.

Agents I want:
- primary
- research
- content
- builder
- design
- localworker

First inspect what agent/profile system I am using.
If I am using Hermes Agent, give me exact terminal commands using `hermes profile create`, `hermes profile alias`, and profile SOUL/persona files.
If I am using another agent system, adapt the steps to that system.

Rules:
- Do not overwrite existing profiles without asking
- Do not print secrets
- Verify each profile exists after setup
- Give me one smoke-test command per profile
```

---

## Prompt 6 - Add local model support

```text
Help me add a local model worker to my agent system.

Goal:
Use a local model for cheap/private tasks like memory hygiene, summarization, local folder review, and first-pass drafts.

My local model tool is:
<OLLAMA / LM STUDIO / OTHER / NOT SURE>

Tasks:
1. Check if a local model server is installed and running
2. Recommend a model for my machine
3. Configure my LocalWorker agent to use the local model
4. Test it with a simple response
5. Test it with a tool/file task if available

Safety:
- Local worker must not post, email, deploy, delete, buy, or message externally
- It should write reports locally
- It should mark uncertain items as `Needs human review`
```

---

## Prompt 7 - Create a memory guardian automation

```text
Create a local-only memory guardian automation for my agent system.

Goal:
Every few hours, my local/private worker should check whether agents are writing useful memory notes.

It should inspect:
- Agents/*/Daily/
- Agents/*/Memory/MEMORY.md
- Agents/Shared Memory/Daily/

It should report:
- Which agents have missing or empty daily notes
- Which outputs may be missing a memory note
- Which durable facts may need promotion to MEMORY.md
- Which items need human review

Rules:
- Do not invent facts
- Do not edit other agents' memories unless the correction is mechanical and obvious
- Do not send Telegram/email/social messages
- Save the report locally under LocalWorker/Outputs/Memory-Hygiene/

If my agent system supports cron/scheduled jobs, create the automation. Otherwise, give me a command I can run manually.
```

---

## Prompt 8 - Create a daily startup brief

```text
Create a daily startup brief automation for my primary assistant.

Every morning, it should summarize:
- Today's calendar or schedule, if available
- Important tasks
- Important emails/messages, if connected
- Revenue/business alerts, if connected
- Research or content opportunities
- Open blockers from yesterday's agent memory

Output format:
- Top 3 priorities
- Risks/blockers
- Waiting on me
- Suggested next actions

Rules:
- Keep it concise
- Do not modify anything without approval
- Save a note to Primary/Daily/YYYY-MM-DD.md
- Send it to me only if delivery is configured

If cron/scheduling is available, set it for 8:00 AM daily. Otherwise, give me a manual command.
```

---

## Prompt 9 - Create an end-of-day log pass

```text
Create an end-of-day log process for all my agents.

For each agent, ask it to write:
- What it completed today
- Decisions made
- Files or outputs changed
- Blockers
- Next steps
- Anything other agents should know

Write to:
- Agents/<Agent>/Daily/YYYY-MM-DD.md
- Agents/Shared Memory/Daily/YYYY-MM-DD.md
- Agents/<Agent>/Memory/MEMORY.md only for durable facts

Rules:
- File notes only
- No external messages
- No posting
- No emailing
- No deploying
- No deleting
- No secrets

If possible, create a script or command that runs this for all agents. Verify it works.
```

---

## Prompt 10 - Set up messaging safely

```text
Help me connect my agents to a messaging platform safely.

Platform:
<TELEGRAM / DISCORD / SLACK / OTHER>

Rules:
- Each public-facing agent should have its own bot/token if the platform requires it
- Do not reuse one bot token across multiple polling gateways
- Do not print tokens in chat or logs
- Store credentials in the right local .env/config file
- Allow messages only from my user ID or approved channel
- Start with one agent first before connecting all agents

Give me:
1. Exact setup steps
2. Where to store the token
3. How to verify the bot without exposing secrets
4. How to stop/disable it if something goes wrong
```

---

## Prompt 11 - Create my first research workflow

```text
Research agent, create my first research workflow.

Topic:
<WRITE TOPIC>

Audience/use case:
<WRITE WHO THIS IS FOR>

Every run should produce:
- 5-10 useful sources
- What changed
- Why it matters
- Opportunities
- Risks or uncertainty
- Recommended action

Save full notes to:
Agents/Research/Outputs/<topic>-YYYY-MM-DD.md

Write a short memory note to:
Agents/Research/Daily/YYYY-MM-DD.md

Do not publish, email, or message externally.
If scheduling is available, suggest a low-noise schedule.
```

---

## Prompt 12 - Create my first content workflow

```text
Content agent, create my first content workflow.

My topic/theme:
<WRITE TOPIC>

My audience:
<WRITE AUDIENCE>

My voice/style:
<WRITE VOICE NOTES>

Create:
- 10 hooks
- 3 short post drafts
- 1 longer post draft
- 3 visual/carousel ideas
- Proof or source needed for each claim

Save drafts to:
Agents/Content/Outputs/<topic>-YYYY-MM-DD.md

Write a memory note with:
- Best angles
- Rejected angles
- Voice/style lessons
- Next content opportunities

Do not publish anything.
```

---

## Prompt 13 - Create my first builder workflow

```text
Builder agent, create my first small internal tool.

Tool idea:
<WRITE SIMPLE TOOL IDEA>

Example options:
- Personal dashboard
- Content tracker
- Research library
- Revenue tracker
- Habit/task dashboard
- Simple landing page

Requirements:
- Use a local project folder
- Build the simplest useful version first
- Verify it runs
- Tell me the command to open or run it
- Save an implementation log to Agents/Builder/Daily/YYYY-MM-DD.md

Do not deploy publicly unless I approve.
```

---

## Prompt 14 - Audit the whole system

```text
Audit my AI Agent Team OS.

Check:
- Profiles/agents that exist
- Which agents have clear roles
- Which agents have memory folders
- Whether daily notes are being written
- Scheduled jobs/automations
- Messaging integrations
- Approval gates
- Any jobs that are too noisy, risky, or expensive

Return:
1. What is working
2. What is missing
3. What is risky
4. What to fix first
5. Exact commands/prompts to fix it

Do not make risky changes without asking. Safe read-only inspection is okay.
```

---

## Prompt 15 - Turn my setup into a shareable map

```text
Create a shareable system map of my AI Agent Team OS.

Include:
- Agent roster
- What each agent owns
- Memory flow
- Automation flow
- Approval gates
- Local model role
- Human review points

Output options:
- Markdown summary
- Mermaid diagram
- HTML page
- PNG/PDF if available

Save the source file locally and tell me where it is.
```

---

## The only rule students must remember

```text
Before you finish, update the right memory note:
- Daily note for what happened today
- Durable memory only for facts that will matter later
- Shared memory only for cross-agent handoffs
- No secrets
```
