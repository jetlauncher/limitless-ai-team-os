
## Cycle 1

### Research Memo: Cycle 1 Update

**Key Findings**
- Hybrid routing reliability hinges on deterministic thresholds (latency, cost, context utilization) rather than heuristic confidence scores. Local→cloud switches typically succeed when triggered by hard SLAs (e.g., >3s inference time or >80% KV cache pressure).
- Multi-agent coordination in research workflows fails most often at context boundary leakage and role drift, not at model capability gaps. Quantized 7B–13B models handle routing/drafting well but struggle with cross-agent state synchronization.
- MVP metrics are viable but require baseline calibration. Time-to-first-insight and intervention frequency are measurable; hallucination/error rates require ground-truth validation sets that are rarely available in early research briefs.
- Local-first architectures yield efficiency gains in iterative refinement loops but incur hidden costs in prompt templating, cache management, and fallback orchestration.

**Evidence/Source Notes**
- *No new external sources fetched this cycle.* Findings synthesized from established patterns in local inference benchmarks (Ollama/vLLM routing behavior), multi-agent orchestration literature (AutoGen/CrewAI context sync failures), and MVP validation frameworks.
- *Uncertainty noted:* Real-world operator intervention rates, exact local-vs-cloud cost ratios, and context drift velocity remain unmeasured. Inferred from industry case studies and architecture teardowns; requires empirical validation.

**What Changed in the Plan**
- Added explicit fallback triggers: KV cache >80%, local inference latency >3s, or retrieval token count >12k.
- Refined kill criteria to include latency SLA breach (>5s end-to-end) alongside the >30% intervention threshold.
- Clarified role boundary validation via deterministic prompt templates and state-diff logging to isolate context leakage.
- Narrowed MVP scope to 3 briefs (informational, comparative, synthesis-heavy) to reduce task-complexity variance in the 2-week sprint.

**Remaining Unknowns**
- Actual operator override frequency when routing 7B–13B local drafts to cloud synthesizers.
- True cost ratio of local quantized inference vs. cloud API calls under sustained retrieval load.
- How context window pressure propagates across the 3-agent fleet during iterative refinement.
- Whether a 2-week sprint captures sufficient task diversity to generalize routing thresholds.

**Next Search Queries**
- `local LLM inference latency cost benchmark 7B 13B quantized ollama vllm`
- `multi-agent context synchronization failure modes research workflow`
- `human-in-the-loop validation metrics autonomous research MVP`
- `hybrid local cloud routing fallback thresholds AI agent orchestration`
