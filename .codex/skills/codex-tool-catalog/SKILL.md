---
name: codex-tool-catalog-73e91f
description: Use this skill when the user needs help with codex tool catalog. It provides
  practical guidance, execution steps, and quality checks for codex tool catalog tasks.
keywords:
- tools
- catalog
- codex
- category
- helpers
suggested_keywords:
- tools
- catalog
- codex
- category
- helpers
---

# Codex Tool Catalog

## When to use
- A new helper script, extractor, or reference library needs to be archived under Codex_Tools
- Updating `catalog.md` summaries or verifying that every category still contains live tooling
- Running preflight checks before publishing changes to the tooling registry

## Workflow
1. Review `Codex_Tools/catalog.md` for existing categories (UnityEx build helpers, Asset extraction helpers, IL2CPP & Ghidra automation helpers, Reference libraries). Use it to decide where the new asset belongs and to confirm the description/use-case format.
2. Copy new helpers with `Codex_Tools/scripts/registry_sync.sh <category> <source> [dest-name]`. The script resolves the repo root, creates the category directory if missing, copies the asset into `Codex_Tools/Tools/<category>/`, makes it executable when applicable, and reminds you to update the catalog entry.
3. After syncing files, open `Codex_Tools/catalog.md` and add or update the bullet that describes the helper (summary + use cases). Link to any supporting notes under `Codex_Tools/notes/` (e.g., `tool_build_notes.md`, `verification-checklist.md`, `dependency-lock.md`, `versions.md`) when they affect rebuild steps or validation.
4. Run `Codex_Tools/scripts/validate_catalog.sh` to ensure required category folders exist, contain at least one helper, the References directory is present, and `catalog.md` still includes the expected section headings. Fix any errors it reports before committing.
5. When large rebuilds occur, append artifacts and attempt reports under `Codex_Tools/efforts/` so future agents can replay the workflow. Reference those snapshots inside the catalog entry to keep provenance clear.

## Anti-patterns
- Dropping files directly into `Tools/<category>` without running `registry_sync.sh` (skips executable bit and copy reminder)
- Forgetting to add the helper description to `catalog.md`, leaving future agents guessing about purpose or usage
- Skipping `validate_catalog.sh`, which allows missing directories or section headings to slip through
- Ignoring the notes/efforts directories when recording rebuild instructions or outputs

## Output
- Updated `Codex_Tools/Tools/<category>/` contents, refreshed `catalog.md` entries, passing validation script output, and optional effort records/notes for traceability
