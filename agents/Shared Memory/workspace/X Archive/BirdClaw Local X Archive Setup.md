# BirdClaw Local X Archive Setup

Date: 2026-05-06
Owner: Jet / Kelly

## Goal
Create a local archive of Jet's X/Twitter posts and eventually make it searchable for Hermes agents.

## Installed
- Node upgraded via Homebrew to meet BirdClaw requirement.
- BirdClaw installed globally via npm at `~/.npm-global/bin/birdclaw`.
- BirdClaw version: `0.3.0`.
- Local storage initialized at `~/.birdclaw/`.
- SQLite DB path: `~/.birdclaw/birdclaw.sqlite`.

## Current status
- BirdClaw local mode is initialized.
- `xurl` is not installed/authenticated yet.
- `bird` is not installed/authenticated yet.
- Search did not find an existing Twitter/X archive zip in common local folders (`Downloads`, `Desktop`, `Documents`, iCloud Documents).

## Recommended import path for a complete archive
The most complete source for "all posts" is the official X/Twitter data archive zip.

User path:
1. X.com → Settings and privacy → Your account → Download an archive of your data.
2. Wait for X to prepare the archive.
3. Download the `.zip` to `~/Downloads/`.
4. Tell Kelly: "Import my X archive now."

Kelly import command:
```bash
export PATH="$HOME/.npm-global/bin:$PATH"
export BIRDCLAW_DISABLE_LIVE_WRITES=1
birdclaw archive find --json
birdclaw import archive ~/Downloads/<twitter-archive-file>.zip --json
birdclaw db stats --json
```

## Safety
- Start read-only/local-first.
- Keep `BIRDCLAW_DISABLE_LIVE_WRITES=1` for import/testing.
- Do not enable posting, replying, DMs, blocks, or mutes until Jet explicitly approves.
- Do not print or inspect X auth token files.

## Future options
- Install/authenticate `xurl` for live X API reads/writes if Jet wants ongoing sync.
- Install/authenticate `bird` for cookie-backed live sync if useful.
- Add a read-only Hermes skill/wrapper so Signal/Blaze/Kelly can search Jet's archived posts for content and relationship intelligence.
