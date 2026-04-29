# AI Audit Architect

A Limitless Club product MVP for turning SMB discovery transcripts into a premium AI workflow audit, Gamma-ready report, and implementation proposal.

## Product Positioning

This is **not** a generic AI tools audit clone.

It is a **Limitless AI Leverage Diagnostic**:

- diagnose founder/time/revenue bottlenecks
- map current workflows into future AI-enabled workflows
- score opportunities by impact, difficulty, reliability, and readiness
- produce a premium client report
- convert the audit into implementation packages

## Current Build Status

MVP CLI is working and tested.

Implemented:

- client audit workspace creation
- intake JSON generation
- transcript ingestion
- heuristic workflow/opportunity analysis
- priority scoring rubric
- Gamma-ready markdown report generation
- implementation proposal generation
- demo clinic audit
- automated tests

Tests:

```bash
python -m pytest tests/ -q
# 7 passed
```

## Commands

Run from this folder:

```bash
cd ~/Projects/ai-audit-architect
PYTHONPATH=src python -m audit_architect.cli --workspace client-audits new "Client Name" --industry "industry"
PYTHONPATH=src python -m audit_architect.cli --workspace client-audits analyze "Client Name" path/to/transcript.md --language English
PYTHONPATH=src python -m audit_architect.cli --workspace client-audits report "Client Name"
PYTHONPATH=src python -m audit_architect.cli --workspace client-audits proposal "Client Name"
```

Outputs are saved under:

```text
client-audits/<client-slug>/
```

## Demo

Demo transcript:

```text
demo-transcript.md
```

Demo output:

```text
demo-audits/bangkok-premium-clinic/
├── intake.json
├── transcript.md
├── analysis.json
├── analysis-preview.md
├── gamma-report.md
└── proposal.md
```

## Next Product Layer

1. Replace heuristic analyzer with LLM-backed analysis using the existing prompt.
2. Add Thai report mode.
3. Add Gamma API report creation.
4. Add Notion/Airtable client audit records.
5. Add Telegram/Kelly command wrapper: `/audit new`, `/audit analyze`, `/audit report`, `/audit proposal`.

## Safety / Quality Rule

Do not recommend tools randomly. Each recommendation must include:

- before workflow
- after workflow
- specific tools
- implementation steps
- hours saved estimate
- risk/maintenance note
- confidence/priority score
