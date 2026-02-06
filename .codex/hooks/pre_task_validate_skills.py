#!/usr/bin/env python3
"""Pre-task skill validator.

Reads hook payload from stdin (JSON or plain text), extracts explicit skill mentions,
and validates them against `.codex/skill_index/active_skills_registry.json`.

Exit codes:
- 0: ok (no invalid mentioned skills)
- 2: invalid skill mention(s) detected
"""

from __future__ import annotations

import difflib
import json
import re
import sys
from pathlib import Path
from typing import Any, Dict, Iterable, List, Set, Tuple


WORKSPACE = Path(__file__).resolve().parents[2]
REGISTRY_PATH = WORKSPACE / ".codex" / "skill_index" / "active_skills_registry.json"


SKILL_DOLLAR_RE = re.compile(r"\$([A-Za-z0-9._-]+)")
# Supports explicit forms like:
# - "skill: mcp"
# - "skill=mcp-local"
SKILL_WORD_RE = re.compile(
    r"(?:^|[\s,(])skill\s*[:=]\s*([A-Za-z0-9._-]+)\b", re.IGNORECASE
)


def load_registry() -> Tuple[Set[str], Dict[str, str]]:
    data = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    canon: Set[str] = set()
    alias_to_canon: Dict[str, str] = {}
    for entry in data.get("skills", []):
        c = str(entry.get("canonical", "")).strip()
        if not c:
            continue
        canon.add(c.lower())
        alias_to_canon[c.lower()] = c
        preferred = str(entry.get("preferred_dir", "")).strip().lower()
        if preferred:
            alias_to_canon[preferred] = c
        for alias in entry.get("aliases", []):
            a = str(alias).strip().lower()
            if a:
                alias_to_canon[a] = c
    return canon, alias_to_canon


def extract_text_fragments(node: Any) -> Iterable[str]:
    if isinstance(node, str):
        yield node
        return
    if isinstance(node, dict):
        for k, v in node.items():
            # Prioritize likely prompt fields.
            if isinstance(k, str) and k.lower() in {
                "user_prompt",
                "prompt",
                "text",
                "message",
                "content",
                "input",
            }:
                yield from extract_text_fragments(v)
            else:
                yield from extract_text_fragments(v)
        return
    if isinstance(node, list):
        for item in node:
            yield from extract_text_fragments(item)


def normalize_mention(raw: str) -> str:
    return raw.strip().strip("`'\"").lower()


def extract_mentions(text: str) -> Set[str]:
    mentions: Set[str] = set()
    for m in SKILL_DOLLAR_RE.findall(text):
        mentions.add(normalize_mention(m))
    for m in SKILL_WORD_RE.findall(text):
        mentions.add(normalize_mention(m))
    return mentions


def closest(name: str, choices: List[str], n: int = 3) -> List[str]:
    return difflib.get_close_matches(name, choices, n=n, cutoff=0.55)


def main() -> int:
    if not REGISTRY_PATH.exists():
        print(
            "Skill registry not found. Run: python3 .codex/skill_index/build_active_skills_registry.py",
            file=sys.stderr,
        )
        return 2

    canonical, alias_map = load_registry()
    raw = sys.stdin.read()
    payload: Any
    try:
        payload = json.loads(raw) if raw.strip() else {}
    except json.JSONDecodeError:
        payload = raw

    texts = list(extract_text_fragments(payload))
    if not texts and isinstance(payload, str):
        texts = [payload]
    joined = "\n".join(texts)
    mentioned = sorted(extract_mentions(joined))

    # No explicit skill mention -> allow.
    if not mentioned:
        print(json.dumps({"ok": True, "reason": "no explicit skill mentions"}, ensure_ascii=True))
        return 0

    unknown: List[Dict[str, Any]] = []
    resolved: List[Dict[str, str]] = []
    all_names = sorted(set(list(canonical) + list(alias_map.keys())))
    for m in mentioned:
        c = alias_map.get(m)
        if c:
            resolved.append({"mention": m, "canonical": c})
        else:
            unknown.append(
                {
                    "mention": m,
                    "suggestions": closest(m, all_names),
                }
            )

    if unknown:
        print(
            json.dumps(
                {
                    "ok": False,
                    "error": "invalid skill mention(s)",
                    "unknown": unknown,
                    "hint": "Use canonical names from .codex/skill_index/active_skills_registry.json",
                },
                ensure_ascii=True,
            )
        )
        return 2

    print(json.dumps({"ok": True, "resolved": resolved}, ensure_ascii=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
