# AI Audit Architect — Vercel Deployment

Status: Deployed as customer-facing chatbot  
Production URL: https://ai-audit-architect.vercel.app  
Latest Inspect URL: https://vercel.com/jetlaunchers-projects/ai-audit-architect/2JF8eySzmY1uX1yATvA7ZEzqgqeT

## What was deployed

A Vercel-compatible chatbot MVP:

- Chatbot UI: `public/index.html`
- Chat API: `api/chat.py`
- Legacy form audit API: `api/audit.py`
- Core engine: `src/audit_architect/`
- Config: `vercel.json`

## Verification

- Automated tests: `12 passed`
- Secret scan: no common token/key patterns found
- Browser QA: loaded production URL, bot asked first intake question, accepted a customer answer, moved to next question, and generated an audit/report when requested.

## Current product capability

The deployed product can:

1. Chat with a customer through a guided intake flow
2. Ask for business, industry/customer, team, bottlenecks, tools, and goals
3. Generate an AI leverage diagnostic from the chat context
4. Show ROI/time-saved metrics
5. Produce top workflow opportunities
6. Generate Gamma-ready markdown report
7. Generate implementation proposal
8. Copy/download report markdown

## Important limitations

- Current chatbot is structured/guided, not yet powered by a live LLM conversation model.
- Current analyzer is heuristic/keyword-based, not yet LLM-backed.
- Thai language option is UI-level only; native Thai output still needs LLM/report localization.
- No database/auth/client accounts yet.
- Gamma API generation is not wired into deployed UI yet.
- No Notion/Airtable persistence yet.

## Recommended next deployment iteration

1. Add LLM-backed chat + transcript analysis
2. Add Thai-native report generation
3. Add Gamma API export button
4. Add lead capture / audit record storage
5. Add admin-only access or password gate before using with clients
