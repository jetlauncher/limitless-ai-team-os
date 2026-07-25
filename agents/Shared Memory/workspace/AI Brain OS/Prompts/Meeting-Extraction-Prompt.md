# Meeting Extraction Prompt

Use this prompt for meeting transcripts, Plaud notes, calls, coaching sessions, and voice memos.

```text
Extract this meeting into my AI Brain.

Output markdown with these sections:

# Meeting Extraction — <date> — <topic>

## 1. Decisions
For each decision:
- what was decided
- who decided
- why
- alternatives considered
- impact

## 2. Commitments
For each commitment:
- owner
- promised action
- due date / timing
- dependency
- follow-up needed

## 3. Preferences
Extract durable preferences about how people work, communicate, buy, decide, or evaluate quality.

## 4. People updates
Mention people who deserve new or updated People files.

## 5. Project updates
Mention projects that deserve new or updated Project files.

## 6. Knowledge / frameworks
Extract reusable frameworks, claims, quotes, mental models, or teaching ideas.

## 7. Open loops
List unresolved questions, blockers, or follow-ups.

## 8. Promotion recommendations
Classify each item:
- Daily note only
- Add to People
- Add to Projects
- Add to Decisions
- Add to Knowledge
- Needs human review

Rules:
- Skip small talk.
- Do not invent missing details.
- Keep raw transcript separate from processed extraction.
- Do not store secrets.
```
