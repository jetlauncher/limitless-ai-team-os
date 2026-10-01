# DRAFT — WAVE 2 THAI TESTIMONIAL ADS

> **DRAFT — MACHINE ASR — HUMAN AUDIO/PERMISSION REVIEW REQUIRED**
>
> ห้าม render, post, schedule หรือ launch paid media จนกว่าจะผ่าน human audio verification, permission/identity/channel review, claims-risk review และ Jet approval

## Production status and hard rules

- Source of truth: `claims/all_claims.jsonl`; package uses only the seven prioritized Wave 2 claim IDs listed in the claim register below.
- ทุก customer line ใช้ `verbatim_quote` เต็มช่วงจาก claim bank แบบตรงตัว ไม่มีการแก้คำ ตัด filler สลับลำดับ หรือแก้ machine ASR.
- Hook, transition, headline, CTA และ disclaimer เป็น **`brand_copy`**; ต้องแยกจากคำพูดลูกค้าอย่างชัดเจนและห้ามใส่เครื่องหมายคำพูดให้ brand copy.
- Timecodes เป็นช่วงเต็มของ claim. **ห้าม trim หรือสร้าง subclip timecode** จนกว่ามนุษย์จะฟังเสียงและล็อก transcript/subclip ใหม่.
- Customer identity ใช้ `Anonymous / รอสิทธิ์` เท่านั้น เพราะทุก claim มี `permission_gate=unknown`, `human_review_required=true`, `status=extracted`.
- Duration เป็น edit target จากช่วง claim เต็ม + brand cards; ไม่มี asset ใด publishable ในสถานะนี้.
- EDL ครอบคลุมวิดีโอ 7 ชิ้นและ montage 2 ชิ้น; proof cards เป็น static concepts จึงไม่มี timeline row ใน EDL.

## Verified machine-claim register

ตรวจแบบ mechanical แล้ว: พบ 7/7 IDs และค่าด้านล่างตรงกับ `claims/all_claims.jsonl` ณ เวลาสร้างแพ็กเกจ. “Verified” ในส่วนนี้หมายถึง **ตรงกับไฟล์ claim bank เท่านั้น ไม่ใช่ human audio verified**.

| Claim ID | Source / full range | Exact machine-ASR quote | Gate |
|---|---|---|---|
| `17d8b421-c4cf-5d18-952e-5a508e0aa3cb` | `a19dbde2654acd51` · `00:00:13.440–00:00:17.240` | “ใครอายุเท่าไหร่พี่ว่าเรียนได้นะ ทีมซัพพอร์ตเยอะมาก ยังไงก็ทัน” | `status=extracted` · `permission=unknown` · human review required |
| `37a5724a-bb5c-5ad6-a2ef-bf318e5d59e8` | `c876756a76ef95e4` · `00:00:17.680–00:00:37.120` | “ตอนแรกศึกษาจาก TikTok ก็จะได้ความรู้แบบ เข้าๆ ทั่วๆ ไปเลย ไม่เจาะลึก รู้แค่ผิวเผิน ตามกระแสเฉยๆ แต่เราไม่รู้ว่ามันเจาะลึกได้อีก ลงรายละเอียดได้อีก แต่คุณเจไดแนะนำดีมาก การสอนดี หันง่าย เข้าใจง่าย แล้วมีทีมงานช่วยสอนแนะนำอีกทีหนึ่ง” | `status=extracted` · `permission=unknown` · human review required |
| `28900af2-a75e-515c-b589-2ae1f79e3686` | `97080e3a871cac2d` · `00:00:31.260–00:00:40.720` | “สนุกค่ะ ได้เจอพี่ๆที่เป็นผู้ประกอบการท่านอื่นๆด้วยนะคะ ได้แลกเปลี่ยน ได้พูดคุยกัน Make friends กันก็รู้สึกว่าได้ความรู้เรื่อง AI แล้วยังได้ Connection เพิ่มด้วยค่ะ” | `status=extracted` · `permission=unknown` · human review required |
| `4e0b271b-7f0e-595e-87da-6c728fa75d7b` | `a19dbde2654acd51` · `00:00:26.340–00:00:33.500` | “ลดคนต้องได้เยอะ ทำให้การทำงานง่ายขึ้น มันประหยัดเวลา พี่จะได้เอาเวลาที่เหลือ ไปทำในส่วนที่ AI ทำไม่ได้” | `status=extracted` · `permission=unknown` · human review required |
| `935b3429-f4f8-5cd5-8398-4256e2d45189` | `e96086149bf2f572` · `00:00:04.700–00:00:12.880` | “ช่วยในการคัดคน เกี่ยวกับช่วยในการคิดคอนเทนต์อะไรต่างๆ สามารถย่นระยะเวลาที่จะต้องใช้เงิน ใช้คนไปมากเยอะเลยครับ” | `status=extracted` · `permission=unknown` · human review required |
| `25e8b006-cb5d-5e11-bb9f-5bfb423c80d3` | `ad250115e4ac5e31` · `00:00:18.800–00:00:25.940` | “ผมว่าเป็นเรื่องมาร์เก็ตติ้ง มันทำได้ง่าย เอาพร้อมออกมาจาก GPT ใช่ไหมครับ แล้วมาทำต่อ แล้วออกมาเป็นแบบเหมือนเป็นสื่ออะไรอย่างนี้ ได้เร็วมาก” | `status=extracted` · `permission=unknown` · human review required |
| `6d49f118-6fcb-5895-9d4a-000a913dd838` | `19ff652b06cee6f3` · `00:00:09.120–00:00:19.260` | “ตั้งผู้ช่วยในตำแหน่งงานต่างๆ ไม่ว่าจะเป็นทั้งด้าน Financial หรือว่าทั้งด้าน Operation อันนี้ก็ช่วยเราได้มากเลยค่ะ ก็มาเรียนที่นี่ก็เหมือนกับว่าเปิดข้อจำกัดของเรา” | `status=extracted` · `permission=unknown` · human review required |

