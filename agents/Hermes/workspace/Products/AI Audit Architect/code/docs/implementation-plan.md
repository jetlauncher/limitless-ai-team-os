# AI Audit Architect MVP Implementation Plan

> **For Hermes:** Use subagent-driven-development skill to implement this plan task-by-task.

**Goal:** Build a first internal product workflow that turns an SMB discovery transcript into a premium AI workflow audit report and implementation proposal.

**Architecture:** Start as a local/Hermes-assisted product workflow with structured prompts, schemas, and templates. Then convert to a CLI or Telegram command flow after the first real audit is validated.

**Tech Stack:** Hermes/Kelly, Python, Markdown templates, Gamma API, Notion API, Obsidian, optional Airtable later.

---

## Phase 1 — No-code/Internal MVP

### Task 1: Collect one real or sample transcript

**Objective:** Get a realistic input to validate the product.

**Files:**
- Create: `~/Documents/Obsidian Vault/Agents/Hermes/Products/AI Audit Architect/client-audits/<client>/transcript.md`

**Verification:** Transcript exists and includes enough workflow detail.

### Task 2: Run the analysis prompt

**Objective:** Generate the first opportunity map.

**Files:**
- Use: `prompts/analyze-discovery-transcript.md`
- Create: `client-audits/<client>/analysis.md`

**Verification:** Output includes top opportunities, scoring, and quick-start plan.

### Task 3: Convert analysis to client report

**Objective:** Produce a premium report draft.

**Files:**
- Use: `templates/gamma-report-template.md`
- Create: `client-audits/<client>/gamma-report.md`

**Verification:** Report can be pasted into Gamma or generated via Gamma API.

### Task 4: Generate Gamma report

**Objective:** Create client-facing visual deliverable.

**Files:**
- Input: `client-audits/<client>/gamma-report.md`
- Output: Gamma URL and PDF/PPTX export

**Verification:** Gamma link opens and report looks premium.

## Phase 2 — Automation MVP

### Task 5: Create Python audit package

**Objective:** Add code for repeatable report generation.

**Files:**
- Create: `src/audit_architect/__init__.py`
- Create: `src/audit_architect/schema.py`
- Create: `src/audit_architect/scoring.py`
- Create: `src/audit_architect/report.py`
- Test: `tests/test_scoring.py`

**TDD:** Write scoring tests before scoring implementation.

### Task 6: Add CLI commands

**Objective:** Run audits from terminal.

**Commands:**
```bash
ai-audit new CLIENT_NAME
ai-audit analyze CLIENT_NAME transcript.md
ai-audit report CLIENT_NAME
```

### Task 7: Add Telegram/Hermes command wrapper

**Objective:** Use Kelly as the operator interface.

**Commands:**
```text
/audit new
/audit transcript
/audit report
/audit proposal
```

## Acceptance Criteria

- Can produce a premium audit report from a transcript in <60 minutes.
- Report contains 3-7 specific recommendations.
- Top 3 recommendations are implementable within 4 days.
- Every recommendation includes ROI/time saved estimate.
- Output can be delivered as Gamma/PDF/Notion.
