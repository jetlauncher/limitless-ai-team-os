# Qwen Obsidian Hygiene Report — 2026-07-21

Scan time: 20:33

---

## Top findings

1. **194 Memory-Hygiene reports accumulated TODAY** (Qwen/Outputs/Memory-Hygiene/) — severe file bloat from repeated hourly scrapes. Needs cleanup.
2. **Shared Memory/MEMORY.md is STALE** — last modified 2026-07-04 (17 days, boundary of OK → leaning STALE). Shared daily notes are active today (47 files).
3. **Qwen/MEMORY.md is STALE** — last modified 2026-06-15 (36 days old, 2397 bytes). Not tiny but very lagging behind operative daily notes. Needs durability merge if agent is active.

## Detailed findings

### Qwen workspace status
- **Daily notes**: Fresh and healthy. Today's note exists (1640B), last modified today. Daily history spans 2026-06-15 to 2026-07-21 — no gaps in the active period.
- **Queue dir**: MISSING — `~/Documents/Limitless OS/Agents/Qwen/Queue/` does not exist on disk. (Legacy/manual queue may be routed elsewhere.)
- **Outputs**: Active — morning-prep, todoist-setup-needed, and memory-hygiene reports for today. 194 hygiene files in Memory-Hygiene/ alone (excessive).
- **MEMORY.md**: 🟡 STALE — 36 days old (2026-06-15). Non-empty (2397B) so likely not fully dormant, but context is very stale.

### Shared Memory status
- **MEMORY.md**: 🟡 OK → leaning STALE — 17 days old (2026-07-04, 1922B). Boundary case between OK and STALE per classification rules.
- **Daily dir**: 47 files total, active daily notes through today. Two anomalies:
  - `2026-07-09-hourly-1000.md` — non-standard hourly file (not a daily note, not an anomaly).
  - `2026-07-09/` — DIRECTORY instead of FILE (structural irregularity; may cause tools expecting .md to fail on July 9 lookups) [Needs Kelly review]

### Anomaly files in Shared Memory/Daily/
- `2026-05-24.md` (1177B) — oldest file, 57 days old. From when? May be pre-agency throwaway.
- `2026-06-15 2.md` (1329B) — space+dup name. Likely copy-paste artifact from iCloud sync conflicts. [Needs Kelly review]

### Staleness classification summary
| File | Age | Status |
|------|-----|--------|
| Qwen/MEMORY.md | 36 days | 🔴 CRITICAL (if tiny → dormant, otherwise very stale) |
| Shared Memory/MEMORY.md | 17 days | 🟡 STALE (boundary) |

## Recommendations (actionable)

### Can clean without review
- Remove old memory-hygiene reports older than today (194 of them accumulated in one day — most are historical noise).
- Recommend keeping only the latest or a daily aggregate, not hourly snapshots.

### Needs Kelly review
- `Shared Memory/Daily/2026-07-09/` directory vs `.md` expectation — could break tools scanning for July 9 daily note.
- `Shared Memory/Daily/2026-06-15 2.md` — duplicate name, likely iCloud artifact.
- Qwen/MEMORY.md staleness (36 days) — decide whether to archive or refresh.

### Next step
Check with Jet on: (1) memory-hygiene report frequency — reduce from hourly to twice-daily minimum? (2) `2026-07-09/` dir vs file status.
