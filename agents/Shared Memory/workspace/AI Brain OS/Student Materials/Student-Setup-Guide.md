# Student Setup Guide — Build Your AI Brain OS

## Outcome

By the end, you will have a small markdown-based AI brain that any AI assistant can read.

## Step 1 — Create the folder

Create a folder called `AI Brain`.

Inside it, create:

```text
USER.md
SOUL.md
IDENTITY.md
People/
Projects/
Decisions/
Companies/
Meetings/
Daily/
Knowledge/
MOC/
Sources/
Review Queue/
```

## Step 2 — Create your identity files

Use `Prompts/Identity-Setup-Prompt.md`.

Ask AI to interview you and draft:

- `USER.md`
- `SOUL.md`
- `IDENTITY.md`

## Step 3 — Add your first daily note

Create:

```text
Daily/YYYY-MM-DD.md
```

Write 3–7 lines:

- what happened today
- decisions made
- people mentioned
- projects moved forward
- open loops

## Step 4 — Add your first meeting extraction

Paste a meeting transcript or voice-note summary into AI and use `Prompts/Meeting-Extraction-Prompt.md`.

Save the output in:

```text
Meetings/YYYY-MM-DD-topic.md
```

## Step 5 — Create your first MOC

Create:

```text
MOC/Home.md
```

Add links to the most important pages:

```markdown
# Home MOC

## Identity
- [[USER]]
- [[SOUL]]
- [[IDENTITY]]

## Active
- [[Projects/current-project]]
- [[Daily/today]]
```

## Step 6 — Run nightly compounding

Use `Prompts/Nightly-Compounding-Prompt.md` at the end of the day.

Review what AI proposes before accepting major changes.

## Rule of thumb

Your AI brain is not a dump. It is a filtered decision system.

Keep raw sources separate. Promote only what will help future decisions.
