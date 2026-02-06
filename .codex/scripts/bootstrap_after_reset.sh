#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$ROOT_DIR"

INSTALL_GLOBAL_HOOKS=0
if [[ "${1:-}" == "--install-global-hooks" ]]; then
  INSTALL_GLOBAL_HOOKS=1
fi

echo "[1/5] Restoring executable bits"
chmod +x \
  .codex/hooks/pre_task_validate_skills.py \
  .codex/hooks/pre_task_validate_skills.sh \
  .codex/skill_index/build_active_skills_registry.py \
  .codex/skill_index/lint_skills.py \
  .codex/scripts/validate_skills_stack.sh \
  .codex/scripts/bootstrap_after_reset.sh

echo "[2/5] Regenerating active skills registry"
python3 .codex/skill_index/build_active_skills_registry.py

echo "[3/5] Validating skill stack"
.codex/scripts/validate_skills_stack.sh

echo "[4/5] Optional global hook installation"
if [[ "$INSTALL_GLOBAL_HOOKS" -eq 1 ]]; then
  mkdir -p "$HOME/.codex/hooks"
  ln -sf "$ROOT_DIR/.codex/hooks/hooks.json" "$HOME/.codex/hooks/hooks.json"
  echo "Installed global hook symlink: $HOME/.codex/hooks/hooks.json"
else
  echo "Skipped global hook install (pass --install-global-hooks to enable)."
fi

echo "[5/5] Done"
echo "Restart Codex session to reload hooks."
