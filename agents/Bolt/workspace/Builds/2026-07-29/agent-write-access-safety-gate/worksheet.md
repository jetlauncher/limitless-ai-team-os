# Agent Write-Access Safety Gate

**Built:** 2026-07-29 02:00 BKK  
**Use:** Student/founder worksheet before giving an AI agent write access.

## The 3 gates

1. **Permission Boundary** — What can this agent read, write, send, buy, or delete?
2. **Independent Verification** — Who checks the output besides the acting agent?
3. **Kill Switch + Audit Trail** — Can a human pause it fast and inspect what changed?

## 7-minute worksheet

| Question | Your answer |
|---|---|
| Workflow name |  |
| Tool/system the agent touches |  |
| Allowed reads |  |
| Allowed writes |  |
| Forbidden actions |  |
| Human checkpoint |  |
| Independent verifier |  |
| Pause/rollback path |  |
| Where logs live |  |

## Decision

- [ ] Score 3/3 — safe bounded pilot.
- [ ] Score 2/3 — draft-only until one missing gate is fixed.
- [ ] Score 0–1/3 — do not grant write access.

## Teaching note

The core lesson: never let the same agent do a high-stakes action and grade its own success. Separate permission, verification, and rollback.
