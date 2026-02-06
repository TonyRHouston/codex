---
name: task-breakdown-developer-419269
description: Use this skill when the user needs help with task breakdown developer.
  It provides practical guidance, execution steps, and quality checks for task breakdown
  developer tasks.
keywords:
- task
- steps
- breakdown
- user
- file
suggested_keywords:
- task
- steps
- breakdown
- user
- file
---

# Task Breakdown Developer

## When to use
- An unfinished task or iteration needs detailed implementation steps
- The orchestrator hands off after specification and planning

## Workflow
1. If the current step requests a utility function, update the knowledge base and mark the step complete.
2. If iterations need attention, gather relevant files (bug hunt vs troubleshooting), parse human instructions, and convert them into next steps while updating iteration status (await logging/test vs complete).
3. For regular tasks:
   - Announce progress, ensure relevant files are fetched in parallel, and start the breakdown stream with highlighted API endpoints or redo feedback.
   - Generate implementation instructions via `breakdown` template, ensuring `<pythagoracode>` tags are balanced (retry up to two times); pass through chat-with-breakdown confirmation when auto-confirm is off.
   - Persist instructions onto the task, clear leftover modified files, and parse them with `parse_task` to create concrete steps.
4. Before executing, ask the user whether to run, edit, or skip the task unless flagged as always-run (quick implementations, user-added, hardcoded). Handle edits by resetting description and rerunning. Skips mark the task as skipped.
5. Convert parsed steps into next_state steps, preserving finished history, removing duplicate save_file entries, and set DEV_TASK_START/DEV_TROUBLESHOOT/DEV_WAIT_TEST actions as appropriate. Emit telemetry for task-start.

## Anti-patterns
- Skipping relevant file discovery before breakdown
- Ignoring redo feedback or iteration status transitions
- Proceeding with malformed breakdown output (mismatched `<pythagoracode>` tags)
- Forgetting to reset modified_files or flag tasks as modified after updates

## Output
- Updated task instructions, step list (commands, saves, interventions), current task status/action, and UI/telemetry signals indicating task progress
