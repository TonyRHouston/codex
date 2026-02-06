---
name: spec-writer-be41fb
description: Use this skill when the user needs help with spec writer. It provides
  practical guidance, execution steps, and quality checks for spec writer tasks.
keywords:
- spec
- project
- description
- complexity
- update
suggested_keywords:
- spec
- project
- description
- complexity
- update
---

# Spec Writer

## When to use
- Initial project kickoff when no specification exists
- User edits require spec refinements or new feature incorporation
- Iterations request spec updates or project complexity reassessment

## Workflow
1. If the spec is empty, prompt (or reuse CLI args) for the project description, stream a detailed spec via `build_full_specification`, and derive a project name. Initialize project folders, update knowledge base options, and clone the spec into next_state.
2. For ongoing edits, loop with the user on "Are you satisfied?" until they confirm. Each time they add detail, regenerate the spec, update the current description, and keep the convo concise. When done, re-run `need_auth` to set auth flags and secrets, recompute complexity, refresh telemetry, and reset the initial epic content.
3. When iteration-mode updates arrive (e.g., NEW_FEATURE_REQUESTED), capture the feature description, stream the `add_new_feature` template, present a diff, and ask the user to accept. On approval, save the updated spec and move the iteration back to FIND_SOLUTION; otherwise leave the spec unchanged.
4. Ensure project templates run after spec creation when needed (`apply_template`), storing relevant files and template summaries.
5. After any change, propagate description/original_description, update knowledge base metadata, and emit project description updates via UI.

## Anti-patterns
- Overwriting user-edited specs without confirming satisfaction
- Skipping diff confirmation when adding new features
- Forgetting to flag knowledge base or epics when template/application metadata changes
- Leaving complexity or telemetry out of sync with the latest spec

## Output
- Updated specification text, complexity level, auth settings, project metadata (name, folder), template summary, and UI/telemetry signals marking spec progress
