# Golden Triangle Strategy Map

## Core idea
Every useful AI workflow needs three things:
1. **Knowledge** — the business context that makes the answer yours
2. **Instructions** — the job description and rules for how work should be done
3. **Output** — a real artifact that lands inside the business

If one corner is missing, the system becomes a chatbot. If all three connect, AI becomes an operating system.

```text
              OUTPUT
       reports / drafts / actions
              /                    /                     /              KNOWLEDGE -------- INSTRUCTIONS
 company context       rules + role brief
```

## Strategy questions
### Knowledge
- What company knowledge does this workflow require?
- Where does that knowledge live today?
- Is it in people's heads, chat, files, CRM, calls, or Notion?
- Is it structured enough for AI to use?
- Who owns updating it?

### Instructions
- What role is the AI playing?
- What is it responsible for?
- What inputs should it use?
- What should it never do without approval?
- What does "good" look like?
- When should it escalate?

### Output
- What should the AI produce?
- Where should the output land?
- Who reviews it?
- What is the acceptance standard?
- What changes in the business if this output is produced every week?

## AI-fit scoring
| Criteria | Score 1 | Score 5 |
|---|---|---|
| Repetition | Rare / one-off | Happens weekly/daily |
| Knowledge availability | Mostly in someone's head | Clear docs, calls, CRM, examples |
| Output clarity | Vague | Clear artifact and format |
| Risk | High external/legal/money risk | Draft/internal/read-only first |
| Review owner | Nobody owns it | Clear human approver |
| ROI | Nice-to-have | Saves time or creates revenue |

Best first workflows: high repetition, clear output, low risk, obvious review owner.

## Department examples
| Department | Knowledge | Instructions | Output |
|---|---|---|---|
| Sales | Offers, objections, CRM notes | Follow-up style, approval rules | Draft follow-up + CRM summary |
| Marketing | Brand voice, past content, offers | Campaign objective, tone, examples | Content calendar + post drafts |
| Ops | SOPs, exception cases, checklists | Process steps, escalation rules | Daily ops report / checklist |
| HR | Role scorecard, culture, interview notes | Screening criteria | Candidate shortlist |
| Finance | Transactions, budgets, revenue targets | Reporting cadence, thresholds | Weekly finance summary |
