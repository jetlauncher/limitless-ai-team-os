# DRAFT — WAVE 3 HERO THAI TESTIMONIAL ADS

> **DRAFT — MACHINE ASR — HUMAN AUDIO/PERMISSION REVIEW REQUIRED**
>
> ห้าม render, post, schedule หรือ launch paid media จนกว่าจะผ่าน human audio verification, permission/identity/channel review, claims-risk/legal review ตามที่ระบุ และ Jet approval

## Production status and hard rules

- Source of truth: `claims/all_claims.jsonl`; package uses exactly 7 found IDs from the delegated list. Prefix `84c?` was not a complete/found claim ID and was ignored as instructed.
- ทุก customer line คือ `verbatim_quote` เต็มช่วงจาก claim bank ไม่มีการแก้คำ ตัด filler สลับลำดับ หรือสร้าง subclip timecode.
- Hook, transition, headline, CTA และ disclaimer คือ **`brand_copy`** และไม่อยู่ในเครื่องหมายคำพูดแบบ customer quote.
- Customer identity: `Anonymous / รอสิทธิ์` เท่านั้น; claims ทั้งหมด `status=extracted`, `permission_gate=unknown`, `human_review_required=true`.
- EDL ครอบคลุม vertical 7 ชิ้น + montage 2 ชิ้น. Proof cards เป็น static concepts ไม่มี EDL row.
- ‘Verified mechanically’ หมายถึงตรงกับ claim bank เท่านั้น ไม่ใช่ human audio verified.

## Mandatory risk flags

- **8 ชั่วโมง → 3–4 ชั่วโมง:** `5483cd46...` เป็น quantified + atypical-result claim; ใช้ได้เฉพาะ exact quote พร้อม review/disclaimer decision; ห้าม implied typicality.
- **Price/value:** `78c4ae87...` มี 700 บาท; `6d08a7e9...` มี Subscribe 690 และ estimate ‘น่าจะ’ 50 บาท. ห้ามแปลงเป็นราคาปัจจุบัน, savings, waste percentage หรือ ROI.
- **Workforce:** ไม่มีหนึ่งใน 7 exact quotes ที่กล่าว workforce reduction โดยตรง. `8ecbb8ff...` กล่าว automation เท่านั้น; **ห้ามตีความ/ทำภาพเป็นการลดคนหรือแทนพนักงาน**. หากเพิ่ม workforce claim ภายหลังต้องใช้ claim ID/source/timecode แยกและ HIGH-risk review.
- **Atypical claims:** `5483cd46...` flagged `ATYPICAL_RESULT_RISK`; คะแนน ‘เต็มสิบให้ร้อย’ ใน `a5483287...` เป็น endorsement เฉพาะบุคคล ไม่ใช่ผลลัพธ์มาตรฐาน.

## Mechanically locked claim register

