---
name: ai-asset-cataloger-bd9810
description: Use this skill when the user needs help with ai asset cataloger. It provides
  practical guidance, execution steps, and quality checks for ai asset cataloger tasks.
keywords:
- asset
- tsv
- inventory
- assets
- instructions
suggested_keywords:
- asset
- tsv
- inventory
- assets
- instructions
---

# AI Asset Cataloger

## When to use
- You need to locate AI-related artifacts (instructions, skills, tools, datasets, repos) across the machine quickly
- Planning backups or audits of AI assets and want category-specific lists
- The asset catalog appears stale and must be regenerated before continuing work

## Workflow
1. Start with `ai-logic/ai_asset_summary.json` to confirm scan metadata (timestamp, counts per category, skipped prefixes). If the scan predates recent changes, schedule a rerun.
2. For targeted lookups, open the matching list in `ai-logic/ai_asset_lists/` (e.g., `instructions.tsv`, `tools.tsv`, `datasets.tsv`). Filter by `path` or `mtime` to identify assets that need review or archival.
3. When you need full fidelity, load `ai-logic/ai_asset_inventory.tsv` into a spreadsheet or pandas DataFrame and filter by `category` (comma-separated), `type`, or `note` to trace exact locations.
4. To refresh the inventory, run `python ai_asset_scan.py` from the `ai-logic` directory (sudo may be required for protected paths). The script walks `/`, skips noisy prefixes, categorizes files/dirs, and rewrites both the TSV and JSON outputs.
5. After rerunning, validate that `ai_asset_summary.json` reflects new counts and check `errors` for inaccessible paths. Update downstream documentation/backups with any new or removed assets.

## Anti-patterns
- Editing inventory TSV rows by hand instead of rerunning the scanner
- Forgetting to review the `errors` array, which can hide missing access to critical directories
- Running the scan from outside the repo root (outputs land in the wrong directory)
- Overlooking comma-separated categories when filtering, leading to missed multi-tagged assets

## Output
- Up-to-date asset inventory files (TSV + JSON) and curated per-category lists ready for archival, auditing, or downstream tooling
