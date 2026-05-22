# Qwen3.7-Max tooling review — 2026-05-22 20:29

- Reviewed Jet's screenshot of Alibaba Qwen announcement.
- Existing tooling already has local Qwen profile (`qwen3.6:35b` via Ollama) and Nous-hosted Qwen 3.6 custom providers across profiles.
- No `DASHSCOPE_API_KEY`/Alibaba Model Studio key is currently configured; direct Qwen3.7-Max integration would require adding a DashScope/Alibaba custom provider and choosing exact model ID from Alibaba Model Studio.
- Best fit: Qwen profile/local-worker upgrade path, long-horizon tool workflows, MCP/productivity assistant, and optional cheaper non-critical cron routing after smoke tests.
