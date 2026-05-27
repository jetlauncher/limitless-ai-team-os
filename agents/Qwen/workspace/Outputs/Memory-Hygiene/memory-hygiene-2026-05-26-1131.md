# Memory Hygiene Audit — 2026-05-26 11:31

## Overview

| Metric | Value |
|---|---|
| Total agents scanned | 15 |
| Agents with today's daily note | 9 / 15 |
| ACTIVE memory (≤7d or recent daily) | 6 |
| STALE memory (4–7d stale) | 0 |
| CRITICAL memory (>7d stale, no daily) | 3 |
| No MEMORY.md on disk | 2 |

## Per-Agent Details

| Agent | Today's Daily | MEMORY.md | Classification |
|---|---|---|---|
| **Hermes** | ✅ exists (100 bytes) | 2.0 days old | ACTIVE ✅ |
| **Blaze** | ✅ exists (2,210 bytes) | 4.9 days old | ACTIVE ✅ |
| **Bolt** | ✅ exists (647 bytes) | 2.1 days old | ACTIVE ✅ |
| **Kaijeaw** | ✅ exists (2,565 bytes) | 3.2 days old | ACTIVE ✅ |
| **Pixel** | ❌ missing | 10.2 days old | CRITICAL 🔴 — Needs Kelly review |
| **Protocol** | ❌ missing | 9.1 days old | CRITICAL 🔴 — Needs Kelly review |
| **Qwen** | ✅ exists (1,198 bytes) | 5.6 days old | ACTIVE ✅ |
| **Signal** | ✅ exists (3,840 bytes) | 3.1 days old | ACTIVE ✅ |
| **Zegna** | ✅ exists (1,050 bytes) | 3.1 days old | ACTIVE ✅ |
| **OpenClaw** | ❌ missing | 10.2 days old | CRITICAL 🔴 — Needs Kelly review |
| **Codex** | ❌ missing | none found | OK (no MEMORY.md defined) |
| **Cowork** | ❌ missing | none found | OK (no MEMORY.md defined) |
| **Oracle** | ✅ exists (2,539 bytes) | 8.9 days old | ACTIVE (🔵) — recent daily activity |
| **JEK Jack** | ❌ missing | Daily/ not found | OK (likely inactive) |
| **Uncle Chris** | ✅ exists (6,803 bytes) | 6.2 days old | ACTIVE ✅ |

## Shared Memory / Daily

- **Path exists:** Yes
- **Total files:** 20
- **Most recent:** `2026-05-16.md` (9.5 days old)
- **Gap:** No shared daily notes since May 16 (10 days ago)

## CRITICAL — Needs Kelly Review

1. **Pixel** — No daily for 10 days, MEMORY.md 10.2 days stale. May need archive/restore review.
2. **Protocol** — No daily for 9 days, MEMORY.md 9.1 days stale. May need archive/restore review.
3. **OpenClaw** — No daily for 10 days, MEMORY.md 10.2 days stale. May need archive/restore review.

## Notes

- **Oracle** has stale MEMORY.md (8.9 days) but recent daily activity (3 files in last 48h). Classified ACTIVE — not urgent.
- **Codex, Cowork, JEK Jack** have no MEMORY.md on disk — no action required unless user wants them created.
- No non-date daily files found in the last 48h.
- No Todoist tasks matched (0 of 392 open tasks matched Qwen selection rule).
