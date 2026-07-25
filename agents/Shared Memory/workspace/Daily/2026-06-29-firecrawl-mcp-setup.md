# Firecrawl MCP setup — 2026-06-29

- Kelly configured Firecrawl for Hermes default profile without storing the key in notes.
- Added `FIRECRAWL_API_KEY` to `~/.hermes/.env` (value redacted here).
- Added MCP server `firecrawl` to `~/.hermes/config.yaml` using `npx -y firecrawl-mcp` with env reference `${FIRECRAWL_API_KEY}`.
- Verified `hermes mcp test firecrawl`: connected in ~1.4s, 26 tools discovered (`firecrawl_search`, `firecrawl_scrape`, `firecrawl_crawl`, `firecrawl_extract`, monitors, research tools, etc.).
- Verified new CLI session web tools: `hermes chat ... --toolsets web` returned `SEARCH_OK 2`.
- Verified new CLI session MCP tools: `hermes chat ... --toolsets firecrawl` returned `FIRECRAWL_MCP_OK 2`.
- Current Telegram gateway process still needs restart/reload to inherit `.env`; avoid restarting mid-conversation unless Jet approves because gateway restart drops active session context.
