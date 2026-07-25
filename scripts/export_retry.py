#!/usr/bin/env python3
"""Export using cat (subprocess) to handle iCloud cloud-optimized files."""
import json, os, re, shutil, subprocess, sys, time
from pathlib import Path

REPO = Path(os.environ.get('LIMITLESS_REPO', Path(__file__).resolve().parents[1])).resolve()
HOME = Path.home()

SECRET_PATTERNS = [
    (re.compile(r'\b\d{8,12}:[A-Za-z0-9_-]{30,}\b'), '[REDACTED_TELEGRAM_BOT_TOKEN]'),
    (re.compile(r'\bgh[opsru]_[A-Za-z0-9_]{20,}\b'), '[REDACTED_GITHUB_TOKEN]'),
    (re.compile(r'\bsk-[A-Za-z0-9_-]{20,}\b'), '[REDACTED_OPENAI_KEY]'),
    (re.compile(r'\bsk-or-v1-[A-Za-z0-9_-]{20,}\b'), '[REDACTED_OPENROUTER_KEY]'),
    (re.compile(r'\bntn_[A-Za-z0-9_-]{20,}\b'), '[REDACTED_NOTION_TOKEN]'),
    (re.compile(r'\bsecret_[A-Za-z0-9_-]{20,}\b'), '[REDACTED_SECRET]'),
    (re.compile(r'\bpat[A-Za-z0-9]{10,}\.[A-Za-z0-9]{10,}\b'), '[REDACTED_AIRTABLE_PAT]'),
    (re.compile(r'Bearer\s+[A-Za-z0-9._-]{20,}', re.I), 'Bearer [REDACTED]'),
    (re.compile(r'(api[_-]?key\s*[:=]\s*)([^\s\n"]+)'), r'\1[REDACTED]'),
    (re.compile(r'(token\s*[:=]\s*)([^\s\n"]+)'), r'\1[REDACTED]'),
    (re.compile(r'(password\s*[:=]\s*)([^\s\n"]+)'), r'\1[REDACTED]'),
]

READ_TIMEOUT_SECONDS = 30


class FileReadError(Exception):
    """A source file could not be read."""


failures = []


def record_failure(message):
    failures.append(message)
    print(f'WARNING: {message}', file=sys.stderr)


def sanitize(text):
    for pat, repl in SECRET_PATTERNS:
        text = pat.sub(repl, text)
    return text

def write(rel, text):
    p = REPO / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(sanitize(text), encoding='utf-8')

def cat_file(path):
    """Read file using cat subprocess — works with iCloud cloud-optimized files."""
    try:
        result = subprocess.run(
            ['cat', str(path)],
            capture_output=True,
            timeout=READ_TIMEOUT_SECONDS,
            text=True,
            errors='ignore'
        )
    except subprocess.TimeoutExpired as exc:
        raise FileReadError(f'timed out after {READ_TIMEOUT_SECONDS}s reading {path}') from exc
    except OSError as exc:
        raise FileReadError(f'could not run cat on {path}: {exc}') from exc
    if result.returncode != 0:
        detail = (result.stderr or '').strip() or f'exit code {result.returncode}'
        raise FileReadError(f'cat failed for {path}: {detail}')
    return result.stdout

def walk_files(root):
    """Yield files under root, reporting directories that cannot be listed."""
    for dirpath, _dirnames, filenames in os.walk(
        root, onerror=lambda exc: record_failure(f'could not list {exc.filename}: {exc}')
    ):
        for name in sorted(filenames):
            yield Path(dirpath) / name


def collect(root, exts, skip_names, skip_dirs):
    results = []
    for f in sorted(walk_files(root)):
        if not f.is_file():
            continue
        if f.suffix.lower() not in exts:
            continue
        sf = str(f)
        if any(s in sf for s in skip_dirs):
            continue
        if f.name in skip_names:
            continue
        if f.name.endswith('_state.json') or f.name == 'state.json':
            continue
        try:
            txt = cat_file(f)
        except FileReadError as exc:
            record_failure(str(exc))
            continue
        if len(txt) > 120000:
            txt = txt[:120000] + '\n\n[TRUNCATED FOR TEMPLATE REPO]\n'
        results.append((f, txt))
    return results

exts = {'.md', '.txt', '.yaml', '.yml', '.json'}
skip_names = {'ACCESS-TOKENS.md'}
skip_dirs = {'Content Archive', 'Generated Assets', 'node_modules'}

# Clean old outputs
for d in ['agents', 'configs']:
    p = REPO / d
    if p.exists():
        shutil.rmtree(p)

# Root config
config_dir = HOME / '.hermes/config.yaml'
if config_dir.exists():
    try:
        write('configs/root/config.example.yaml', cat_file(config_dir))
        print(f'Exported configs/root/config.example.yaml')
    except FileReadError as exc:
        record_failure(str(exc))

agents_map = {'Hermes':'default','Blaze':'blaze','Bolt':'bolt','Kaijeaw':'kaijeaw','Protocol':'protocol','Qwen':'qwen','Signal':'signal','Zegna':'zegna'}

total_exported = 0

for agent, prof in agents_map.items():
    cfg = HOME / f'.hermes/profiles/{prof}/config.yaml'
    if prof != 'default' and cfg.exists():
        try:
            write(f'configs/profiles/{prof}/config.example.yaml', cat_file(cfg))
            print(f'Exported configs/profiles/{prof}/config.example.yaml')
        except FileReadError as exc:
            record_failure(str(exc))

    soul = HOME / ('.hermes/SOUL.md' if prof == 'default' else f'.hermes/profiles/{prof}/SOUL.md')
    if soul.exists():
        try:
            soul_text = cat_file(soul)
        except FileReadError as exc:
            record_failure(str(exc))
        else:
            write(f'agents/{agent}/SOUL.md', soul_text)
            total_exported += 1
            print(f'Exported {agent}/SOUL.md ({len(soul_text)} bytes)')

    obs = HOME / f'Documents/Obsidian Vault/Agents/{agent}'
    if obs.exists():
        files = collect(obs, exts, skip_names, skip_dirs)
        for f, txt in files:
            rel = f.relative_to(obs)
            key = f'agents/{agent}/workspace/{rel}'
            write(key, txt)
            total_exported += 1
        print(f'Exported {agent}: {len(files)} workspace files')
    else:
        print(f'Skipped {agent}: obs dir not found')

shared = HOME / 'Documents/Obsidian Vault/Agents/Shared Memory'
if shared.exists():
    files = collect(shared, exts, skip_names, skip_dirs)
    for f, txt in files:
        rel = f.relative_to(shared)
        key = f'agents/Shared Memory/workspace/{rel}'
        write(key, txt)
        total_exported += 1
    print(f'Exported Shared Memory: {len(files)} workspace files')

write('agent-registry.json', json.dumps({
    'repo': 'limitless-ai-team-os',
    'agents': [{'name': a, 'profile': p} for a, p in agents_map.items()]
}, indent=2))
print(f'\nTotal files exported: {total_exported}')

if failures:
    print(f'\nExport finished with {len(failures)} unreadable file(s):', file=sys.stderr)
    for message in failures:
        print(f' - {message}', file=sys.stderr)
    sys.exit(1)

print('Export complete.')
