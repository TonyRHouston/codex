#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$ROOT_DIR"

echo "[1/5] Regenerating active skills registry"
python3 .codex/skill_index/build_active_skills_registry.py >/tmp/active_skills_registry.out
cat /tmp/active_skills_registry.out

echo "[2/5] Validating hook/config syntax"
python3 -m json.tool .codex/hooks/hooks.json >/dev/null
bash -n \
  .codex/hooks/pre_task_validate_skills.sh \
  .codex/hooks/session_start_check_index.sh
python3 -m py_compile \
  .codex/hooks/pre_task_validate_skills.py \
  .codex/skill_index/build_active_skills_registry.py \
  .codex/skill_index/lint_skills.py

echo "[3/5] Checking executable bits"
test -x .codex/hooks/pre_task_validate_skills.sh
test -x .codex/hooks/session_start_check_index.sh
test -x .codex/hooks/pre_task_validate_skills.py
test -x .codex/skill_index/build_active_skills_registry.py
test -x .codex/skill_index/lint_skills.py

echo "[4/5] Linting SKILL.md files"
python3 .codex/skill_index/lint_skills.py

echo "[5/5] Ensuring generated registry files are committed"
git diff --exit-code -- \
  .codex/skill_index/active_skills_registry.json \
  .codex/skill_index/active_skills_registry.tsv \
  .codex/skill_index/invalid_skills_report.json

echo "Skill stack validation passed."