## 1. W2-A01-FIT-SUPPORT — อายุหรือพื้นฐานไม่ใช่เหตุให้ต้องเรียนคนเดียว

> **DRAFT — MACHINE ASR — HUMAN AUDIO/PERMISSION REVIEW REQUIRED**

- **Format:** 9:16 vertical master; 4:5 cutdown only after approval
- **Target duration:** 15s
- **Audience:** เจ้าของธุรกิจ/ผู้เรียนที่กังวลเรื่องอายุ ความเหมาะสม หรือกลัวตามไม่ทัน
- **Funnel:** solution-aware / retargeting
- **Ad job:** ตอบข้อกังวลเรื่อง fit และ support ด้วยประสบการณ์ของผู้เรียน
- **Risk:** Medium — เป็นความเห็นของผู้เรียนหนึ่งคน; ห้ามขยายเป็นการรับประกันว่าทุกคนจะตามทัน

### Hook variants — all `brand_copy`

1. **[brand_copy]** อายุเท่าไหร่ถึงจะเริ่มเรียน AI ได้? ฟังจากผู้เรียนคนนี้
2. **[brand_copy]** กลัวตามไม่ทัน? นี่คือประสบการณ์เรื่องทีมซัพพอร์ตจากคนเรียน
3. **[brand_copy]** คำถามเรื่องอายุและการตามบทเรียน—ผู้เรียนคนนี้ตอบไว้อย่างไร?

### Master script / timeline

| Ad time | Type | Spoken/on-screen line | Lineage |
|---|---|---|---|
| 00.00–02.50s | `brand_copy` | HOOK (เลือก 1 จาก 3 variants; EDL ใช้ variant 1 เป็น master selection) | — (brand copy; no customer claim) |
| 02.50–06.30s | `verbatim_quote` | “ใครอายุเท่าไหร่พี่ว่าเรียนได้นะ ทีมซัพพอร์ตเยอะมาก ยังไงก็ทัน” | `claim_id=17d8b421-c4cf-5d18-952e-5a508e0aa3cb` · `source_video_id=a19dbde2654acd51` · `segment_id=a19dbde2654acd51-segments-4-5` · `source=00:00:13.440–00:00:17.240` · `transcript=asr-mlx-whisper-large-v3-mlx` · `transcript_sha256=76f5a9688961fc04171ad9bb2755a8eca3aec16aa60efa3624874e7587688e4a` |
| 06.30–15.00s | `brand_copy` | ดูรูปแบบการเรียนและการซัพพอร์ตของ Limitless Club • ประสบการณ์ขึ้นอยู่กับแต่ละบุคคล | — (brand copy; no customer claim) |

### Edit direction

Talking head เต็มเฟรม; caption เน้นเฉพาะคำในเสียง “ทีมซัพพอร์ตเยอะมาก” และ “ยังไงก็ทัน”; ห้ามขึ้น super ว่าเหมาะกับทุกวัยในฐานะข้อเท็จจริงของแบรนด์.

### Required gate before use

- [ ] Human listens to the full quoted source range and creates an approved human transcript/subclip if needed
- [ ] Customer/speaker identity and paid/organic permissions confirmed for channel, territory, edits and expiry
- [ ] Exact Thai captions matched to the approved human transcript
- [ ] Claims/risk review complete; no unsupported supers, B-roll implication or typicality claim

## 2. W2-A02-TIKTOK-TO-DEPTH — จากความรู้ผิวเผิน สู่การเห็นรายละเอียดมากขึ้น

> **DRAFT — MACHINE ASR — HUMAN AUDIO/PERMISSION REVIEW REQUIRED**

- **Format:** 9:16 vertical master; 4:5 cutdown only after approval
- **Target duration:** 27s
- **Audience:** ผู้เริ่มต้นที่เรียนจาก TikTok/คอนเทนต์สั้นแล้วรู้สึกว่ายังไม่ลึก
- **Funnel:** problem-aware / solution-aware
- **Ad job:** เปรียบเทียบประสบการณ์เรียนเองจาก TikTok กับการสอนและทีมช่วยสอน
- **Risk:** Medium — comparison เป็นประสบการณ์เฉพาะบุคคล; คงคำ ASR “หันง่าย” จนกว่าจะตรวจเสียง

### Hook variants — all `brand_copy`

