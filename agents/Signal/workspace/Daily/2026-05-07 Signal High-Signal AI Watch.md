

---

## Anthropic raises Claude Code/API limits after SpaceX compute deal

- **Timestamp:** 2026-05-07 00:46:11 UTC+07:00
- **Source:** Anthropic — [Higher usage limits for Claude and a compute deal with SpaceX](https://www.anthropic.com/news/higher-limits-spacex) (May 6, 2026)
- **What changed:** Anthropic says it has agreed to use all compute capacity at SpaceX's Colossus 1 data center, adding more than 300 MW / over 220,000 NVIDIA GPUs within the month. Effective immediately, Anthropic is doubling Claude Code five-hour rate limits for Pro, Max, Team, and seat-based Enterprise plans; removing peak-hour limit reduction for Claude Code on Pro/Max; and raising API rate limits for Claude Opus models.
- **Why it matters:** This directly affects builders/operators using Claude Code and Claude API for long-running coding/agent workflows. More capacity + higher rate limits reduce a practical bottleneck that has pushed teams to split work across models or accounts.
- **Who should care:** Founders, technical operators, AI educators, teams building with Claude Code, and Limitless Club members running agentic coding or document workflows.
- **Recommended action/angle:** Re-test Claude Code for larger repo tasks and scheduled agent workflows this week; update procurement guidance to treat rate-limit capacity as a model-selection criterion, not just benchmark quality. Teaching angle: frontier model competition is increasingly a compute-supply and workflow-reliability game.
- **Verification notes:** Official Anthropic page fetched successfully (HTTP 200). `session_search` for exact SpaceX/Claude limits terms returned no recent prior alert, so this is not an exact duplicate.


## OpenAI/NVIDIA MRC: open AI-training networking protocol

**Timestamp:** 2026-05-07 03:03:12 UTC+07:00

**Source links:**
- OpenAI RSS-confirmed article: https://openai.com/index/mrc-supercomputer-networking
- OpenAI RSS feed used for verification: https://openai.com/news/rss.xml
- NVIDIA official technical/partner post: https://blogs.nvidia.com/blog/spectrum-x-ethernet-mrc/
- Google News corroboration query surfaced OpenAI/NVIDIA/industry coverage for `Multipath Reliable Connection`.

**What changed:**
- OpenAI RSS lists **“Unlocking large scale AI training networks with MRC (Multipath Reliable Connection)”** dated 2026-05-05, describing MRC as a new supercomputer networking protocol released via OCP to improve resilience/performance in large-scale AI training clusters.
- NVIDIA’s official 2026-05-06 post confirms **Multipath Reliable Connection (MRC)** is an **RDMA transport protocol** introduced by NVIDIA, Microsoft, and OpenAI; it lets a single RDMA connection distribute traffic across multiple network paths for better throughput, load balancing, and availability in large AI training fabrics.
- NVIDIA says MRC was proven first in production, optimized on Spectrum-X Ethernet hardware, and released as an open specification through the **Open Compute Project**.
- NVIDIA quotes OpenAI’s Sachin Katti saying deployment in the Blackwell generation helped avoid typical network slowdowns/interruptions and maintain frontier training-run efficiency; NVIDIA also says Microsoft Fairwater and Oracle/OCI Abilene AI factories rely on MRC.

**Why it matters:**
- This is not a model launch; it is a frontier-AI infrastructure tell. Training-scale progress is increasingly gated by network reliability, GPU idle time, congestion recovery, and multi-path fabric design.
- For AI infra founders/operators, the opportunity shifts toward cluster networking, observability, congestion/failure recovery, and GPU utilization tooling—not just model wrappers.
- For enterprise buyers, MRC/Spectrum-X/OCP signals that future AI-cloud procurement will increasingly involve network-fabric choices, not just GPU counts.

**Who should care:**
- AI infrastructure founders, data-center/networking operators, cloud/enterprise AI platform teams, and investors tracking frontier-model bottlenecks.
- Limitless operators should care mainly as a strategic curriculum/reference point: “the next AI moat is systems + infrastructure efficiency.”

**Recommended action/angle:**
- Track OCP/MRC spec availability and partner adoption. Use this as a teaching/research angle on why AI infrastructure advantage is moving down-stack: GPU clusters, RDMA/Ethernet fabrics, recovery from micro-failures, and utilization economics.
