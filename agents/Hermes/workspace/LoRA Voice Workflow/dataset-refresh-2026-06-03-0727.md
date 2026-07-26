# Jedi LoRA Dataset Refresh
- Started: 2026-06-03T07:27:50
- Finished: 2026-06-03T07:27:51
- Status: ok
- Train examples: 704
- Validation examples: 61
- Total examples: 765
- Project zip: `/Users/njjimac/Documents/Jedi-LoRA-Voice-Workflow.zip` (719,846 bytes)
- Training bundle: `/Users/njjimac/Documents/Jedi-LoRA-Training-Bundle.zip` (719,225 bytes)

## Command outputs
### `bash scripts/hydrate_icloud_sources.sh`
- exit: 0
```
Hydrating: /Users/njjimac/Documents/Jedi Tone of Voice
Hydrating: /Users/njjimac/Documents/Jedi Content/youtube-transcripts
Hydrating: /Users/njjimac/Documents/Obsidian Vault/Apple Notes
Hydrating: /Users/njjimac/Library/Mobile Documents/com~apple~CloudDocs/AI OS/Brand & Content/Transcripts
Hydrating: /Users/njjimac/Library/Mobile Documents/com~apple~CloudDocs/AI OS/Brand & Content/Jedi's YouTube Transcripts
Hydrating: /Users/njjimac/Library/Mobile Documents/com~apple~CloudDocs/AI OS/YouTube Engine/youtube-transcripts
Hydrating: /Users/njjimac/Library/Mobile Documents/com~apple~CloudDocs/AI OS/YouTube Engine/transcripts/jedi
Hydrating: /Users/njjimac/Library/Mobile Documents/com~apple~CloudDocs/AI OS/Limitless Academy/AI Assets/Program Transcripts
Hydrating: /Users/njjimac/Documents/Jedi LoRA Voice Workflow/data/raw
Hydration requested. If many files were offloaded, wait a few minutes, then run: make build-data
```
### `python3 scripts/build_dataset.py --out data/processed --max-files 1000 --chunk-chars 2600 --val-ratio 0.08`
- exit: 0
```
{
  "files": 10,
  "examples": 765,
  "train": 704,
  "val": 61
}
```
### `python3 scripts/profile_corpus.py data/processed/manifest.json`
- exit: 0
```
72 chunks | en | /Users/njjimac/Documents/Jedi Content/youtube-transcripts/8 Insane Claude Code Use Cases (code anything!).en.vtt
-  47 chunks | en | /Users/njjimac/Documents/Jedi Content/youtube-transcripts/Turn Meeting Notes Into Content with AI Agents (Fireflies x Relevance AI Demo).en.srt
-  36 chunks | en | /Users/njjimac/Documents/Jedi Content/youtube-transcripts/2026-01-27 - This is the CHEAPEST and EASIEST way to set up ClawdBot.vtt
-  17 chunks | en | /Users/njjimac/Documents/Jedi Content/youtube-transcripts/2026-01-27 - Why People Are Freaking Out About Clawdbot.txt
-  15 chunks | en | /Users/njjimac/Documents/Jedi Content/youtube-transcripts/2026-01-29 - Turn Meeting Notes Into Content with AI Agents.txt
-   7 chunks | en | /Users/njjimac/Documents/Jedi Content/youtube-transcripts/2026-01-27 - This is the CHEAPEST and EASIEST way to set up ClawdBot.txt
-   1 chunks | en | /Users/njjimac/Documents/Jedi Tone of Voice/Workshop Transcripts/GMT20250327-070656_Recording.transcript.vtt
-   0 chunks | None | /Users/njjimac/Library/Mobile Documents/com~apple~CloudDocs/AI OS/Brand & Content/Jedi's YouTube Transcripts/20251013 - คู่มือสร้างความมั่งคั่งจากคุณ Kim Property Live.th.vtt
-   0 chunks | None | /Users/njjimac/Library/Mobile Documents/com~apple~CloudDocs/AI OS/YouTube Engine/youtube-transcripts/20251013 - คู่มือสร้างความมั่งคั่งจากคุณ Kim Property Live.th.vtt
-   0 chunks | None | /Users/njjimac/Library/Mobile Documents/com~apple~CloudDocs/AI OS/YouTube Engine/youtube-transcripts/20260305 - Meet The Woman Who Built A $3B Beauty Brand from $0 ｜ Anastasia Soare.th.vtt
-   0 chunks | None | /Users/njjimac/Library/Mobile Documents/com~apple~CloudDocs/AI OS/Brand & Content/Jedi's YouTube Transcripts/20251210 - How to Run a $100M Company Working 0 Hours (The Dan Martell Protocol).en.vtt
-   0 chunks | None | /Users/njjimac/Library/Mobile Documents/com~apple~CloudDocs/AI OS/YouTube Engine/youtube-transcripts/20251210 - How to Run a $100M Company Working 0 Hours (The Dan Martell Protocol).en.vtt
-   0 chunks | None | /Users/njjimac/Library/Mobile Documents/com~apple~CloudDocs/AI OS/Brand & Content/Jedi's YouTube Transcripts/20260302 - ได้เวลาย้าย OpenClaw เข้า Mac Studio และ รีวิว หลังจากใช้ มา 30 วัน.th.vtt
-   0 chunks | None | /Users/njjimac/Library/Mobile Documents/com~apple~CloudDocs/AI OS/YouTube Engine/youtube-transcripts/20260302 - ได้เวลาย้าย OpenClaw เข้า Mac Studio และ รีวิว หลังจากใช้ มา 30 วัน.th.vtt
-   0 chunks | None | /Users/njjimac/Library/Mobile Documents/com~apple~CloudDocs/AI OS/Brand & Content/Transcripts/combined-transcripts.md
-   0 chunks | None | /Users/njjimac/Library/Mobile Documents/com~apple~CloudDocs/AI OS/YouTube Engine/youtube-transcripts/20260305 - Meet The Woman Who Built A $3B Beauty Brand from $0 ｜ Anastasia Soare.en.vtt
-   0 chunks | None | /Users/njjimac/Library/Mobile Documents/com~apple~CloudDocs/AI OS/YouTube Engine/youtube-transcripts/corpus/KNyFFKn4IBM___"ค้นพบความมั่นคงทางจิตใจ"กับ คุณกันต์ ลง.th.txt
```
### `python3 scripts/evaluate_voice.py data/processed/train.jsonl`
- exit: 0
```
examples: 704
languages: {'en': 704, 'th': 0}
chars avg/min/max: 2540 487 2600
phrase hits:
- AI: 408
- agent: 58
- business: 39
- system: 35
- founder: 1
- content: 211
```