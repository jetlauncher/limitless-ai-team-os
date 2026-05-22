# Subscription Routing Audit — 7-Day Experiment Checklist

## Purpose
Reduce premium model (GPT/Blaze/Kaijeaw) usage by routing safe, high-volume tasks to Qwen — without degrading output quality. Kelly reviews results after 7 days.

## Background
Qwen (qwen3.6:35b, local Ollama) is Jet's cheap, private, high-volume processing layer. Per the local-worker routing protocol:
- **Qwen**: read, summarize, cluster, draft, inspect.
- **Kelly/GPT**: decide, verify, report, coordinate.
- **Claude Code / Blaze / Kaijeaw**: serious app building and final polish.

## 7-Day Experiment Checklist

### Day 1 — Baseline
- [ ] Log current premium model usage stats (number of requests, approximate token cost) for the past 7 days.
- [ ] Identify the top 5 task categories that consume the most premium model calls (e.g., summarization, research clustering, content drafting).

### Day 2 — Task Inventory
- [ ] For each of the top 5 categories, list specific recurring tasks (e.g., "daily digest summarization," "Obsidian memory cleanup," "signal conversation clustering").
- [ ] Tag each task as: Qwen-safe (draft/summarize) or premium-only (customer-facing, brand taste, payment-related).

### Day 3 — First Shift
- [ ] Route one high-volume, low-risk task to Qwen (e.g., long-file summarization).
- [ ] Compare Qwen output side-by-side with previous premium-model output. Note any gaps.

### Day 4 — Second Shift
- [ ] Route a second task type to Qwen (e.g., research clustering, first-pass content ideas).
- [ ] Log time saved and quality delta.

### Day 5 — Third Shift
- [ ] Route a third task type to Qwen (e.g., local QA/log review before Bolt/Claude Code work).
- [ ] Confirm no regression in downstream work quality.

### Day 6 — Triage & Iterate
- [ ] Review all three Qwen outputs against expectations. Identify any that should remain premium-only.
- [ ] Adjust routing rules: tighten what goes to Qwen, keep what doesn't fit.

### Day 7 — Decision Point
- [ ] Compare total cost/time of the 7-day period: premium vs. Qwen-re routed mix.
- [ ] Determine which routing pattern to keep permanently.

## Output Quality Guardrails
- No Qwen output goes customer-facing, social, or email without Kelly review.
- No premium model output should degrade — if it does, revert that task to premium.
- Qwen drafts are first-pass only; Kelly or a specialist model provides final taste.

## Recommendation After 7 Days
Kelly should review the side-by-side quality comparisons and the routing log, then make one decision:
- **Keep/expand Qwen routing** if outputs are acceptable or close to premium quality (likely 40-70% cost reduction on those tasks).
- **Revert/limit Qwen routing** to specific narrow task types if quality gaps are significant.
- Document the final routing triage rules in `Agents/Qwen/Protocols/subscription-routing-final.md` for ongoing use.
