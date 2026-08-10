# Limitless Club AI Content Production System

> The Hormozi-style media stack rebuilt as an AI-agent workflow for Jedi / Limitless Club.

Source document: `/Users/ultrafriday/.hermes/cache/documents/doc_0713a47ca6d1_agents.pdf`

## One-line operating model

Jedi drops **one idea seed** — voice memo, paragraph, raw conversation, workshop recording, or transcript. Three agents activate in parallel:

1. **Long-form Director Agent** → YouTube/package/recording brief.
2. **Short-form Agent** → native Reels/TikTok/Shorts/FB/X/LinkedIn scripts.
3. **Clipping Agent / Miner** → clip map, buried hooks, mids candidates.

Output lands in one idea bundle:

```text
YYYY-MM-DD_idea-slug/
├── 00-brief.md
├── 01-longform/
├── 02-shorts/
└── 03-clips/
```

## Core philosophy

- Start from **Jedi's actual interest, experience, and proof**, not trend-copying.
- Package last: idea → audience → problem → value → YouTube viability → title/thumbnail.
- Optimize for **audience quality × views → enrollments**, not raw views.
- Long-form conversation/training is the master asset; short-form is advertising for long-form.
- Clips are mined non-linearly: the best hook may be buried in the middle.

## Start here

1. Read `00-Operating System/content-production-protocol.md`.
2. Fill the starter knowledge files in `02-Knowledge Base/`.
3. For every new idea, copy `03-Idea Bundles/_template/` to `03-Idea Bundles/YYYY-MM-DD_idea-slug/`.
4. Run the three agent prompts in `01-Agent Prompts/` against the same idea.
5. Log performance in `04-Performance Logs/proven-content-log.md` after 7 and 28 days.
