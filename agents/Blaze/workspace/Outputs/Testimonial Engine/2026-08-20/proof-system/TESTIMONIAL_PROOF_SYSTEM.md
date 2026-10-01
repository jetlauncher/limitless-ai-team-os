# Limitless Club Testimonial Proof System

**Purpose:** Convert verified customer-review transcripts into traceable, direct-response proof without inventing, strengthening, or decontextualizing customer claims.

**Audience/market:** Thai-first premium founder and AI education. Keep the customer’s actual language. English translations are discovery aids unless separately reviewed; they are never the canonical quote.

## 1. Non-negotiable evidence rules

1. **The source clip is the authority.** Every quote, paraphrase, subtitle, and ad asset must resolve to a source video, transcript version, and exact time range.
2. **Verbatim means verbatim.** Preserve Thai wording, qualifiers, uncertainty, slang, and material pauses. Remove filler only in an explicitly labeled `edited_quote`, never in `verbatim_quote`.
3. **One proof unit, one atomic claim.** Split a segment when it contains multiple outcomes, mechanisms, objections, or time periods.
4. **Do not upgrade the claim.** “รู้สึกว่าทำงานเร็วขึ้น” cannot become “ทำงานเร็วขึ้น 2 เท่า.” A customer’s estimate stays an estimate.
5. **Context travels with the quote.** Store the preceding/following transcript and all conditions needed to interpret the statement honestly.
6. **No causal rewrite.** A before/after sequence is not automatically proof that Limitless Club caused the result. Causality must be explicit in the customer’s words.
7. **No implied typicality.** Exceptional outcomes need an atypical-result flag and appropriate disclaimer review.
8. **Permission is a gate, not a score.** No asset becomes publishable until consent, identity-display rights, channel/territory, and expiry are confirmed.
9. **Translations never replace source text.** Thai transcript + video remain canonical. Back-translate high-value quotes before public use.
10. **Human review before publishing.** Mechanical extraction may create candidates; a reviewer approves quote accuracy, context, permissions, and claims risk.

## 2. Mining taxonomy

### 2.1 Customer context (`persona_*`)
Use only facts stated in the transcript or verified customer metadata.

- Role: founder / owner / executive / manager / operator / creator / professional / employee / student / other / unknown
- Business stage: idea / early / operating / scaling / established / unknown
- Team size: solo / 2–5 / 6–20 / 21–50 / 51+ / unknown
- AI starting level: none / beginner / intermediate / advanced / unknown
- Industry: controlled list plus `other`
- Use-case family: strategy, marketing, sales, operations, automation, content, product, leadership, personal productivity, other
- Purchase context: self-funded / company-funded / gift / scholarship / unknown

### 2.2 Voice-of-customer problem taxonomy (`problem_codes`)
Multi-select; preserve the customer’s words separately.

- `P_TIME`: too slow / manual workload / no time
- `P_CONFUSION`: overwhelmed by AI/tools/information
- `P_NO_SYSTEM`: isolated tactics without a repeatable workflow
- `P_EXECUTION`: knows what to do but cannot implement
- `P_SKILL_GAP`: lacks practical AI/business skill
- `P_CONFIDENCE`: fear, hesitation, or low confidence
- `P_DIRECTION`: unclear priority, strategy, or next step
- `P_GROWTH`: stalled revenue, lead flow, or scaling
- `P_TEAM`: delegation, adoption, alignment, or training friction
- `P_CONTENT`: ideation, production, consistency, distribution
- `P_NETWORK`: isolation or lack of peers/mentors
- `P_ACCOUNTABILITY`: inconsistent action/follow-through
- `P_COST`: wasted spend or expensive alternatives
- `P_OTHER`: reviewer-specified

### 2.3 Trigger and buying-motivation taxonomy (`trigger_codes`)

- Urgent business problem
- Opportunity/FOMO around AI
- Recommendation/referral
- Trust in Jet/instructor
- Curriculum specificity
- Community/network
- Premium positioning
- Implementation support
- Prior failed alternative
- Event/content exposure
- Other / not stated

### 2.4 Objection taxonomy (`objection_codes`)
Capture both the objection and whether the quote actually resolves it.

