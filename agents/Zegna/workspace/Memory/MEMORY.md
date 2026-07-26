# Zegna Memory

Durable human-readable memory for Zegna. Do not store secrets here.

## Operating notes
- Recurring curation refresh: run `/Users/ultrafriday/zegna-curations/update_curations.py`, verify `/Users/ultrafriday/zegna-curations/index.html`, archive each run to Notion target `3581290f50f44b7dbc8b93879ca31916` (database as of 2026-06-16).

## Scheduled scout notes
- Jet taste anchors for daily scouts: Kamakura Shirts, Ring Jacket, Saint Laurent/Dior/Goyard/Golden Goose, occasional Prada, Brunello Cucinelli as aspirational value-watch; include complete-look references where possible.
- If `productivity/notion` skill is missing but a Notion archive is explicitly required, clearly warn user, then use the Notion API directly with the configured env token or `~/.config/notion/api_key`; never print secrets. Target `3581290f50f44b7dbc8b93879ca31916` resolves as a database with title property `Name`.

- Jet taste anchors: Kamakura Shirts, Ring Jacket, Saint Laurent, Dior, Goyard, Golden Goose, occasional Prada, Brunello Cucinelli as aspirational/value-watch; prefers complete looks/outfit references.

## Durable taste context
- Jet taste anchors for scouts: Kamakura Shirts/Ring Jacket, Saint Laurent/Dior/Goyard/Golden Goose, occasional Prada, Brunello Cucinelli value-watch; likes complete looks and quiet luxury/Japanese-European minimal/tactical-refined utility.

- Jet taste anchors: Kamakura Shirts, Ring Jacket, Saint Laurent, Dior, Goyard, Golden Goose shoes; occasional Prada; Brunello Cucinelli as aspirational/value-watch. Daily scouts should stay phone-readable and bias quiet luxury/Japanese-European minimal/tactical-refined.

- Jet daily scout should mention if Notion skill unavailable; use direct source/RSS fallback when Firecrawl web_search is not configured.

- Daily scout archive target confirmed as Notion database `3581290f50f44b7dbc8b93879ca31916`; use Type `Daily Scout`, Status `Done`, Agent `Zegna`.

## Durable workflow notes
- Jet daily scout target: archive Zegna curation outputs to Notion database 3581290f50f44b7dbc8b93879ca31916 (Work Output by Friday team) with Agent=Zegna, Type=Daily Scout, Status=Done.

- Jet taste anchors for daily scout: Kamakura Shirts, Ring Jacket tailoring, Saint Laurent/Dior/Goyard/Golden Goose, occasional Prada, Brunello Cucinelli as aspirational/value-watch; likes complete looks and quiet luxury/Japanese-European minimal/tactical-refined references.

- 2026-05-19: Blogwatcher feeds tracked for daily scouts include Acquire, Design Milk, Dezeen, Highsnobiety, Hypebeast, The Verge, Uncrate. Some feeds may fail: Acquire/Uncrate 403, Highsnobiety 404.

- 2026-05-20: Daily scout uses blogwatcher-cli feeds. Notion skill was unavailable in scheduled run; archive skipped. Feed issues observed: Acquire 403, Highsnobiety 404, Uncrate 403.

- 2026-05-21 taste signal: Jet’s scout performed well around heritage utility (Levi’s archive denim), refined workspace adaptability (Vitra/Hem), discreet AI eyewear, and Kengo Kuma warm timber architecture references. Notion skill unavailable in this run, so archive was not posted to Notion.
## Local curation landing page
- Local project: `/Users/ultrafriday/zegna-curations/`; refresh command: `/usr/bin/python3 /Users/ultrafriday/zegna-curations/update_curations.py`; output landing page: `/Users/ultrafriday/zegna-curations/index.html`.
- Scheduled archive target for refresh runs: Notion ID `3581290f50f44b7dbc8b93879ca31916` (determined 2026-05-22 as a database). Use Notion API token from env or `~/.config/notion/api_key`; do not store token.
- 2026-05-23: `update_curations.py` now has resilient fallback for live source failures: if Kamakura/Ring refresh errors, it reuses cached items from `curations.json`, rebuilds `index.html`, stores warnings in `curations.json`, and exits successfully when cache exists.


## Taste anchors
- Jet taste anchors confirmed in recurring scout: Kamakura Shirts/Ring Jacket tailoring, Saint Laurent/Dior/Goyard/Golden Goose, quiet luxury with Japanese-European minimal and tactical-refined utility.