1. **[brand_copy]** ดู TikTok มาหลายคลิป แต่ยังรู้สึกว่าได้แค่ผิวเผินไหม?
2. **[brand_copy]** จากความรู้ตามกระแส—ผู้เรียนคนนี้เห็นอะไรเพิ่มขึ้น?
3. **[brand_copy]** เรียนจากคอนเทนต์สั้นกับเรียนแบบมีทีมช่วยสอน ต่างกันอย่างไรในมุมของเธอ?

### Master script / timeline

| Ad time | Type | Spoken/on-screen line | Lineage |
|---|---|---|---|
| 00.00–02.50s | `brand_copy` | HOOK (เลือก 1 จาก 3 variants; EDL ใช้ variant 1 เป็น master selection) | — (brand copy; no customer claim) |
| 02.50–21.94s | `verbatim_quote` | “ตอนแรกศึกษาจาก TikTok ก็จะได้ความรู้แบบ เข้าๆ ทั่วๆ ไปเลย ไม่เจาะลึก รู้แค่ผิวเผิน ตามกระแสเฉยๆ แต่เราไม่รู้ว่ามันเจาะลึกได้อีก ลงรายละเอียดได้อีก แต่คุณเจไดแนะนำดีมาก การสอนดี หันง่าย เข้าใจง่าย แล้วมีทีมงานช่วยสอนแนะนำอีกทีหนึ่ง” | `claim_id=37a5724a-bb5c-5ad6-a2ef-bf318e5d59e8` · `source_video_id=c876756a76ef95e4` · `segment_id=c876756a76ef95e4-segments-6-12` · `source=00:00:17.680–00:00:37.120` · `transcript=asr-mlx-whisper-large-v3-mlx` · `transcript_sha256=489efad99b8bfe928bfb169b70b8861cd9d2213284151779d48ce0a17fec83f4` |
| 21.94–27.00s | `brand_copy` | อยากเรียน AI แบบลงรายละเอียดมากขึ้น? • ดูรายละเอียด Limitless Club | — (brand copy; no customer claim) |

### Edit direction

ใช้ visual split “ศึกษาจาก TikTok” / “การสอน + ทีมช่วยสอน” เป็น brand labels เท่านั้น; subtitle ต้องคงถ้อยคำเต็มและห้ามแก้ “หันง่าย” ก่อนฟังเสียง.

### Required gate before use

- [ ] Human listens to the full quoted source range and creates an approved human transcript/subclip if needed
- [ ] Customer/speaker identity and paid/organic permissions confirmed for channel, territory, edits and expiry
- [ ] Exact Thai captions matched to the approved human transcript
- [ ] Claims/risk review complete; no unsupported supers, B-roll implication or typicality claim

## 3. W2-A03-COMMUNITY-CONNECTION — ได้ทั้งความรู้ AI และ Connection

> **DRAFT — MACHINE ASR — HUMAN AUDIO/PERMISSION REVIEW REQUIRED**

- **Format:** 9:16 vertical master; 4:5 cutdown only after approval
- **Target duration:** 17s
- **Audience:** ผู้ประกอบการ/มืออาชีพที่มองหาการเรียนรู้พร้อมเครือข่าย
- **Funnel:** product-aware / retargeting / close
- **Ad job:** พิสูจน์ community/network value ตามคำผู้เรียน
- **Risk:** Low–Medium — ประสบการณ์ด้าน community; ไม่รับประกัน connection ทางธุรกิจหรือผลลัพธ์จากเครือข่าย

### Hook variants — all `brand_copy`

1. **[brand_copy]** มาเรียน AI แล้วได้อะไรนอกจากเนื้อหา?
2. **[brand_copy]** ผู้เรียนคนนี้พูดถึงทั้งความรู้ AI และ Connection
3. **[brand_copy]** ถ้าคุณอยากเรียนพร้อมเจอผู้ประกอบการคนอื่น—ฟังประสบการณ์นี้

### Master script / timeline

| Ad time | Type | Spoken/on-screen line | Lineage |
|---|---|---|---|
| 00.00–02.50s | `brand_copy` | HOOK (เลือก 1 จาก 3 variants; EDL ใช้ variant 1 เป็น master selection) | — (brand copy; no customer claim) |
| 02.50–11.96s | `verbatim_quote` | “สนุกค่ะ ได้เจอพี่ๆที่เป็นผู้ประกอบการท่านอื่นๆด้วยนะคะ ได้แลกเปลี่ยน ได้พูดคุยกัน Make friends กันก็รู้สึกว่าได้ความรู้เรื่อง AI แล้วยังได้ Connection เพิ่มด้วยค่ะ” | `claim_id=28900af2-a75e-515c-b589-2ae1f79e3686` · `source_video_id=97080e3a871cac2d` · `segment_id=97080e3a871cac2d-segments-9-11` · `source=00:00:31.260–00:00:40.720` · `transcript=asr-mlx-whisper-large-v3-mlx` · `transcript_sha256=bbcf893afaf0947896131878f198996071f4d599007860d2543b73b085497e1b` |
| 11.96–17.00s | `brand_copy` | เรียนรู้ AI ท่ามกลางผู้ประกอบการหลากหลายประสบการณ์ • ดูรายละเอียดรุ่นถัดไป | — (brand copy; no customer claim) |

