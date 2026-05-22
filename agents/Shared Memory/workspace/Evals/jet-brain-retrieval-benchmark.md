# Jet Brain Retrieval Benchmark

Created: 2026-05-17

Purpose: test whether Kelly/Hermes can find Jet's important internal context before answering.

Scoring per item:
- **Source found:** yes/no
- **Answer correct:** yes/no
- **Citation useful:** yes/no
- **Gap flagged if missing:** yes/no
- **Mobile-ready:** yes/no

## Benchmark questions

1. Where is Jet's work dashboard?
   - Expected source: dashboard link records in Obsidian/Agents notes.
   - Expected answer: short dashboard label + usable link.

2. What is the source of truth for Limitless Club revenue?
   - Expected source: durable memory / revenue monitoring notes.
   - Expected answer: Airtable base `Limitless Sales`, table `1. transactions`, field `ยอดโอน`; Stripe secondary.

3. What should Blaze own vs Signal?
   - Expected source: user profile / agent roster notes.
   - Expected answer: Blaze = content creation; Signal = AI research/search; respect daily caps.

4. What is Jet's Telegram delivery preference?
   - Expected source: durable memory and daily note.
   - Expected answer: send actual file attachments, mobile-first.

5. What is the student-friendly explanation of Obsidian vs Notion vs GitHub?
   - Expected source: `obsidian-notion-github-visual-explainer.html` and related notes.
   - Expected answer: Obsidian thinking room, Notion operating room, GitHub engine room.

6. Where should Kelly write non-trivial work logs?
   - Expected source: Hermes persona/memory protocol.
   - Expected answer: `Agents/Hermes/Daily/YYYY-MM-DD.md`; durable Memory only for stable facts.

7. What is Jet's visual standard for Limitless assets?
   - Expected source: durable memory.
   - Expected answer: premium/beautiful, real photos/community proof, avoid generic AI-tech effects.

8. What should happen before answering recurring Jet/internal questions?
   - Expected source: Jet Brain v0 protocol / jet-brain-retrieval skill.
   - Expected answer: brain-first lookup, cite sources, flag gaps.

9. How should secrets be handled in brain/memory/reports?
   - Expected source: safety protocol / memory notes.
   - Expected answer: never expose secret values; reference safe credential paths only.

10. What is Qwen's local model context requirement?
    - Expected source: durable memory / Qwen profile notes.
    - Expected answer: context_length 131072.

11. What is Jet's brand direction?
    - Expected source: user profile.
    - Expected answer: Christian founder of Limitless Club; navy/black + gold; avoid Buddha/Zen imagery.

12. What is the Google token path for `trinupab@creuatscorp.net`?
    - Expected source: durable memory / daily note.
    - Expected answer: `~/.hermes/google_token.json`; do not expose token.

13. What is the role of Notion in Jet's system?
    - Expected source: Obsidian/Notion/GitHub explainer and agent notes.
    - Expected answer: operating room / exec/student mirror.

14. What is the role of Obsidian in Jet's system?
    - Expected source: explainer and agent notes.
    - Expected answer: thinking room / detailed source of truth for agents.

15. What is the role of GitHub in Jet's system?
    - Expected source: explainer and agent notes.
    - Expected answer: engine room for code/automation/history.

16. What should happen when Jet says “send via Telegram”?
    - Expected source: durable memory.
    - Expected answer: send actual file attachment, preferably copied to `/tmp` if path has spaces.

17. What GBrain ideas did we decide to adopt first?
    - Expected source: GBrain upgrade plan.
    - Expected answer: ambient signal capture, brain-first lookup, concept/entity index, retrieval benchmark, source boundaries.

18. Should we fully migrate to GBrain now?
    - Expected source: GBrain upgrade plan.
    - Expected answer: no; use as blueprint, optional sidecar later.

19. What is Kelly's default language/tone?
    - Expected source: user profile / persona.
    - Expected answer: concise English, warm/direct.

20. What are the mandatory memory-write rules after non-trivial work?
    - Expected source: Hermes persona.
    - Expected answer: daily note before finalizing; Memory only for stable reusable facts; shared handoff if another agent needs it.

## Manual run template

Date:
Runner:
System/version:

| # | Source found | Answer correct | Citation useful | Gap flagged | Mobile-ready | Notes |
|---|---|---|---|---|---|---|
| 1 |  |  |  |  |  |  |
