# Jet Personal Artifact Brain Protocol

Purpose: make Jet Brain evolve with Jet's real thinking, not just agent outputs.

## Primary evolving artifacts

1. **Plaud transcripts** — spoken ideas, meetings, walk-and-talk strategy, founder intuition.
2. **YouTube videos** — published thinking, teaching material, audience-facing explanations.
3. **Brain dumps** — deliberate freeform capture space for ideas before structure.
4. **Apple Notes** — existing day-to-day notes from iPhone/Mac that should be promoted when valuable.

## Canonical source folders

Primary live source root from Jet: iCloud Drive `AI OS`, located on this Mac at:

`~/Library/Mobile Documents/com~apple~CloudDocs/AI OS/`

Important AI OS source folders:

- Plaud: `AI OS/Plaud Library/` and `AI OS/Limitless Academy/Plaud Library/`
- YouTube: `AI OS/YouTube Engine/`
- Brain dump / operating context: `AI OS/_Context Bridge/`, `AI OS/_Task Dispatch/`, `AI OS/00 Dashboard.md`, `AI OS/MEMORY.md`

Normalized imports and agent-readable copies should land under:

`~/Documents/Obsidian Vault/Agents/Shared Memory/Sources/`

Recommended structure:

```text
Sources/
├── Plaud Transcripts/
│   ├── Inbox/
│   ├── Processed/
│   └── _template.md
├── YouTube Videos/
│   ├── Transcripts/
│   ├── Summaries/
│   └── _template.md
├── Brain Dumps/
│   ├── Inbox.md
│   ├── Daily/
│   └── _template.md
└── Apple Notes/
    ├── Imports/
    ├── Promoted/
    └── _template.md
```

## Processing rule

Raw artifact -> normalized source note -> extracted signals -> promoted concepts/projects/entities.

Do not skip directly from raw transcript to durable memory unless the idea is stable and clearly useful.

## Signal extraction schema

For every imported artifact, extract:

- Original source path/link
- Date captured/published
- Artifact type: Plaud / YouTube / Brain Dump / Apple Notes
- One-line summary
- Important raw quotes from Jet
- Decisions made
- Open loops
- People/entities mentioned
- Tools/products mentioned
- Project links
- Content ideas
- Teaching ideas
- Business/revenue implications
- Recommended promotion target:
  - `Concepts/`
  - `Entities/People/`
  - `Entities/Tools/`
  - `Projects/`
  - `Daily/`
  - `Archive only`

## Digest integration

Daily Jet Brain Digest should include a section when new personal artifacts exist:

```markdown
**Jet source signals**
- Plaud: [1 key idea / decision]
- YouTube: [1 reusable teaching/content insight]
- Brain dump: [1 open loop or project seed]
- Apple Notes: [1 promoted note, if any]
```

Weekly digest should include:

- Top 5 raw Jet ideas captured
- Ideas promoted into concepts/projects
- Best content clips/topics from YouTube
- Open loops from Plaud/brain dumps
- Notes needing Jet clarification

## Safety and privacy

- Do not index entire home folders or credential/config folders.
- Apple Notes import should be explicit or query-scoped until Jet approves broad export.
- Plaud transcripts may include private meetings; default to local Obsidian only.
- YouTube videos can be treated as public unless Jet marks them private/unlisted.
- Keep raw transcripts separate from promoted durable memory.

## Current setup notes

- YouTube transcript canonical path already exists: `~/clawd/youtube-transcripts/` and is exposed in `~/Documents/Limitless OS/Inbox/YouTube Transcripts/`.
- Apple Notes CLI `memo` is not currently installed in this environment; install with `brew tap antoniorodr/memo && brew install antoniorodr/memo/memo` before automated Apple Notes search/export.
- Plaud source folders are discovered and scanner-wired: `AI OS/Plaud Library/` and `AI OS/Limitless Academy/Plaud Library/`, plus canonical `Sources/Plaud Transcripts/Inbox/` / `Processed/` drop folders.
