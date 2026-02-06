---
name: code-monkey-fe4d91
description: Use this skill when the user needs help with code monkey. It provides
  practical guidance, execution steps, and quality checks for code monkey tasks.
keywords:
- file
- files
- metadata
- code
- instructions
suggested_keywords:
- file
- files
- metadata
- code
- instructions
---

# Code Monkey

## When to use
- Developer or Troubleshooter produced implementation instructions with `<pythagoracode>` blocks
- Steps include saving a file or reworking code after review feedback
- Project files need descriptive metadata once imported or generated

## Workflow
1. For `save_file` steps, gather the target path and existing content; set UI status (creating/updating/reworking) and note review attempts.
2. Try relace first when instructions include a block for the file and an access token is available; pass the snippet through `IMPLEMENT_CHANGES_AGENT` to merge edits.
3. If relace fails/absent, call `CODE_MONKEY_AGENT` with the file content, instructions, user feedback, and optional review context to produce the new code.
4. After generation, compute diff line counts, render the diff to the UI, persist the new content, and mark the step complete. Return `INPUT_REQUIRED` when inserted code expects manual values.
5. When responding to DESCRIBE_FILES requests, fan out across un-described files using `DESCRIBE_FILES_AGENT` and store summaries/references in metadata for later discovery.

## Anti-patterns
- Skipping UI status updates, causing stale file indicators
- Falling back to relace without guarding token availability or snippet presence
- Forgetting to record review attempts or feed prior feedback back into the convo
- Leaving file metadata empty after import/creation, hindering downstream search

## Output
- Updated file contents with diffs, optional `INPUT_REQUIRED` prompts, and refreshed metadata (description, references) for described files