- `O_PRICE`: expensive / ROI uncertainty
- `O_TIME`: no time to learn or implement
- `O_COMPLEXITY`: too technical / difficult
- `O_FIT`: not for my role, company, or level
- `O_SKEPTICISM`: distrust of course/AI/claims
- `O_TOO_EARLY_LATE`: timing concern
- `O_SUPPORT`: fear of being left alone
- `O_IMPLEMENTATION`: learning without execution
- `O_TOOL_CHANGE`: fear knowledge becomes outdated
- `O_COMMUNITY`: uncertainty about peer quality
- `O_APPROVAL`: partner/team/budget approval
- `O_OTHER`

`objection_resolution_strength`: none / implied / explicit / explicit-with-reason / explicit-with-result.

### 2.5 Proof type (`proof_types`)
One claim can have several types, but choose a primary.

1. **Quantified outcome** — a number, unit, baseline, and time window are present.
2. **Specific unquantified outcome** — concrete observable change without a number.
3. **Before/after transformation** — clear prior state and later state.
4. **Speed/time saved** — faster execution or shorter cycle.
5. **Revenue/cost/business outcome** — money, customers, sales, margin, spend, pipeline.
6. **Implementation proof** — what the customer built, shipped, changed, or now does.
7. **Skill/capability gain** — new ability demonstrated or described.
8. **Confidence/identity shift** — emotional or professional self-perception change.
9. **Curriculum/product proof** — specificity, quality, structure, recency, usability.
10. **Instructor/mentor proof** — teaching, feedback, expertise, trust.
11. **Community/network proof** — peers, introductions, support, collaboration.
12. **Support/accountability proof** — coaching, follow-up, momentum.
13. **Ease/accessibility proof** — beginner-friendly, understandable, practical.
14. **Objection reversal** — directly answers a buying concern.
15. **Comparison/alternative proof** — contrasts with prior course/tool/DIY attempt.
16. **Recommendation/endorsement** — explicit who it is for and why.
17. **Sensory/emotional reaction** — delight, surprise, relief; useful as hook/support, rarely core substantiation.

### 2.6 Outcome taxonomy (`outcome_codes`)

- `R_REVENUE`, `R_PROFIT`, `R_SALES`, `R_LEADS`, `R_CUSTOMERS`
- `R_COST_SAVED`, `R_TIME_SAVED`, `R_SPEED`, `R_OUTPUT_VOLUME`
- `R_CONVERSION`, `R_RETENTION`, `R_REACH`, `R_ENGAGEMENT`
- `R_AUTOMATION`, `R_WORKFLOW`, `R_CONTENT`, `R_PRODUCT_LAUNCH`
- `R_DECISION_QUALITY`, `R_STRATEGY_CLARITY`, `R_TEAM_ADOPTION`
- `R_SKILL`, `R_CONFIDENCE`, `R_ACCOUNTABILITY`, `R_NETWORK`
- `R_OTHER`, `R_NONE`

### 2.7 Mechanism taxonomy (`mechanism_codes`)
What the customer attributes the change to; do not infer.

- Framework/template/checklist
- Prompt/workflow/automation
- Live teaching/replay/module
- Coaching/feedback/Q&A
- Community/peer example/network
- Accountability/challenge/deadline
- Tool discovery/tool selection
- Mindset/decision framework
- Other / not stated

### 2.8 Claim specificity anatomy
For each claim, populate only what is said or verified:

- Before state
- Action/mechanism
- After state
- Metric + value + unit
- Comparison baseline
- Time to result
- Observation period
- Customer scope (self/team/company/client)
- Conditions/qualifiers
- Attribution language: direct / contributory / temporal only / none
- Recommendation target (“เหมาะกับ…”)

### 2.9 Creative utility tags

- Funnel stage: cold / problem-aware / solution-aware / product-aware / retargeting / close
- Ad job: stop scroll / establish relevance / explain mechanism / answer objection / prove outcome / de-risk / justify premium / close
- Emotional tone: surprise / relief / confidence / ambition / belonging / urgency / gratitude / authority / other
- Hook pattern: number-first / before-after / confession / skepticism-to-belief / “I thought…” / identity / unexpected detail / recommendation / other
- Visual quality: clean talking head / usable with crop / audio-led / B-roll required / unusable
- Delivery energy: high / medium / low

## 3. Data model and structured database fields

Use four linked tables. IDs must be immutable UUIDs or stable platform IDs.

### A. `source_videos` — one row per original review file

