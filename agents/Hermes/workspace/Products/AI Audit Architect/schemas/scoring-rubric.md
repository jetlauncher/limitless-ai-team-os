# AI Audit Architect Scoring Rubric

Each opportunity is scored 1-5.

## Scores

- **Time Saved:** How many owner/team hours are likely saved weekly?
- **Revenue Impact:** Does this increase sales, conversion, retention, or speed to cash?
- **Pain Intensity:** How emotionally painful or urgent is this workflow?
- **Implementation Ease:** How fast can we ship a working version?
- **Tool Reliability:** Is the tool/workflow stable enough for SMB use?
- **Maintenance Risk:** Will it break often or require expert upkeep?
- **Client Readiness:** Is the client capable of adopting it now?

## Priority Formula

```text
priority = (time_saved + revenue_impact + pain_intensity + client_readiness) * tool_reliability / (6 - implementation_ease + maintenance_risk)
```

## Recommendation Rules

1. Recommend only tools/workflows we can explain and demo.
2. Prioritize boring reliable automation over shiny AI demos.
3. Never give more than 7 recommendations.
4. The top 3 must be implementable within 4 days.
5. Every recommendation needs a before/after workflow.
6. Every recommendation needs a measurable success metric.
