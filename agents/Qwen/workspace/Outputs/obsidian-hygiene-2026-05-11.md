# Obsidian Hygiene Report — 2026-05-11
**Agent**: Qwen
**Scope**: `Agents/Qwen/` and `Agents/Shared Memory/`
**Date**: 2026-05-11

---

## Summary

- **Qwen workspace**: Healthy, current. Daily notes and MEMORY.md are fresh.
- **Shared Memory**: Some root-level files have drifted from their proper subdirectories. Credentials file needs review.
- **Duplicates**: One confirmed duplicate (subscription-routing-audit.md).
- **No empty folders** or structural gaps found in Qwen workspace.

---

## 1. Duplicate Files — Actionable

### subscription-routing-audit.md
- **Location 1**: `Agents/Qwen/Queue/done/subscription-routing-audit.md` (task stub — 1.0KB)
- **Location 2**: `Agents/Qwen/Outputs/subscription-routing-audit.md` (completed work product — 2.8KB)

**Assessment**: Queue/done version is a task stub with the same title as the Output version. The Output file is the actual deliverable; the Queue/done file is a leftover artifact.

**Recommendation**: Move `Queue/done/subscription-routing-audit.md` to `Queue/archive/` so it no longer looks like a lingering done task.
**Risk**: Low. No content loss.

---

## 2. Shared Memory Root-Level Files — Drift

These files sit directly in `Agents/Shared Memory/` and do not follow the `Daily/`, `Infrastructure/`, or `Protocols/` convention:

### ACCESS-TOKENS.md — NEEDS KELLY REVIEW 🔴
- **Age**: 20 days old
- **Content**: Contains Notion API keys, database IDs, and other credentials.
- **Problem**: Credential files in Shared Memory root breaks the security convention ("no raw API keys").
- **Recommendation**: `Needs Kelly review`. Determine if this file should exist in Shared Memory at all. If kept, move to a secure location outside the agent workspace or redact API key values.
- **Risk**: **High** — credential exposure risk.

### 2026-04-21.md
- **Age**: 20 days old
- **Content**: Original shared-memory setup note.
- **Problem**: Orphaned daily note in root. Its content was superseded by subsequent daily notes in `Shared Memory/Daily/`.
- **Recommendation**: Safe to archive or delete. No unique information not already captured elsewhere.
- **Risk**: Low.

### Jedi Offer Architecture.md
- **Age**: 18 days old
- **Content**: Business offer/content architecture reference (from limitlessclub-shop).
- **Problem**: Business content belongs in a `Jedi/` or `Projects/` folder, not Shared Memory.
- **Recommendation**: Move to `Agents/Jedi/Offer-Architecture.md` or equivalent projects folder. Not really a hygiene issue for Shared Memory.
- **Risk**: Low.

---

## 3. Shared Memory/Intel/ — 1 Stale File

- **`2026-04-26 - Signal Daily AI Intel Report.md`** (15 days old, cutoff: 14 days)

**Recommendation**: Review if Signal still needs Intel reports retained past 14 days. If not, archive them. Otherwise, establish a monthly archival routine.
**Risk**: Low — informational content.

---

## 4. Shared Memory/Protocols/ — Slightly Stale but Acceptable

| File | Age | Status |
|------|-----|--------|
| agent-workflow.md | 20d | OK — may want quarterly review |
| handoff-template.md | 20d | OK |
| agent-memory-routing.md | 15d | OK |
| revenue-reporting-rule.md | 20d | OK |
| README.md | 20d | OK |

**Recommendation**: No immediate action. These are stable documents. Consider a quarterly review cadence.
**Risk**: None.

---

## 5. Shared Memory/Infrastructure/ — Healthy

All files are 0–15 days old. Latest is `Qwen Background Worker Setup.md` (today).
**Risk**: None.

---

## 6. Qwen Workspace Status

| Area | Status | Notes |
|------|--------|-------|
| Daily/2026-05-11.md | ✅ Current | Today's daily note exists (2.1KB) |
| Daily/2026-05-10.md | ✅ OK | Yesterday's note intact |
| Memory/MEMORY.md | ✅ Current | Last durable review: 2026-05-11 16:38 |
| Queue/ | ✅ OK | todo/ empty, doing/ empty, archive/ empty, done/ has 1 item |
| Queue/done/ | ⚠️ 1 item | subscription-routing-audit.md (see #1 above) |
| Outputs/ | ✅ OK | 3 output files, all actionable |
| Outputs/Todoist/ | ✅ OK | todoist-cron-fix-needed.md documents known gap |
| Protocols/ | ✅ OK | 2 protocol files, current |
| Scratchpad/ | ✅ OK | Has README, no stray content |

---

## 7. Todoist Integration Notes

`Outputs/todoist-setup-needed.md` and `Outputs/Todoist/todoist-cron-fix-needed.md` are **valid, actionable notes** documenting real gaps:
- The fetch script exists at `~/.hermes/scripts/qwen_todoist_fetch.py` (not the originally expected path).
- No active Qwen Todoist cron is currently registered.
- **Action**: These are operational notes, not hygiene issues. They should be kept until the cron is re-added and verified.

---

## Action Items Summary

| # | Issue | Action | Risk | Owner |
|---|-------|--------|------|-------|
| 1 | subscription-routing-audit.md duplicated | Move Queue/done/ to Queue/archive/ | Low | Qwen (auto) |
| 2 | ACCESS-TOKENS.md in Shared Memory root | Needs Kelly review — possibly redact or relocate | **High** | Kelly |
| 3 | 2026-04-21.md in Shared Memory root | Safe to archive/delete | Low | Qwen (auto) |
| 4 | Jedi Offer Architecture.md in wrong path | Move to Projects/Jedi/ | Low | Kelly |
| 5 | 1 stale Signal Intel report | Review retention policy | Low | Signal |
| 6 | No current Qwen Todoist cron | Operational gap (documented) | Medium | Kelly |

**Items Qwen can self-correct**: #1, #3
**Items needing Kelly review**: #2, #4, #6

---

*Report auto-generated by Qwen. No external side effects performed.*