| Field | Type | Required | Notes |
|---|---|---:|---|
| `source_video_id` | UUID/string | yes | Stable primary key |
| `original_file_name` | text | yes | Never overwrite |
| `storage_uri` | text | yes | Controlled-access canonical file |
| `source_platform` | enum | yes | upload, Drive, Zoom, Line, etc. |
| `platform_asset_id` | text | no | External immutable ID |
| `file_sha256` | text | yes | Detect replacement/duplication |
| `duration_ms` | integer | yes | Exact media duration |
| `recorded_at` | datetime | no | Source metadata |
| `received_at` | datetime | yes | Ingestion audit |
| `language_primary` | BCP-47 | yes | Usually `th` |
| `customer_id` | string | yes | Pseudonymous internal link |
| `customer_display_name` | text | no | Only if approved |
| `consent_status` | enum | yes | unknown, requested, granted, restricted, revoked, expired |
| `consent_record_uri` | text | no | Signed form/message evidence |
| `allowed_channels` | array | no | Meta, TikTok, YouTube, landing page, organic, etc. |
| `allowed_territories` | array | no | If restricted |
| `allowed_edits` | array | no | crop, captions, translation, montage, paid ads |
| `identity_rights` | enum | yes | full, first-name, initials, anonymous, none |
| `consent_expires_at` | datetime | no | Null only if genuinely perpetual |
| `ingestion_status` | enum | yes | received, hashed, transcribed, reviewed, blocked |
| `created_at`, `updated_at` | datetime | yes | Audit fields |

### B. `transcript_segments` — canonical timestamped evidence

| Field | Type | Required | Notes |
|---|---|---:|---|
| `segment_id` | UUID/string | yes | Primary key |
| `source_video_id` | FK | yes | Parent source |
| `transcript_version` | text | yes | E.g. `asr-v1`, `human-v2` |
| `transcript_sha256` | text | yes | Locks the reviewed text version |
| `start_ms`, `end_ms` | integer | yes | Millisecond precision; `end_ms > start_ms` |
| `speaker_id` | text | yes | Distinguish customer/interviewer |
| `speaker_role` | enum | yes | customer, interviewer, other, unknown |
| `verbatim_text` | text | yes | Original-language evidence |
| `language` | BCP-47 | yes | Never infer from campaign language |
| `asr_confidence` | decimal 0–1 | no | Machine confidence, not truth score |
| `human_verified` | boolean | yes | Required for publication |
| `reviewer_id` | text | no | Required when verified |
| `reviewed_at` | datetime | no | Required when verified |
| `context_before` | text | yes | Suggested 1–2 sentences |
| `context_after` | text | yes | Suggested 1–2 sentences |
| `overlap_or_audio_issue` | boolean | yes | Flags ambiguity |
| `source_deeplink` | text | yes | Opens media near `start_ms` |

### C. `proof_claims` — atomic, scored proof units

| Field group | Fields |
|---|---|
| Identity | `claim_id`, `segment_id`, `source_video_id`, `claim_version`, `status` |
| Exact evidence | `quote_start_ms`, `quote_end_ms`, `verbatim_quote`, `edited_quote`, `edit_operations`, `translation_en`, `back_translation_th`, `translation_reviewer_id` |
| Taxonomy | `primary_proof_type`, `proof_types[]`, `problem_codes[]`, `trigger_codes[]`, `objection_codes[]`, `outcome_codes[]`, `mechanism_codes[]` |
| Persona | `persona_role`, `persona_business_stage`, `persona_team_size_band`, `persona_ai_level`, `persona_industry`, `persona_use_cases[]` |
| Claim anatomy | `before_state`, `action_or_mechanism`, `after_state`, `metric_name`, `metric_value_raw`, `metric_value_numeric`, `metric_unit`, `baseline`, `time_to_result`, `observation_period`, `scope`, `qualifiers`, `attribution_strength` |
| DR utility | `funnel_stages[]`, `ad_jobs[]`, `hook_patterns[]`, `emotional_tones[]`, `best_audience_match`, `suggested_lead_in`, `suggested_follow_up`, `counterclaim_risk` |
| Scoring | ten component fields below, `dr_score_raw`, `dr_score_adjusted`, `score_notes`, `scored_by`, `scored_at` |
| Risk/gates | `quantified_claim`, `financial_claim`, `health_or_legal_claim`, `atypical_result_risk`, `context_dependency`, `claim_risk_level`, `legal_review_status`, `permission_gate`, `publish_status`, `rejection_reason` |
| Lineage | `source_file_sha256`, `transcript_sha256`, `parent_claim_id`, `created_by`, `reviewed_by`, `created_at`, `updated_at` |

`status`: extracted → transcript_verified → claim_reviewed → permission_cleared → approved → used → archived/rejected.

