# Signal X AI Training Radar — Thu Jul 16, 2026 ~14:35 ICT

**Note:** Script `signal_x_training_context.py` was not found at `~/.hermes/profiles/tiff/scripts/`. Using web lookup directly.

---

## Top 3 Signals

### 1. Post-Training RL Is the Frontier Moat (2026)
All frontier labs have inverted their compute ratio — post-training RL now exceeds pretraining compute. Cursor's Composer 1.5 explicitly disclosed 20× RL scale-up on the same base model. SpaceX × Cursor's $60B deal is fundamentally an RL-infrastructure play (access to xAI Colossus cluster). Opus 4.7's +6.8 pt SWE-Bench jump was entirely post-training driven, not base-model size.

- → **Jet angle:** When teaching Thai founders about "buy vs build" AI strategy, the moat is no longer in base model choice — it's in post-training on proprietary task data. Content hook: "Your AI advantage isn't which model you pick, it's what you train it to do." Practical: show a simple RL post-training workflow for a Thai business-specific task (e.g., tax-compliance agent, supply-chain planner).

### 2. Google DeepMind's SRL Framework — Small Models, Big Reasoning
Google/UCLA's Supervised Reinforcement Learning (SRL) bridges SFT and RLVR by teaching models step-wise intermediate actions rather than just final-answer rewards. On agentic coding tasks: +74% relative improvement over standard SFT using only a 7B model. On math benchmarks: 3% average boost. The key insight: dense, fine-grained per-step feedback beats sparse outcome-only feedback for small models tackling complex multi-step reasoning.

- → **Jet angle:** Demonstrates that Thai non-tech businesses don't need GPT-5-class models to get agent-level performance — they need better training methodology on smaller/cheaper models. Content hook: "You don't need the biggest AI to solve your hardest problems. You need the right training loop." Practical workshop idea: build a small-model agentic workflow for a real Thai SME problem (e.g., automated invoice processing, customer triage).

### 3. Peak Data → Synthetic Loop Is Now the Industry's Core Strategy
Sutskever announced "peak data" at Neurips. The solution: test-time compute generates synthetic training data that feeds back into the next model generation. Satya Nadella calls it "another scaling law." Early evidence suggests synthetic data from reasoning models already outperforms raw internet data for training quality. This creates a self-reinforcing flywheel where better models → better synthetic data → even better models.

- → **Jet angle:** For Thai business owners, the implication is clear: your organization's real-world operational data (not internet scrapes) will be increasingly valuable as synthetic data loops become the standard. Content hook: "Your proprietary business processes are now AI gold — they're what will differentiate trained agents in 2026." Practical angle: position Jet's curriculum around helping businesses structure their internal data for agent training, not just using off-the-shelf models.

---

## Watchlist
- Anthropic's Claude Cowork going cross-device (phone → laptop → phone async) — implications for non-tech operators who need to review agent work from mobile.
- GPT-5.6 Sol Ultra Mode: 64 subagents on one problem claims a proof in under an hour — multi-agent orchestration is moving from concept to reality.
- Amazon AGI director: "AI agent reliability, not capability, is blocking enterprise deployment." — speaks directly to Thai business adoption barriers.

## Sources
- [The Post-Training Revolution: RL Is the New Moat in 2026](https://www.digitalapplied.com/blog/post-training-revolution-rl-new-moat-2026) — Digital Applied, May 2026
- [Google's SRL Framework for Small Models](https://venturebeat.com/ai/googles-new-ai-training-method-helps-small-models-tackle-complex-reasoning) — VentureBeat, Nov 2025
- [AI Hit 'Peak Data' — Google's Solution](https://www.businessinsider.com/ai-peak-data-google-deepmind-researchers-solution-test-time-compute-2025-1) — Business Insider, Jan 2025
- [The 2025 AI Agent Index (MIT)](https://aiagentindex.mit.edu/data/2025-AI-Agent-Index.pdf)
- [Synthetic Data + Multi-Step RL (arXiv)](https://arxiv.org/html/2504.04736v2)

---

**Next tiny step:** Consider a Thai-language content piece or short video on "Why post-training beats pretraining for your business" — ties signals 1+2 together with a practical SME angle.
