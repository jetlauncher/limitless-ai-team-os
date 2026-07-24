#!/usr/bin/env python3
"""Shared redaction and config-hardening helpers for the sanitized mirror export.

Run directly to re-harden the config templates already committed to this repo:

    python3 scripts/sanitize_lib.py configs
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

# Value part of an assignment: everything up to whitespace, quote or comment,
# skipping values that are already placeholders (${VAR}, [REDACTED...], <fill-me>).
_VALUE = r'(?!\$\{|\[REDACTED|<)[^\s\'"#]+'

SECRET_PATTERNS: list[tuple[re.Pattern[str], str]] = [
    (re.compile(r'\b\d{8,12}:[A-Za-z0-9_-]{30,}\b'), '[REDACTED_TELEGRAM_BOT_TOKEN]'),
    (re.compile(r'\bgh[opsru]_[A-Za-z0-9_]{20,}\b'), '[REDACTED_GITHUB_TOKEN]'),
    (re.compile(r'\bgithub_pat_[A-Za-z0-9_]{20,}\b'), '[REDACTED_GITHUB_TOKEN]'),
    (re.compile(r'\bsk-ant-[A-Za-z0-9_-]{20,}\b'), '[REDACTED_ANTHROPIC_KEY]'),
    (re.compile(r'\bsk-or-v1-[A-Za-z0-9_-]{20,}\b'), '[REDACTED_OPENROUTER_KEY]'),
    (re.compile(r'\bsk-[A-Za-z0-9_-]{20,}\b'), '[REDACTED_OPENAI_KEY]'),
    (re.compile(r'\bntn_[A-Za-z0-9_-]{20,}\b'), '[REDACTED_NOTION_TOKEN]'),
    (re.compile(r'\bsecret_[A-Za-z0-9_-]{20,}\b'), '[REDACTED_SECRET]'),
    (re.compile(r'\bpat[A-Za-z0-9]{10,}\.[A-Za-z0-9]{10,}\b'), '[REDACTED_AIRTABLE_PAT]'),
    (re.compile(r'\bAKIA[0-9A-Z]{16}\b'), '[REDACTED_AWS_ACCESS_KEY_ID]'),
    (re.compile(r'\bASIA[0-9A-Z]{16}\b'), '[REDACTED_AWS_ACCESS_KEY_ID]'),
    (re.compile(r'\bxox[baprs]-[A-Za-z0-9-]{10,}\b'), '[REDACTED_SLACK_TOKEN]'),
    (re.compile(r'\bAIza[0-9A-Za-z_-]{35}\b'), '[REDACTED_GOOGLE_API_KEY]'),
    (re.compile(r'\bya29\.[A-Za-z0-9._-]{20,}\b'), '[REDACTED_GOOGLE_OAUTH_TOKEN]'),
    (re.compile(r'\bbh_[A-Za-z0-9]{20,}\b'), '[REDACTED_BEEHIIV_KEY]'),
    (re.compile(r'\beyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\b'), '[REDACTED_JWT]'),
    (
        re.compile(r'-----BEGIN (?:[A-Z ]+ )?PRIVATE KEY-----.*?-----END (?:[A-Z ]+ )?PRIVATE KEY-----', re.S),
        '[REDACTED_PRIVATE_KEY]',
    ),
    (re.compile(r'Bearer[ \t]+[A-Za-z0-9._-]{20,}', re.I), 'Bearer [REDACTED]'),
    # Keyed assignments. [ \t]* (not \s*) so an empty placeholder such as
    # "OPENAI_API_KEY=" does not swallow the newline and redact the next line.
    (re.compile(rf'((?:api[_-]?key|apikey|secret|client[_-]?secret)[ \t]*[:=][ \t]*)({_VALUE})', re.I), r'\1[REDACTED]'),
    (re.compile(rf'((?:token|access[_-]?token|auth[_-]?token)[ \t]*[:=][ \t]*)({_VALUE})', re.I), r'\1[REDACTED]'),
    (re.compile(rf'((?:password|passwd)[ \t]*[:=][ \t]*)({_VALUE})', re.I), r'\1[REDACTED]'),
]

# Config keys whose literal values are credentials and must never ship.
CREDENTIAL_KEYS = {'api_key', 'apikey', 'token', 'access_token', 'auth_token', 'secret', 'client_secret', 'password'}

# Config keys holding private workspace identifiers (channel/chat/guild IDs).
IDENTIFIER_KEYS = {
    'allowed_chats',
    'allowed_channels',
    'allowed_rooms',
    'free_response_channels',
    'free_response_rooms',
    'dm_role_auth_guild',
    'server_actions',
    'default_assignee',
    'orchestrator_profile',
}

# Safe defaults forced onto exported example configs, as dotted paths.
SAFE_DEFAULTS: dict[str, object] = {
    'approvals.mode': 'manual',
    'approvals.cron_mode': 'deny',
    'approvals.mcp_reload_confirm': True,
    'approvals.destructive_slash_confirm': True,
    'command_allowlist': [],
    'hooks_auto_accept': False,
    'delegation.subagent_auto_approve': False,
    'security.redact_secrets': True,
    'security.allow_private_urls': False,
    'security.tirith_fail_open': False,
    'browser.allow_private_urls': False,
}


class _IndentedDumper(yaml.SafeDumper):
    """Dump sequences indented under their key, matching the Hermes config style."""

    def increase_indent(self, flow=False, indentless=False):  # noqa: FBT002 - yaml API
        return super().increase_indent(flow, False)


def sanitize(text: str) -> str:
    """Redact known credential shapes from arbitrary text."""
    for pattern, replacement in SECRET_PATTERNS:
        text = pattern.sub(replacement, text)
    return text


CREDENTIAL_ENV_SUFFIXES = ('_KEY', '_TOKEN', '_SECRET', '_PASSWORD', '_PAT')


def _is_placeholder(value: object) -> bool:
    return isinstance(value, str) and ('${' in value or value == '')


def _scrub(node: object) -> object:
    if isinstance(node, dict):
        for key, value in node.items():
            lowered = str(key).lower()
            if lowered in CREDENTIAL_KEYS and isinstance(value, (str, list)):
                node[key] = value if _is_placeholder(value) else ''
            elif lowered in IDENTIFIER_KEYS and isinstance(value, (str, int)):
                node[key] = ''
            elif lowered == 'headers' and isinstance(value, dict):
                for header, header_value in value.items():
                    if str(header).lower() == 'authorization' and not _is_placeholder(header_value):
                        value[header] = 'Bearer ${YOUR_MCP_TOKEN}'
            elif lowered == 'env' and isinstance(value, dict):
                for name, env_value in value.items():
                    if str(name).upper().endswith(CREDENTIAL_ENV_SUFFIXES) and not _is_placeholder(env_value):
                        value[name] = '${' + str(name).upper() + '}'
            else:
                _scrub(value)
    elif isinstance(node, list):
        for item in node:
            _scrub(item)
    return node


def _set_path(data: dict, dotted: str, value: object) -> None:
    keys = dotted.split('.')
    cursor = data
    for key in keys[:-1]:
        nxt = cursor.get(key)
        if not isinstance(nxt, dict):
            return
        cursor = nxt
    if keys[-1] in cursor:
        cursor[keys[-1]] = value


def harden_config(text: str) -> str:
    """Strip credentials/private IDs and force safe approval defaults in a config YAML."""
    try:
        data = yaml.safe_load(text)
    except yaml.YAMLError:
        return sanitize(text)
    if not isinstance(data, dict):
        return sanitize(text)
    _scrub(data)
    for dotted, value in SAFE_DEFAULTS.items():
        _set_path(data, dotted, value)
    return sanitize(yaml.dump(data, Dumper=_IndentedDumper, sort_keys=False, allow_unicode=True))


def main(argv: list[str]) -> int:
    targets = [Path(a) for a in argv[1:]] or [Path(__file__).resolve().parents[1] / 'configs']
    for target in targets:
        files = sorted(target.rglob('*.yaml')) if target.is_dir() else [target]
        for path in files:
            original = path.read_text(encoding='utf-8')
            hardened = harden_config(original)
            if hardened != original:
                path.write_text(hardened, encoding='utf-8')
                print(f'hardened {path}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main(sys.argv))
