# Social Posting System Research — Jet

Created: 2026-04-24

## Goal

Create an approval-based social posting system where Kelly/Hermes drafts posts, Jet approves in the workspace/dashboard, then the system posts or schedules to LinkedIn and X/Twitter.

## Recommendation

Use **Blotato API as the primary posting layer**.

Reasons:
- One API can post to multiple platforms, including Twitter/X and LinkedIn.
- Handles connected social accounts through Blotato.
- Supports immediate publishing and scheduled publishing.
- Supports Twitter/X threads through `content.additionalPosts[]`.
- Supports LinkedIn personal profile and LinkedIn Company Page targets.
- Avoids fragile browser automation and most platform anti-bot/login/2FA issues.

Use browser automation only as a fallback/manual emergency path.

## Blotato API findings

Docs: https://help.blotato.com/api/llm

REST API:
- Base URL: `https://backend.blotato.com/v2`
- Auth header: `blotato-api-key: [REDACTED]
- Content-Type: `application/json`

Important endpoints:
- `GET /users/me` — verify API key
- `GET /users/me/accounts` — list connected social accounts and get `accountId`
- `GET /users/me/accounts/:accountId/subaccounts` — get LinkedIn/Facebook page IDs
- `POST /posts` — create/publish/schedule post
- `GET /posts/:postSubmissionId` — poll status
- `GET /schedules` — list scheduled posts
- `PATCH /schedules/:id` — update a scheduled post
- `DELETE /schedules/:id` — cancel scheduled post
- `POST /media/uploads` — upload local media via presigned URL

Publishing rules:
- `content.platform` and `target.targetType` must match.
- `mediaUrls` is required; pass `[]` for text-only posts.
- If neither `scheduledTime` nor `useNextFreeSlot` is provided, the post publishes immediately.
- `scheduledTime` and `useNextFreeSlot` must be top-level fields, siblings of `post`, not nested inside `post`.

Twitter/X payload shape:
```json
{
  "post": {
    "accountId": "ACCOUNT_ID",
    "content": {
      "text": "Hello world",
      "mediaUrls": [],
      "platform": "twitter"
    },
    "target": { "targetType": "twitter" }
  },
  "scheduledTime": "2026-04-25T02:00:00Z"
}
```

Twitter/X thread support:
```json
{
  "post": {
    "accountId": "ACCOUNT_ID",
    "content": {
      "text": "First tweet",
      "mediaUrls": [],
      "platform": "twitter",
      "additionalPosts": [
        { "text": "Second tweet", "mediaUrls": [] },
        { "text": "Third tweet", "mediaUrls": [] }
      ]
    },
    "target": { "targetType": "twitter" }
  }
}
```

LinkedIn target:
- For LinkedIn personal profile: `target: { "targetType": "linkedin" }`
- For LinkedIn Company Page: include `target.pageId` from `GET /users/me/accounts/:accountId/subaccounts`
- LinkedIn carousel: more than one image URL in `content.mediaUrls`, image-only, max 10.

Rate limits:
- `POST /posts`: 30 requests/minute
- `GET /posts/:id`: 60 requests/minute
- `GET /users/me/accounts`: no stated limit

## X/Twitter direct route

Could also use `xurl`, the official X API CLI, for direct X posting.

Status on this machine: `xurl` is **not installed**.

Direct X posting would require:
1. Install `xurl`
2. Jet creates/configures an X Developer app
3. Jet runs OAuth locally; I should not handle/paste secrets
4. Then I can post via `xurl post`, upload media, create threads, etc.

Recommendation: use Blotato first. Add direct X later only if needed.

## LinkedIn direct route

Direct LinkedIn API posting is possible but usually more annoying because of LinkedIn app permissions, approval, organization/person URNs, and platform restrictions.

Recommendation: use Blotato for LinkedIn rather than building direct LinkedIn API integration from scratch.

## Browser automation route

Possible but not preferred.

Pros:
- Can use existing logged-in desktop browser/session.
- Can work even if API access is incomplete.

Cons:
- Brittle UI selectors.
- Login/2FA/session expiry problems.
- Anti-bot/rate-limit risk.
- Harder to verify post success cleanly.
- More dangerous if automation clicks wrong thing.

Use as fallback only.

## Proposed approval workflow

### Storage
Use existing workspace:
- Notion for canonical content archive/review if desired.
- Obsidian clone for shared agent memory.
- Mission Control dashboard as the approval cockpit.

Create a local/social queue with fields:
- `id`
- `title`
- `platforms`: `twitter`, `linkedin`
- `target_account_ids`
- `content_text`
- `thread_posts` optional
- `media_urls`
- `status`: `draft`, `ready_for_review`, `approved`, `scheduled`, `published`, `failed`, `rejected`
- `scheduled_time`
- `created_from`: Notion page / research sweep / manual request
- `approval_timestamp`
- `published_urls`
- `error_message`

### Dashboard UX
Add a new dashboard section: **Social Queue**

Tabs:
- Drafts
- Ready for Review
- Approved / Scheduled
- Published
- Failed

Actions:
- Approve
- Reject
- Edit text
- Schedule next slot
- Post now
- Open source Notion/Obsidian note
- View published URL

### Automation behavior
- Content engine generates proposed posts.
- Posts enter `ready_for_review`, never auto-publish.
- Jet approves in dashboard.
- Posting job picks up only `approved` items.
- Posting job sends to Blotato `/posts` with either `scheduledTime` or `useNextFreeSlot`.
- Job polls `/posts/:postSubmissionId` until `published` or `failed`.
- Dashboard updates with public URLs / errors.

## What I need from Jet

1. **Blotato API key**
   - Best storage: put it in `~/.config/blotato/api_key` on this machine, or tell me where it is already stored.
   - Do not paste publicly if avoidable.

2. **Connected accounts in Blotato**
   - Connect X/Twitter account `@jeditrinupab`.
   - Connect LinkedIn account.
   - If posting to LinkedIn company page, connect/select the company page too.

3. **Posting targets**
   - X personal account: yes/no.
   - LinkedIn personal profile: yes/no.
   - LinkedIn company page: yes/no and which page.

4. **Approval rule**
   - Recommended: never post unless status is `approved`.
   - Decide if dashboard approval is enough, or if Telegram confirmation is also required.

5. **Posting cadence**
   - Suggested start:
     - X: 2–4 posts/day, optionally 1 thread/day
     - LinkedIn: 1 post/day
   - Or use Blotato next available slots.

6. **Brand voice rules**
   - Thai/English mix.
   - Topics to push: AI for business owners, operator leverage, AI workflows, founder OS, Limitless training, Claude/OpenClaw, revenue/productivity.
   - Topics to avoid.

## Build phases

### Phase 1 — Safe MVP
- Store Blotato key locally.
- Verify `GET /users/me` and `GET /users/me/accounts`.
- Build Social Queue local JSON + Obsidian log.
- Add Social Queue section to Mission Control.
- Add approve/reject/post-now actions.
- Post one test draft to X or LinkedIn after explicit approval.

### Phase 2 — Scheduling
- Add schedule slots / next available slot support.
- Add daily content generation → social queue.
- Add published URL/error tracking.

### Phase 3 — Growth machine
- Pull best research/content from Notion/Obsidian.
- Generate daily X/LinkedIn variants.
- Score by hook strength, founder relevance, clarity.
- Queue best posts for Jet approval.
- Track performance manually or via available APIs.
