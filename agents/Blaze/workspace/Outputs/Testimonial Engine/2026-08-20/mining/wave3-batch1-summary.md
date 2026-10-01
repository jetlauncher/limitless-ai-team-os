# Wave 3 Batch 1 — Testimonial Claim Mining Summary

- **Assigned canonical transcripts:** 21
- **Transcripts with accepted claims:** 17
- **Transcripts rejected/no accepted claim:** 4
- **Atomic claims extracted:** 24
- **Evidence state:** machine ASR only; every claim has `human_review_required=true`, `permission_gate=unknown`, and `status=extracted`.
- **Quote handling:** every quote is the exact text of complete, contiguous canonical ASR segments; no filler removal, punctuation cleanup, translation, or silent correction was applied.
- **Source-path preservation:** each claim’s `source_deeplink` retains the canonical Dropbox remote + manifest `source_path` + exact start/end locator; the exact path is also recorded in `scores.score_notes`.
- **Source hash note:** `source_file_sha256` is `null` because the artifacts expose an audio hash, not a verified original-video hash; no hash was relabeled or invented.

## Score bands (adjusted)

- Hero proof (85–100): 4
- Strong proof (70–84): 11
- Support proof (55–69): 7
- Texture/VOC (40–54): 2
- Archive (<40): 0

## Primary proof types

- `before_after_transformation`: 8
- `quantified_outcome`: 3
- `community_network_proof`: 2
- `comparison_alternative_proof`: 2
- `implementation_proof`: 2
- `speed_time_saved`: 2
- `curriculum_product_proof`: 1
- `ease_accessibility_proof`: 1
- `objection_reversal`: 1
- `skill_capability_gain`: 1
- `support_accountability_proof`: 1

## Highest-priority review candidates

- **88.6** — `5483cd46-c21d-5f61-a0ae-aef3626ad8a9` — `f48b609680dc567c` 17020–34700 ms — “คนละแบบเลย สามารถเจาะลึก ChatGPT ใช้เวลาแป๊บเดียวในการคิดคอนเทนต์ แล้วก็มีไอเดียไหลมาให้เราโดยที่ละเอียดมาก ย่นย่อระยะเวลา คนปกติทำงาน 8 ชั่วโมง เราทำงานแค่ 3-4 ชั่วโมงคือได้ผลลัพธ์เยอะแล้ว”
- **88.0** — `78c4ae87-3565-5310-9215-6e593ee168a6` — `fd3b4327c0da8f26` 12200–25540 ms — “จริง ๆ ใช้ ChatGPT อยู่แล้ว แต่ว่าเหมือนใช้ไม่เต็มประสิทธิภาพ ก็เลยอยากมาเรียนรู้เพิ่มเติม ในการที่จะทำให้เราจ่ายเงินหน้า 700 บาท ให้มันคุ้มค่า 700 ตอนนี้ก็คือใช้ได้เต็มพื้นที่มากขึ้นนะคะ”
- **87.0** — `ff776c98-4c5b-5409-ad93-40308631e243` — `f2238a839d461a07` 0–8780 ms — “คุ้มมากครับ การที่มาเรียนที่นี่เขาเลือกตัวที่มันดีมาแล้ว เรียนรู้ได้อย่างรวดเร็วดีกว่า ไม่เสียเวลาต้องแบบไปลองหลายๆตัว เอากลับไปประยุกต์กับงานเราได้ทันทีเลยครับ”
- **85.4** — `b3f89e86-7fff-532a-a891-c2376dddce78` — `b96d350ea9650873` 30000–43480 ms — “ตั้งแต่แรก ถ้าประทับใจต้องบอกว่าตั้งแต่แรกเลยนะครับ เป็นวิธีการที่มันค่อนข้างที่เข้าใจง่ายและทำได้จริง บริจารณ์โดยรวมถือว่า ถ้าถามผมแล้วค่อนข้างที่จะเฟรนลี่นะครับ ก็ไม่มีความกดดันนะครับ เป็นการที่เรียนรู้เพื่อใช้งานได้จริง”
- **84.6** — `8a59e192-ef74-56e1-8aaa-a41ef119502e` — `737ba376b63d2262` 10520–32080 ms — “เป็น Deep Analysis ค่ะ คือส่วนตัวเรียน Business มาค่ะ แล้วก็จะทำพวก Data Research ค่อนข้างเยอะ ก่อนอันนี้คือ DASearch คือมัน Search นาน ทีเดียวครึ่งชั่วโมงทำงานจบแน่นอน”
- **84.0** — `a5483287-bdc6-5300-936f-421409be8d65` — `1e10049af634d940` 33080–43440 ms — “ถ้าเต็มสิบให้ร้อยเลยค่ะ เป็น Community ของกรุ๊ป AI ทำให้เราได้เข้ามาพัฒนา AI คือจบคลาสแล้วก็ไม่จบ เราก็สามารถที่จะพัฒนาต่อเนื่องได้อย่างต่อไปด้วยค่ะ”
- **83.0** — `8ecbb8ff-ae3b-55c9-adad-270118e9378c` — `5b11154a541dec4c` 17360–27300 ms — “ที่ว้าวมากที่สุดเลยนะครับ ก็จะเป็น Workflow นะครับ เราสามารถจังตัวนี้ไป แล้วก็ให้เขาทำงานได้โดยอัตโนมัติเลย น่าสนใจมากๆ เลยครับ”
- **82.6** — `6d08a7e9-62a6-53b6-85ee-059f424f2170` — `b96d350ea9650873` 0–7240 ms — “ปกติผมใช้ AI ค่อนข้างที่จะ Basic มาก Subscribe เดือนละ 690 ใช้จริงๆ น่าจะอยู่มา 50 บาท พอมาวันนี้ปุ๊บมีความรู้สึกว่ามันทำได้มากกว่านี้”

