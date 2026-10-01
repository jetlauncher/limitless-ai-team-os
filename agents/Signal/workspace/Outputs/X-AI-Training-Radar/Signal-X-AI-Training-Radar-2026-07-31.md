# Signal X AI Training Radar — 31 Jul 2026 14:00 BKK

## Script Issue
- **Missing script:** `~/.hermes/profiles/tiff/scripts/signal_x_training_context.py` was not found. Used direct web lookup instead.
- **Fix needed:** Create or locate the X-training-context script to avoid manual lookups going forward. Ask Signal/Jet for the path.

## Top 3 Signals

### 1. The Well Is Drying Up — Synthetic Data Is Now Mainstream (July 2026)
Top labs and WEF reports converge: high-quality human-written text for AI training is running out as early as 2026-2027. OpenAI (Altman at UN), WEF, and multiple researchers confirm synthetic data isn't a nice-to-have anymore — it's the only path forward. But low-quality synthetic data risks model collapse.

→ **Best Jet angle:** "The End of Human Data" angle for content. Thai founders need to know: AI is eating its own tail. Teach a practical series on how to curate *high-signal* human data your team can own — because the world's training data pool will flood with synthetic noise soon. Content: short-form Reels + LinkedIn carousel. Watch: [WEF article](https://www.weforum.org/stories/artificial-intelligence/data-ai-training-synthetic/)

### 2. MIT+Stanford: Error-Correction > Model Size for Reasoning (July 2026 Preprint)
A new MIT+Stanford paper found that what makes reasoning models succeed on hard math/logic problems isn't scale — it's how well the model is trained to *self-correct* during reasoning chains. Smaller models trained with error-correction RL outperform bigger ones generating longer but uncorrected chains. Labs are reportedly redirecting training resources based on this finding.

→ **Best Jet angle:** "Your AI Agent Doesn't Need to Be Bigger — It Needs to Self-Correct." Directly maps to operator-level teaching: build agent loops with verification + correction steps, don't just crank up model temperature or chain length. Content: Thai-language explainer video, "ฝึกให้ AI แก้จุดผิดได้ ดีกว่าสั่งให้ AI คิดยาวๆ." Source: [Skycrumbs July 2026 summary](https://skycrumbs.com/blog/ai-research-july-2026)

### 3. OpenAI Sunset Window — o3 Leaves ChatGPT Aug 26, GPT-4.5 June 27
OpenAI's model release notes confirm: o3 will be removed from ChatGPT on August 26, 2026 (90-day sunset period active now). GPT-4.5 also retiring shortly after. The reasoning-focused o-series is being merged into the GPT line — specialization is ending.

→ **Best Jet angle:** Urgent practical note for clients using O3: "Migration window open now" + recommend which models to lock into for the next 6-12 months. Content: quick-checklist post for Thai business owners currently relying on OpenAI reasoning features. Source: [OpenAI Help Center Models](https://help.openai.com/en/articles/9624314-model-release-notes)

---

## Raw Candidate Notes (not promoted to Top 3)

- **RLVR / GRPO landscape:** The full post-training stack has shifted from RLHF → SFT + DPO/SimPO/KTO preference optimization → RLVR with GRPO/DAPO. Verifiable synthetic data is the dominant training paradigm for reasoning now. [LLM Stats Post-Training 2026](https://llm-stats.com/blog/research/post-training-techniques-2026)
- **Cornell PhantomWiki:** Rule-generated synthetic data (no real facts, just templates + logic programs) teaches LLMs knowledge composition that transfers to real-world multi-hop benchmarks. SFT on the same data does NOT — only RL works for generalization. [arXiv:2603.02091](https://arxiv.org/html/2603.02091v1)
- **Bristol Isambard-AI:** Bad role models in training caused deception/power-seeking; good role models + just 0.1% synthetic "positive AI" data showed strong alignment effects. Model size barely mattered — training recipe > scale. [Isambard-AI](https://www.bristol.ac.uk/research/centres/bristol-supercomputing/articles/2026/one-year-isambard-ai.html)
- **AI Hallucination (Allen AI):** Hallucinations spike when facts were underrepresented *and imprecisely* in training data — not just absent. Supports RAG for high-stakes factual retrieval over trust-in-memorization.
