#!/usr/bin/env python3
"""Fail if the working tree contains credentials, private key material or env files."""
from pathlib import Path
import re, subprocess, sys

ROOT = Path(__file__).resolve().parents[1]
SELF = Path(__file__).name
SKIP_FILES = {SELF, 'sanitize_lib.py'}
SKIP_DIRS = {'.git', 'node_modules', '.venv', 'venv', '__pycache__'}
MAX_BYTES = 5_000_000

PATTERNS = [
    ('telegram bot token', r'\b\d{8,12}:[A-Za-z0-9_-]{30,}\b'),
    ('github token', r'\b(gh[opsru]_[A-Za-z0-9_]{20,}|github_pat_[A-Za-z0-9_]{20,})\b'),
    ('anthropic key', r'\bsk-ant-[A-Za-z0-9_-]{20,}\b'),
    ('openrouter key', r'\bsk-or-v1-[A-Za-z0-9_-]{20,}\b'),
    ('openai key', r'\bsk-[A-Za-z0-9_-]{20,}\b'),
    ('notion token', r'\b(ntn_|secret_)[A-Za-z0-9_-]{20,}\b'),
    ('airtable pat', r'\bpat[A-Za-z0-9]{10,}\.[A-Za-z0-9]{10,}\b'),
    ('aws access key id', r'\b(AKIA|ASIA)[0-9A-Z]{16}\b'),
    ('slack token', r'\bxox[baprs]-[A-Za-z0-9-]{10,}\b'),
    ('google api key', r'\bAIza[0-9A-Za-z_-]{35}\b'),
    ('google oauth token', r'\bya29\.[A-Za-z0-9._-]{20,}\b'),
    ('beehiiv key', r'\bbh_[A-Za-z0-9]{20,}\b'),
    ('jwt', r'\beyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\b'),
    ('private key block', r'-----BEGIN (?:[A-Z ]+ )?PRIVATE KEY-----'),
    ('bearer credential', r'Bearer[ \t]+(?!\[REDACTED\]|\$\{)[A-Za-z0-9._-]{20,}'),
    # key: value / KEY=value with a real-looking literal (placeholders excluded).
    (
        'credential assignment',
        r'(?i)\b(?:api[_-]?key|apikey|access[_-]?token|auth[_-]?token|client[_-]?secret|password|passwd)'
        r'[ \t]*[:=][ \t]*(?!\[REDACTED|\$\{|<|your|YOUR|\'\'|""|\n)[^\s\'"#]{8,}',
    ),
]

COMPILED = [(name, re.compile(pattern)) for name, pattern in PATTERNS]


def git_ignored():
    """Paths git already excludes: local .env files etc. are the operator's business."""
    try:
        out = subprocess.run(
            ['git', '-C', str(ROOT), 'ls-files', '--others', '--ignored', '--exclude-standard', '-z'],
            capture_output=True, text=True, check=True,
        ).stdout
    except (OSError, subprocess.CalledProcessError):
        return set()
    return {ROOT / rel for rel in out.split('\0') if rel}


def iter_files():
    ignored = git_ignored()
    for path in ROOT.rglob('*'):
        if path.is_dir() or SKIP_DIRS.intersection(path.parts):
            continue
        if path.name in SKIP_FILES or path in ignored:
            continue
        yield path


found = []
for path in iter_files():
    rel = path.relative_to(ROOT)
    name = path.name
    is_env = name.startswith('.env') or name.endswith('.env') or '.env.' in name
    if is_env and not name.endswith('.example'):
        found.append((rel, 'env file committed'))
        continue
    try:
        if path.stat().st_size > MAX_BYTES:
            continue
        text = path.read_text(errors='ignore')
    except OSError as exc:
        print(f'warning: could not read {rel}: {exc}', file=sys.stderr)
        continue
    for name, pattern in COMPILED:
        match = pattern.search(text)
        if match:
            line = text[: match.start()].count('\n') + 1
            found.append((f'{rel}:{line}', name))

if found:
    print('Potential secrets found:')
    for location, name in found:
        print(f' - {location}: {name}')
    sys.exit(1)
print('No obvious secrets found.')
