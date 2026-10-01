# Signal X AI Training Radar — 2026-07-30

**Run by:** Kelly (acting as Signal) on behalf of Jet  
**Time:** Bangkok ~20:30 Thu Jul 30, 2026  
**Status:** x_search disabled / xurl credits depleted → used web lookup only  

---

## Top 3 Signals for Jet

### 1. Microsoft's Routing Thesis — "Don't Upgrade, Route" (July 27)
Microsoft announced **MAI-Cyber-1-Flash** — their first in-house cybersecurity model inside the MDASH agent harness. The design deliberately routes **~90% of routine tasks to a cheaper specialist**, reserving GPT-5.4 only for the hardest 10%. Satya Nadella framed this broadly on July 23: frontier capability is saturated; the competitive advantage now is **tiered model routing + orchestration**, not buying the biggest model.

**Source:** https://www.digitalapplied.com/blog/microsoft-mai-cyber-1-flash-mdash-specialist-model-routing  
**→ Best Jet angle:** Write a content piece for non-technical business owners: *"Stop Routing Everything to Your Smartest (Most Expensive) AI."* Use the 90/10 routing principle as the core framework — show how Jet's agents should handle easy tasks cheaply/fast and escalate only edge cases. This validates what Jet teaches: the operating layer (routing, orchestration) is the real moat, not which base model you buy.

---

### 2. Post-Training RL Is Now the Primary Moat (Deep Dive, May–Jul 2026)
Frontier labs have **inverted compute ratios**: post-training (RL/GRPO) now exceeds pretraining spend. Cursor Composer 1.5 was the first public admission of this. OpenAI/o-series, Anthropic/Constitutional AI, DeepSeek-R1 all confirm. The moat shifted from **pretraining data + model size** to **custom RL loops on proprietary task distributions**. New CUDA 2026 paper (arxiv 2606.07698) adds theoretical grounding for why RLVR/GRPO beats PPO at scale. SpaceX × Cursor's $60B option is fundamentally an RL-infrastructure deal, not a Cursor valuation event.

**Source:** https://www.digitalapplied.com/blog/post-training-revolution-rl-new-moat-2026  
**→ Best Jet angle:** This is foundational content for Jet's "AI Team OS" narrative. Frame it as: *"Your AI advantage won't come from which model you use — it'll come from the RL loop you run on your proprietary business data."* For teaching Thai founders: build your data flywheel; let labs innovate on pretraining while you differentiate on post-training on YOUR workflows.

---

### 3. Kimi K3 Open Weights + 51% Hallucination Rate (Shipped July 27)
Moonshot's **Kimi K3** (2.8T parameters) shipped open weights with ~99th percentile coding performance on Arena.ai Frontend Code Arena — but independent Artificial Analysis evaluation found a **51% hallucination rate** on AA-Omniscience, up from 39% on K2.6. Moonshot omitted this entirely from published benchmarks. Also notable: Kimi generates **3.5× more enterprise shadow AI traffic** than DeepSeek per Harmonic Security research. The lesson: benchmark rankings ≠ production readiness for knowledge-sensitive tasks.

**Source:** https://www.techtimes.com/articles/321499/20260724/kimi-k3-open-weights-drop-july-27-near-frontier-coding-undisclosed-hallucination-risk.htm  
**→ Best Jet angle:** Content hook: *"The 51% Hallucination Rate No One Talks About Before You Ship Kimi K3."* For non-technical businesses adopting AI: your first model evaluation script should measure hallucinations on YOUR domain, not just chase benchmark rankings. This is exactly the kind of grounded, eval-first thinking Jet teaches — don't be seduced by leaderboard optics.

---

## Notable Runner-Ups (Watch)

- **Grok 4.5 pricing:** $2M input / $6M output vs Opus 4.8 at $5/$25; ~60% fewer output tokens for equivalent work. Makes agentic infrastructure much more affordable — business angle: cost basis shift favors building agent-heavy workflows.
  - Source: https://devops.com/spacexais-grok-4-5-undercuts-anthropic-and-openai-on-coding-agent-pricing/

- **NVIDIA Post-Training Guide (Day 3, GPU Tech Conference):** RLVR in practice — synthetic data → GRPO → agent specialization. Practical workflow for customizing agents to proprietary toolchains without real usage data.
  - Source: https://www.youtube.com/watch?v=sVyZVtnygD8

- **Grok 5 AGI timeline still in training on Colossus 2:** Musk claims "10% probability of AGI" at 6T parameters, but original Q1 2026 launch window has passed. Directional signal more than operational.
  - Source: https://lumichats.com/blog/grok-5-agi-claims-6-trillion-parameters-explained-2026

---

## Signal Status & Next Steps

**Status:** ✅ 3 high-signal picks identified (all from web lookup — x_search/xurl unavailable)  
**X Monitor outage continues:** Nitter RSS dead for 3+ consecutive days; xurl credits depleted. Consider:
- Renewing xurl credits or switching to the Hermes x_search tool when enabled
- Adding Grok API key to `~/.hermes/limitless/config.json` if not already present

**Best content production action:** Signal → Blaze handoff on the "90% / 10% AI routing" framework (Signal #1). This is both a standalone article and a recurring content pillar for Jet's audience learning to architect their AI team OS.

**Watch note:** Grok 5 Colossus 2 training progress — if/when it ships or provides a public capability demo, this will reset several assumptions in this week's radar.
