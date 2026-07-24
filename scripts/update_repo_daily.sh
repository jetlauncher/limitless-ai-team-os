#!/usr/bin/env bash
set -euo pipefail
trap 'echo "error: daily refresh failed at ${BASH_SOURCE[0]}:${LINENO}" >&2' ERR
cd "$(dirname "$0")/.."

if ! command -v python3 >/dev/null 2>&1; then
  echo "error: python3 is required for the daily refresh." >&2
  exit 1
fi

python3 scripts/export_sanitized_agent_system.py
python3 scripts/validate_no_secrets.py
git add .
if git diff --cached --quiet; then
  echo "No changes to commit."
  exit 0
fi
git commit -m "chore: daily sanitized agent system refresh"
git push
