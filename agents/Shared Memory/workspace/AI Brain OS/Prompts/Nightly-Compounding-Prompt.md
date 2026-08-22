# Nightly Compounding Prompt

Use this at the end of the day or as a scheduled local-only job.

```text
Run a safe nightly compounding pass on my AI Brain.

Scope:
- Read only notes created or modified today.
- Do not delete anything.
- Do not send messages, emails, posts, or external requests.
- Do not modify secrets or credential files.
- If an update is uncertain, write it to Review Queue instead of durable memory.

Tasks:
1. Find orphan mentions of people, projects, companies, and concepts that do not yet have files.
2. Propose new files for those entities.
3. Consolidate obvious duplicate notes by writing a proposed merge note, not by deleting originals.
4. Update relevant MOC/index files with new links.
5. Extract durable facts that should be promoted to memory.
6. Flag strategic items for human review tomorrow.
7. Write a short daily compounding report.

Output:
- Files created
- Files updated
- Proposed merges
- Durable facts promoted
- Items needing human review
- Risks / uncertainty

Approval rule:
Only make low-risk link/index/template updates automatically. Put anything strategic, sensitive, or ambiguous into Review Queue.
```