### Edit direction

ใช้ B-roll บรรยากาศแลกเปลี่ยนโดยไม่เปิดเผยใบหน้าจนกว่าสิทธิ์ครบ; แยกคำ English ใน caption ตามเสียง “Make friends” / “Connection”.

### Required gate before use

- [ ] Human listens to the full quoted source range and creates an approved human transcript/subclip if needed
- [ ] Customer/speaker identity and paid/organic permissions confirmed for channel, territory, edits and expiry
- [ ] Exact Thai captions matched to the approved human transcript
- [ ] Claims/risk review complete; no unsupported supers, B-roll implication or typicality claim

## 4. W2-A04-TIME-FOR-HUMAN-WORK — ประหยัดเวลาไว้ทำสิ่งที่ AI ทำไม่ได้

> **DRAFT — MACHINE ASR — HUMAN AUDIO/PERMISSION REVIEW REQUIRED**

- **Format:** 9:16 vertical master; 4:5 cutdown only after approval
- **Target duration:** 15s
- **Audience:** เจ้าของธุรกิจที่มีงานปฏิบัติการและต้องจัดสรรเวลาทีม
- **Funnel:** problem-aware / solution-aware
- **Ad job:** แสดง outcome เรื่องงานง่ายขึ้นและเวลาที่เหลือสำหรับงานมนุษย์
- **Risk:** HIGH — มีถ้อยคำ workforce reduction “ลดคน”; ต้องตรวจบริบท/เสียง/claims/legal และห้ามสื่อว่าเลิกจ้างหรือรับประกันลดต้นทุน

### Hook variants — all `brand_copy`

1. **[brand_copy]** ถ้า AI ช่วยคืนเวลาให้เจ้าของธุรกิจ—เวลานั้นควรไปอยู่ตรงไหน?
2. **[brand_copy]** ผู้เรียนคนนี้อยากเอาเวลาที่เหลือไปทำอะไร?
3. **[brand_copy]** ฟังมุมมองตรงๆ เรื่องงานง่ายขึ้น เวลา และสิ่งที่ AI ทำไม่ได้

### Master script / timeline

| Ad time | Type | Spoken/on-screen line | Lineage |
|---|---|---|---|
| 00.00–02.50s | `brand_copy` | HOOK (เลือก 1 จาก 3 variants; EDL ใช้ variant 1 เป็น master selection) | — (brand copy; no customer claim) |
| 02.50–09.66s | `verbatim_quote` | “ลดคนต้องได้เยอะ ทำให้การทำงานง่ายขึ้น มันประหยัดเวลา พี่จะได้เอาเวลาที่เหลือ ไปทำในส่วนที่ AI ทำไม่ได้” | `claim_id=4e0b271b-7f0e-595e-87da-6c728fa75d7b` · `source_video_id=a19dbde2654acd51` · `segment_id=a19dbde2654acd51-segments-9-11` · `source=00:00:26.340–00:00:33.500` · `transcript=asr-mlx-whisper-large-v3-mlx` · `transcript_sha256=76f5a9688961fc04171ad9bb2755a8eca3aec16aa60efa3624874e7587688e4a` |
| 09.66–15.00s | `brand_copy` | สำรวจแนวทางใช้ AI กับงานธุรกิจ • ผลลัพธ์ขึ้นอยู่กับบริบทและการนำไปใช้ | — (brand copy; no customer claim) |

### Edit direction

เปิดด้วยภาพงานซ้ำเชิงนามธรรม; ห้ามใช้ภาพพนักงานถูกแทนที่/เลิกจ้าง; caption ต้องรักษาคำ “ลดคนต้องได้เยอะ” พร้อมบริบทต่อเนื่องทั้ง claim.

### Required gate before use

- [ ] Human listens to the full quoted source range and creates an approved human transcript/subclip if needed
- [ ] Customer/speaker identity and paid/organic permissions confirmed for channel, territory, edits and expiry
- [ ] Exact Thai captions matched to the approved human transcript
- [ ] Claims/risk review complete; no unsupported supers, B-roll implication or typicality claim

## 5. W2-A05-HR-CONTENT-EFFICIENCY — Use case เดียว แตะทั้งคัดคนและคอนเทนต์

> **DRAFT — MACHINE ASR — HUMAN AUDIO/PERMISSION REVIEW REQUIRED**

- **Format:** 9:16 vertical master; 4:5 cutdown only after approval
- **Target duration:** 16s
- **Audience:** เจ้าของธุรกิจที่ดูแลงาน HR และคอนเทนต์
- **Funnel:** problem-aware / solution-aware
- **Ad job:** แสดง use cases และ qualitative time/cost/team efficiency จากคำลูกค้า
- **Risk:** HIGH — cost/workforce claim แบบไม่ระบุตัวเลขหรือฐานเปรียบเทียบ; ต้อง claims/legal review และห้ามสร้างตัวเลขประหยัด

### Hook variants — all `brand_copy`

