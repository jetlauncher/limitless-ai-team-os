# 2026-06-02 Signal X High-Alert Scan

Timestamp: 2026-06-02 00:10 +07
Method: `xurl --app jet-x whoami` succeeded; per-account xurl search returned JSON `CreditsDepleted`, so current scan used Nitter RSS for curated AI/operator accounts, then official/credible source verification.

Selected source-grounded X signals:
1. Anthropic draft S-1 — X: https://x.com/AnthropicAI/status/2061478052257841495; verification: https://www.anthropic.com/news/confidential-draft-s1-sec
2. Vercel AI endpoint token-theft controls — X: https://x.com/vercel_dev/status/2061447653129671014; verification: https://vercel.com/blog/protecting-against-token-theft
3. Databricks Genie data-agent research — X: https://x.com/databricks/status/2061187235207065750; verification: https://www.databricks.com/blog/pushing-frontier-data-agents-genie
4. Databricks Lakebase CMK for Postgres — X: https://x.com/databricks/status/2061464072726397211; verification: https://www.databricks.com/blog/take-control-customer-managed-keys-lakebase-postgres
5. JetBrains Mellum2 open source 12B workflow model — X: https://x.com/jetbrains/status/2061444430884675791; verification: https://blog.jetbrains.com/ai/2026/06/mellum2-goes-open-source-a-fast-model-for-ai-workflows/
6. Google Gemini Enterprise long-running agents and Inbox — X: https://x.com/googlecloud/status/2061105927692919271; verification: https://cloud.google.com/blog/products/ai-machine-learning/whats-new-in-gemini-enterprise
7. NVIDIA Cosmos 3 open physical-AI world model — X: https://x.com/NVIDIAAI/status/2061310183335473418; verification: https://developer.nvidia.com/blog/develop-physical-ai-reasoning-world-and-action-models-with-nvidia-cosmos-3/
8. Runway joins Cosmos Coalition — X: https://x.com/runwayml/status/2061315089869721682; verification: https://runwayml.com/news/introducing-cosmos-coalition
9. Runway London world-model hub — X: https://x.com/runwayml/status/2061450141614145621; verification: https://runwayml.com/news/runway-opens-london-hq
10. Robinhood agentic trading surface — X: https://x.com/RobinhoodApp/status/2061492908394451098; verification: https://robinhood.com/us/en/support/articles/agentic-trading-overview/

Dedupe notes: same-day local Signal notes were empty at scan time. session_search showed prior June 1 coverage for Gemini Enterprise/Cosmos, so final wording keeps those concise and prioritizes fresh Anthropic/Vercel/Databricks/JetBrains/Runway/Robinhood signals.

Backfill status: completed; signal_reports_db_backfill.py returned ok true with total_artifacts=1829, created=3, updated=1826, failed=0.


## Follow-up scan — 2026-06-02 02:17:00 +07

Method: `xurl --app jet-x whoami` succeeded, but all tested per-account searches returned JSON `CreditsDepleted`; used Nitter RSS curated accounts and official/credible verification. Same-day note already contained the 00:10 source-grounded digest, so this follow-up prioritized incremental X-sourced items and retained only high-value repeats where useful for a 10-item simple alert.

Incremental / refreshed source-grounded signals:
- AWS + Poolside private frontier AI inside customer AWS accounts — X: https://x.com/awscloud/status/2061523521331671423 and https://x.com/awscloud/status/2061523523403669560; verification/context: https://aws.amazon.com/isv/
- Vercel Blob OIDC short-lived project-scoped tokens — X: https://x.com/vercel_dev/status/2061516371499123016; verification: https://vercel.com/changelog/vercel-blob-now-supports-oidc-authentication
- xAI Composer 2.5 in Grok Build — X: https://x.com/xai/status/2061510464325206163; verification/context: https://docs.x.ai/llms.txt
- Perplexity Search as Code / Agent API sandbox — X: https://x.com/perplexity_ai/status/2061506376741134845; verification: https://docs.perplexity.ai/docs/agent-api/tools/sandbox
- Alibaba Qwen3.7-Plus multimodal/browser-agent thread — X: https://x.com/Alibaba_Qwen/status/2061506644367069392; verification/context: https://www.alibabacloud.com/blog/qwen3-7-the-agent-frontier_603154
- NVIDIA Cosmos 3 leaderboard amplification remains current but was already covered in the 00:10 note; final wording should avoid exact duplicate framing.

Backfill status: completed for this follow-up section; signal_reports_db_backfill.py returned ok true with total_artifacts=1830, created=1, updated=1829, failed=0.