`edit_operations` is an ordered array such as `[{type:"remove_filler", original:"เอ่อ", position:12}]`. Never allow an edited quote without this audit trail.

### D. `ad_assets` — generated derivatives, never detached from proof

| Field | Type | Required | Notes |
|---|---|---:|---|
| `asset_id` | UUID/string | yes | Primary key |
| `format_code` | enum | yes | See section 5 |
| `claim_ids` | array FK | yes | Every substantive line maps to ≥1 claim |
| `primary_claim_id` | FK | yes | Main proof |
| `script_or_copy` | text | yes | Draft output |
| `lineage_map` | JSON | yes | Each line/scene → claim + timecode |
| `language` | BCP-47 | yes | Thai-first |
| `channel`, `placement` | enum/text | yes | Meta Feed, Reels, TikTok, LP, etc. |
| `aspect_ratio` | enum | yes | 9:16, 4:5, 1:1, 16:9 |
| `duration_target_sec` | integer | no | For video |
| `funnel_stage`, `ad_job` | enum | yes | Intended use |
| `hook_variant` | text | no | Must not add unsupported claim |
| `cta_variant` | text | no | Brand copy, not customer quote |
| `disclaimer_text` | text | no | As reviewed |
| `permission_snapshot` | JSON | yes | Consent status/rights at generation time |
| `review_status` | enum | yes | draft, proof_checked, legal_checked, approved, rejected |
| `proof_checked_by`, `proof_checked_at` | audit | no | Required before approved |
| `render_uri`, `thumbnail_uri` | text | no | Output links |
| `campaign_id`, `ad_id` | text | no | Performance linkage |
| `created_at`, `updated_at` | datetime | yes | Audit |

### Required lineage map example

```json
{
  "asset_id": "asset_uuid",
  "lines": [
    {
      "line_no": 1,
      "text_type": "verbatim_quote",
      "claim_id": "claim_uuid",
      "source_video_id": "video_uuid",
      "segment_id": "segment_uuid",
      "start_ms": 12400,
      "end_ms": 16800,
      "transcript_version": "human-v2",
      "transcript_sha256": "…"
    }
  ]
}
```

Brand-written hooks, transitions, and CTAs use `text_type: brand_copy` and must be labeled as such; they cannot be presented inside customer quotation marks.

## 4. Direct-response scoring rubric

Score each component **0–5**. Weighted raw score totals 100.

| Component | Weight | 0 | 3 | 5 |
|---|---:|---|---|---|
| Outcome magnitude/importance | 15 | no outcome | meaningful but moderate | commercially or personally decisive |
| Specificity/concreteness | 15 | generic praise | clear action/result | precise metric, baseline, unit, time |
| Credibility/naturalness | 10 | scripted/vague | believable detail | candid, nuanced, self-authenticating detail |
| Product attribution | 10 | no link | contributory link | customer explicitly explains product → mechanism → result |
| Audience relevance | 10 | unclear persona/problem | recognizable segment | exact high-priority buyer + pain/use case |
| Objection-killing power | 10 | none | partially answers concern | names and resolves major objection with reason/result |
| Mechanism clarity | 10 | “it helped” | identifies feature/activity | shows what was applied and how |
| Hook/stop-scroll strength | 8 | no tension | usable opening | immediate number, reversal, confession, or surprise |
| Emotional resonance | 7 | flat | clear emotion | vivid, transferable tension and release |
| Editability/standalone clarity | 5 | unusable alone | usable with setup | concise, clear, clean clip with minimal context |

### Scoring anchors

- **0:** absent, contradicted, or unusable.
- **1:** present only as a weak implication.
- **2:** present but generic or context-heavy.
- **3:** clear and useful.
- **4:** strong, specific, and highly reusable.
- **5:** exceptional; can lead an ad without exaggeration.

### Formula

`raw_score = Σ(component_score / 5 × component_weight)`

Apply a separate evidence/risk multiplier; do not hide risk inside subjective creative scores:

- Transcript human-verified: ×1.00; not verified: **publish blocked**
- Exact timecode + matching clip: ×1.00; incomplete locator: ×0.75
- Context complete: ×1.00; moderate dependency: ×0.85; severe dependency: ×0.60
- Quantified result with unit + baseline + period: ×1.00; one missing: ×0.90; two+ missing: ×0.75
- Permission cleared for intended channel/edit: ×1.00; otherwise **publish blocked**
- High claim/compliance risk: score remains for prioritization but **legal review required**

`adjusted_score = raw_score × applicable multipliers`

