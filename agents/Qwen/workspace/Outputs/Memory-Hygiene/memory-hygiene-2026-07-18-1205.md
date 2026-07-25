# Memory Hygiene Audit — 2026-07-18 12:05

## Scan Summary

| Check | Result |
|-------|--------|
| Agents scanned | 9 canonical + 6 extras = 15 total |
| Today's daily note exists | ✅ 12 of 15 have today's note |
| Missing today's note | Codex, Cowork, Friday, Nova, Team, Uncle Chris (3 per vault × 2 paths) |
| MEMORY.md healthy (≤7d) | Hermes, Blaze, Kaijeaw, Signal, Oracle = 5 agents ✅ |
| MEMORY.md stale 🟡 | Qwen (33d), Protocol (10d), Zegna (10d), Jekjack (20d) = 4 agents |
| MEMORY.md critical 🔴 | Pixel (32d, 84B), Tiff (32d, 82B) = 2 agents — tiny AND old |

## Key Findings

### ✅ Healthy (0 items needing attention)
- 12 agents have today's daily note (2026-07-18)
- 5 agents have fresh MEMORY.md (≤7 days): Hermes, Blaze, Kaijeaw, Signal, Oracle
- Vault architecture intact — both Obsidian and Limitless OS paths show consistent agent directories

### 🟡 Needs attention
1. **Qwen MEMORY.md** — 33 days old (2026-06-15), 2397B. Substantive content but unmerged in a month. Daily notes active at 2222B today — ACTIVE + diverged.
2. **Protocol MEMORY.md** — 10 days old, 581B. Has today's daily output (961B). ACTIVE + diverged.
3. **Zegna MEMORY.md** — 10 days old, 4073B. Healthy content but could use a fresh merge.
4. **Jekjack MEMORY.md** — 20 days old, 68B (tiny). Borderline CRITICAL given the small size.

### 🔴 Critical — Needs Kelly review
5. **Pixel MEMORY.md** — 32 days old (2026-06-16), only 84 bytes. Tiny AND old = likely dormant or memory lost. Has today's daily note (946B) so agent IS active but memory was cleared/not updated.
6. **Tiff MEMORY.md** — 32 days old (2026-06-16), only 82 bytes. Same pattern as Pixel.

### 📎 Missing today's daily note — Needs Kelly review
Agents without 2026-07-18 daily notes: Codex, Cowork, Friday, Nova, Team, Uncle Chris (6 total). Some have substantive files elsewhere in their workspace (Codex 57md, Cowork 77md, Uncle Chris 62md), so they may be dormant or use a different naming convention. Friday has 0 md files — flagged for review.

## Divergence Detail (agent producing daily content but MEMORY.md lagging)
- Pixel: 946B daily today vs 84B MEMORY.md → massive divergence
- Protocol: 961B daily today vs 581B MEMORY.md → moderate
- Qwen: 2222B daily today vs 2397B MEMORY.md (substantial but 33d stale)

## Staleness Classification (skill's unified scheme)
| Agent | Days old | Size (B) | Class | Action |
|-------|----------|----------|-------|--------|
| Hermes | 4 | 10064 | OK ✅ | None |
| Blaze | 4 | 2451 | OK ✅ | None |
| Kaijeaw | 4 | 3553 | OK ✅ | None |
| Signal | 5 | 5913 | OK ✅ | None |
| Oracle | 5 | 1217 | OK ✅ | None |
| Qwen | 33 | 2397 | 🟡 stale | Review recommended |
| Protocol | 10 | 581 | 🟡 stale + diverged | Merge daily summary to MEMORY.md |
| Zegna | 10 | 4073 | 🟡 stale | Quick refresh OK |
| Jekjack | 20 | 68 | 🟡→🔴 borderline | Review → likely too small |
| Pixel | 32 | 84 | 🔴 critical | Needs Kelly review + recreation |
| Tiff | 32 | 82 | 🔴 critical | Needs Kelly review + recreation |

---
Scan completed: 12:05. All data from `~/Documents/Limitless OS/Agents/`. No writes to other agents' memories.
