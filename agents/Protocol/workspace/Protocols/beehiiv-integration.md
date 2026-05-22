# Beehiiv Integration Protocol

## Status
Pending Jet-created Beehiiv API key/token.

## Credential path
Expected path:

```text
~/.config/beehiiv/api_key
```

Never print the key. Never save it in Obsidian.

## Initial automation target
Phase 1: generate Beehiiv-ready markdown drafts only.
Phase 2: create Beehiiv drafts via API, but do not publish.
Phase 3: schedule/publish only after Jet explicitly approves the exact issue.

## Needed from Jet
- Beehiiv API key/token
- Publication ID, if Beehiiv requires it for API calls
- Confirmation of sender/from-name and default CTA

## Approval rule
Draft creation is okay after setup.
Publishing/scheduling requires explicit Jet approval every time until Jet says otherwise.
