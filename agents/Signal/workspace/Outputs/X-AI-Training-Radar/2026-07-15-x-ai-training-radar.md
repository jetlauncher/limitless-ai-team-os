# X-AI-Training-Radar — Wed 15 Jul 2026, 14:30 ICT

> Script `signal_x_training_context.py` not found. Used web lookup only.

---

## Signal 1: Post-training stack has fundamentally shifted — RLVR + GRPO replaced RLHF across all frontier labs

**What happened:** The standard recipe (pretrain → RLHF with human labels) is dead. Every major model from DeepSeek-R1 through Nemotron 3 Super and GPT-5.3 Codex now uses a three-stage post-training pipeline: SFT → GRPO/RLVR → test-time compute scaling. Synthetic self-play + verifiable rewards replaced human preference labeling as the dominant method.

**Why it matters:** This is not incremental improvement — it's a paradigm shift in how models actually learn to reason. The models Jet's audience is using are fundamentally different from what was trained just 12 months ago.

**Sources:**
- https://llm-stats.com/blog/research/post-training-techniques-2026
- https://www.digitalapplied.com/blog/post-training-revolution-rl-new-moat-2026
- https://github.com/TsinghuaC3I/Awesome-RL-for-LRMs

---

## Signal 2: Synthetic data is eating the world — frontier labs running out of "real" training data

**What happened:** WSJ confirmed OpenAI and others are hitting a wall — the public internet literally isn't big enough for next-gen model training. Labs are pivoting to synthetic self-generated training data at scale. This feeds into the growing "model collapse" literature where AI trained on AI data degrades in quality over time.

**Why it matters for Jet's audience:** Thai business owners using AI as their team OS need to understand that AI output quality is increasingly dependent on synthetic data pipelines they can't see or control. The signal-to-noise ratio of AI outputs may change unpredictably.

**Sources:**
- https://www.wsj.com/tech/ai/ai-training-data-synthetic-openai-anthropic-9230f8d8
- https://arxiv.org/html/2601.22607v3 (Self-Evolving Synthetic Data to Verifiable-Reward RL)

---

## Signal 3: The 62% vs 11% AI agent deployment gap — real content opportunity for Jet

**What happened:** McKinsey State of AI 2025: 62% of orgs experimenting with AI agents, but only 11% have deployed them in production. That 51-point gap is where the content opportunity lives. Meanwhile, Anthropic donated MCP to the Agentic AI Foundation under Linux Foundation — standardizing agent communication protocols.

**Why it matters:** Jet's audience (non-technical Thai founders) are squarely in that experimental bucket but need guidance on crossing into production. A "bridge from experiment to deployment" series would directly serve this market gap.

**Sources:**
- https://dancumberlandlabs.com/blog/ai-agents-for-business/
- https://www.averi.ai/how-to/ai-agent-marketing-how-autonomous-ai-is-changing-content-ops-in-2026

---

## Watch list
- Google I/O 2026 (Dec) — DeepMind CEO Demis Hassabis declared "gold medal-level" model performance; worth checking what new training methods were announced.
- OpenAI funding round (~$730B valuation) — could signal aggressive synthetic data investment.

## Raw candidates (lower priority)
- Voice-first AI scaling rapidly (LinkedIn: AI Agent Trends 2026) — interesting for Thai voice-based services but less core to Jet's main angle.
- DAPO emerging as GRPO successor (llm-stats) — too technical for Jet audience unless it affects model behavior dramatically.
