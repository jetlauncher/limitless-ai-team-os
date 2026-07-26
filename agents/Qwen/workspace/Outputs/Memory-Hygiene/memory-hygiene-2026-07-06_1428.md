# Memory Hygiene Audit — 2026-07-06 14:28

## Vault status
- Directory count: 9 agents + Shared Memory — all present ✅ (no disappearance)
- Primary vault (Limitless OS): active, real data ✅
- Obsidian vault: iCloud stub state (Shared Memory dirname = 224 bytes) — normal cloud placeholder

## Today's daily notes (2026-07-06)

| Agent | Status | Size | Lines |
|-------|--------|------|-------|
| Hermes | ✅ OK | 2,842 B | 33 |
| Blaze | ✅ OK | 1,919 B | 20 |
| Bolt | ✅ OK | 1,122 B | 22 |
| Kaijeaw | ✅ OK | 2,522 B | 15 |
| **Pixel** | ❌ MISSING | — | — |
| **Protocol** | ❌ MISSING | — | — |
| Qwen | ✅ OK | 436 B | 9 |
| Signal | ✅ OK | 2,073 B | 19 |
| Zegna | ✅ OK | 1,188 B | 11 |
| Shared Memory | ✅ OK | 240 B | 3 |

## MEMORY.md staleness

| Agent | SIZE | Age | Classification |
|-------|------|-----|----------------|
| Hermes | 4,922 B | 2d | ✅ ACTIVE |
| Blaze | 1,088 B | 2d | ✅ ACTIVE |
| Bolt | 2,609 B | 12d | 🟡 STALE — suggest durable-context merge |
| Kaijeaw | 956 B | 17d | 🟡 STALE — stale for weeks, daily active but memory untouched |
| Pixel | 84 B | 20d | 🔴 CRITICAL — nearly empty placeholder + missed daily note |
| Protocol | 90 B | 20d | 🔴 CRITICAL — nearly empty placeholder + missed daily note |
| Qwen | 2,397 B | 21d | 🔴 STALE — full content but >7d since last update |
| Signal | 86 B | 20d | 🔴 CRITICAL — near-empty placeholder |
| Zegna | 1,797 B | 0d | ✅ ACTIVE |

## Divergent-output check
- No agents flagged: none have heavy daily output (>50 lines) with tiny MEMORY.md (<200 bytes).

## Diverged/stale flags (agent has daily activity but MEMORY.md lagging):
- **Bolt** — 12d stale, MEMORY present but dated. Needs durable-context merge when agent next active.
- **Kaijeaw** — 17d stale + missed today's daily note? No, kaijeaw HAS today (2,522 B). Memory just stale.
- **Qwen** — 21d stale with full 2,397B content; memory file exists but not refreshed in ~3 weeks.
- **Signal** — 86B placeholder, 20d old — likely never started filling durable memory despite daily activity.

## iCloud note
- Shared Memory dirname = 224 bytes → confirmed iCloud cloud stub. Active data on Limitless OS path is correct.
- Qwen MEMORY.md: stat confirms 2,397B but `cat` throws "Resource deadlock avoided" — iCloud read timing gap confirmed for this file. File exists and intact; can be refreshed later when sync window opens.

## Needs Kelly review
1. **Signal MEMORY.md** — 86B placeholder. If Signal is active (daily notes show it is), durable memory should be populated.
2. **Pixel & Protocol MEMORY.md** — both ~90B placeholders, 20d old. Both also missed today's daily note. May need archive/review.
3. **Pixel & Protocol** — missing today's daily note. Could be intentional (weekend/dormant) or agent cron failure.

## Summary
- **Healthy**: Hermes, Blaze, Qwen (daily), Zegna (daily + fresh memory)
- **Needs attention**: Bolt (memory stale 12d), Kaijeaw (memory stale 17d)  
- **Needs Kelly review**: Signal & Pixel & Protocol — near-empty MEMORY.md files; Pixel & Protocol also missed today's daily note
