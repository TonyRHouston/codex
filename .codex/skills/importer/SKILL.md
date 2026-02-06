---
name: importer-50b5e2
description: Use this skill when the user needs help with importer. It provides practical
  guidance, execution steps, and quality checks for importer tasks.
keywords:
- project
- files
- import
- specification
- spec
suggested_keywords:
- project
- files
- import
- specification
- spec
---

# Importer

## When to use
- Spec Writer requests `IMPORT_PROJECT` to pull an external codebase into Pythagora
- A freshly imported workspace needs entrypoint discovery and spec generation
- Project complexity must reflect the imported size before planning begins

## Workflow
1. When triggered by Spec Writer, signal the UI to open the project root, instruct the user to copy files (warning about the 10k LOC soft limit), and wait for confirmation before calling `state_manager.import_files()` and committing.
2. Outside the initial import, stream the `get_entrypoints` template to find key files, filtering `current_state.files` to a relevant subset.
3. Feed those files plus `EXAMPLE_PROJECT_DESCRIPTION` into the `analyze_project` template to produce a narrative spec update.
4. Clone the existing specification, overwrite its description, and set `next_state.specification` alongside a completed "Import project" epic whose complexity depends on file count.
5. Emit the `existing-project` telemetry event capturing file and line counts plus the generated description.

## Anti-patterns
- Skipping the UI prompt before import, which can leave workspaces empty
- Rewriting the spec without cloning, leading to accidental shared-state edits
- Forgetting to adjust epic complexity based on imported size or to commit after copying files

## Output
- Imported files staged in the workspace, updated specification text, a completed import epic, and telemetry describing the imported project
