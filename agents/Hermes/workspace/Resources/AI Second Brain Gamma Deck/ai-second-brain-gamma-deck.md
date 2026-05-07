# Build Your Own AI Second Brain
## Obsidian + Codex + Agentic Wiki + Journal + CRM

**Teaching promise:** By the end, you can build a personal knowledge system that does not just store information — it talks back using your own saved content.

Source: YouTube transcript from https://youtu.be/yke4fLQUsh4

---

# The Problem
## Most second brains become graveyards

- We save YouTube videos, articles, tweets, podcasts, meeting notes
- But most of it becomes passive storage
- The knowledge is rarely resurfaced when we actually need it
- The fix: turn the second brain into an active AI system

**Teaching point:** A second brain should not only remember — it should help you think.

---

# The Big Idea
## Put a knowledge base at the center

Build one central markdown vault where everything connects:

- **Wiki / Knowledge Base:** saved sources from the web
- **CRM:** people, meetings, relationships, follow-ups
- **Journal:** daily thoughts, decisions, emotional patterns
- **AI Agent Layer:** processes, links, summarizes, and answers

**Core principle:** Your AI becomes more useful because it is grounded in your own context.

---

# System Map
## The three-input architecture

1. **Raw Inputs**
   - YouTube transcripts
   - Articles
   - Podcasts
   - Tweets / posts
   - Meeting notes

2. **Structured Memory**
   - Concepts
   - Tools
   - Companies
   - People
   - Themes

3. **Active Interface**
   - Chat with the wiki
   - Journal against your own knowledge
   - Ask about relationships and meetings

---

# Required Tools
## Keep the stack simple

- **Obsidian** — markdown vault and visibility layer
- **Obsidian Web Clipper** — save web pages and YouTube transcripts
- **Codex / Claude Code / AI coding agent** — processes and maintains the vault
- **GitHub private repo** — optional backup and version history
- **Automation scheduler** — process new raw files every hour

**Teaching point:** Obsidian is the brain’s body. Codex is the working agent.

---

# Step 1 — Create The Obsidian Vault
## Start with an empty vault

- Create a new Obsidian vault, e.g. `Second Brain`
- Save it somewhere easy to access
- Open the same folder in Codex as a project
- Delete the default welcome note
- Treat the folder as your source of truth

**Instructor note:** Make students write down the exact vault path — the AI agent needs this folder.

---

# Step 2 — Create The Core Folder Structure
## Minimal Carpathy-style wiki architecture

Use this starting structure:

```text
Second Brain/
  raw/
    processed/
  wiki/
  journal/
  CRM/
  agents.md
  index.md
  log.md
```

- `raw/` = unprocessed source material
- `raw/processed/` = archived after processing
- `wiki/` = AI-generated knowledge pages
- `journal/` = daily entries and AI reflections
- `CRM/` = people records
- `agents.md` = operating instructions
- `index.md` = catalog
- `log.md` = changelog

---

# Step 3 — Configure Obsidian Web Clipper
## Capture sources into `raw/`

In Web Clipper settings:

- Set vault name exactly: `Second Brain`
- Set note location: `raw`
- Capture metadata:
  - source title
  - source URL
  - created date
  - tags
- For YouTube, make sure transcripts are included when available

**Teaching point:** The clipper is your intake pipe. Everything enters raw first.

---

# Step 4 — Write The Agent Instructions
## The whole system is powered by `agents.md`

Tell the AI agent how to behave:

- Read new files from `raw/`
- Summarize long source material
- Extract people, companies, tools, ideas, and themes
- Create or update related wiki pages
- Cross-link wiki pages to original sources
- Update `index.md`
- Append actions to `log.md`
- Move processed files into `raw/processed/`

**Key lesson:** The quality of the system is the quality of the operating instructions.

---

# Step 5 — Process Your First Source
## Use one saved article or YouTube transcript

Workflow:

1. Clip a source into Obsidian
2. Confirm it appears in `raw/`
3. Ask Codex: “Process the files inside the raw folder.”
4. Review generated pages in `wiki/`
5. Check `index.md` and `log.md`
6. Confirm the raw file moved to `raw/processed/`

