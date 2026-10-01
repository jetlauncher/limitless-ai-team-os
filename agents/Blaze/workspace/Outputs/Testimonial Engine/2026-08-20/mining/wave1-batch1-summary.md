# Wave 1 Batch 1 Testimonial Mining Summary

- Assigned canonical sources reviewed: **6**
- Extracted atomic proof claims: **5**
- Sources contributing claims: **2**
- Sources rejected with no claims: **4**
- Transcript state: **machine ASR only; not human verified**
- Publication state: **all claims blocked pending human transcript review and permission clearance**

## Claim counts by source

- `2b9e179abf9ee8e7` — 3 claims (`CTA ไม่มีวันที่/ADs ใหม่ รีวิแบบสับๆ ไม่มีวันที่.mp4`): value, low-stress class experience, friendship/community. Montage speaker/context ambiguity flagged.
- `3b1684b316ce33df` — 2 claims (`Short Ads/รวม CTA รุ่น3/แยก KruPANN CTA รุ่น3.mp4`): AI-use awareness/capability shift and recommendation/AI-job-displacement objection.

## Rejected sources

- `59577c43f9e8e13a` — Rejected: Jet/instructor promotional CTA; no customer testimonial.
- `0777dcbf160fcf28` — Rejected: English promotional CTA; no customer testimonial.
- `02f7132a34e37b41` — Rejected: low-content/mismatched Japanese ASR; no testimonial proof.
- `8ef8cf6963f143fc` — Rejected: ASR contains only “!”; no testimonial proof.

## QA notes

- `verbatim_quote` values are copied directly from canonical ASR segment text without edits.
- Quote boundaries are exact ASR segment start/end times converted to integer milliseconds.
- Transcript SHA-256 values were recomputed and matched the source manifest and `COMPLETE.json`.
- `adjusted_score` is `null` because the proof system treats unverified transcripts and unknown permission as publication blockers rather than numeric penalties.
- All records use `status: extracted`, `permission_gate: unknown`, and `human_review_required: true`.
