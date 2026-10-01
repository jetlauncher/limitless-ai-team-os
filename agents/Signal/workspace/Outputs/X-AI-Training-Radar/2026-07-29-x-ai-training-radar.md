---
type: signal-radar
date: 2026-07-29
source: web_search (x_search HTTP 400; xurl credits depleted)
status: delivered
summary: Post-training RL is the structural moat; Grok 4.5 uses Cursor agent-data; frontier models race on reasoning depth not just base params
---

# Signal X AI Training Radar — 2026-07-29 16:00 BKK

**Collection status:** Degraded — x_url credits depleted (HTTP 402), x_search HTTP 400. Picked up signals from web search instead.

---

## Top 3 Signals

### 1. Post-training compute is the new AI moat
- **What:** Cursor Composer 1.5 disclosure confirmed post-training compute exceeded pretraining compute (20× RL scale-up). SpaceX × Cursor $60B deal was fundamentally an RL-infrastructure purchase, not a valuation event. Opus 4.7's +6.8pt SWE-Bench lift came entirely from CAI+RL post-training, not base model size.
- **Why it matters:** The foundation layer (base models) is becoming commoditized. All frontier labs are converging on the same thesis — differentiation lives in proprietary training pipelines: task distributions, reward models, and RL compute scale.
- **Best Jet angle:** Write a Thai content piece framing "AI tools are commodities; the real edge is how you train them." Explain to Thai business owners that competitive advantage no longer comes from which AI tool they use, but what training/optimization layer sits on top of it — the same way any phone can run WhatsApp, but the business advantage comes from internal process optimization.
- **Sources:** digitalapplied.com/blog/post-training-revolution (May 2026), Opus 4.7 announcement (Jul 1, 2026), Cursor Composer 1.5 disclosure

### 2. Grok 4.5 — first model trained on real Cursor agent-interaction data
- **What:** xAI released Grok 4.5 (V9 base, 1.5T MoE) trained with trillions of tokens of real Cursor agent-interaction data. xAI dissolved into unified SpaceXAI brand. Monthly model cadence continued.
- **Why it matters:** Real-world agentic workflow data is now a legitimate training corpus. The loop "agents do work → that work trains the next model → next model makes better agents" is closing for real. This validates the AI Team OS concept at infrastructure scale.
- **Best Jet angle:** "xAI is literally feeding robot work back into the AI as teaching material." Use this to reinforce why Jet's students should be building operational feedback loops — not just using AI tools, but having AI observe/improve their own workflows daily. Concrete example: the same principle applies to any Thai SME that records how their staff uses tools, then trains the system better over time.
- **Sources:** ThursdAI July 2026 releases, AlphaSignal LinkedIn (Jul 27), Medium "Christmas in July" analysis

### 3. Reasoning models are racing on inference-time scaling, not just pretraining
- **What:** OpenAI o-series shows dual scaling curves — both training-time AND test-time compute improve accuracy log-linearly. Inference-time scaling (spending more compute during generation) is now a confirmed axis alongside RL post-training. DeepSeekMath-V2 pushed gold-level math competition performance via inference-time methods.
- **Why it matters:** The cost-latency-accuracy triangle is getting real for business owners. Spending 5× inference compute can produce dramatically better outcomes, but the economics matter — Jet's audience needs to understand when this tradeoff makes sense (complex decisions) vs. doesn't (simple automation).
- **Best Jet angle:** "AI ที่คิดนานกว่า = ผลลัพธ์ดีกว่า แต่แพงขึ้น" — teach Thai founders how to calibrate their AI use cases: which tasks deserve deep reasoning spend, which should stay fast-and-cheap. Position Jet as the one who tells them where to invest compute vs. save it.
- **Sources:** Sebastian Raschka "State of LLMs 2025", NVIDIA RLVR in Practice (DAY-3 session, 2026), OpenAI o-series scaling curves

---

## Watch notes
- x_url credits depleted — renew at https://platform.x.ai to restore bookmark/search collection for tomorrow's run
- Kimi K3 open weights shipped with hallucination rate of 51% (digitalapplied.com, Jul 27) — worth monitoring for Thai deployment implications if students consider using it

## Collection failures
- xurl bookmarks: HTTP 402 credits depleted
- x_search Responses: HTTP 400 endpoint (disabled)
- Nitter RSS: confirmed dead (previous days' daily notes confirm)