### Action bands

- **85–100: Hero proof** — lead ad/landing page candidate after gates.
- **70–84: Strong proof** — single-claim ad or prominent supporting proof.
- **55–69: Support proof** — montage, retargeting, carousel, objection section.
- **40–54: Texture/voice-of-customer** — hooks, research, organic/social proof wall.
- **<40: Archive** — insight mining only; do not force into an ad.

### Selection rule for ad testing

Prioritize a **portfolio**, not only the highest scores:

1. Best result proof by major persona.
2. Best objection reversal for price, time, complexity, and fit.
3. Best mechanism/implementation proof.
4. Best premium-value/community proof.
5. Best emotional/identity proof.

Avoid running five variants that all express the same claim.

## 5. Rapid ad asset formats generated after transcripts arrive

All outputs are **draft candidates** until transcript, context, consent, and risk gates pass.

### `A01_QUOTE_CARD` — 15-minute static
- Input: one standalone quote, approved name/identity, one persona tag.
- Output: 4:5 + 9:16; 8–22 Thai words preferred; source ID/timecode in internal notes.
- Layout: short quote, customer descriptor, subtle “ผลลัพธ์ขึ้นอยู่กับบริบท” if required.
- Never place a paraphrase inside quotation marks.

### `A02_RESULT_CARD` — metric-led static
- Input: quantified claim with value, unit, baseline, and period.
- Output: number headline + exact supporting quote + customer context.
- Gate: quantified-claim review; preserve estimate language such as “ประมาณ”.

### `A03_PROBLEM_TO_PROOF` — 10–20s vertical
- 0–2s brand hook naming the customer’s stated problem.
- 2–5s “before” verbatim clip.
- 5–14s result/mechanism verbatim clip.
- 14–20s brand CTA.
- Burned-in Thai captions; every clip line mapped to timecodes.

### `A04_SKEPTIC_TO_BELIEVER` — 15–30s vertical
- Customer’s initial doubt → what changed their mind → result/recommendation.
- Best for retargeting and objection handling.
- Do not manufacture skepticism from interviewer questions.

### `A05_OBJECTION_KILLER` — 10–25s vertical/static
- One objection per asset: price, time, complexity, fit, implementation, community.
- Template: objection label (brand copy) → exact customer answer → evidence/result → CTA.

### `A06_MECHANISM_PROOF` — 20–40s vertical
- Shows the specific framework, workflow, module, feedback, or community mechanism the customer says they used.
- Structure: “สิ่งที่เอาไปใช้จริง” → action → observable change.
- Useful for solution-aware/product-aware buyers.

### `A07_BEFORE_AFTER` — 15–30s vertical/carousel
- Requires explicit before and after states from the same customer.
- On-screen split: ก่อน / หลัง; include time period if stated.
- Do not imply causality unless attribution language supports it.

### `A08_THREE_PROOF_MONTAGE` — 20–35s vertical
- Three customers, one tightly defined claim theme.
- Each clip 3–6s; distinct persona labels; no stitched sentence fragments that alter meaning.
- Themes: “เริ่มจากศูนย์,” “เอาไปใช้จริง,” “คุ้มค่าเพราะ…,” etc., only when supported.

### `A09_PERSONA_MONTAGE` — 20–40s vertical
- Multiple claims from one persona/industry/use case.
- Hook: brand-written segment callout, e.g. “สำหรับเจ้าของธุรกิจที่…”
- Each customer must independently support the advertised relevance.

### `A10_TESTIMONIAL_UGC_CUT` — 30–60s vertical
- Hook → customer context → problem → mechanism → result → recommendation → CTA.
- Customer words remain primary; brand transitions clearly distinguished.
- Include B-roll suggestions, caption emphasis, and exact edit decision list (EDL).

### `A11_FOUNDER_CASE_SNAPSHOT` — 4–6 slide carousel
1. Customer context (approved disclosure only)
2. Before/problem
3. What they applied
4. Result
5. Why it mattered / objection resolved
6. CTA

Every slide stores claim IDs; no composite “case study” facts from different customers.

### `A12_PROOF_STRIP` — landing-page module
- 3–6 compact proof tiles grouped by buyer problem or objection.
- Includes exact quote, approved identity, source/consent status internally.
- Generate mobile-first and desktop copy variants.

### `A13_SALES_ENABLEMENT_SNIPPET` — chat/call follow-up
- One quote + persona + objection answered + internal source deeplink.
- Produce Thai plain text, not a designed ad.
- For sales team use only after permission scope confirms this channel.