1. **[brand_copy]** AI ในธุรกิจเดียว ช่วยแตะทั้ง HR และคอนเทนต์ได้อย่างไร?
2. **[brand_copy]** เจ้าของธุรกิจคนนี้พูดถึงการคัดคน คอนเทนต์ และเวลาที่ใช้
3. **[brand_copy]** ถ้างาน HR กับคอนเทนต์กินทั้งเวลา เงิน และคน—ฟัง use case นี้

### Master script / timeline

| Ad time | Type | Spoken/on-screen line | Lineage |
|---|---|---|---|
| 00.00–02.50s | `brand_copy` | HOOK (เลือก 1 จาก 3 variants; EDL ใช้ variant 1 เป็น master selection) | — (brand copy; no customer claim) |
| 02.50–10.68s | `verbatim_quote` | “ช่วยในการคัดคน เกี่ยวกับช่วยในการคิดคอนเทนต์อะไรต่างๆ สามารถย่นระยะเวลาที่จะต้องใช้เงิน ใช้คนไปมากเยอะเลยครับ” | `claim_id=935b3429-f4f8-5cd5-8398-4256e2d45189` · `source_video_id=e96086149bf2f572` · `segment_id=e96086149bf2f572-segments-2-3` · `source=00:00:04.700–00:00:12.880` · `transcript=asr-mlx-whisper-large-v3-mlx` · `transcript_sha256=4ed18740c10d23620c856cba49a9403322fe961dd961a57a8e15404fd9a8380b` |
| 10.68–16.00s | `brand_copy` | ดูตัวอย่างการประยุกต์ AI กับงานธุรกิจ • ไม่มีการรับประกันผลลัพธ์ | — (brand copy; no customer claim) |

### Edit direction

ใช้ icon/workflow HR → Content โดยไม่โชว์ตัวเลขหรือกราฟต้นทุน; คำ “ใช้เงิน ใช้คน” ต้องอยู่ใน quote เดิม ไม่ทำเป็น headline brand claim.

### Required gate before use

- [ ] Human listens to the full quoted source range and creates an approved human transcript/subclip if needed
- [ ] Customer/speaker identity and paid/organic permissions confirmed for channel, territory, edits and expiry
- [ ] Exact Thai captions matched to the approved human transcript
- [ ] Claims/risk review complete; no unsupported supers, B-roll implication or typicality claim

## 6. W2-A06-GPT-TO-MEDIA — จาก GPT ไปสู่สื่อได้เร็วมาก

> **DRAFT — MACHINE ASR — HUMAN AUDIO/PERMISSION REVIEW REQUIRED**

- **Format:** 9:16 vertical master; 4:5 cutdown only after approval
- **Target duration:** 15s
- **Audience:** เจ้าของร้าน/ธุรกิจที่ต้องทำมาร์เก็ตติ้งและคอนเทนต์
- **Funnel:** solution-aware / product-aware
- **Ad job:** แสดง workflow จาก GPT ไปต่อเป็นสื่อและความเร็วตามประสบการณ์ผู้เรียน
- **Risk:** Medium — qualitative speed claim; ASR คำ “พร้อม” อาจหมายถึง “พรอมต์” ต้อง human audio check ก่อน caption/render

### Hook variants — all `brand_copy`

1. **[brand_copy]** จาก GPT ไปเป็นสื่อ—ผู้เรียนคนนี้ทำต่ออย่างไร?
2. **[brand_copy]** งานมาร์เก็ตติ้งแบบไหนที่เขาบอกว่า “ได้เร็วมาก”?
3. **[brand_copy]** ถ้ามี output จาก GPT แล้ว ขั้นต่อไปจะกลายเป็นสื่อได้อย่างไร?

### Master script / timeline

| Ad time | Type | Spoken/on-screen line | Lineage |
|---|---|---|---|
| 00.00–02.50s | `brand_copy` | HOOK (เลือก 1 จาก 3 variants; EDL ใช้ variant 1 เป็น master selection) | — (brand copy; no customer claim) |
| 02.50–09.64s | `verbatim_quote` | “ผมว่าเป็นเรื่องมาร์เก็ตติ้ง มันทำได้ง่าย เอาพร้อมออกมาจาก GPT ใช่ไหมครับ แล้วมาทำต่อ แล้วออกมาเป็นแบบเหมือนเป็นสื่ออะไรอย่างนี้ ได้เร็วมาก” | `claim_id=25e8b006-cb5d-5e11-bb9f-5bfb423c80d3` · `source_video_id=ad250115e4ac5e31` · `segment_id=ad250115e4ac5e31-segments-7-10` · `source=00:00:18.800–00:00:25.940` · `transcript=asr-mlx-whisper-large-v3-mlx` · `transcript_sha256=684e84856af9c6813a7e7b2a031e523fc6b08c982401fd6ce8302551faf8248c` |
| 09.64–15.00s | `brand_copy` | เรียนรู้ workflow AI สำหรับมาร์เก็ตติ้งและคอนเทนต์ • ดูรายละเอียด Limitless Club | — (brand copy; no customer claim) |

### Edit direction

Motion flow GPT → ทำต่อ → สื่อ; ห้ามแก้คำ “พร้อม” เป็น “พรอมต์” ใน subtitle จนกว่ามนุษย์จะยืนยันเสียง; ไม่แสดงเวลาตัวเลข.

