#!/usr/bin/env bash
set -euo pipefail
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
hermes doctor || true