| Claim ID | Source / full range | Exact machine-ASR quote | Risk/gate |
|---|---|---|---|
| `5483cd46-c21d-5f61-a0ae-aef3626ad8a9` | `f48b609680dc567c` · `00:00:17.020–00:00:34.700` · [source deeplink](dropbox-jedienterprise:Limitless%20Club/All%20Reviews/%E0%B8%A3%E0%B8%B8%E0%B9%88%E0%B8%99%207/%E0%B8%A3%E0%B8%B8%E0%B9%88%E0%B8%99%207%20K.Nida.mp4#t=17.020,34.700) | “คนละแบบเลย สามารถเจาะลึก ChatGPT ใช้เวลาแป๊บเดียวในการคิดคอนเทนต์ แล้วก็มีไอเดียไหลมาให้เราโดยที่ละเอียดมาก ย่นย่อระยะเวลา คนปกติทำงาน 8 ชั่วโมง เราทำงานแค่ 3-4 ชั่วโมงคือได้ผลลัพธ์เยอะแล้ว” | `high` · `MACHINE_ASR_ONLY, HUMAN_AUDIO_REVIEW_REQUIRED, PERMISSION_UNKNOWN, SOURCE_FILE_SHA256_NOT_AVAILABLE, QUANTIFIED_CLAIM, ATYPICAL_RESULT_RISK, OUTPUT_VOLUME_UNQUANTIFIED` · permission unknown · human review required |
| `78c4ae87-3565-5310-9215-6e593ee168a6` | `fd3b4327c0da8f26` · `00:00:12.200–00:00:25.540` · [source deeplink](dropbox-jedienterprise:Limitless%20Club/All%20Reviews/%E0%B8%A3%E0%B8%B8%E0%B9%88%E0%B8%99%205/K.AOR.mp4#t=12.200,25.540) | “จริง ๆ ใช้ ChatGPT อยู่แล้ว แต่ว่าเหมือนใช้ไม่เต็มประสิทธิภาพ ก็เลยอยากมาเรียนรู้เพิ่มเติม ในการที่จะทำให้เราจ่ายเงินหน้า 700 บาท ให้มันคุ้มค่า 700 ตอนนี้ก็คือใช้ได้เต็มพื้นที่มากขึ้นนะคะ” | `medium` · `MACHINE_ASR_ONLY, HUMAN_AUDIO_REVIEW_REQUIRED, PERMISSION_UNKNOWN, SOURCE_FILE_SHA256_NOT_AVAILABLE, ASR_AMBIGUITY, PRICE_REFERENCE` · permission unknown · human review required |
| `ff776c98-4c5b-5409-ad93-40308631e243` | `f2238a839d461a07` · `00:00:00.000–00:00:08.780` · [source deeplink](dropbox-jedienterprise:Limitless%20Club/All%20Reviews/Review%20Creative%20AI/K.Pupm.mp4#t=0.000,8.780) | “คุ้มมากครับ การที่มาเรียนที่นี่เขาเลือกตัวที่มันดีมาแล้ว เรียนรู้ได้อย่างรวดเร็วดีกว่า ไม่เสียเวลาต้องแบบไปลองหลายๆตัว เอากลับไปประยุกต์กับงานเราได้ทันทีเลยครับ” | `low` · `MACHINE_ASR_ONLY, HUMAN_AUDIO_REVIEW_REQUIRED, PERMISSION_UNKNOWN, SOURCE_FILE_SHA256_NOT_AVAILABLE` · permission unknown · human review required |
| `b3f89e86-7fff-532a-a891-c2376dddce78` | `b96d350ea9650873` · `00:00:30.000–00:00:43.480` · [source deeplink](dropbox-jedienterprise:Limitless%20Club/All%20Reviews/%E0%B8%A3%E0%B8%B8%E0%B9%88%E0%B8%99%208/04-JD-%E0%B8%A3%E0%B8%B8%E0%B9%88%E0%B8%998%20K.Keng-Q.mp4#t=30.000,43.480) | “ตั้งแต่แรก ถ้าประทับใจต้องบอกว่าตั้งแต่แรกเลยนะครับ เป็นวิธีการที่มันค่อนข้างที่เข้าใจง่ายและทำได้จริง บริจารณ์โดยรวมถือว่า ถ้าถามผมแล้วค่อนข้างที่จะเฟรนลี่นะครับ ก็ไม่มีความกดดันนะครับ เป็นการที่เรียนรู้เพื่อใช้งานได้จริง” | `low` · `MACHINE_ASR_ONLY, HUMAN_AUDIO_REVIEW_REQUIRED, PERMISSION_UNKNOWN, SOURCE_FILE_SHA256_NOT_AVAILABLE, ASR_AMBIGUITY_BORIJAN_WORD` · permission unknown · human review required |
| `8ecbb8ff-ae3b-55c9-adad-270118e9378c` | `5b11154a541dec4c` · `00:00:17.360–00:00:27.300` · [source deeplink](dropbox-jedienterprise:Limitless%20Club/All%20Reviews/%E0%B8%A3%E0%B8%B8%E0%B9%88%E0%B8%99%203/ICE.mp4#t=17.360,27.300) | “ที่ว้าวมากที่สุดเลยนะครับ ก็จะเป็น Workflow นะครับ เราสามารถจังตัวนี้ไป แล้วก็ให้เขาทำงานได้โดยอัตโนมัติเลย น่าสนใจมากๆ เลยครับ” | `low` · `MACHINE_ASR_ONLY, HUMAN_AUDIO_REVIEW_REQUIRED, PERMISSION_UNKNOWN, SOURCE_FILE_SHA256_NOT_AVAILABLE, ASR_AMBIGUITY` · permission unknown · human review required |
| `6d08a7e9-62a6-53b6-85ee-059f424f2170` | `b96d350ea9650873` · `00:00:00.000–00:00:07.240` · [source deeplink](dropbox-jedienterprise:Limitless%20Club/All%20Reviews/%E0%B8%A3%E0%B8%B8%E0%B9%88%E0%B8%99%208/04-JD-%E0%B8%A3%E0%B8%B8%E0%B9%88%E0%B8%998%20K.Keng-Q.mp4#t=0.000,7.240) | “ปกติผมใช้ AI ค่อนข้างที่จะ Basic มาก Subscribe เดือนละ 690 ใช้จริงๆ น่าจะอยู่มา 50 บาท พอมาวันนี้ปุ๊บมีความรู้สึกว่ามันทำได้มากกว่านี้” | `medium` · `MACHINE_ASR_ONLY, HUMAN_AUDIO_REVIEW_REQUIRED, PERMISSION_UNKNOWN, SOURCE_FILE_SHA256_NOT_AVAILABLE, PRICE_REFERENCE, ASR_AMBIGUITY` · permission unknown · human review required |
| `a5483287-bdc6-5300-936f-421409be8d65` | `1e10049af634d940` · `00:00:33.080–00:00:43.440` · [source deeplink](dropbox-jedienterprise:Limitless%20Club/All%20Reviews/%E0%B8%A3%E0%B8%B8%E0%B9%88%E0%B8%99%207/3-jedi-%E0%B8%A3%E0%B8%B8%E0%B9%88%E0%B8%997%20k.fern-q.mp4#t=33.080,43.440) | “ถ้าเต็มสิบให้ร้อยเลยค่ะ เป็น Community ของกรุ๊ป AI ทำให้เราได้เข้ามาพัฒนา AI คือจบคลาสแล้วก็ไม่จบ เราก็สามารถที่จะพัฒนาต่อเนื่องได้อย่างต่อไปด้วยค่ะ” | `low` · `MACHINE_ASR_ONLY, HUMAN_AUDIO_REVIEW_REQUIRED, PERMISSION_UNKNOWN, SOURCE_FILE_SHA256_NOT_AVAILABLE, ASR_AMBIGUITY` · permission unknown · human review required |

## 1. W3-A01-8H-TO-3-4H — จาก 8 ชั่วโมง สู่ 3–4 ชั่วโมง—ตามคำผู้เรียน

> **DRAFT — MACHINE ASR — HUMAN AUDIO/PERMISSION REVIEW REQUIRED**

- **Format:** 9:16 vertical master; 4:5 cutdown only after approval
- **Target duration:** 25s
- **Audience:** ผู้ทำอาชีพออนไลน์ที่ใช้เวลาคิดคอนเทนต์
- **Funnel:** problem-aware / solution-aware / product-aware
- **Ad job:** stop scroll / prove outcome / explain mechanism
- **Risk:** HIGH — QUANTIFIED + ATYPICAL RESULT: มีตัวเลข 8 ชั่วโมง → 3–4 ชั่วโมง และคำว่าได้ผลลัพธ์เยอะโดยไม่มีจำนวน output/ช่วงสังเกต; ห้ามทำเป็นผลลัพธ์ทั่วไปหรือการรับประกัน

### Hook variants — all `brand_copy`

1. **[brand_copy]** ผู้เรียนคนนี้พูดถึงเวลาทำงาน 8 ชั่วโมง กับ 3–4 ชั่วโมงไว้อย่างไร?
2. **[brand_copy]** เมื่อการคิดคอนเทนต์กินเวลา—ฟังตัวเลขจากประสบการณ์ของผู้เรียนคนนี้
3. **[brand_copy]** ตัวเลข 8 ชั่วโมง และ 3–4 ชั่วโมง มาจากคำพูดของผู้เรียนหนึ่งคน

### Master script / timeline

| Ad time | Type | Spoken/on-screen line | Lineage |
|---|---|---|---|
| 00.00–02.50s | `brand_copy` | HOOK (เลือก 1 จาก 3; EDL ใช้ variant 1) | — |
| 02.50–20.18s | `verbatim_quote` | “คนละแบบเลย สามารถเจาะลึก ChatGPT ใช้เวลาแป๊บเดียวในการคิดคอนเทนต์ แล้วก็มีไอเดียไหลมาให้เราโดยที่ละเอียดมาก ย่นย่อระยะเวลา คนปกติทำงาน 8 ชั่วโมง เราทำงานแค่ 3-4 ชั่วโมงคือได้ผลลัพธ์เยอะแล้ว” | `claim_id=5483cd46-c21d-5f61-a0ae-aef3626ad8a9` · `source_video_id=f48b609680dc567c` · `segment_id=f48b609680dc567c-segments-3-4` · `source=00:00:17.020–00:00:34.700` · `transcript=asr-mlx-whisper-large-v3-mlx` · `transcript_sha256=6a76fec7e94bfcde1fb3600dda63a26495e638846ba7c68b58f7e6439b047887` |
| 20.18–25.00s | `brand_copy` | ดูแนวทางใช้ AI กับงานคอนเทนต์ • ผลลัพธ์ขึ้นอยู่กับบริบทและการนำไปใช้ | — |

### Edit direction

Talking head เต็มเฟรม; caption รักษา 8 ชั่วโมง และ 3-4 ชั่วโมงตาม ASR; ห้ามทำกราฟ typical result, x เท่า, เปอร์เซ็นต์ หรือรับประกันผล

### Required gate before use

- [ ] Human listens to full quoted source range and creates approved human transcript/subclip if needed
- [ ] Speaker identity + paid/organic channel, territory, edit and expiry permissions confirmed
- [ ] Thai captions matched to approved human transcript; no silent ASR correction
- [ ] Claims/risk review completed; no unsupported super, B-roll implication or typicality claim

## 2. W3-A02-700-BAHT-VALUE — จ่าย ChatGPT 700 บาท แต่รู้สึกว่ายังใช้ไม่เต็มประสิทธิภาพ

> **DRAFT — MACHINE ASR — HUMAN AUDIO/PERMISSION REVIEW REQUIRED**

- **Format:** 9:16 vertical master; 4:5 cutdown only after approval
- **Target duration:** 20s
- **Audience:** เจ้าของธุรกิจที่จ่าย ChatGPT แต่รู้สึกว่ายังใช้ไม่เต็มประสิทธิภาพ
- **Funnel:** solution-aware / product-aware / retargeting
- **Ad job:** prove outcome / answer price-value objection
- **Risk:** MEDIUM — PRICE REFERENCE + ASR AMBIGUITY: 700 บาทเป็นคำผู้เรียน; คำว่า ‘หน้า 700’ และ ‘เต็มพื้นที่’ ต้องฟังเสียงยืนยัน; ห้ามแปลงเป็นราคาปัจจุบันหรือ ROI

### Hook variants — all `brand_copy`

1. **[brand_copy]** จ่าย ChatGPT อยู่แล้ว แต่ยังรู้สึกว่าใช้ไม่เต็มประสิทธิภาพไหม?
2. **[brand_copy]** ผู้เรียนคนนี้พูดถึงเงิน 700 บาทและการใช้ ChatGPT ไว้อย่างไร?
3. **[brand_copy]** ความคุ้มค่าของค่า AI—ฟังจากประสบการณ์ของเจ้าของธุรกิจคนนี้

### Master script / timeline

| Ad time | Type | Spoken/on-screen line | Lineage |
|---|---|---|---|
| 00.00–02.50s | `brand_copy` | HOOK (เลือก 1 จาก 3; EDL ใช้ variant 1) | — |
| 02.50–15.84s | `verbatim_quote` | “จริง ๆ ใช้ ChatGPT อยู่แล้ว แต่ว่าเหมือนใช้ไม่เต็มประสิทธิภาพ ก็เลยอยากมาเรียนรู้เพิ่มเติม ในการที่จะทำให้เราจ่ายเงินหน้า 700 บาท ให้มันคุ้มค่า 700 ตอนนี้ก็คือใช้ได้เต็มพื้นที่มากขึ้นนะคะ” | `claim_id=78c4ae87-3565-5310-9215-6e593ee168a6` · `source_video_id=fd3b4327c0da8f26` · `segment_id=fd3b4327c0da8f26-segments-2-4` · `source=00:00:12.200–00:00:25.540` · `transcript=asr-mlx-whisper-large-v3-mlx` · `transcript_sha256=4193df9b3d0ec87403cd0032d59c919f3e51b14e81affb648189b509bbe6d2a4` |
| 15.84–20.00s | `brand_copy` | สำรวจวิธีใช้เครื่องมือ AI ให้เหมาะกับงานของคุณ • ไม่มีการรับประกันความคุ้มค่า | — |

### Edit direction

ใช้ on-screen label ‘คำพูดของผู้เรียน’ เมื่อขึ้น 700 บาท; ห้ามทำเป็น price card ของ Limitless Club หรือคำนวณ ROI; คงถ้อยคำ ASR ทุกคำ

### Required gate before use

- [ ] Human listens to full quoted source range and creates approved human transcript/subclip if needed
- [ ] Speaker identity + paid/organic channel, territory, edit and expiry permissions confirmed
- [ ] Thai captions matched to approved human transcript; no silent ASR correction
- [ ] Claims/risk review completed; no unsupported super, B-roll implication or typicality claim

## 3. W3-A03-CURATED-TOOLS — ไม่ต้องเสียเวลาลองหลายตัว—ตามประสบการณ์ Content Creator

> **DRAFT — MACHINE ASR — HUMAN AUDIO/PERMISSION REVIEW REQUIRED**

- **Format:** 9:16 vertical master; 4:5 cutdown only after approval
- **Target duration:** 15s
- **Audience:** Content Creator ที่สับสนกับเครื่องมือ AI หลายตัว
- **Funnel:** problem-aware / solution-aware / product-aware
- **Ad job:** explain mechanism / prove implementation / de-risk
- **Risk:** LOW — เป็น comparison และประสบการณ์เฉพาะบุคคล; ‘ทันที’ ต้องไม่ถูกยกระดับเป็นการรับประกันสำหรับทุกคน

### Hook variants — all `brand_copy`

1. **[brand_copy]** AI มีหลายตัว—ต้องลองเองทุกตัวจริงไหม?
2. **[brand_copy]** Content Creator คนนี้เลือกทางลัดในการเรียนรู้เครื่องมืออย่างไร?
3. **[brand_copy]** ฟังเหตุผลที่เขาบอกว่าไม่ต้องเสียเวลาไปลองหลาย ๆ ตัว

### Master script / timeline

| Ad time | Type | Spoken/on-screen line | Lineage |
|---|---|---|---|
| 00.00–02.50s | `brand_copy` | HOOK (เลือก 1 จาก 3; EDL ใช้ variant 1) | — |
| 02.50–11.28s | `verbatim_quote` | “คุ้มมากครับ การที่มาเรียนที่นี่เขาเลือกตัวที่มันดีมาแล้ว เรียนรู้ได้อย่างรวดเร็วดีกว่า ไม่เสียเวลาต้องแบบไปลองหลายๆตัว เอากลับไปประยุกต์กับงานเราได้ทันทีเลยครับ” | `claim_id=ff776c98-4c5b-5409-ad93-40308631e243` · `source_video_id=f2238a839d461a07` · `segment_id=f2238a839d461a07-segments-0-2` · `source=00:00:00.000–00:00:08.780` · `transcript=asr-mlx-whisper-large-v3-mlx` · `transcript_sha256=dae107f19a9ca63f5f6e3fd7780f3c828ea6dfa70bf58f796c221f1601454b75` |
| 11.28–15.00s | `brand_copy` | ดูแนวทางเลือกและประยุกต์เครื่องมือ AI กับงานของคุณ • ประสบการณ์ขึ้นอยู่กับแต่ละบุคคล | — |

### Edit direction

ตัดบน talking head + abstract tool tiles; ห้ามใส่โลโก้/รายชื่อเครื่องมือที่ผู้เรียนไม่ได้กล่าว; ‘ทันที’ อยู่ใน quote เท่านั้น

### Required gate before use

- [ ] Human listens to full quoted source range and creates approved human transcript/subclip if needed
- [ ] Speaker identity + paid/organic channel, territory, edit and expiry permissions confirmed
- [ ] Thai captions matched to approved human transcript; no silent ASR correction
- [ ] Claims/risk review completed; no unsupported super, B-roll implication or typicality claim

## 4. W3-A04-EASY-PRACTICAL — เข้าใจง่าย ไม่มีความกดดัน และใช้งานได้จริง—ตามคำผู้เรียน

> **DRAFT — MACHINE ASR — HUMAN AUDIO/PERMISSION REVIEW REQUIRED**

- **Format:** 9:16 vertical master; 4:5 cutdown only after approval
- **Target duration:** 20s
- **Audience:** เจ้าของ e-commerce มือใหม่ AI ที่กังวลเรื่องความยาก
- **Funnel:** solution-aware / product-aware / retargeting
- **Ad job:** answer complexity objection / de-risk / prove implementation
- **Risk:** LOW — ASR AMBIGUITY: คำว่า ‘บริจารณ์’ ต้องฟังเสียงยืนยัน; ห้ามสรุปว่าเป็นประสบการณ์ของผู้เรียนทุกคน

### Hook variants — all `brand_copy`

1. **[brand_copy]** กลัวเรียน AI แล้วกดดันหรือทำตามไม่ได้? ฟังประสบการณ์นี้
2. **[brand_copy]** เจ้าของ e-commerce มือใหม่พูดถึงความเข้าใจง่ายไว้อย่างไร?
3. **[brand_copy]** จากความกังวลเรื่องความยาก—ผู้เรียนคนนี้บอกว่าอะไรทำให้ใช้งานได้จริง?

### Master script / timeline

| Ad time | Type | Spoken/on-screen line | Lineage |
|---|---|---|---|
| 00.00–02.50s | `brand_copy` | HOOK (เลือก 1 จาก 3; EDL ใช้ variant 1) | — |
| 02.50–15.98s | `verbatim_quote` | “ตั้งแต่แรก ถ้าประทับใจต้องบอกว่าตั้งแต่แรกเลยนะครับ เป็นวิธีการที่มันค่อนข้างที่เข้าใจง่ายและทำได้จริง บริจารณ์โดยรวมถือว่า ถ้าถามผมแล้วค่อนข้างที่จะเฟรนลี่นะครับ ก็ไม่มีความกดดันนะครับ เป็นการที่เรียนรู้เพื่อใช้งานได้จริง” | `claim_id=b3f89e86-7fff-532a-a891-c2376dddce78` · `source_video_id=b96d350ea9650873` · `segment_id=b96d350ea9650873-segments-8-13` · `source=00:00:30.000–00:00:43.480` · `transcript=asr-mlx-whisper-large-v3-mlx` · `transcript_sha256=eb1e61a148c298e6beebd51b17f2888d7f5431c5e60e0285d95f295931f39910` |
| 15.98–20.00s | `brand_copy` | ดูรูปแบบการเรียนและการนำไปใช้ • ประสบการณ์ของแต่ละคนอาจแตกต่างกัน | — |

### Edit direction

Talking head แบบอบอุ่น; caption ต้องคงคำ ‘บริจารณ์’ จนกว่าจะ human verify; ห้ามแก้ ASR เงียบ ๆ หรือขึ้น super ว่า ‘ทุกคนทำได้’

### Required gate before use

- [ ] Human listens to full quoted source range and creates approved human transcript/subclip if needed
- [ ] Speaker identity + paid/organic channel, territory, edit and expiry permissions confirmed
- [ ] Thai captions matched to approved human transcript; no silent ASR correction
- [ ] Claims/risk review completed; no unsupported super, B-roll implication or typicality claim

## 5. W3-A05-WORKFLOW-AUTOMATION — สิ่งที่ว้าวที่สุดคือ Workflow—ตามคำผู้จัดการระบบ

> **DRAFT — MACHINE ASR — HUMAN AUDIO/PERMISSION REVIEW REQUIRED**

- **Format:** 9:16 vertical master; 4:5 cutdown only after approval
- **Target duration:** 16s
- **Audience:** ผู้จัดการระบบ/operations ที่สนใจ workflow automation
- **Funnel:** solution-aware / product-aware
- **Ad job:** explain mechanism / prove implementation
- **Risk:** LOW — ASR AMBIGUITY: คำว่า ‘จังตัวนี้’ ต้องฟังเสียงยืนยัน; automation ไม่เท่ากับ workforce reduction และห้ามสื่อว่าทดแทนพนักงาน

### Hook variants — all `brand_copy`

1. **[brand_copy]** ผู้จัดการระบบคนนี้บอกว่าอะไร ‘ว้าวมากที่สุด’?
2. **[brand_copy]** Workflow ที่ทำงานอัตโนมัติ—ฟังคำอธิบายจากผู้เรียน
3. **[brand_copy]** ถ้า AI เข้าไปอยู่ใน workflow งานจริง มุมที่เขาสนใจคืออะไร?

### Master script / timeline

| Ad time | Type | Spoken/on-screen line | Lineage |
|---|---|---|---|
| 00.00–02.50s | `brand_copy` | HOOK (เลือก 1 จาก 3; EDL ใช้ variant 1) | — |
| 02.50–12.44s | `verbatim_quote` | “ที่ว้าวมากที่สุดเลยนะครับ ก็จะเป็น Workflow นะครับ เราสามารถจังตัวนี้ไป แล้วก็ให้เขาทำงานได้โดยอัตโนมัติเลย น่าสนใจมากๆ เลยครับ” | `claim_id=8ecbb8ff-ae3b-55c9-adad-270118e9378c` · `source_video_id=5b11154a541dec4c` · `segment_id=5b11154a541dec4c-segments-3-4` · `source=00:00:17.360–00:00:27.300` · `transcript=asr-mlx-whisper-large-v3-mlx` · `transcript_sha256=d2406c1aa5936ce7a30ffac8f4d13335a72f3d502ca4ba8196fbfdd1ac1f7020` |
| 12.44–16.00s | `brand_copy` | สำรวจ workflow AI ที่เหมาะกับบริบทธุรกิจของคุณ • ไม่มีการรับประกันผลลัพธ์ | — |

### Edit direction

ใช้ motion node → workflow → automation แบบนามธรรม; ห้ามแสดงภาพลดคน/เลิกจ้างหรือเติมงานที่ไม่ได้กล่าว; คง ‘จังตัวนี้’ ตาม ASR

### Required gate before use

- [ ] Human listens to full quoted source range and creates approved human transcript/subclip if needed
- [ ] Speaker identity + paid/organic channel, territory, edit and expiry permissions confirmed
- [ ] Thai captions matched to approved human transcript; no silent ASR correction
- [ ] Claims/risk review completed; no unsupported super, B-roll implication or typicality claim

## 6. W3-A06-690-VS-50 — Subscribe 690 แต่รู้สึกว่าใช้จริงราว 50—คำประเมินของผู้เรียน

> **DRAFT — MACHINE ASR — HUMAN AUDIO/PERMISSION REVIEW REQUIRED**

- **Format:** 9:16 vertical master; 4:5 cutdown only after approval
- **Target duration:** 15s
- **Audience:** เจ้าของ e-commerce ที่จ่ายค่า AI แต่ใช้เพียงพื้นฐาน
- **Funnel:** problem-aware / solution-aware / product-aware
- **Ad job:** stop scroll / answer price-value objection / prove awareness shift
- **Risk:** MEDIUM — PRICE + ESTIMATE + ASR AMBIGUITY: 690/50 บาทเป็นคำประเมินพร้อม qualifier ‘น่าจะ’; ‘อยู่มา 50 บาท’ ต้องฟังเสียง; ห้ามคำนวณ % สูญเปล่าหรือ ROI

### Hook variants — all `brand_copy`

1. **[brand_copy]** Subscribe เดือนละ 690—แต่ผู้เรียนคนนี้ประเมินว่าใช้จริงแค่ไหน?
2. **[brand_copy]** จ่ายค่า AI ทุกเดือน แต่ยังใช้แบบ Basic อยู่หรือเปล่า?
3. **[brand_copy]** ตัวเลข 690 กับ 50 บาท สะท้อนความรู้สึกก่อนเรียนของเขาอย่างไร?

### Master script / timeline

| Ad time | Type | Spoken/on-screen line | Lineage |
|---|---|---|---|
| 00.00–02.50s | `brand_copy` | HOOK (เลือก 1 จาก 3; EDL ใช้ variant 1) | — |
| 02.50–09.74s | `verbatim_quote` | “ปกติผมใช้ AI ค่อนข้างที่จะ Basic มาก Subscribe เดือนละ 690 ใช้จริงๆ น่าจะอยู่มา 50 บาท พอมาวันนี้ปุ๊บมีความรู้สึกว่ามันทำได้มากกว่านี้” | `claim_id=6d08a7e9-62a6-53b6-85ee-059f424f2170` · `source_video_id=b96d350ea9650873` · `segment_id=b96d350ea9650873-segments-0-2` · `source=00:00:00.000–00:00:07.240` · `transcript=asr-mlx-whisper-large-v3-mlx` · `transcript_sha256=eb1e61a148c298e6beebd51b17f2888d7f5431c5e60e0285d95f295931f39910` |
| 09.74–15.00s | `brand_copy` | ดูวิธีเรียนรู้ความสามารถของ AI เพิ่มเติม • ตัวเลขเป็นประสบการณ์และการประเมินเฉพาะบุคคล | — |

### Edit direction

ขึ้นตัวเลขพร้อม label ‘คำประเมินของผู้เรียน: น่าจะ’; ห้ามสร้าง savings/ROI graphic; caption คงคำ ASR ‘อยู่มา 50 บาท’

### Required gate before use

- [ ] Human listens to full quoted source range and creates approved human transcript/subclip if needed
- [ ] Speaker identity + paid/organic channel, territory, edit and expiry permissions confirmed
- [ ] Thai captions matched to approved human transcript; no silent ASR correction
- [ ] Claims/risk review completed; no unsupported super, B-roll implication or typicality claim

## 7. W3-A07-CLASS-DOES-NOT-END — จบคลาสแล้วก็ไม่จบ—Community เพื่อพัฒนาต่อเนื่อง

> **DRAFT — MACHINE ASR — HUMAN AUDIO/PERMISSION REVIEW REQUIRED**

- **Format:** 9:16 vertical master; 4:5 cutdown only after approval
- **Target duration:** 17s
- **Audience:** เจ้าของกิจการที่ต้องการ community หลังจบคลาส
- **Funnel:** product-aware / retargeting / close
- **Ad job:** justify premium / de-risk continuation concern
- **Risk:** LOW — ASR AMBIGUITY: ประโยคท้าย ‘พัฒนาต่อเนื่องได้อย่างต่อไป’ ต้องฟังเสียง; คะแนน ‘เต็มสิบให้ร้อย’ เป็นความเห็น ไม่ใช่ผลลัพธ์ทั่วไป

### Hook variants — all `brand_copy`

1. **[brand_copy]** สำหรับผู้เรียนคนนี้—ทำไม ‘จบคลาสแล้วก็ไม่จบ’?
2. **[brand_copy]** ถ้าคุณไม่อยากเรียนจบแล้วต้องไปต่อคนเดียว ฟังประสบการณ์นี้
3. **[brand_copy]** Community หลังคลาสมีความหมายอย่างไรในคำพูดของผู้เรียนคนนี้?

### Master script / timeline

| Ad time | Type | Spoken/on-screen line | Lineage |
|---|---|---|---|
| 00.00–02.50s | `brand_copy` | HOOK (เลือก 1 จาก 3; EDL ใช้ variant 1) | — |
| 02.50–12.86s | `verbatim_quote` | “ถ้าเต็มสิบให้ร้อยเลยค่ะ เป็น Community ของกรุ๊ป AI ทำให้เราได้เข้ามาพัฒนา AI คือจบคลาสแล้วก็ไม่จบ เราก็สามารถที่จะพัฒนาต่อเนื่องได้อย่างต่อไปด้วยค่ะ” | `claim_id=a5483287-bdc6-5300-936f-421409be8d65` · `source_video_id=1e10049af634d940` · `segment_id=1e10049af634d940-segments-8-10` · `source=00:00:33.080–00:00:43.440` · `transcript=asr-mlx-whisper-large-v3-mlx` · `transcript_sha256=c73c6d09594852ecb454434c2b2fa5cba49c4fde2dcadda7f1b0bf05afbfa364` |
| 12.86–17.00s | `brand_copy` | ดูรายละเอียด Community ของ Limitless Club • ประสบการณ์ขึ้นอยู่กับการมีส่วนร่วมของแต่ละบุคคล | — |

### Edit direction

ใช้ abstract community rings หรือภาพกิจกรรมที่สิทธิ์ครบเท่านั้น; ห้ามรับประกัน support ระยะยาวเกินสิ่งที่ quote กล่าว; คง ASR เดิม

### Required gate before use

- [ ] Human listens to full quoted source range and creates approved human transcript/subclip if needed
- [ ] Speaker identity + paid/organic channel, territory, edit and expiry permissions confirmed
- [ ] Thai captions matched to approved human transcript; no silent ASR correction
- [ ] Claims/risk review completed; no unsupported super, B-roll implication or typicality claim

## Proof-card concepts (internal drafts only)

> **DRAFT — MACHINE ASR — HUMAN AUDIO/PERMISSION REVIEW REQUIRED**

All concepts: 4:5 + 9:16, Midnight Luxe Editorial, `Anonymous / รอสิทธิ์`. Full locked quote used despite the 8–22-word preference because no subclip may be created before human audio review.

### W3-PC01-TIME

- **Headline (`brand_copy`):** เวลาในคำพูดของผู้เรียนหนึ่งคน
- **Exact quote (`verbatim_quote`):** “คนละแบบเลย สามารถเจาะลึก ChatGPT ใช้เวลาแป๊บเดียวในการคิดคอนเทนต์ แล้วก็มีไอเดียไหลมาให้เราโดยที่ละเอียดมาก ย่นย่อระยะเวลา คนปกติทำงาน 8 ชั่วโมง เราทำงานแค่ 3-4 ชั่วโมงคือได้ผลลัพธ์เยอะแล้ว”
- **Lineage:** `claim_id=5483cd46-c21d-5f61-a0ae-aef3626ad8a9` · `source_video_id=f48b609680dc567c` · `segment_id=f48b609680dc567c-segments-3-4` · `source=00:00:17.020–00:00:34.700` · `transcript=asr-mlx-whisper-large-v3-mlx` · `transcript_sha256=6a76fec7e94bfcde1fb3600dda63a26495e638846ba7c68b58f7e6439b047887` · [source deeplink](dropbox-jedienterprise:Limitless%20Club/All%20Reviews/%E0%B8%A3%E0%B8%B8%E0%B9%88%E0%B8%99%207/%E0%B8%A3%E0%B8%B8%E0%B9%88%E0%B8%99%207%20K.Nida.mp4#t=17.020,34.700)
- **Visual:** ใช้เลข 8 ชั่วโมง / 3–4 ชั่วโมงเป็นส่วนหนึ่งของ exact quote เท่านั้น; ไม่ทำ comparison badge หรือ typical-result graphic
- **Footer (`brand_copy`, placeholder):** ผลลัพธ์ขึ้นอยู่กับบริบทและการนำไปใช้ • quantified/atypical claim review required

### W3-PC02-CURATED

- **Headline (`brand_copy`):** เรียนรู้โดยไม่ต้องลองทุกตัวเอง
- **Exact quote (`verbatim_quote`):** “คุ้มมากครับ การที่มาเรียนที่นี่เขาเลือกตัวที่มันดีมาแล้ว เรียนรู้ได้อย่างรวดเร็วดีกว่า ไม่เสียเวลาต้องแบบไปลองหลายๆตัว เอากลับไปประยุกต์กับงานเราได้ทันทีเลยครับ”
- **Lineage:** `claim_id=ff776c98-4c5b-5409-ad93-40308631e243` · `source_video_id=f2238a839d461a07` · `segment_id=f2238a839d461a07-segments-0-2` · `source=00:00:00.000–00:00:08.780` · `transcript=asr-mlx-whisper-large-v3-mlx` · `transcript_sha256=dae107f19a9ca63f5f6e3fd7780f3c828ea6dfa70bf58f796c221f1601454b75` · [source deeplink](dropbox-jedienterprise:Limitless%20Club/All%20Reviews/Review%20Creative%20AI/K.Pupm.mp4#t=0.000,8.780)
- **Visual:** Midnight Luxe Editorial + abstract tool grid; headline เป็น brand_copy แยกจาก quote
- **Footer (`brand_copy`, placeholder):** ประสบการณ์ขึ้นอยู่กับแต่ละบุคคล

### W3-PC03-COMMUNITY

- **Headline (`brand_copy`):** จบคลาสแล้วก็ไม่จบ—ในคำพูดของผู้เรียน
- **Exact quote (`verbatim_quote`):** “ถ้าเต็มสิบให้ร้อยเลยค่ะ เป็น Community ของกรุ๊ป AI ทำให้เราได้เข้ามาพัฒนา AI คือจบคลาสแล้วก็ไม่จบ เราก็สามารถที่จะพัฒนาต่อเนื่องได้อย่างต่อไปด้วยค่ะ”
- **Lineage:** `claim_id=a5483287-bdc6-5300-936f-421409be8d65` · `source_video_id=1e10049af634d940` · `segment_id=1e10049af634d940-segments-8-10` · `source=00:00:33.080–00:00:43.440` · `transcript=asr-mlx-whisper-large-v3-mlx` · `transcript_sha256=c73c6d09594852ecb454434c2b2fa5cba49c4fde2dcadda7f1b0bf05afbfa364` · [source deeplink](dropbox-jedienterprise:Limitless%20Club/All%20Reviews/%E0%B8%A3%E0%B8%B8%E0%B9%88%E0%B8%99%207/3-jedi-%E0%B8%A3%E0%B8%B8%E0%B9%88%E0%B8%997%20k.fern-q.mp4#t=33.080,43.440)
- **Visual:** Midnight Luxe Editorial + community rings; anonymous identity; ภาพคนใช้ได้เมื่อสิทธิ์ครบเท่านั้น
- **Footer (`brand_copy`, placeholder):** ประสบการณ์ขึ้นอยู่กับการมีส่วนร่วมของแต่ละบุคคล

## Montage concepts

> **DRAFT — MACHINE ASR — HUMAN AUDIO/PERMISSION REVIEW REQUIRED**

Montages use full locked ranges and hard cuts with `เสียงจากผู้เรียนอีกคน`; no audio stitch creates a composite sentence. Durations exceed the default 20–35s where necessary because machine-ASR ranges may not be trimmed before human review.

### W3-M01-PRACTICAL-PATHS — 3 เส้นทางจากการเรียนรู้สู่การใช้งานจริง

- **Target duration:** 39s
- **Theme:** การเลือกเครื่องมือ, workflow automation และรูปแบบเรียนที่เข้าใจง่าย/ใช้งานได้จริง
- **Hook (`brand_copy`):** 3 เสียงจากผู้เรียน: จากเลือกเครื่องมือ สู่ workflow และการใช้งานจริง
- **CTA (`brand_copy`):** สำรวจแนวทางเรียนและประยุกต์ AI กับงานของคุณ • ประสบการณ์ขึ้นอยู่กับบริบท
- **Risk:** MEDIUM — มีคำ ASR ที่ต้องตรวจใน 8ec... และ b3f...; ใช้ full claim ranges จึงยาวเกิน default 35s; ห้าม trim จนกว่าจะมี human-approved subclips
- **Clip order:**
  1. “คุ้มมากครับ การที่มาเรียนที่นี่เขาเลือกตัวที่มันดีมาแล้ว เรียนรู้ได้อย่างรวดเร็วดีกว่า ไม่เสียเวลาต้องแบบไปลองหลายๆตัว เอากลับไปประยุกต์กับงานเราได้ทันทีเลยครับ” — `claim_id=ff776c98-4c5b-5409-ad93-40308631e243` · `source_video_id=f2238a839d461a07` · `segment_id=f2238a839d461a07-segments-0-2` · `source=00:00:00.000–00:00:08.780` · `transcript=asr-mlx-whisper-large-v3-mlx` · `transcript_sha256=dae107f19a9ca63f5f6e3fd7780f3c828ea6dfa70bf58f796c221f1601454b75` · [source deeplink](dropbox-jedienterprise:Limitless%20Club/All%20Reviews/Review%20Creative%20AI/K.Pupm.mp4#t=0.000,8.780)
  2. “ที่ว้าวมากที่สุดเลยนะครับ ก็จะเป็น Workflow นะครับ เราสามารถจังตัวนี้ไป แล้วก็ให้เขาทำงานได้โดยอัตโนมัติเลย น่าสนใจมากๆ เลยครับ” — `claim_id=8ecbb8ff-ae3b-55c9-adad-270118e9378c` · `source_video_id=5b11154a541dec4c` · `segment_id=5b11154a541dec4c-segments-3-4` · `source=00:00:17.360–00:00:27.300` · `transcript=asr-mlx-whisper-large-v3-mlx` · `transcript_sha256=d2406c1aa5936ce7a30ffac8f4d13335a72f3d502ca4ba8196fbfdd1ac1f7020` · [source deeplink](dropbox-jedienterprise:Limitless%20Club/All%20Reviews/%E0%B8%A3%E0%B8%B8%E0%B9%88%E0%B8%99%203/ICE.mp4#t=17.360,27.300)
  3. “ตั้งแต่แรก ถ้าประทับใจต้องบอกว่าตั้งแต่แรกเลยนะครับ เป็นวิธีการที่มันค่อนข้างที่เข้าใจง่ายและทำได้จริง บริจารณ์โดยรวมถือว่า ถ้าถามผมแล้วค่อนข้างที่จะเฟรนลี่นะครับ ก็ไม่มีความกดดันนะครับ เป็นการที่เรียนรู้เพื่อใช้งานได้จริง” — `claim_id=b3f89e86-7fff-532a-a891-c2376dddce78` · `source_video_id=b96d350ea9650873` · `segment_id=b96d350ea9650873-segments-8-13` · `source=00:00:30.000–00:00:43.480` · `transcript=asr-mlx-whisper-large-v3-mlx` · `transcript_sha256=eb1e61a148c298e6beebd51b17f2888d7f5431c5e60e0285d95f295931f39910` · [source deeplink](dropbox-jedienterprise:Limitless%20Club/All%20Reviews/%E0%B8%A3%E0%B8%B8%E0%B9%88%E0%B8%99%208/04-JD-%E0%B8%A3%E0%B8%B8%E0%B9%88%E0%B8%998%20K.Keng-Q.mp4#t=30.000,43.480)
- **Edit rule:** hard cut + visual label `เสียงจากผู้เรียนอีกคน` at every speaker change; anonymous labels until rights clear; no trimming before human-approved subclips.

### W3-M02-TIME-AND-SUBSCRIPTION-VALUE — เวลาและค่า Subscription—3 คำพูดที่ต้อง review เข้ม

- **Target duration:** 45s
- **Theme:** เวลาทำงานและความรู้สึกต่อการใช้ค่า AI subscription
- **Hook (`brand_copy`):** เวลา 8 ชั่วโมง, 3–4 ชั่วโมง, 700, 690 และ 50 บาท—ทั้งหมดคือคำพูดจากผู้เรียนแต่ละคน
- **CTA (`brand_copy`):** ดูรายละเอียดการเรียนรู้ AI • ผลลัพธ์และความคุ้มค่าขึ้นอยู่กับแต่ละบุคคล
- **Risk:** HIGH — quantified atypical time claim + price/estimate claims; legal/claims review required; ห้ามรวมตัวเลขเป็นผลลัพธ์เดียวหรือ implied typicality
- **Clip order:**
  1. “คนละแบบเลย สามารถเจาะลึก ChatGPT ใช้เวลาแป๊บเดียวในการคิดคอนเทนต์ แล้วก็มีไอเดียไหลมาให้เราโดยที่ละเอียดมาก ย่นย่อระยะเวลา คนปกติทำงาน 8 ชั่วโมง เราทำงานแค่ 3-4 ชั่วโมงคือได้ผลลัพธ์เยอะแล้ว” — `claim_id=5483cd46-c21d-5f61-a0ae-aef3626ad8a9` · `source_video_id=f48b609680dc567c` · `segment_id=f48b609680dc567c-segments-3-4` · `source=00:00:17.020–00:00:34.700` · `transcript=asr-mlx-whisper-large-v3-mlx` · `transcript_sha256=6a76fec7e94bfcde1fb3600dda63a26495e638846ba7c68b58f7e6439b047887` · [source deeplink](dropbox-jedienterprise:Limitless%20Club/All%20Reviews/%E0%B8%A3%E0%B8%B8%E0%B9%88%E0%B8%99%207/%E0%B8%A3%E0%B8%B8%E0%B9%88%E0%B8%99%207%20K.Nida.mp4#t=17.020,34.700)
  2. “จริง ๆ ใช้ ChatGPT อยู่แล้ว แต่ว่าเหมือนใช้ไม่เต็มประสิทธิภาพ ก็เลยอยากมาเรียนรู้เพิ่มเติม ในการที่จะทำให้เราจ่ายเงินหน้า 700 บาท ให้มันคุ้มค่า 700 ตอนนี้ก็คือใช้ได้เต็มพื้นที่มากขึ้นนะคะ” — `claim_id=78c4ae87-3565-5310-9215-6e593ee168a6` · `source_video_id=fd3b4327c0da8f26` · `segment_id=fd3b4327c0da8f26-segments-2-4` · `source=00:00:12.200–00:00:25.540` · `transcript=asr-mlx-whisper-large-v3-mlx` · `transcript_sha256=4193df9b3d0ec87403cd0032d59c919f3e51b14e81affb648189b509bbe6d2a4` · [source deeplink](dropbox-jedienterprise:Limitless%20Club/All%20Reviews/%E0%B8%A3%E0%B8%B8%E0%B9%88%E0%B8%99%205/K.AOR.mp4#t=12.200,25.540)
  3. “ปกติผมใช้ AI ค่อนข้างที่จะ Basic มาก Subscribe เดือนละ 690 ใช้จริงๆ น่าจะอยู่มา 50 บาท พอมาวันนี้ปุ๊บมีความรู้สึกว่ามันทำได้มากกว่านี้” — `claim_id=6d08a7e9-62a6-53b6-85ee-059f424f2170` · `source_video_id=b96d350ea9650873` · `segment_id=b96d350ea9650873-segments-0-2` · `source=00:00:00.000–00:00:07.240` · `transcript=asr-mlx-whisper-large-v3-mlx` · `transcript_sha256=eb1e61a148c298e6beebd51b17f2888d7f5431c5e60e0285d95f295931f39910` · [source deeplink](dropbox-jedienterprise:Limitless%20Club/All%20Reviews/%E0%B8%A3%E0%B8%B8%E0%B9%88%E0%B8%99%208/04-JD-%E0%B8%A3%E0%B8%B8%E0%B9%88%E0%B8%998%20K.Keng-Q.mp4#t=0.000,7.240)
- **Edit rule:** hard cut + visual label `เสียงจากผู้เรียนอีกคน` at every speaker change; anonymous labels until rights clear; no trimming before human-approved subclips.

## Review handoff

1. Human-listen all seven full ranges; prioritize numeric/price and ASR-ambiguous wording.
2. Claims/legal review: `5483cd46...` (8h→3–4h, atypical), `78c4ae87...` (700), `6d08a7e9...` (690/estimated 50).
3. Workforce safeguard: automation in `8ecbb8ff...` must not be reframed as reducing/replacing people.
4. Confirm speaker identity and paid/organic permission scope, territory, allowed edits and expiry for each source.
5. After approval, regenerate captions and EDL from human-verified ranges; do not overwrite this machine-ASR draft.

---

**DRAFT — MACHINE ASR — HUMAN AUDIO/PERMISSION REVIEW REQUIRED**