## Transcript disposition

- `2b1059c092bfcbb3` — `CTA ไม่มีวันที่/02_Mind_review_ไม่มีวันที่.mp4` — accepted 1 claim(s).
- `d4ec7c263165efa2` — `CTA ไม่มีวันที่/02_Pocky_review_ไม่มีวันที่.mp4` — Rejected: low-content/ASR-ambiguous testimonial fragment; the core item learned is transcribed as ‘เพื่อนมือต่างๆ’ and the business application is future intent rather than a realized outcome.
- `153131a50f1e5ae4` — `CTA ไม่มีวันที่/02_อ้น_review_ไม่มีวันที่.mp4` — accepted 1 claim(s).
- `0b021704aee50b1a` — `Review Creative AI/K.BJ.mp4` — accepted 1 claim(s).
- `5835dd99d8db98b4` — `Review Creative AI/K.NIK.mp4` — accepted 2 claim(s).
- `f2238a839d461a07` — `Review Creative AI/K.Pupm.mp4` — accepted 1 claim(s).
- `3391c32035bfccde` — `รุ่น 1/แก้ มายด์.mp4` — accepted 1 claim(s). Duplicate testimonial content was retained as a separate canonical source and explicitly risk-flagged.
- `f89c56c3f7313a22` — `รุ่น 1/แก้ อ้น.mp4` — accepted 1 claim(s). Duplicate testimonial content was retained as a separate canonical source and explicitly risk-flagged.
- `d4aa8c81e9438637` — `รุ่น 2/K.Heng.mp4` — accepted 1 claim(s).
- `5b11154a541dec4c` — `รุ่น 3/ICE.mp4` — accepted 2 claim(s).
- `e50af465a7b072e2` — `รุ่น 4/02_NEE แก้_F.mp4` — Rejected: machine ASR is heavily corrupted/repetitive; no quote could be preserved as reliable atomic testimonial proof without silent correction.
- `959dbce1eec895d5` — `รุ่น 4/แก้ K.Ake.mp4` — Rejected: mostly promotional/FOMO and instructor-energy reaction; no concrete, realized customer outcome, mechanism application, or sufficiently substantive testimonial proof.
- `fd3b4327c0da8f26` — `รุ่น 5/K.AOR.mp4` — accepted 3 claim(s).
- `6d7a84123ffc7716` — `รุ่น 5/K.FERN.mp4` — accepted 1 claim(s).
- `938f540016d2be9e` — `รุ่น 5/K.KAI.mp4` — accepted 2 claim(s).
- `9ddb9a7a768525af` — `รุ่น 6/02_K.Tan.mp4` — accepted 1 claim(s).
- `737ba376b63d2262` — `รุ่น 7/3-jedi-รุ่น7 k.da-q.mp4` — accepted 1 claim(s).
- `1e10049af634d940` — `รุ่น 7/3-jedi-รุ่น7 k.fern-q.mp4` — accepted 1 claim(s).
- `f48b609680dc567c` — `รุ่น 7/รุ่น 7 K.Nida.mp4` — accepted 2 claim(s).
- `b2095e3ea44abddb` — `รุ่น 7/รุ่น 7 K.Wichai.mp4` — Rejected: machine ASR is fragmented/ambiguous and product attribution is unclear; remaining statements are generic AI benefit language or low-content fragments.
- `b96d350ea9650873` — `รุ่น 8/04-JD-รุ่น8 K.Keng-Q.mp4` — accepted 2 claim(s).

## Validation

- 21/21 `COMPLETE.json` records reported `COMPLETE`, and every on-disk `transcript.json` SHA-256 matched both the assignment manifest and completion artifact hash.
- 24/24 JSONL lines parsed successfully; 24 unique claim IDs.
- 24/24 claims passed `testimonial_claim.schema.json` (Draft 2020-12 with URI format checking).
- 24/24 verbatim quotes and millisecond ranges matched the exact contiguous canonical ASR segments.

## Required review gates

- Listen to each exact clip and correct ASR errors before treating any quote as verified.
- Confirm the speaker is the customer, not an interviewer, promotional talent, or a stitched/duplicated cut.
- Confirm consent, identity display, channels, territories, edits, and expiry before publication.
- Review quantified, price, cost-saving, time-saving, workforce-substitution, and atypical-result claims for context, methodology, legal risk, and disclaimer needs.
- Deduplicate alternate cuts of the Mind and On testimonials before portfolio-level counting or creative use.
