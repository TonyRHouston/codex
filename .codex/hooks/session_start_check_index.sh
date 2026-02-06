#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
INDEX_MD="$ROOT_DIR/.codex/workspace_index/ASSET_INDEX.md"
INDEX_JSON="$ROOT_DIR/.codex/workspace_index/asset_manifest.json"

# Consume hook payload to avoid pipe/backpressure issues.
cat >/dev/null || true

if [[ ! -f "$INDEX_MD" ]]; then
  echo "Workspace index missing: $INDEX_MD" >&2
  exit 2
fi

if [[ ! -f "$INDEX_JSON" ]]; then
  echo "Workspace manifest missing: $INDEX_JSON" >&2
  exit 2
fi

# Lightweight sanity checks for required sections/keys.
if ! rg -q "^# Workspace Asset Index" "$INDEX_MD"; then
  echo "Workspace index malformed (missing title)" >&2
  exit 2
fi

if ! python3 - "$INDEX_JSON" <<'PY'
import json
import sys
from pathlib import Path

path = Path(sys.argv[1])
data = json.loads(path.read_text(encoding="utf-8"))
groups = data.get("groups", {})
required = ("product_code", "codex_runtime", "transient")
if not all(k in groups for k in required):
    raise SystemExit(2)
PY
then
  echo "Workspace manifest malformed (missing required groups)" >&2
  exit 2
fi

# SessionStart informational output.
printf '{"ok":true,"checked":".codex/workspace_index","index":"ASSET_INDEX.md"}\n'