### Required gate before use

- [ ] Human listens to the full quoted source range and creates an approved human transcript/subclip if needed
- [ ] Customer/speaker identity and paid/organic permissions confirmed for channel, territory, edits and expiry
- [ ] Exact Thai captions matched to the approved human transcript
- [ ] Claims/risk review complete; no unsupported supers, B-roll implication or typicality claim

## 7. W2-A07-FINANCE-OPS-ASSISTANTS — ตั้งผู้ช่วยสำหรับ Financial และ Operation

> **DRAFT — MACHINE ASR — HUMAN AUDIO/PERMISSION REVIEW REQUIRED**

- **Format:** 9:16 vertical master; 4:5 cutdown only after approval
- **Target duration:** 18s
- **Audience:** เจ้าของร้าน/SME ที่ต้องดูทั้งการเงินและปฏิบัติการ
- **Funnel:** solution-aware / product-aware
- **Ad job:** แสดง implementation idea เรื่องตั้งผู้ช่วยตามตำแหน่งงาน
- **Risk:** Medium — “ช่วยเราได้มาก” เป็นประสบการณ์ qualitative; ห้ามทำให้ดูเป็นระบบอัตโนมัติเต็มรูปแบบหรือผลลัพธ์ที่ยืนยันด้วยตัวเลข

### Hook variants — all `brand_copy`

1. **[brand_copy]** เจ้าของร้านคนนี้ตั้งผู้ช่วย AI ไว้ตรงไหนบ้าง?
2. **[brand_copy]** Financial กับ Operation—สองงานที่ผู้เรียนคนนี้พูดถึง
3. **[brand_copy]** ถ้าตั้งผู้ช่วยตามตำแหน่งงานได้ คุณจะเริ่มที่ส่วนไหน?

### Master script / timeline

| Ad time | Type | Spoken/on-screen line | Lineage |
|---|---|---|---|
| 00.00–02.50s | `brand_copy` | HOOK (เลือก 1 จาก 3 variants; EDL ใช้ variant 1 เป็น master selection) | — (brand copy; no customer claim) |
| 02.50–12.64s | `verbatim_quote` | “ตั้งผู้ช่วยในตำแหน่งงานต่างๆ ไม่ว่าจะเป็นทั้งด้าน Financial หรือว่าทั้งด้าน Operation อันนี้ก็ช่วยเราได้มากเลยค่ะ ก็มาเรียนที่นี่ก็เหมือนกับว่าเปิดข้อจำกัดของเรา” | `claim_id=6d49f118-6fcb-5895-9d4a-000a913dd838` · `source_video_id=19ff652b06cee6f3` · `segment_id=19ff652b06cee6f3-segments-2-3` · `source=00:00:09.120–00:00:19.260` · `transcript=asr-mlx-whisper-large-v3-mlx` · `transcript_sha256=e4d10fdf55664ea22184a7a2917711ef76e388311fe6f22735f804c6c9211ab0` |
| 12.64–18.00s | `brand_copy` | สำรวจวิธีออกแบบผู้ช่วย AI ให้เหมาะกับงานของคุณ • ดูรายละเอียดรุ่นถัดไป | — (brand copy; no customer claim) |

### Edit direction

ใช้ two-column “Financial” / “Operation” ซึ่งเป็นคำใน quote; ห้ามเติมฟังก์ชัน ระบบ หรือผลลัพธ์ที่ลูกค้าไม่ได้กล่าว.

### Required gate before use

- [ ] Human listens to the full quoted source range and creates an approved human transcript/subclip if needed
- [ ] Customer/speaker identity and paid/organic permissions confirmed for channel, territory, edits and expiry
- [ ] Exact Thai captions matched to the approved human transcript
- [ ] Claims/risk review complete; no unsupported supers, B-roll implication or typicality claim

## Proof-card concepts (internal draft concepts only)

> **DRAFT — MACHINE ASR — HUMAN AUDIO/PERMISSION REVIEW REQUIRED**

All concepts: 4:5 + 9:16, Midnight Luxe Editorial, `Anonymous / รอสิทธิ์`, production-only lineage slug. Headlines/footers are `brand_copy`; only the text labeled Exact quote is customer speech.

### W2-PC01-FIT

- **Headline (`brand_copy`):** เรียน AI โดยไม่ต้องถูกทิ้งไว้ข้างหลัง
- **Exact quote (`verbatim_quote`):** “ใครอายุเท่าไหร่พี่ว่าเรียนได้นะ ทีมซัพพอร์ตเยอะมาก ยังไงก็ทัน”
- **Lineage:** `claim_id=17d8b421-c4cf-5d18-952e-5a508e0aa3cb` · `source_video_id=a19dbde2654acd51` · `segment_id=a19dbde2654acd51-segments-4-5` · `source=00:00:13.440–00:00:17.240` · `transcript=asr-mlx-whisper-large-v3-mlx` · `transcript_sha256=76f5a9688961fc04171ad9bb2755a8eca3aec16aa60efa3624874e7587688e4a`
- **Visual:** Midnight navy field, oversized support-ring motif, compact quote block; no age icons that imply a guaranteed universal fit.
- **Footer (`brand_copy`, placeholder):** `ประสบการณ์และผลลัพธ์ขึ้นอยู่กับบริบทของแต่ละบุคคล` — legal review required

