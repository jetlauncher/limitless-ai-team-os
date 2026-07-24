#!/usr/bin/env python3
from pathlib import Path
import re, sys
ROOT=Path(__file__).resolve().parents[1]
patterns=[
 ('telegram bot token', r'\b\d{8,12}:[A-Za-z0-9_-]{30,}\b'),
 ('github token', r'\bgh[opsru]_[A-Za-z0-9_]{20,}\b'),
 ('openai key', r'\bsk-[A-Za-z0-9_-]{20,}\b'),
 ('openrouter key', r'\bsk-or-v1-[A-Za-z0-9_-]{20,}\b'),
 ('notion token', r'\bntn_[A-Za-z0-9_-]{20,}|\bsecret_[A-Za-z0-9_-]{20,}'),
 ('airtable pat', r'\bpat[A-Za-z0-9]{10,}\.[A-Za-z0-9]{10,}\b'),
]
found=[]
unreadable=[]
for p in ROOT.rglob('*'):
    if p.is_dir() or '.git' in p.parts: continue
    if p.name == 'validate_no_secrets.py': continue
    try:
        txt=p.read_text(errors='ignore')
    except OSError as exc:
        unreadable.append((str(p.relative_to(ROOT)), str(exc)))
        continue
    for name,pat in patterns:
        if re.search(pat, txt): found.append((str(p.relative_to(ROOT)), name))
if unreadable:
    print('Files could not be scanned:', file=sys.stderr)
    for f,e in unreadable: print(f' - {f}: {e}', file=sys.stderr)
if found:
    print('Potential secrets found:')
    for f,n in found: print(f' - {f}: {n}')
if found or unreadable:
    sys.exit(1)
print('No obvious secrets found.')
