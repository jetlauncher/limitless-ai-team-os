# Jet Brain v0 Protocol

Created: 2026-05-17

## Goal

Make Jet's Hermes + Obsidian + Notion + agent fleet behave more like a reliable operating brain, inspired by GBrain patterns, without a risky full migration.

## Core rules

1. **Brain-first lookup** — for recurring Jet topics, check durable memory, session history, Obsidian, and relevant systems before external research or recreating docs.
2. **Ambient signal capture** — capture only high-value stable facts/ideas; do not interrupt fast mobile replies.
3. **Exact-phrase preservation** — if Jet gives a strong idea, save the exact phrasing plus context.
4. **Entity/concept linking** — important people, tools, projects, and concepts get linked pages.
5. **Citations and gap flags** — answers should cite source files/URLs when possible and explicitly say when a source is missing.
6. **Mobile-first delivery** — short Telegram summaries; send files as attachments when deliverables are requested.
7. **No secret indexing** — never ingest or quote token/API-key/credential contents.

## Where things go

- Concepts → `Agents/Shared Memory/Concepts/`
- People → `Agents/Shared Memory/Entities/People/`
- Tools → `Agents/Shared Memory/Entities/Tools/`
- Projects → `Agents/Shared Memory/Projects/`
- Retrieval tests → `Agents/Shared Memory/Evals/`
- Protocols → `Agents/Shared Memory/Protocols/`

## Write decision table

- User preference/correction that will recur → durable Hermes memory + daily note.
- Temporary task status → daily note/session only.
- Reusable workflow → Hermes skill.
- Stable concept or teaching idea → concept page.
- Shared cross-agent decision → Shared Memory daily note or project page.
- Sensitive credential/token → never store value; reference safe path only if needed.
