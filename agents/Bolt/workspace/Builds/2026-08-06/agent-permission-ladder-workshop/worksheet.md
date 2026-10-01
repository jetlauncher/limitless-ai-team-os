# Read / Draft / Action Agent Permission Ladder — Student Worksheet

**Use case:** Before a founder or student gives an AI agent access to a real tool.

## 1. Workflow scenario
- Tool/account involved:
- Customer/business impact if wrong:
- Data sensitivity:
- Current human owner:

## 2. Pick the minimum permission level
| Level | Allowed | Not allowed | Approval needed |
|---|---|---|---|
| READ | Look, summarize, classify, recommend | Write, send, delete, buy, deploy | Source/folder approval |
| DRAFT | Prepare output in a queue/doc/dashboard | Send, publish, update CRM, charge money | Human review before action |
| ACTION | Execute a narrow approved workflow | Anything outside approved scope | Named approval phrase + log + rollback |

## 3. Six checks
- [ ] What is the smallest permission level that still creates value?
- [ ] What exact source proves the agent is right?
- [ ] Where does the output wait for human review?
- [ ] How do we pause it within 60 seconds?
- [ ] What log shows every read/write/send/delete attempt?
- [ ] What is the rollback plan if the agent is wrong?

## 4. Final permission decision
- Selected level: READ / DRAFT / ACTION
- Human approver:
- Approval phrase, if ACTION:
- Log path:
- Pause/kill switch:
- Rollback plan:

## 5. Teaching reflection
What would make this agent safer without making it useless?

---
Generated locally by Kelly nightly build on 2026-08-06T02:05:35+0700. No external actions were taken.
