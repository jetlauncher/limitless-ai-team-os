# Fire — Handle Availability Audit

Checked: 2026-05-01 Bangkok time

Candidates checked:
- `firebyjet`
- `buildwithfire`
- `fireosai`
- `getfireai`
- `fireoperator`

## Recommendation

Best reserve-first handle: **`@firebyjet`**

Why:
- Available / not found on X, Instagram, TikTok, YouTube, LinkedIn, Substack, GitHub, Pinterest based on direct checks.
- Brand is clear and ownable: Fire by Jet.
- Caveat: Telegram `@firebyjet` appears taken/claimable by an existing t.me contact page.

Backup: **`@getfireai`**

Why:
- Available / not found on X, Instagram, TikTok, YouTube, Substack, GitHub, Pinterest.
- More SaaS/product-like than founder-led.
- Telegram appears taken/claimable by an existing t.me contact page.

Avoid as primary:
- `@buildwithfire` — X and GitHub are taken.
- `@fireosai` — YouTube is taken by “Fire Osai”; LinkedIn uncertain.
- `@fireoperator` — X, YouTube, Telegram appear taken.

## Platform results

Legend:
- ✅ likely available / not found
- ❌ taken / existing profile found
- ⚠️ uncertain / blocked / needs in-app check

| Handle | X | Instagram | Threads | TikTok | YouTube | LinkedIn | Facebook | Substack | GitHub | Telegram | Pinterest | Medium |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `firebyjet` | ✅ | ✅ | ✅ likely via IG | ✅ | ✅ | ✅ | ⚠️ | ✅ | ✅ | ❌ | ✅ | ⚠️ |
| `buildwithfire` | ❌ | ✅ | ✅ likely via IG | ✅ | ✅ | ✅ | ⚠️ | ✅ | ❌ | ❌ | ✅ | ⚠️ |
| `fireosai` | ✅ | ✅ | ✅ likely via IG | ✅ | ❌ | ⚠️ | ⚠️ | ✅ | ✅ | ❌ | ✅ | ⚠️ |
| `getfireai` | ✅ | ✅ | ✅ likely via IG | ✅ | ✅ | ⚠️ | ⚠️ | ✅ | ✅ | ❌ | ✅ | ⚠️ |
| `fireoperator` | ❌ | ✅ | ✅ likely via IG | ✅ | ❌ | ⚠️ | ⚠️ | ✅ | ✅ | ❌ | ✅ | ⚠️ |

## Evidence notes

### X / Twitter
Used Jina reader fallback on X public pages.
- `firebyjet`: “This account doesn’t exist.” ✅
- `buildwithfire`: existing profile “BuildwithFIRE (@BuildwithFIRE)” ❌
- `fireosai`: “This account doesn’t exist.” ✅
- `getfireai`: “This account doesn’t exist.” ✅
- `fireoperator`: existing profile “Sloan (@fireoperator)” ❌

### Instagram
Browser verification for `firebyjet` showed title: “Profile isn't available • Instagram.” Direct checks for the other candidates returned the same not-found pattern. ✅

### Threads
Threads redirects to login/authwall, but because Threads handles are tied to Instagram handles, Instagram availability makes these likely available. Needs final in-app reservation. ⚠️/✅ likely

### TikTok
Browser verification for `firebyjet` showed: “Couldn’t find this account.” Direct checks for other candidates showed not-found patterns. ✅

### YouTube
Jina/direct checks:
- `firebyjet`: 404 ✅
- `buildwithfire`: 404 ✅
- `fireosai`: existing channel “Fire Osai” ❌
- `getfireai`: 404 ✅
- `fireoperator`: existing channel “barrom @fireoperator” ❌

### Telegram
`t.me/firebyjet` showed “If you have Telegram, you can contact @firebyjet right away,” which indicates the username exists/is claimed. Same pattern appeared for most candidate handles; `fireoperator` explicitly shows “View @fireoperator.” Treat as taken unless checked inside Telegram username flow. ❌

### LinkedIn / Facebook / Medium
- LinkedIn returned clear 404 for `firebyjet` and `buildwithfire`, but 999/blocked for several others.
- Facebook returned generic 400/error pages, so availability cannot be confirmed via direct public checks.
- Medium Cloudflare-blocked checks; do not rely on result.

## Next action

Reserve `@firebyjet` immediately on:
1. X
2. Instagram
3. TikTok
4. YouTube
5. LinkedIn page/custom URL if available
6. Substack if needed
7. GitHub if this becomes product/code-facing

Use `@getfireai` as backup for any platform where `@firebyjet` fails during in-app signup.
