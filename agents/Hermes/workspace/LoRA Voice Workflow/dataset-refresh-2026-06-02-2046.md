# Jedi LoRA Dataset Refresh
- Started: 2026-06-02T20:46:39
- Finished: 2026-06-02T20:46:40
- Status: ok
- Train examples: 36
- Validation examples: 3
- Total examples: 39
- Project zip: `/Users/njjimac/Documents/Jedi-LoRA-Voice-Workflow.zip` (186,075 bytes)
- Training bundle: `/Users/njjimac/Documents/Jedi-LoRA-Training-Bundle.zip` (185,454 bytes)

## Command outputs
### `bash scripts/hydrate_icloud_sources.sh`
- exit: 0
```
Hydrating: /Users/njjimac/Documents/Jedi Tone of Voice
Hydrating: /Users/njjimac/Documents/Jedi Content/youtube-transcripts
Hydrating: /Users/njjimac/Documents/Obsidian Vault/Apple Notes
Hydrating: /Users/njjimac/Documents/Jedi LoRA Voice Workflow/data/raw
Hydration requested. If many files were offloaded, wait a few minutes, then run: make build-data
```
### `python3 scripts/build_dataset.py --out data/processed --max-files 1000 --chunk-chars 2600 --val-ratio 0.08`
- exit: 0
```
{
  "files": 3,
  "examples": 39,
  "train": 36,
  "val": 3
}
```
### `python3 scripts/profile_corpus.py data/processed/manifest.json`
- exit: 0
```
Corpus profile
files: 6947
clean_chars: 96609
chunks/examples before dedupe: 39
languages: {'unknown': 6877, 'en': 3, 'too_short': 67}
totals: {'files': 3, 'examples': 39, 'train': 36, 'val': 3}

Top sources by chunks:
-  17 chunks | en | /Users/njjimac/Documents/Jedi Content/youtube-transcripts/2026-01-27 - Why People Are Freaking Out About Clawdbot.txt
-  15 chunks | en | /Users/njjimac/Documents/Jedi Content/youtube-transcripts/2026-01-29 - Turn Meeting Notes Into Content with AI Agents.txt
-   7 chunks | en | /Users/njjimac/Documents/Jedi Content/youtube-transcripts/2026-01-27 - This is the CHEAPEST and EASIEST way to set up ClawdBot.txt
-   0 chunks | None | /Users/njjimac/Documents/Jedi Tone of Voice/Random Text Files/44 Harsh Truths About The Game Of Life - Naval Ravikant (4K).md
-   0 chunks | None | /Users/njjimac/Documents/Obsidian Vault/Apple Notes/000000 Speaker 1.md
-   0 chunks | None | /Users/njjimac/Documents/Obsidian Vault/Apple Notes/Why EVERYONE should be on Substack  What it is, How it Works….md
-   0 chunks | None | /Users/njjimac/Documents/Obsidian Vault/Apple Notes/https--chatgpt.com-share-68377095-4260-800b-a415-da5d96dc5300.md
-   0 chunks | None | /Users/njjimac/Documents/Obsidian Vault/Apple Notes/บทเรียนจากการทำธุรกิจ 15 ปีของผม.md
-   0 chunks | None | /Users/njjimac/Documents/Obsidian Vault/Apple Notes/BDCA  JetLauncher.md
-   0 chunks | None | /Users/njjimac/Documents/Obsidian Vault/Apple Notes/Business/New HSM Introduction video.md
-   0 chunks | None | /Users/njjimac/Documents/Obsidian Vault/Apple Notes/3 Steps To Discovering The Purpose of Your Life.md
-   0 chunks | None | /Users/njjimac/Documents/Obsidian Vault/Apple Notes/I'll create detailed outlines for all 9 prioritized topics. Let me….md
-   0 chunks | None | /Users/njjimac/Documents/Obsidian Vault/Apple Notes/No limits book content.md
-   0 chunks | None | /Users/njjimac/Documents/Obsidian Vault/Apple Notes/I help busy professionals attract their dream life partner..md
-   0 chunks | None | /Users/njjimac/Documents/Obsidian Vault/Apple Notes/50 Standard Social Media Posts Based on Transcript.md
-   0 chunks | None | /Users/njjimac/Documents/Obsidian Vault/Apple Notes/มอนิ่ง routine ของผมที่มีผู้ติดตามของผมคนนึงถามผมมาว่าแต่ละวันผมทำ….md
-   0 chunks | None | /Users/njjimac/Documents/Obsidian Vault/Apple Notes/content 14.md
-   0 chunks | None | /Users/njjimac/Documents/Obsidian Vault/Apple Notes/ผมมีแนวคิดหนึ่งฝากให้ทุกท่านพิจารณานะครับ.md
-   0 chunks | None | /Users/njjimac/Documents/Obsidian Vault/Apple Notes/Key Insights from “Why Being Unpleasant Will Make You Magnetic….md
-   0 chunks | None | /Users/njjimac/Documents/Obsidian Vault/Apple Notes/That's a great idea! A simpler version with powerful Bible verses….md
```
### `python3 scripts/evaluate_voice.py data/processed/train.jsonl`
- exit: 0
```
examples: 36
languages: {'en': 36, 'th': 0}
chars avg/min/max: 2525 769 2600
phrase hits:
- AI: 34
- agent: 13
- business: 1
- system: 7
- content: 9
```