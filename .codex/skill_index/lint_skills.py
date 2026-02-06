#!/usr/bin/env python3
"""Lint SKILL.md files for structural and source-reference integrity."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
WORKSPACE = ROOT.parent

SOURCE_RE = re.compile(r"^source:\s*(.+?)\s*$")


def resolve_source(raw: str) -> list[Path]:
    src = raw.strip().strip('"').strip("'")
    return [
        WORKSPACE / src,
        ROOT / src,
        SKILLS_DIR / src,
    ]


def main() -> int:
    errors: list[str] = []
    skill_files = sorted(SKILLS_DIR.rglob("SKILL.md"))

    for f in skill_files:
        text = f.read_text(encoding="utf-8", errors="replace")
        rel = f.relative_to(WORKSPACE)

        if "allowed-tools: []---" in text:
            errors.append(f"{rel}: contains malformed frontmatter delimiter 'allowed-tools: []---'")

        lines = text.splitlines()
        for idx, line in enumerate(lines, start=1):
            m = SOURCE_RE.match(line)
            if not m:
                continue
            candidates = resolve_source(m.group(1))
            if not any(p.exists() for p in candidates):
                errors.append(f"{rel}:{idx}: unresolved source '{m.group(1).strip()}'")

    if errors:
        print("Skill lint failed:")
        for e in errors:
            print(f"- {e}")
        print(f"Total errors: {len(errors)}")
        return 2

    print(f"Skill lint passed: scanned {len(skill_files)} SKILL.md files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
