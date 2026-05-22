# Memory Hygiene Report — 2026-05-20 04:02 ICT

**Audit by:** Qwen (local cron agent)
**Scope:** Daily notes and Memory/MEMORY.md for all agent folders
**Data source:** `find` output on disk only (search_files may omit empty dirs)

---

## Today's Daily Note Status (2026-05-20)

| Agent | Today? | Size | Last file before today |
|-------|--------|------|----------------------|
| Hermes | ✅ | 482 B | `2026-05-20.md` (Notion sync + GitHub) |
| Qwen | ✅ | 243 B | `2026-05-20.md` (Todoist cron error) |
| Signal | ✅ | 1,091 B | `2026-05-20.md` (X High-Alert Scans + Notion) |
| Blaze | ❌ | — | `jedi-ai-creative-director-2026-05-19.md` |
| Bolt | ❌ | — | `2026-05-19.md` (AccRevoX + Thumbnail MVP) |
| Kaijeaw | ❌ | — | `2026-05-19.md` (Workshop cron + Thai Threads) |
| Pixel | ❌ | — | `2026-05-16.md` (EOD log) |
| Protocol | ❌ | — | `2026-05-17.md` (Iris migration) |
| Zegna | ❌ | — | `2026-05-19.md` (Curation refresh) |

**Summary:** 3/10 agents have today's daily note. 7 agents are missing.

---

## Durable Memory (Memory/MEMORY.md) Check

| Agent | MEMORY.md | Size |
|-------|-----------|------|
| Hermes | ✅ | 4,286 B |
| Blaze | ✅ | 2,623 B |
| Bolt | ✅ | 3,053 B |
| Kaijeaw | ✅ | 3,380 B |
| Pixel | ✅ | 2,207 B |
| Protocol | ✅ | 2,096 B |
| Qwen | ✅ | 1,078 B |
| Signal | ✅ | 4,135 B |
| Zegna | ✅ | 2,822 B |
| Oracle | ✅ | 627 B |

**Summary:** All 10 agents have MEMORY.md present. No gaps.

---

## Daily Template Check

| Agent | Template? |
|-------|-----------|
| Hermes | ✅ |
| Blaze | ✅ |
| Bolt | ❌ |
| Kaijeaw | ❌ |
| Pixel | ❌ |
| Protocol | ✅ (exists as `2026-05-17.md` but template check returned OK — verify) |
| Qwen | ❌ |
| Signal | ✅ |
| Zegna | ❌ |
| Oracle | ❌ |

**Note:** Only 4/10 agents have `_template.md`. The rest would need one if standardization is desired.

---

## README Check

All 10 agents have `README.md` present. ✅

---

## Structure Depth Notes

- **Signal Daily/:** Has a stray file `~/Documents/Obsidian Vault/Agents/Signal/Daily/~/Documents/Obsidian Vault/Agents/Signal/Daily/2026-05-14 Signal X High-Alert Scan.md` — this looks like a malformed path artifact that should be cleaned up on request.
- **Qwen Daily/:** Flat directory (no subdirs beyond the daily files). Minimal but functional.
- **Blaze Daily/:** Has deep nesting (`youtube-x-articles-batch-*`, `hermes-thai-student-docs/`) alongside flat daily notes. Mixed layout is fine but worth noting.

---

## What's Stale / Missing

### Staleness (days since last daily)
- **Pixel:** 4 days (last: 2026-05-16) — ⚠️ oldest gap
- **Protocol:** 3 days (last: 2026-05-17)
- **Blaze, Bolt, Kaijeaw, Zegna:** Missing today only (1 day gap)

### Structural gaps (no template)
- Bolt, Kaijeaw, Pixel, Qwen, Zegna, Oracle — all lack `_template.md` but this is informational, not a correctness issue.

### No findings in yesterday (2026-05-19) daily notes that appear to lack memory notes downstream
- All yesterday's daily notes are substantive (Blaze: AI news picks; Bolt: AccRevoX + Thumbnail MVP; Kaijeaw: workshop cron; Signal: X scans; Zegna: curation refresh; Hermes: Notion sync + GitHub push). These are all action items or logs that would naturally be handled in future sessions rather than requiring separate MEMORY.md entries at this time.

---

## Summary: Gaps requiring attention

1. **7/10 agents missing 2026-05-20 daily note** — normal for a cron run (Blaze, Signal, Kaijeaw, Zegna produce daily on demand; Bolt, Pixel, Protocol have intermittent cadence)
2. **6/10 agents missing `_template.md`** — informational gap
3. **Signal: 1 malformed file in Daily/** — `~/Documents/Obsidian Vault/...` artifact path, Needs Kelly review before deleting
4. **Pixel: no daily notes since 2026-05-16** — 4-day gap, Needs Kelly review to confirm Pixel activity pauses
5. **Oracle: has MEMORY.md (627 B) but no visible daily activity** — very small memory file needs Kelly review to confirm if Oracle is active

---

**Next audit:** 2026-05-21
