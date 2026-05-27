# Tiff agent Telegram setup — 2026-05-26

- Renamed/created Jet's private-life/family/team coordination profile as `tiff`.
- Configured alias `tiff`, model `gpt-5.5` via `openai-codex`, and shared Codex auth symlink without exposing secrets.
- Wrote `~/.hermes/profiles/tiff/SOUL.md` and `Agents/Tiff/README.md`.
- Configured dedicated Telegram bot in `~/.hermes/profiles/tiff/.env` with token omitted from notes.
- Started persistent gateway service `ai.hermes.gateway-tiff`.
- Verified gateway log: connected to Telegram polling mode and running with 1 platform.
- Verified smoke test: `TIFF_PROFILE_OK`.
- Sent readiness ping to Jet via the Tiff bot.
- LINE remains pending: current Hermes gateway install has no native LINE platform adapter, so next step is a LINE Messaging API webhook bridge or a native adapter.
