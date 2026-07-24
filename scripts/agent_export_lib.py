#!/usr/bin/env python3
"""Shared helpers for the export and secret-validation scripts.

Holds the single source of truth for the secret redaction rules, the agent ->
profile map, the export path layout and the workspace file filters.
"""
from __future__ import annotations

import json
import os
import re
import shutil
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, List, Optional, Tuple

REPO_ROOT = Path(__file__).resolve().parents[1]
HOME = Path.home()

MAX_FILE_CHARS = 120000
TRUNCATION_NOTICE = '\n\n[TRUNCATED FOR TEMPLATE REPO]\n'

TEXT_EXTS = {'.md', '.txt', '.yaml', '.yml', '.json'}
SKIP_PATH_FRAGMENTS = ('Content Archive', 'Content Drops', 'Generated Assets', 'node_modules')
SKIP_FILE_NAMES = {'ACCESS-TOKENS.md', 'state.json'}

AGENT_PROFILES = {
    'Hermes': 'default',
    'Blaze': 'blaze',
    'Bolt': 'bolt',
    'Kaijeaw': 'kaijeaw',
    'Protocol': 'protocol',
    'Qwen': 'qwen',
    'Signal': 'signal',
    'Zegna': 'zegna',
}

EXPORT_DIRS = ('agents', 'configs')

VAULT_AGENTS_DIR = HOME / 'Documents/Obsidian Vault/Agents'
SHARED_MEMORY_DIR = VAULT_AGENTS_DIR / 'Shared Memory'


@dataclass(frozen=True)
class SecretRule:
    """A redaction rule. `scan` marks rules specific enough to fail CI on."""
    name: str
    pattern: re.Pattern
    replacement: str
    scan: bool


SECRET_RULES: List[SecretRule] = [
    SecretRule('telegram bot token', re.compile(r'\b\d{8,12}:[A-Za-z0-9_-]{30,}\b'),
               '[REDACTED_TELEGRAM_BOT_TOKEN]', True),
    SecretRule('github token', re.compile(r'\bgh[opsru]_[A-Za-z0-9_]{20,}\b'),
               '[REDACTED_GITHUB_TOKEN]', True),
    SecretRule('openai key', re.compile(r'\bsk-[A-Za-z0-9_-]{20,}\b'),
               '[REDACTED_OPENAI_KEY]', True),
    SecretRule('openrouter key', re.compile(r'\bsk-or-v1-[A-Za-z0-9_-]{20,}\b'),
               '[REDACTED_OPENROUTER_KEY]', True),
    SecretRule('notion token', re.compile(r'\bntn_[A-Za-z0-9_-]{20,}\b'),
               '[REDACTED_NOTION_TOKEN]', True),
    SecretRule('generic secret', re.compile(r'\bsecret_[A-Za-z0-9_-]{20,}\b'),
               '[REDACTED_SECRET]', True),
    SecretRule('airtable pat', re.compile(r'\bpat[A-Za-z0-9]{10,}\.[A-Za-z0-9]{10,}\b'),
               '[REDACTED_AIRTABLE_PAT]', True),
    SecretRule('bearer header', re.compile(r'Bearer\s+[A-Za-z0-9._-]{20,}', re.I),
               'Bearer [REDACTED]', False),
    SecretRule('api key assignment', re.compile(r'(api[_-]?key\s*[:=]\s*)([^\s\n"\']+)', re.I),
               r'\1[REDACTED]', False),
    SecretRule('token assignment', re.compile(r'(token\s*[:=]\s*)([^\s\n"\']+)', re.I),
               r'\1[REDACTED]', False),
    SecretRule('password assignment', re.compile(r'(password\s*[:=]\s*)([^\s\n"\']+)', re.I),
               r'\1[REDACTED]', False),
]


def sanitize(text: str) -> str:
    """Apply every redaction rule to `text`."""
    for rule in SECRET_RULES:
        text = rule.pattern.sub(rule.replacement, text)
    return text


def find_secrets(text: str) -> List[str]:
    """Names of the high-confidence rules matching `text`."""
    return [rule.name for rule in SECRET_RULES if rule.scan and rule.pattern.search(text)]


def write_sanitized(rel: str, text: str, repo: Path = REPO_ROOT) -> Path:
    """Write `text` to `repo/rel`, redacted, creating parent directories."""
    path = repo / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(sanitize(text), encoding='utf-8')
    return path


def reset_export_dirs(repo: Path = REPO_ROOT) -> None:
    for name in EXPORT_DIRS:
        shutil.rmtree(repo / name, ignore_errors=True)


def root_config_path() -> Path:
    return HOME / '.hermes/config.yaml'


def profile_config_path(profile: str) -> Path:
    return HOME / f'.hermes/profiles/{profile}/config.yaml'


def soul_path(profile: str) -> Path:
    if profile == 'default':
        return HOME / '.hermes/SOUL.md'
    return HOME / f'.hermes/profiles/{profile}/SOUL.md'


def workspace_path(agent: str) -> Path:
    return VAULT_AGENTS_DIR / agent


def is_exportable(path: Path) -> bool:
    """Whether a vault file belongs in the template repo."""
    if path.suffix.lower() not in TEXT_EXTS:
        return False
    if any(fragment in str(path) for fragment in SKIP_PATH_FRAGMENTS):
        return False
    if path.name in SKIP_FILE_NAMES or path.name.endswith('_state.json'):
        return False
    return True


def walk_files(base_dir: Path) -> List[Path]:
    """Walk a tree, skipping directories that raise OSError (iCloud placeholders)."""
    results = []
    for root, dirs, files in os.walk(base_dir):
        for d in list(dirs):
            try:
                os.scandir(os.path.join(root, d)).close()
            except OSError:
                dirs.remove(d)
        for name in files:
            path = Path(root, name)
            try:
                if path.is_file():
                    results.append(path)
            except OSError:
                pass
    return sorted(results)


def truncate(text: str) -> str:
    if len(text) > MAX_FILE_CHARS:
        return text[:MAX_FILE_CHARS] + TRUNCATION_NOTICE
    return text


def collect_workspace(base_dir: Path, reader: Callable[[Path], Optional[str]]) -> List[Tuple[Path, str]]:
    """Read every exportable file under `base_dir` with `reader`, truncated."""
    collected = []
    for path in walk_files(base_dir):
        if not is_exportable(path):
            continue
        text = reader(path)
        if not text:
            continue
        collected.append((path, truncate(text)))
    return collected


def export_workspace(base_dir: Path, dest_prefix: str, reader: Callable[[Path], Optional[str]],
                     repo: Path = REPO_ROOT) -> int:
    """Export a vault directory into `dest_prefix`; returns the file count."""
    files = collect_workspace(base_dir, reader)
    for path, text in files:
        write_sanitized(f'{dest_prefix}/{path.relative_to(base_dir)}', text, repo)
    return len(files)


def write_agent_registry(repo: Path = REPO_ROOT) -> None:
    registry = {
        'repo': 'limitless-ai-team-os',
        'agents': [{'name': agent, 'profile': profile} for agent, profile in AGENT_PROFILES.items()],
    }
    write_sanitized('agent-registry.json', json.dumps(registry, indent=2), repo)
