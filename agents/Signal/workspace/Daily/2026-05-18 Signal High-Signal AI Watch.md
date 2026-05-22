# 2026-05-18 Signal High-Signal AI Watch


---

## 2026-05-18 23:04:08 UTC+07:00+0700 - AWS AgentCore adds Lambda-based custom evaluators for production agent QA

### Source links
- AWS Machine Learning Blog: https://aws.amazon.com/blogs/machine-learning/build-custom-code-based-evaluators-in-amazon-bedrock-agentcore/
- Related signal, Hugging Face/IBM Research Open Agent Leaderboard: https://huggingface.co/blog/ibm-research/open-agent-leaderboard

### What changed
- AWS published a new Amazon Bedrock AgentCore workflow for registering custom code-based evaluators backed by AWS Lambda.
- The evaluators can score agent traces at TRACE, TOOL_CALL, or SESSION levels and return labels such as PASS/FAIL, optional numeric scores, and explanations into CloudWatch metrics and AgentCore Observability.
- AWS positions the same evaluator for both on-demand CI/CD gates and online evaluation of live production traffic.
- The launch specifically targets deterministic checks that are often wasteful or unreliable with LLM-as-judge: JSON/schema validation, regex/structural checks, external data lookups, business rules, PII detection, grounded fact checking, and real-time alerting.
- A separate same-day IBM Research/Hugging Face item launched an Open Agent Leaderboard evaluating full agent systems, not just models, with success-rate and cost-per-task comparisons. This reinforces the same operator shift: agent quality is becoming measurable at the system/workflow layer.

### Why it matters
- Production agent reliability is moving from ad-hoc prompt review to instrumented evaluation pipelines: traces, deterministic checks, online monitoring, and CI gates.
- For operators, this lowers the cost of catching tool misuse, bad schemas, PII leakage, and ungrounded outputs before agents touch customer or internal workflows.
- For founders, eval/observability is now a wedge: teams that sell agents will need proof artifacts, not just demos.

### Who should care
- Founders building agentic SaaS or internal copilots.
- Ops/revops teams putting agents near CRM, finance, support, docs, or compliance workflows.
- Limitless Club educators teaching practical AI implementation beyond prompting.

### Recommended action / angle for Jet
- Add an "agent QA gate" module to operator teaching: every production agent needs deterministic checks plus optional LLM-judge checks, wired into CI and live monitoring.
- Practical test this week: pick one Limitless workflow agent and define 3 Lambda-style evaluators: schema validity, source-grounding, and PII/no-secret leakage. Treat pass/fail traces as the evidence layer for deployment readiness.

### Duplicate check
- session_search found no prior exact alert for AWS AgentCore custom code-based evaluators or the IBM Open Agent Leaderboard. Same-day Signal local notes did not contain these terms.


### Storage / backfill confirmation (2026-05-18 23:04:50 UTC+07:00+0700)
- Obsidian append completed at this note path.
- Canonical Signal Reports DB backfill completed successfully: ok=True; database_id=353d076c-9ad3-81cd-aff3-e054bd10e43b; total_artifacts=1468; created=2; updated=1466; failed=0.
- Note patched with this confirmation; backfill rerun once more so Notion metadata reflects final note state.
