# Memory Hygiene Report — 2026-05-18 04:12

## Daily Note Status (2026-05-18)

| Agent | Today's Daily? | Yesterday (05-17)? | Most Recent Date |
|-------|---------------|-------------------|-----------------|
| Hermes | ✓ (499b) | ✓ daily exists, repo refresh entry | 2026-05-18 |
| Blaze | ✗ MISSING | ✗ no date-file daily notes (has content .md files) | content files only |
| Bolt | ✗ MISSING | ✓ (2026-05-17, 3672b) | 2026-05-17 |
| Kaijeaw | ✗ MISSING | ✓ (2026-05-17, 4120b) | 2026-05-17 |
| Pixel | ✗ MISSING | ✗ last: 2026-05-16 | 2026-05-16 |
| Protocol | ✗ MISSING | ✓ (2026-05-17 likely exists) | 2026-05-17 |
| Qwen | ✓ (329b) | ✓ (2026-05-17, 329b) | 2026-05-18 |
| Signal | ✓ (1017b) | ✓ (2026-05-17) | 2026-05-18 |
| Zegna | ✗ MISSING | ✓ (2026-05-17, 1443b) | 2026-05-17 |
| Shared Memory | ✗ MISSING | ✓ (2026-05-17) | 2026-05-17 |

> Today is early morning (04:12 AM). Agents with today's notes (Hermes, Qwen, Signal) are active. The rest are quiet or not yet scheduled for their daily cron.

## MEMORY.md Inventory

All 9 agent workspaces have `Memory/MEMORY.md` files present and populated. Shared Memory does not use MEMORY.md (it uses a flat directory with dated notes and categorized subfolders).

| Agent | Memory.md Exists | Size |
|-------|-----------------|------|
| Hermes | ✓ | 3,697b |
| Blaze | ✓ | 2,623b |
| Bolt | ✓ | 3,053b |
| Kaijeaw | ✓ | 3,380b |
| Pixel | ✓ | 2,207b |
| Protocol | ✓ | 2,096b |
| Qwen | ✓ | 2,472b |
| Signal | ✓ | 3,457b |
| Zegna | ✓ | 2,344b |

## Folder Structure Health

| Agent | Daily | Protocols | Memory/ | Scratchpad/ | Output/ |
|-------|-------|-----------|---------|-------------|---------|
| Hermes | ✓ 614 files | ✓ 8 files | ✓ | — | — |
| Blaze | ✓ 24 files | ✓ 1 | ✓ | ✓ inbox | — |
| Bolt | ✓ 5 files | ✓ 0 (empty) | ✓ | ✓ (0b) | — |
| Kaijeaw | ✓ 4 files | ✓ 0 (empty) | ✓ | ✓ (0b) | — |
| Pixel | ✓ 1 file | ✓ 0 (empty) | ✓ | ✓ (0b) | — |
| Protocol | ✓ 6 files | ✓ 15 (5 JSON) | ✓ | ✓ 100b | — |
| Qwen | ✓ 9 files | ✓ 4 files | ✓ | — | ✓ |
| Signal | ✓ 90 files | ✓ 1 | ✓ | ✓ 89b | — |
| Zegna | ✓ 4 files | ✓ 0 (empty) | ✓ | ✓ (0b) | — |
| Shared Memory | ✓ 11 files | ✓ 9 files | N/A | — | — |

## Notable Items

### Potential Issues
- **Blaze daily notes use content filenames instead of date filenames** (e.g. `midday-content-burst-2026-05-11.md`). The Daily folder contains ~722 .md files but none follow the `YYYY-MM-DD.md` convention. This may be by-design and is not necessarily wrong — Blaze's daily cadence is content-driven rather than date-driven.
- **Protocol/Protocols/** contains 15 JSON files (e.g., `beehiiv-backlog-*.json`) — these don't belong in a Protocols folder. May be a previous automation's output that was dropped here.
- **Empty Protocols folders**: Bolt, Kaijeaw, Pixel, Zegna all have empty `Protocols/` — not an error, just unused space.

### Healthy Signs
- All agents have Memory/MEMORY.md (durable memory layer intact).
- Shared Memory has a rich structure (Daily, Protocols, Infrastructure, Intel, Projects, etc.).
- Hermes is actively committing (90 files in today's repo refresh).
- Signal is running its X high-alert scan twice today — active and engaged.
- Qwen's daily note exists with todoist-setup-needed update.

### Missing (Likely Benign)
- Today's date notes for Blaze are absent, but this may be because Blaze is a content agent without automated daily note generation at this hour.
- Shared Memory/Daily/ has no 2026-05-18 note — it aggregates agent updates rather than having agent-specific entries.

## File System Overview

Full Agents/ directory tree:
```
Agents/
├── Blaze/
├── Bolt/
├── Codex/           ← non-standard, last note 2026-05-13
├── Cowork/          ← non-standard, last note 2026-05-13
├── Hermes/
├── Kaijeaw/
├── OpenClaw/        ← legacy/non-standard, last note 2026-05-16
├── Oracle/          ← non-standard, last note 2026-05-17
├── Pixel/
├── Protocol/
├── Qwen/
├── Shared Memory/
├── Signal/
├── Uncle Chris/     ← non-standard, last note 2026-05-17
└── Zegna/
```

5 non-standard folders detected (Codex, Cowork, OpenClaw, Oracle, Uncle Chris). These are not in the primary agent memory scope but are present on disk.
