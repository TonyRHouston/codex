---
name: skill-function-deduper-ec3b5b
description: Use this skill when the user needs help with skill function deduper.
  It provides practical guidance, execution steps, and quality checks for skill function
  deduper tasks.
---

# Skill Function Deduper

## When to use
- Auditing a large skills directory for duplicate functionality
- Cleaning up noisy skill catalogs with multiple names for the same intent
- Preparing a consolidation plan before deleting or merging skills

## Core workflow
1. Inventory skills: collect every top-level `*/SKILL.md` in the target skills root.
2. Extract intent signals: parse frontmatter `name`, `description`, and body headings.
3. Score overlap: compare functional similarity using normalized keywords and trigger phrases.
4. Group candidates: cluster near-duplicate skills and choose a canonical skill per cluster.
5. Produce decisions: emit `keep`, `merge`, or `remove` recommendations with confidence and evidence.
6. Validate before deletion: keep anything below confidence threshold for manual review.

## Decision rules
- Prefer skills with clearer trigger descriptions and richer, task-specific workflows.
- Prefer non-generated names over wrapper/alias names when capability is equivalent.
- Never auto-delete based on name similarity alone; require functional evidence.
- Treat high-overlap but different scope as `merge` candidates, not immediate removals.

## Output expectations
- Duplicate candidate report (JSON/CSV/Markdown)
- Canonical skill per duplicate cluster
- Explicit action list: `keep`, `merge`, `remove`, `review`
- Confidence score and overlap rationale for every action

## Script
Use `scripts/assess_overlap.py` for deterministic first-pass analysis:

```bash
python3 scripts/assess_overlap.py --skills-root /path/to/skills --out-json overlap.json --out-csv overlap.csv
```

Recommended thresholds:
- `>= 0.82`: likely duplicate function
- `0.68-0.82`: likely overlap, requires manual review
- `< 0.68`: usually distinct function

## Anti-patterns (NEVER)
- Deleting skills solely because names look similar
- Collapsing security-sensitive skills into broad generic skills without review
- Merging skills that target different tools, environments, or safety constraints
