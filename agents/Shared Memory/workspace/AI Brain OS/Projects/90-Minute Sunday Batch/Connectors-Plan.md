# Connectors Plan — Saved X Posts + YouTube Watch History

**Created:** 2026-06-28  
**Project:** Sunday Content Engine / 90-Minute Sunday Batch

## 1. Saved X posts via Readwise

### Verdict
Yes — best path is to integrate **Readwise / Readwise Reader** as the normalized source layer for saved X/Twitter items.

**Wiring status — 2026-06-28:** Connected. Hermes default profile now has MCP server `readwise` configured at `https://mcp2.readwise.io/mcp`; OAuth token is stored locally at `~/.config/readwise/mcp_oauth.json` and exposed to Hermes via `READWISE_MCP_TOKEN` in `~/.hermes/.env`. Do not copy token values into notes.

Verified with:
- `hermes mcp test readwise` → connected, 22 tools discovered.
- Hermes smoke test → `reader_list_documents` returned 3 documents.

### Why Readwise is the right layer
- It avoids brittle X browser scraping and bookmark UI limitations.
- It can provide clean URLs, titles/text/highlights/tags/updated timestamps through API export/list endpoints.
- It lets Jet keep using a personal capture workflow while Kelly consumes a stable API source.

### Required setup
- Current setup uses Readwise OAuth MCP token at `~/.config/readwise/mcp_oauth.json` plus `READWISE_MCP_TOKEN` in `~/.hermes/.env`.
- Do **not** store the token in Shared Memory or project files.
- Confirm whether Jet's X saves are already flowing into Readwise/Reader, or whether a capture rule is needed.

### Connector output format
Write normalized source records to:

`Shared Memory/AI Brain OS/Projects/90-Minute Sunday Batch/Sources/readwise-x-saves/YYYY-MM-DD.jsonl`

Each record:

```json
{
  "source": "readwise",
  "source_type": "x_saved_post",
  "captured_at": "ISO timestamp",
  "updated_at": "ISO timestamp from Readwise if available",
  "title": "...",
  "url": "https://x.com/...",
  "author": "... if available",
  "text": "post/article/highlight text if available",
  "tags": ["..."],
  "highlights": ["..."],
  "content_use": ["hook inspiration", "format pattern", "market signal"]
}
```

### Sunday Engine use
- Use Readwise X saves as the **taste and pattern layer**, not as factual news unless the linked source is verified.
- Label these items as `Saved X / Readwise` in the output table.
- For viral/claim-heavy posts, verify claims separately before turning into facts.

## 2. YouTube watched history via Google auth/API

### Verdict
Google OAuth is available locally for several Google services, but **the normal YouTube Data API does not expose a user's full watch history as a public endpoint**.

Current local token check:
- `~/.hermes/google-accounts/youtube-upload/google_token.json` exists but only has `youtube.upload` scope.
- `~/.hermes/google-accounts/jeditrinupab-gmail/google_token.json` has Gmail/Drive/Sheets/Calendar/Contacts/Docs scopes, not YouTube watch-history scope.

Even with broader OAuth, the YouTube Data API supports things like uploads, playlists, subscriptions, liked videos, and channel resources — not a direct watch-history feed equivalent to what the YouTube app UI shows.

### Best practical alternatives

#### A. Google Takeout / My Activity export — best reliable source
Use Google Takeout / My Activity export for YouTube watch history and import the JSON/HTML into the Sunday Engine.

Target normalized path:

`Shared Memory/AI Brain OS/Projects/90-Minute Sunday Batch/Sources/youtube-watch-history/YYYY-MM-DD.jsonl`

#### B. Browser history approximation — useful but incomplete
Read local browser history for visited YouTube URLs. This can infer watched/opened videos but misses mobile app viewing and may include videos opened but not watched.

#### C. YouTube API partial signals
Use API/OAuth for:
- own uploads
- public/private playlists if accessible
- liked videos playlist if available
- subscriptions and channel metadata

But do not label those as full watch history.

## Recommended integration architecture

1. **Readwise X Saves connector** — daily or Sunday pull; stable API; high value.
2. **YouTube Takeout/My Activity importer** — manual/export-driven at first; reliable for true watch history.
3. **Browser history fallback** — optional local-only proxy for desktop YouTube viewing.
4. **YouTube API connector** — use for uploads/playlists/subscriptions, not watch history.

## Next implementation steps

1. Build `readwise_x_saves_to_sunday_engine.py` using MCP tools `reader_list_documents`, `reader_search_documents`, and/or `reader_export_documents`.
2. Confirm the Readwise/Reader query or tag that represents Jet's saved X posts.
3. Ask Jet to export YouTube History from Google Takeout/My Activity, then place it in a watched folder.
4. Build `youtube_takeout_history_to_sunday_engine.py`.
5. Update Sunday Engine Inputs page to include `Readwise X Saves` and `YouTube Takeout History` as first-class sources.
