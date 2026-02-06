#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PYTHON_BIN="${PYTHON_BIN:-python3}"

# Pass through hook payload stdin unchanged.
payload="$(cat)"

if result="$(printf '%s' "$payload" | "$PYTHON_BIN" "$SCRIPT_DIR/pre_task_validate_skills.py")"; then
  printf '%s\n' "$result"
  exit 0
fi

printf '%s\n' "$result" >&2
exit 2