### `A14_HOOK_BANK` — brand-copy derivatives
- Generate 3–5 hooks per approved claim: number-first, confession, before/after, problem-first, recommendation.
- Hooks must be labeled `brand_copy`, cannot introduce facts, and should point into the exact quote rather than restate it more strongly.

### `A15_CAPTION_COPY_PACK` — copy variants
- Primary text: short (≤125 chars), medium, long.
- Headline, description, CTA, disclaimer placeholder.
- Include a `support_map` showing which sentences are brand positioning vs customer-supported claims.

### `A16_PROOF_TEST_MATRIX` — testing brief
- Rows: hook × proof clip × CTA.
- Hold proof constant while testing hook first; then hold hook constant while testing proof.
- Store audience, funnel stage, claim ID, asset ID, hypothesis, spend/result fields.

## 6. Mechanical generation pipeline

1. **Ingest:** preserve original file; calculate SHA-256; assign source ID; record rights status.
2. **Transcribe:** timestamp by speaker; keep original Thai; version and hash transcript.
3. **Verify:** human checks candidate segments against audio/video; correct Thai names, numbers, negation, units.
4. **Atomize:** split into one claim per proof record; attach context and exact timecodes.
5. **Classify:** apply taxonomy tags and claim anatomy without inference.
6. **Score:** two-pass scoring recommended; adjudicate ≥15-point disagreement.
7. **Risk/permission gate:** block missing consent, identity rights, unsupported quantified outcomes, or materially context-dependent cuts.
8. **Generate assets:** populate only formats whose input requirements are satisfied.
9. **Proof check:** compare every quote/subtitle/claim line to the locked transcript and source clip.
10. **Approve/render:** snapshot permission status and lineage map in the asset record.
11. **Measure:** attach campaign/ad performance to asset and claim IDs; learn which proof type/persona/objection works.
12. **Revoke/update:** consent revocation or transcript correction cascades to all linked assets and campaigns.

## 7. Output contract for an automated miner

For each candidate segment, return:

```json
{
  "claim_id": "uuid",
  "source_video_id": "uuid",
  "segment_id": "uuid",
  "quote_start_ms": 0,
  "quote_end_ms": 0,
  "verbatim_quote": "",
  "context_before": "",
  "context_after": "",
  "primary_proof_type": "",
  "problem_codes": [],
  "objection_codes": [],
  "outcome_codes": [],
  "mechanism_codes": [],
  "claim_anatomy": {
    "before_state": null,
    "action_or_mechanism": null,
    "after_state": null,
    "metric_value_raw": null,
    "metric_unit": null,
    "baseline": null,
    "time_to_result": null,
    "qualifiers": []
  },
  "unsupported_inferences": [],
  "score_components": {},
  "raw_score": null,
  "risk_flags": [],
  "permission_gate": "unknown",
  "recommended_asset_formats": [],
  "human_review_required": true
}
```

If a field is not explicitly supported, return `null`, `[]`, or `not_stated`; never guess.

## 8. QA checklist before any public use

- [ ] File hash, source ID, transcript hash, version, and timecodes present
- [ ] Human reviewer watched the exact clip
- [ ] Thai quote matches speech; negation, numbers, and qualifiers preserved
- [ ] Edited quote has an operation log and does not change meaning
- [ ] Translation/back-translation reviewed where used
- [ ] Before, after, mechanism, metric, baseline, and period are not inferred
- [ ] Brand copy is visually/textually distinguishable from customer quotation
- [ ] Customer identity, channel, edit, territory, and expiry rights are valid
- [ ] Quantified/financial/atypical claims received required review/disclaimer
- [ ] Asset lineage map resolves every proof-bearing line to a claim and clip
- [ ] Revocation cascade can identify every live derivative
- [ ] Final render checked, not only the script

## 9. Recommended operating views

- **Hero proof queue:** approved claims ≥85, grouped by persona.
- **Objection library:** strongest approved claim per objection and funnel stage.
- **Needs verification:** high raw score but transcript/context incomplete.
- **Permission blocked:** valuable claims that cannot yet be used.
- **Expiring rights:** assets linked to consent expiring in 30/60/90 days.
- **Claim coverage gaps:** priority personas/problems with no strong proof.
- **Performance by proof:** spend, thumb-stop/hold, CTR, CVR, CPA/ROAS keyed to proof type and claim ID.

This system is intentionally empty of customer claims until verified transcripts are ingested.
