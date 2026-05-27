# Personal agent setup — 2026-05-26

- Created lightweight Hermes profile `personal` with alias `personal`; configured GPT-5.5/OpenAI-Codex and symlinked shared auth without exposing secrets.
- Wrote privacy-first `SOUL.md` at `~/.hermes/profiles/personal/SOUL.md` and Obsidian README at `Agents/Personal/README.md`.
- Verified `personal chat` smoke test: `PERSONAL_PROFILE_OK`.
- Gateway remains stopped until a dedicated Telegram BotFather token and LINE bridge/adapter are approved.
- Initial `--clone-all` failed because `.hermes/exports` contains large media and disk was near full; partial profile was removed and recreated lightweight.
- Current blocker: native LINE gateway adapter is not present in this Hermes install. Next step is either a LINE Messaging API webhook bridge or adding a native platform adapter.