### W2-PC02-COMMUNITY

- **Headline (`brand_copy`):** ความรู้ AI + Connection ในคำพูดของผู้เรียน
- **Exact quote (`verbatim_quote`):** “สนุกค่ะ ได้เจอพี่ๆที่เป็นผู้ประกอบการท่านอื่นๆด้วยนะคะ ได้แลกเปลี่ยน ได้พูดคุยกัน Make friends กันก็รู้สึกว่าได้ความรู้เรื่อง AI แล้วยังได้ Connection เพิ่มด้วยค่ะ”
- **Lineage:** `claim_id=28900af2-a75e-515c-b589-2ae1f79e3686` · `source_video_id=97080e3a871cac2d` · `segment_id=97080e3a871cac2d-segments-9-11` · `source=00:00:31.260–00:00:40.720` · `transcript=asr-mlx-whisper-large-v3-mlx` · `transcript_sha256=bbcf893afaf0947896131878f198996071f4d599007860d2543b73b085497e1b`
- **Visual:** Editorial group-light texture with abstract silhouettes only until attendee/image rights are confirmed.
- **Footer (`brand_copy`, placeholder):** `ประสบการณ์และผลลัพธ์ขึ้นอยู่กับบริบทของแต่ละบุคคล` — legal review required

### W2-PC03-HUMAN-TIME

- **Headline (`brand_copy`):** เก็บเวลาไว้ทำส่วนที่ AI ทำไม่ได้
- **Exact quote (`verbatim_quote`):** “ลดคนต้องได้เยอะ ทำให้การทำงานง่ายขึ้น มันประหยัดเวลา พี่จะได้เอาเวลาที่เหลือ ไปทำในส่วนที่ AI ทำไม่ได้”
- **Lineage:** `claim_id=4e0b271b-7f0e-595e-87da-6c728fa75d7b` · `source_video_id=a19dbde2654acd51` · `segment_id=a19dbde2654acd51-segments-9-11` · `source=00:00:26.340–00:00:33.500` · `transcript=asr-mlx-whisper-large-v3-mlx` · `transcript_sha256=76f5a9688961fc04171ad9bb2755a8eca3aec16aa60efa3624874e7587688e4a`
- **Visual:** Split visual: automated task lane vs human judgment lane; never depict layoffs or workforce replacement.
- **Footer (`brand_copy`, placeholder):** `ประสบการณ์และผลลัพธ์ขึ้นอยู่กับบริบทของแต่ละบุคคล` — legal review required

## Montage concepts

> **DRAFT — MACHINE ASR — HUMAN AUDIO/PERMISSION REVIEW REQUIRED**

ทุก montage ใช้ claim ranges เต็มและ hard cut ระหว่างผู้พูด; ห้ามทำ audio stitch ให้ฟังเป็นประโยคเดียว.

### W2-M01-BUSINESS-IMPLEMENTATION — 3 เจ้าของธุรกิจ — AI กับงานจริง

- **Target duration:** 33s
- **Theme:** implementation ในงานธุรกิจ: ตั้งผู้ช่วย, ทำสื่อ, คัดคน/คิดคอนเทนต์
- **Hook (`brand_copy`):** 3 มุมจากเจ้าของธุรกิจ: พวกเขาเห็น AI ไปอยู่ตรงไหนในงานจริง?
- **CTA (`brand_copy`):** ดูแนวทางประยุกต์ AI กับงานธุรกิจของคุณ • ผลลัพธ์ขึ้นอยู่กับบริบท
- **Risk:** HIGH — มี cost/workforce language ใน claim 935b...; ทั้งสามคนต้องผ่านสิทธิ์ paid/organic และ claims review แยกกัน.
- **Clip order:**
  1. “ตั้งผู้ช่วยในตำแหน่งงานต่างๆ ไม่ว่าจะเป็นทั้งด้าน Financial หรือว่าทั้งด้าน Operation อันนี้ก็ช่วยเราได้มากเลยค่ะ ก็มาเรียนที่นี่ก็เหมือนกับว่าเปิดข้อจำกัดของเรา” — `claim_id=6d49f118-6fcb-5895-9d4a-000a913dd838` · `source_video_id=19ff652b06cee6f3` · `segment_id=19ff652b06cee6f3-segments-2-3` · `source=00:00:09.120–00:00:19.260` · `transcript=asr-mlx-whisper-large-v3-mlx` · `transcript_sha256=e4d10fdf55664ea22184a7a2917711ef76e388311fe6f22735f804c6c9211ab0`
  2. “ผมว่าเป็นเรื่องมาร์เก็ตติ้ง มันทำได้ง่าย เอาพร้อมออกมาจาก GPT ใช่ไหมครับ แล้วมาทำต่อ แล้วออกมาเป็นแบบเหมือนเป็นสื่ออะไรอย่างนี้ ได้เร็วมาก” — `claim_id=25e8b006-cb5d-5e11-bb9f-5bfb423c80d3` · `source_video_id=ad250115e4ac5e31` · `segment_id=ad250115e4ac5e31-segments-7-10` · `source=00:00:18.800–00:00:25.940` · `transcript=asr-mlx-whisper-large-v3-mlx` · `transcript_sha256=684e84856af9c6813a7e7b2a031e523fc6b08c982401fd6ce8302551faf8248c`
  3. “ช่วยในการคัดคน เกี่ยวกับช่วยในการคิดคอนเทนต์อะไรต่างๆ สามารถย่นระยะเวลาที่จะต้องใช้เงิน ใช้คนไปมากเยอะเลยครับ” — `claim_id=935b3429-f4f8-5cd5-8398-4256e2d45189` · `source_video_id=e96086149bf2f572` · `segment_id=e96086149bf2f572-segments-2-3` · `source=00:00:04.700–00:00:12.880` · `transcript=asr-mlx-whisper-large-v3-mlx` · `transcript_sha256=4ed18740c10d23620c856cba49a9403322fe961dd961a57a8e15404fd9a8380b`
