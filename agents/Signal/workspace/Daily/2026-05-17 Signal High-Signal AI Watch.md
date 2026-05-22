# Signal High-Signal AI Watch - 2026-05-17

## 2026-05-17 05:09 UTC+07:00 - Google Genkit Middleware for governed agent loops

**What changed**
- Google Developers published **"Announcing Genkit Middleware: Intercept, extend, and harden your agentic apps"** on 2026-05-14.
- Official page says Genkit middleware provides composable hooks that intercept generation calls, including the tool-execution loop.
- The middleware is available now in **TypeScript, Go, and Dart**, with **Python support coming soon**.
- Google frames the concrete use cases as retries/fallbacks, human approval before destructive tool calls, context/message injection, tool-loop observability, and policy/security hardening.

**Why it matters**
- This is another sign that production agents are shifting from prompt demos to **governed execution loops**: every model/tool call needs interception, logging, approval, and recovery paths.
- For founders and operators, middleware is the practical layer where agent safety and reliability become product features rather than after-the-fact audits.
- For Limitless/education, this is a useful teaching primitive: agents are not just prompts + tools; they need a control plane around tool use.

**Who should care**
- AI app builders, Firebase/Google Cloud teams, internal-tool founders, agent-workflow consultants, and operators deploying tool-calling agents into customer or business systems.

**Recommended action / angle for Jet**
- Add Genkit Middleware to the agent-governance watchlist and benchmark it against OpenAI Agents SDK hooks/sandboxing, AWS AgentCore, and LangGraph middleware.
- Good angle: **"The moat is moving from prompts to the middleware around every agent action."**

**Sources / verification**
- Official Google Developers Blog: https://developers.googleblog.com/announcing-genkit-middleware-intercept-extend-and-harden-your-agentic-apps/
- Official page metadata verified `datePublished: 2026-05-14`; body verified middleware hooks intercept generation/tool loops and support TypeScript, Go, and Dart today, Python soon.

**Duplicate check**
- `session_search` found adjacent agent-governance coverage but no prior exact Genkit Middleware alert. Same-day Signal local notes did not contain `Genkit Middleware`.


---

## 2026-05-17 17:05:49 UTC+07:00+0700 - Microsoft Teams SDK adds A2A bot-to-bot communication pattern

**What changed**
- Microsoft Learn published/updated **"Bot-to-Bot Communication with A2A"** on 2026-05-15 for the Teams SDK AI integrations path.
- The doc frames Agent2Agent (A2A) as a third interaction model beyond people-chatbots and tools/APIs/MCP: agents communicate directly with peer agents, each with its own model, capability description, and human audience.
- The Teams example shows an LLM-backed bot reading peers' capability descriptions, deciding whether to answer directly or delegate to a better-suited peer, then looping the receiving bot's human operator in through an Adaptive Card before returning the answer over A2A.
- Microsoft also documents Agent Cards as machine-readable capability adverts for peers to fetch and use for routing/delegation decisions.

**Why it matters for founders/operators**
- This is a practical enterprise surface for **agent-to-agent delegation inside Microsoft Teams**, not just an abstract A2A protocol doc.
- Teams can become the coordination layer where specialist bots/agents route work to each other while preserving human review at the edge.
- Operators building internal AI assistants should design around agent cards/capability metadata, auth, audit logs, and human approval flows now; Teams-native agents will increasingly be expected to interoperate rather than live as isolated chatbots.

**Who should care**
- Microsoft 365/Teams integrators, internal automation teams, agent-workflow founders, customer-support/revops operators, and Limitless-style educators teaching enterprise agent workflows.

**Recommended action / angle for Jet**
- Add this to the agent-control-plane watchlist: **"enterprise agents are becoming discoverable coworkers, not standalone bots."**
- For any Limitless demo/workshop, prototype a simple `sales bot -> finance bot -> human approval -> Teams response` handoff and compare Microsoft A2A with Google ADK/Genkit, AWS AgentCore, and OpenAI Agents SDK handoff patterns.

**Sources / verification**
- Microsoft Learn: https://learn.microsoft.com/en-us/microsoftteams/platform/teams-sdk/in-depth-guides/ai-integrations/a2a
- Microsoft Learn search API verified `lastUpdatedDate: 2026-05-15T13:55:00+00:00` for the exact title.
- Related Microsoft Agent Framework A2A integration docs: https://learn.microsoft.com/en-us/agent-framework/integrations/a2a

**Duplicate check**
- `session_search` found no prior session for "Microsoft Bot-to-Bot Communication with A2A". Same-day Signal High-Signal, Morning Brief, and X High-Alert notes did not contain `Bot-to-Bot`, `A2A`, `Microsoft Learn`, or `Teams SDK`.

**Backfill confirmation (2026-05-17 17:06:43 UTC+07:00+0700)**
- `signal_reports_db_backfill.py` completed successfully: ok=true; database_id=353d076c-9ad3-81cd-aff3-e054bd10e43b; total_artifacts=1430; created=1; updated=1429; failed=0.
