# Memory Hygiene Report — 2026-05-27 05:30

Scan date: 2026-05-27 (Wednesday) — early AM cron

---

## 1. Today's daily note status (2026-05-27)

| Agent         | Today's daily | Status   | Comments                              |
|---------------|--------------|----------|---------------------------------------||
| Hermes        | 2026-05-27.md| ✅ OK    | 1.4 KB — active (05:15)               |
| **Blaze**     | MISSING      | 🟡       | Newest: 2026-05-26-dom-operator-lesson.md (May 26 23:13) — likely dormant overnight |
| **Bolt**      | MISSING      | 🟡       | Newest: 2026-05-26.md (May 26 08:09) — likely dormant                         |
| **Kaijeaw**   | MISSING      | 🟡       | Newest: 2026-05-26.md (May 26 09:04) — likely dormant                         |
| **Pixel**     | MISSING      | ⚠️       | **Stale**: last daily 2026-05-16 (11 days ago) — Needs Kelly review            |
| **Protocol**  | MISSING      | ⚠️       | **Stale**: last daily 2026-05-20 (7 days ago) — Needs Kelly review             |
| Qwen          | 2026-05-27.md| ✅ OK    | 0.6 KB — active (05:28, includes this scan)      |
| Signal        | 2026-05-27.md| ✅ OK    | 2.2 KB — **very active**: 4 outputs today (daily note, X-bookmarks, X high-alert scan, daily note) |
| **Zegna**     | MISSING      | 🟡       | Newest: 2026-05-26.md (May 26 09:02) — likely dormant overnight                |
| Shared Memory | MISSING      | 🟡       | Newest: 2026-05-26.md (May 26 20:09) — 1-day gap, likely dormant overnight    |

**Summary: 2/9 active today, 6 missing today (5 likely dormant overnight + 1 critical stale), 1 missing today due to age**

---

## 2. MEMORY.md staleness

| Agent    | Last Modified | Age     | Classification |
|----------|--------------|---------|----------------|
| Hermes   | 2026-05-24   | 3 days  | ✅ OK          |
| Blaze    | 2026-05-21   | 6 days  | 🟡 STALE but has daily activity — suggest quick durable-context merge |
| Bolt     | 2026-05-24   | 3 days  | ✅ OK          |
| Kaijeaw  | 2026-05-23   | 4 days  | ✅ OK          |
| Pixel    | 2026-05-16   | 11 days | 🔴 **CRITICAL** — 11 days stale, 11-day gap in daily activity — Needs Kelly review for archive/restore |
| Protocol | 2026-05-17   | 10 days | 🔴 **CRITICAL** — 10 days stale, 7-day gap in daily activity — Needs Kelly review for archive/restore |
| Qwen     | 2026-05-20   | 7 days  | ✅ OK (borderline — review at next scan) |
| Signal   | 2026-05-23   | 4 days  | ✅ OK — active               |
| Zegna    | 2026-05-23   | 4 days  | ✅ OK |

**CRITICAL agents: Pixel (11d), Protocol (10d)**
**STALE agents: Blaze (6d — but has daily activity, not urgent)**

---

## 3. Recent daily activity (last 48h, since ~May 25 05:00)

| Agent     | Recent activity | Notes                               |
|-----------|----------------|-------------------------------------|
| Hermes    | Heavy          | Multiple files active (May 22-27)   |
| Blaze     | Heavy          | 26+ files in last 48h including large packages |
| Bolt      | Moderate       | Active through May 26 morning       |
| Kaijeaw   | Moderate       | Active through May 26 morning       |
| Qwen      | Active         | Today's daily note + this scan      |
| **Signal** | **Very heavy** | **Most active agent today — 2.1MB folder with 176 files, 4 new today** |
| Zegna     | Light          | Active Mon-Fri pattern through May 26 |
| Pixel     | DORMANT        | No activity since May 16 (11 days)  |
| Protocol  | DORMANT        | No activity since May 20 (7 days)   |

---

## 4. Key findings / Flags

1. **Signal** is the most active agent — massive daily output today. MEMORY.md is fresh (4 days).
2. **Blaze** is producing heavily (large creative packages) but MEMORY.md is 6 days stale — suggest a quick durable-context merge when Blaze next runs.
3. **Pixel** is completely dormant (11 days since last daily, 11-day MEMORY.md). Needs Kelly review for archive/restore decision.
4. **Protocol** is dormant (7 days since last daily, 10-day MEMORY.md). Needs Kelly review for archive/restore decision.
5. **Shared Memory** daily note missing for today — last entry May 26 20:09. Expected for overnight handoffs.
6. **Qwen** daily note exists (0.6 KB) — this scan is running as its first activity for today.

---

## 5. Recommendations

- **Needs Kelly review:** Pixel (dormant 11d, CRITICAL MEMORY.md), Protocol (dormant 7d, CRITICAL MEMORY.md)
- **Suggest quick merge:** Blaze MEMORY.md (6d stale but agent is active with heavy daily output)
- **Monitor:** Shared Memory daily note absence — verify on next daytime run (likely not an issue for early AM)