- **Edit rule:** hard cut + visual label `เสียงจากผู้เรียนอีกคน` at every speaker change; anonymous label until identity rights clear.

### W2-M02-EASIER-FASTER-WORK — 3 เสียงเรื่องงานง่ายขึ้นและเวลา

- **Target duration:** 28s
- **Theme:** qualitative speed/time/workflow efficiency ตามประสบการณ์ผู้เรียน
- **Hook (`brand_copy`):** เมื่อ AI เข้าไปอยู่ใน workflow—คนเรียนสามคนพูดเรื่องเวลาไว้อย่างไร?
- **CTA (`brand_copy`):** สำรวจ workflow AI ที่เหมาะกับธุรกิจคุณ • ไม่มีการรับประกันผลลัพธ์
- **Risk:** HIGH — workforce/cost language และ qualitative speed claims; ห้ามใส่ตัวเลขประหยัดหรือสรุปว่าผลเป็นค่ามาตรฐาน.
- **Clip order:**
  1. “ลดคนต้องได้เยอะ ทำให้การทำงานง่ายขึ้น มันประหยัดเวลา พี่จะได้เอาเวลาที่เหลือ ไปทำในส่วนที่ AI ทำไม่ได้” — `claim_id=4e0b271b-7f0e-595e-87da-6c728fa75d7b` · `source_video_id=a19dbde2654acd51` · `segment_id=a19dbde2654acd51-segments-9-11` · `source=00:00:26.340–00:00:33.500` · `transcript=asr-mlx-whisper-large-v3-mlx` · `transcript_sha256=76f5a9688961fc04171ad9bb2755a8eca3aec16aa60efa3624874e7587688e4a`
  2. “ผมว่าเป็นเรื่องมาร์เก็ตติ้ง มันทำได้ง่าย เอาพร้อมออกมาจาก GPT ใช่ไหมครับ แล้วมาทำต่อ แล้วออกมาเป็นแบบเหมือนเป็นสื่ออะไรอย่างนี้ ได้เร็วมาก” — `claim_id=25e8b006-cb5d-5e11-bb9f-5bfb423c80d3` · `source_video_id=ad250115e4ac5e31` · `segment_id=ad250115e4ac5e31-segments-7-10` · `source=00:00:18.800–00:00:25.940` · `transcript=asr-mlx-whisper-large-v3-mlx` · `transcript_sha256=684e84856af9c6813a7e7b2a031e523fc6b08c982401fd6ce8302551faf8248c`
  3. “ช่วยในการคัดคน เกี่ยวกับช่วยในการคิดคอนเทนต์อะไรต่างๆ สามารถย่นระยะเวลาที่จะต้องใช้เงิน ใช้คนไปมากเยอะเลยครับ” — `claim_id=935b3429-f4f8-5cd5-8398-4256e2d45189` · `source_video_id=e96086149bf2f572` · `segment_id=e96086149bf2f572-segments-2-3` · `source=00:00:04.700–00:00:12.880` · `transcript=asr-mlx-whisper-large-v3-mlx` · `transcript_sha256=4ed18740c10d23620c856cba49a9403322fe961dd961a57a8e15404fd9a8380b`
- **Edit rule:** hard cut + visual label `เสียงจากผู้เรียนอีกคน` at every speaker change; anonymous label until identity rights clear.

## Review handoff

1. Human-listen all seven full source ranges; correct machine ASR only by creating a reviewed transcript/claim version—never by silently editing this package.
2. Prioritize audio checks for `37a5724a...` (“หันง่าย”) and `25e8b006...` (“พร้อม”) because wording may be ASR-sensitive.
3. Run claims/legal review on `4e0b271b...` and `935b3429...` before any use because they include workforce/cost language.
4. Confirm each speaker is the customer and snapshot paid/organic channel, identity, territory, edit and expiry permissions.
5. After approval, regenerate captions and EDL from human-verified timecodes; do not overwrite this machine-ASR draft.

---

**DRAFT — MACHINE ASR — HUMAN AUDIO/PERMISSION REVIEW REQUIRED**
