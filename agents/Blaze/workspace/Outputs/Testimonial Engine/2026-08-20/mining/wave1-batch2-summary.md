# Wave 1 Batch 2 — Testimonial Claim Mining Summary

- **Assigned canonical sources:** 6
- **Claims extracted:** 8
- **Sources yielding claims:** 4
- **Sources rejected entirely:** 2
- **Raw score range:** 45.60–69.00
- **Adjusted score range:** 38.76–69.00
- **Publication state:** all `status=extracted`, `permission_gate=unknown`, `human_review_required=true`
- **Transcript state:** machine ASR (`asr-v1`), not human verified

## Per-source results

| Source video ID | Canonical source path | Claims | Decision / note |
|---|---|---:|---|
| `9a811c4563d6e016` | `รีวิวรวม/ADs ใหม่ รีวิแบบสับๆ.mp4` | 0 | Rejected: promotional montage with stitched speakers, Jet-speaking opener, generic praise, and ambiguous speaker/clip lineage. |
| `b84bfe0dfcbcdccf` | `รุ่น 1/แก้ จอย.mp4` | 2 | Retained skill/capability and output-quality claims; exact ASR ambiguity flagged. |
| `eb95af255c5cbceb` | `รุ่น 4/K.TOEY รุ่น4.mp4` | 3 | Retained cost comparison, implementation, and time-to-usability claims; financial/atypical claim is high risk. |
| `0a757aa2f0e07fd6` | `รุ่น 4/แก้ K.Pluem.mp4` | 0 | Rejected: largely generic AI/FOMO language, unclear attribution, long low-content/garbled ASR segment, and no concrete testimonial outcome. |
| `240e0f97ac975865` | `รุ่น 5/K.PUENG.mp4` | 2 | Retained photo-editing skill shift and work-summary use case; causality remains temporal/not explicit. |
| `c0139c22b065e796` | `รุ่น 9/K.JADED.mp4` | 1 | Retained curriculum clarity candidate; rejected weak price reassurance and disconnected 3–4-hour fragment as low-content/context-dependent. |

## QA notes

- Every quote is constructed only from complete, contiguous canonical ASR segment text; no filler removal or quote editing was performed.
- Millisecond bounds are the exact rounded start of the first quoted segment and end of the last quoted segment.
- `transcript_sha256` values match each assigned source manifest and `COMPLETE.json`.
- Canonical source paths are preserved in each claim's source deeplink and score note, and listed exactly above.
- Source-video file SHA-256 was not available in the supplied artifacts; `source_file_sha256` is `null` and each claim carries `SOURCE_FILE_SHA256_NOT_AVAILABLE`. Audio hashes were not substituted for source-file hashes.
- Adjusted scores apply only the stated context-dependency multiplier (1.00 / 0.85). Unknown permission and non-human-verified ASR block publication rather than numerically reducing prioritization scores.