**Demo idea:** Use the tutorial transcript itself as the first source.

---

# Step 6 — Turn The Wiki Into A Chat System
## Ask questions grounded in your saved knowledge

Example question:

> “What are some tips for motivation when I don’t feel like doing the hard task today?”

Expected behavior:

- Agent checks `index.md`
- Finds relevant wiki pages
- Answers using saved sources
- Adds a reusable answer back into the wiki if useful
- Updates `index.md` and `log.md`

**Teaching point:** The wiki improves every time you ask better questions.

---

# Step 7 — Add A Journal Layer
## Make journaling an active thinking partner

Add rules to `agents.md`:

- If a chat starts with `journal`, save the conversation as a new markdown file
- Name it with date + short title
- Add the entry to `journal/index.md`
- Ground the response in:
  - wiki content
  - past journal entries
  - CRM notes
  - general LLM knowledge
- Log the journal entry and summary

**Result:** Your journal can reflect patterns and resurface your own saved ideas.

---

# Step 8 — Add A Personal CRM
## Remember people and conversations

Add rules to `agents.md`:

- If the user says `add to CRM`, create or update a person file
- File name = person’s name
- Include:
  - how you met
  - events / meetings
  - contact details
  - conversation notes
  - relationship context
  - follow-up ideas
- Maintain `CRM/index.md` alphabetically
- Let chat answer questions from CRM records

Example:

> “Where did I meet Matthew Berman?”

---

# Step 9 — Automate The Processing
## Stop manually running the workflow

Create an automation:

- Title: `Process Second Brain Raw Files`
- Project: your `Second Brain` folder
- Cadence: hourly or daily
- Prompt:

```text
If there are any unprocessed files inside the raw directory, process them according to agents.md. After processing, move them to raw/processed, update index.md and log.md, then commit and push to GitHub.
```

**Teaching point:** Automation turns the vault from a project into a living system.

---

# Step 10 — Back It Up With GitHub
## Version control your brain

Optional but recommended:

- Create a private GitHub repo
- Connect the local vault folder
- Commit the current version
- Push to the private repo
- Update automation to commit and push after processing

**Why it matters:** Your vault becomes durable, recoverable, and auditable.

---

# Example `agents.md` Rules
## Copy this operating logic

```markdown
When the user adds a source and asks to process it:
1. Read source files from raw/
2. Summarize important ideas
3. Extract people, companies, tools, concepts, and themes
4. Create/update wiki pages
5. Cross-link related notes and original source pages
6. Update index.md
7. Append an entry to log.md
8. Move processed source to raw/processed/

When the user starts with "journal":
1. Save the conversation to journal/
2. Add a short title and date
3. Ground the response in wiki, CRM, and past journals
4. Update journal/index.md and log.md

When the user says "add to CRM":
1. Create/update a person record in CRM/
2. Add relationship context and notes
3. Update CRM/index.md and log.md
```

---

# Classroom Exercise
## Build the system in 45 minutes

**Lab 1: Setup**
- Create Obsidian vault
- Add folder structure
- Add starter `agents.md`

**Lab 2: Ingest**
- Clip one YouTube video
- Process it into wiki pages
- Check links, index, log

**Lab 3: Activate**
- Ask one grounded question
- Add one CRM contact
- Write one journal entry

**Lab 4: Automate**
- Create hourly processing automation
- Optional: push to GitHub

---

# Common Mistakes
## What breaks the system

- Dumping everything into one folder with no processing rules
- Forgetting to move processed sources out of `raw/`
- Not updating `index.md`
- Letting AI create too many unnecessary files
- Not cross-linking back to sources
- Treating the vault like storage instead of an operating system
- Skipping backups

**Teaching point:** Simple structure beats clever chaos.

---

# The Final Mental Model
## Your second brain becomes a personal AI operating system

It can:

- Store what you learn
- Extract reusable ideas
- Connect related concepts
- Remember people and meetings
- Reflect on your journal
- Surface old knowledge at the right moment
- Get smarter with every source, question, and entry

**Closing line:** Don’t build a knowledge graveyard. Build a living intelligence layer around your life and work.
