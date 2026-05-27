# Memory Hygiene Report — 2026-05-27 01:02

## Date coverage

| Agent            | Today's Daily (05-27) | Last Daily File          | Days Since Last Daily | Daily files (48h) |
|------------------|-----------------------|--------------------------|-----------------------|-------------------|
| Hermes           | ✅ EXISTS              | 2026-05-27               | 0                     | 10                |
| Blaze            | ❌ MISSING             | 2026-05-26               | 1                     | 8                 |
| Bolt             | ❌ MISSING             | 2026-05-26               | 1                     | 2                 |
| Kaijeaw          | ❌ MISSING             | 2026-05-26               | 1                     | 2                 |
| Pixel            | ❌ MISSING             | 2026-05-16               | 11                    | 0                 |
| Protocol         | ❌ MISSING             | 2026-05-20               | 7                     | 0                 |
| Qwen             | ✅ EXISTS              | 2026-05-27               | 0                     | 3                 |
| Signal           | ❌ MISSING             | 2026-05-26               | 1                     | 15                |
| Zegna            | ❌ MISSING             | 2026-05-26               | 1                     | 2                 |
| Shared Memory    | ❌ MISSING             | 2026-05-26               | 1                     | —                 |

## MEMORY.md staleness

| Agent            | Last Updated | Age (Days) | Classification |
|------------------|-------------|------------|----------------|
| Hermes           | 2026-05-24  | 3          | ACTIVE ✅ (has fresh daily) |
| Blaze            | 2026-05-21  | 6          | STALE 🟡 (4-7d, agent active) |
| Bolt             | 2026-05-24  | 3          | ACTIVE ✅ |
| Kaijeaw          | 2026-05-23  | 4          | ACTIVE ✅ (has fresh daily) |
| Pixel            | 2026-05-16  | 11         | CRITICAL 🔴 (>7d, no daily activity) |
| Protocol         | 2026-05-17  | 10         | CRITICAL 🔴 (>7d, no daily activity) |
| Qwen             | 2026-05-20  | 7          | STALE 🟡 |
| Signal           | 2026-05-23  | 4          | ACTIVE ✅ |
| Zegna            | 2026-05-23  | 4          | ACTIVE ✅ |

## Key findings

1. **Only 2 agents have today's daily note**: Hermes and Qwen. 7 agents + Shared Memory are missing daily notes for 2026-05-27.
2. **Pixel and Protocol are dormant**: Both have been inactive for 7+ days (Pixel: 11 days, Protocol: 7 days). Both have stale MEMORY.md without daily activity → CRITICAL.
3. **Blaze MEMORY.md is borderline stale**: Updated 6 days ago (2026-05-21) but Blaze is actively producing daily content. The durable memory should be updated.
4. **Qwen MEMORY.md**: Updated 7 days ago (2026-05-20) — borderline stale given that Qwen itself is active. Qwen should update its own MEMORY.md.
5. **Qwen's latest daily file** in its own Daily/ was 2026-05-26 (not a date-named today-file). Qwen's 2026-05-27 daily exists — check if it has content.
6. **Blaze non-date file churn**: Blaze's Daily/ contains 2+ non-date files modified recently (e.g., `creative_director_2026-05-25.md`, `jedi-ai-creative-director-2026-05-22.md`). These are large output files (~40-60KB) and may indicate content packages that haven't been promoted or archived properly. They are not harmful but clutter the daily inbox.
7. **Signal is the most active agent**: 15 daily files modified in the last 48h. Signal's MEMORY.md was updated 4 days ago — likely still relevant given its output velocity.

## Flags

- **NEEDS KELLY REVIEW**: Pixel hasn't produced daily notes since 2026-05-16 (11 days). Confirm whether Pixel is dormant or needs a fresh start.
- **NEEDS KELLY REVIEW**: Protocol hasn't produced daily notes since 2026-05-20 (7 days). Confirmed dormant — needs review for archive/restore decision.
- **BLOCKER**: Shared Memory/Daily/ has no 2026-05-27 note. Cross-agent coordination may be incomplete.
