#!/usr/bin/env python3
"""Build a stable active-skills registry from .codex/skills.

Outputs:
- active_skills_registry.json
- active_skills_registry.tsv
- invalid_skills_report.json
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Tuple


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
OUT_DIR = ROOT / "skill_index"
WORKSPACE_ROOT = ROOT.parent


HEX_SUFFIX_RE = re.compile(r"-(?:[0-9a-f]{6,8})$")


@dataclass
class SkillMeta:
    dir_name: str
    skill_path: Path
    frontmatter: Dict[str, str]

    @property
    def fm_name(self) -> str:
        return self.frontmatter.get("name", "")

    @property
    def fm_description(self) -> str:
        return self.frontmatter.get("description", "")


def parse_frontmatter(text: str) -> Optional[Dict[str, str]]:
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    if end == -1:
        return None
    fm_raw = text[4:end]
    result: Dict[str, str] = {}
    for line in fm_raw.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if stripped.startswith("-"):
            continue
        if ":" not in stripped:
            continue
        key, value = stripped.split(":", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        result[key] = value
    return result


def normalize_alias(name: str) -> str:
    n = name.lower()
    n = HEX_SUFFIX_RE.sub("", n)

    if n.startswith("tools-copilot-toolkit-skills-"):
        n = n[len("tools-copilot-toolkit-skills-") :]
    elif n.startswith("tools-"):
        n = n[len("tools-") :]

    if n.startswith("skills-"):
        n = n[len("skills-") :]

    if n.startswith("curated-"):
        n = n[len("curated-") :]
    if n.startswith("-curated-"):
        n = n[len("-curated-") :]

    if n.endswith("-skill"):
        n = n[: -len("-skill")]

    n = n.replace("-plugins-plugin-dev-", "-")
    n = n.replace("-skills-", "-")
    n = n.strip("-_")
    return n


def preference_score(dir_name: str) -> Tuple[int, int, int, int, int]:
    # Higher score is better.
    # Prefer first-party/simple names over wrapper/mirror variants.
    return (
        1 if not dir_name.startswith(".") else 0,
        1 if not dir_name.startswith("-curated-") else 0,
        1 if not dir_name.startswith("skills-") else 0,
        1 if not dir_name.startswith("tools-") else 0,
        1 if HEX_SUFFIX_RE.search(dir_name) is None else 0,
    )


def load_skills() -> Tuple[List[SkillMeta], List[dict], List[dict]]:
    valids: List[SkillMeta] = []
    invalids: List[dict] = []
    excluded: List[dict] = []
    for p in sorted(SKILLS_DIR.iterdir()):
        if not p.is_dir():
            continue
        dir_name = p.name
        if dir_name.startswith("."):
            excluded.append(
                {
                    "dir": dir_name,
                    "path": str((p / "SKILL.md").relative_to(WORKSPACE_ROOT)),
                    "reason": "internal skill namespace",
                }
            )
            continue
        skill_md = p / "SKILL.md"
        if not skill_md.exists():
            invalids.append(
                {
                    "dir": dir_name,
                    "path": str(skill_md.relative_to(WORKSPACE_ROOT)),
                    "reason": "missing SKILL.md",
                }
            )
            continue
        text = skill_md.read_text(encoding="utf-8", errors="replace")
        fm = parse_frontmatter(text)
        if fm is None:
            invalids.append(
                {
                    "dir": dir_name,
                    "path": str(skill_md.relative_to(WORKSPACE_ROOT)),
                    "reason": "missing or malformed frontmatter",
                }
            )
            continue
        if not fm.get("name"):
            invalids.append(
                {
                    "dir": dir_name,
                    "path": str(skill_md.relative_to(WORKSPACE_ROOT)),
                    "reason": "frontmatter missing name",
                }
            )
            continue
        if not fm.get("description"):
            invalids.append(
                {
                    "dir": dir_name,
                    "path": str(skill_md.relative_to(WORKSPACE_ROOT)),
                    "reason": "frontmatter missing description",
                }
            )
            continue
        valids.append(SkillMeta(dir_name=dir_name, skill_path=skill_md, frontmatter=fm))
    return valids, invalids, excluded


def main() -> None:
    valids, invalids, excluded_internal = load_skills()

    groups: Dict[str, List[SkillMeta]] = {}
    for skill in valids:
        canonical = normalize_alias(skill.dir_name)
        groups.setdefault(canonical, []).append(skill)

    active = []
    for canonical, members in sorted(groups.items()):
        members_sorted = sorted(
            members,
            key=lambda s: (
                preference_score(s.dir_name),
                s.dir_name,
            ),
            reverse=True,
        )
        preferred = members_sorted[0]
        aliases = sorted({m.dir_name for m in members_sorted if m.dir_name != preferred.dir_name})
        active.append(
            {
                "canonical": canonical,
                "preferred_dir": preferred.dir_name,
                "preferred_path": str(preferred.skill_path.relative_to(WORKSPACE_ROOT)),
                "preferred_frontmatter_name": preferred.fm_name,
                "description": preferred.fm_description,
                "aliases": aliases,
            }
        )

    registry = {
        "summary": {
            "raw_skill_dirs": len([p for p in SKILLS_DIR.iterdir() if p.is_dir()]),
            "valid_skill_dirs": len(valids),
            "active_canonical_skills": len(active),
            "excluded_internal_dirs": len(excluded_internal),
            "invalid_skill_dirs": len(invalids),
        },
        "excluded_internal": excluded_internal,
        "skills": active,
    }

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "active_skills_registry.json").write_text(
        json.dumps(registry, indent=2) + "\n",
        encoding="utf-8",
    )

    tsv_lines = [
        "canonical\tpreferred_dir\tpreferred_path\tpreferred_frontmatter_name\taliases"
    ]
    for item in active:
        aliases = ",".join(item["aliases"])
        tsv_lines.append(
            f"{item['canonical']}\t{item['preferred_dir']}\t{item['preferred_path']}\t{item['preferred_frontmatter_name']}\t{aliases}"
        )
    (OUT_DIR / "active_skills_registry.tsv").write_text(
        "\n".join(tsv_lines) + "\n",
        encoding="utf-8",
    )

    (OUT_DIR / "invalid_skills_report.json").write_text(
        json.dumps({"invalid_skills": invalids}, indent=2) + "\n",
        encoding="utf-8",
    )

    print(
        f"raw={registry['summary']['raw_skill_dirs']} "
        f"valid={registry['summary']['valid_skill_dirs']} "
        f"active={registry['summary']['active_canonical_skills']} "
        f"invalid={registry['summary']['invalid_skill_dirs']}"
    )


if __name__ == "__main__":
    main()
