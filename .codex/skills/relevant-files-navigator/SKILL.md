---
name: relevant-files-navigator-dda69d
description: Use this skill when the user needs help with relevant files navigator.
  It provides practical guidance, execution steps, and quality checks for relevant
  files navigator tasks.
keywords:
- files
- relevant
- state
- current
- client
suggested_keywords:
- files
- relevant
- state
- current
- client
---

# Relevant Files Navigator

## When to use
- Before breaking down a task or iteration where targeted file context matters
- Any time the agents need a refreshed list of files to inspect/edit

## Workflow
1. Kick off two async requests (client + server) using `filter_files` to propose relevant paths based on user feedback, solution description, and directory type.
2. Merge responses, keep only existing files, and append always-relevant entries from `ALWAYS_RELEVANT_FILES`.
3. Store the resulting list on both `current_state.relevant_files` and `next_state.relevant_files` so downstream agents reuse it.
4. Return immediately; callers decide how to continue once relevant files are in place.

## Anti-patterns
- Accepting file suggestions that do not exist in the workspace
- Forgetting to include default always-relevant files when appropriate
- Updating only current_state or next_state, leaving the other stale

## Output
- Updated relevant file list synchronized across current and next project state
