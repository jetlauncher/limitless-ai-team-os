#!/usr/bin/env bash
set -euo pipefail

if ! command -v curl >/dev/null 2>&1; then
  echo "error: curl is required to install Hermes." >&2
  exit 1
fi

installer="$(mktemp)"
trap 'rm -f "$installer"' EXIT

if ! curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh -o "$installer"; then
  echo "error: failed to download the Hermes installer." >&2
  exit 1
fi

bash "$installer"

if ! command -v hermes >/dev/null 2>&1; then
  echo "error: 'hermes' not found on PATH after install; check the installer output above." >&2
  exit 1
fi

if ! hermes doctor; then
  echo "warning: 'hermes doctor' reported problems; review its output above before continuing." >&2
fi
