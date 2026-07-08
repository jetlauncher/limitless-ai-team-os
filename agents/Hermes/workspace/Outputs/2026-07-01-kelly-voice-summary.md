# Kelly Voice — Full Build Summary (2026-07-01)

Combined overview of everything built today across both Kelly Voice systems: the **Twilio/ElevenLabs phone line** and the **Nova desktop companion** (Electron app). Repo: `github.com/jetlauncher/Kelly-Voice` (private).

---

## 1. Phone line — Twilio → ElevenLabs → Hermes

**How to call:** Dial the number in `~/clawd/.env` (`TWILIO_PHONE_NUMBER`) — Kelly answers.

**Architecture**

```
Caller → Twilio → ElevenLabs Conversational AI Agent
                       ↓ custom LLM
              /fast-llm/v1 chat-completions proxy
                       ├─ simple conversation → OpenAI gpt-4o-mini (instant)
                       └─ work request → instant ACK + detached Hermes CLI worker
                                                ↓
                                      Hermes tools / skills / memory
                                                ↓
                                      Telegram completion update
```

**Key product decision:** hybrid router, not one-size-fits-all. Full Hermes on every phone turn was too slow for natural voice (~4-6s). A single fast LLM alone couldn't do real work. The fix: instant spoken acknowledgement from a fast model, then full Hermes executes the actual task asynchronously and reports back on Telegram.

**Status:** Live and working. Agent ID `agent_7401ktat1stjfp7vbrgfz9d8vb5w`, phone registered via ElevenLabs, LaunchAgent `com.limitless.elevenlabs-fast-llm` running on port 8790, public via Tailscale Funnel at `https://ultras-mac-studio.tail3b403f.ts.net/fast-llm/v1`.

---

## 2. Desktop companion — Nova (Electron app)

A standalone desktop app: an animated gold orb face that listens, thinks, and speaks via OpenAI Realtime (`gpt-realtime-2`), with a computer-use mode that lets Nova drive the Mac directly.

### What was built in Phase 1 (initial build)
- Frameless, translucent, always-on-top 360×360 window (dark navy + gold theme)
- Animated orb face: idle/listening/thinking/speaking states + natural blinking
- Real microphone capture (24kHz PCM16, matches OpenAI Realtime's native rate)
- Real gapless streaming audio playback
- Interruption handling (user talking over Nova cuts her off cleanly)
- Computer-use mode: Nova can drive the Mac via 16 tools (`cua-driver` bridge) — click, type, browse, launch apps — gated off by default, narrates actions before taking them
- Compact 120×120 "dock" mode when computer-use is active

### What was finished today (this session)
| Area | Before | After |
|---|---|---|
| Settings | Gear button was a no-op stub | Real panel: connection status, endpoint, live scrollable transcript, clear button |
| Reconnect | Fixed 2-second retry forever | Exponential backoff (1s → 2s → 4s → 8s → 15s cap, resets on success) |
| Reliability | Messages silently dropped if disconnected | Bounded queue (300 messages), flushed in order once reconnected |
| Transcript | Received from backend but never shown | Backend now extracts real conversation text; UI renders it live |
| Packaging | Only ran via `npm run dev` (needed a dev server) | Real double-clickable `Nova.app` via electron-builder — verified: packaged, launched, full process tree confirmed alive |
| Auto-launch | None | One-command enable/disable scripts + LaunchAgent for open-at-login |

**Verification performed:** `npm run typecheck` clean, `npm run build` clean, `npm run package` produced a working `Nova.app` — launched it directly and confirmed the full Electron process tree (main + GPU + renderer + network utility processes) spawned and stayed alive with no crashes, then quit cleanly.

**Known remaining gaps (non-blocking):**
- No error toast/banner in the UI (errors just log to console — rare, and reconnect recovers automatically)
- No preference UI yet for voice/mic-device selection
- Not code-signed/notarized — macOS Gatekeeper will show a one-time warning on a moved/downloaded copy (right-click → Open bypasses it); would need an Apple Developer ID certificate to remove this if ever shipped publicly

### How to run it
```bash
cd ~/Projects/nova-companion
npm install
npm run dev          # hot-reload dev mode
npm run package       # produces release/mac-arm64/Nova.app — double-click to launch
./scripts/enable-autolaunch.sh   # optional: open automatically at login
```

---

## Repo

Everything above is committed and pushed to the private repo:

**`github.com/jetlauncher/Kelly-Voice`**

Structure: `voice-server/` (the shared OpenAI Realtime backend + Twilio bridge + Nova WebSocket endpoint), `companion/` (the Nova Electron desktop app). No secrets or API keys are committed — all credentials are read from local env vars / config files at runtime.
