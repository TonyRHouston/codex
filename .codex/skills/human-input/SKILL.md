---
name: human-input-78e7dc
description: Use this skill when the user needs help with human input. It provides
  practical guidance, execution steps, and quality checks for human input tasks.
keywords:
- human
- input
- user
- step
- required
suggested_keywords:
- human
- input
- user
- step
- required
---

# Human Input

## When to use
- A task step requires manual review, approvals, or other human-only actions
- An earlier agent returned `INPUT_REQUIRED` with file positions to inspect
- The workflow needs to halt until the user signals readiness to continue

## Workflow
1. When resuming an `INPUT_REQUIRED` response, open each referenced file/line through `state_manager.file_system.get_full_path` and `ui.open_editor` so the user can inspect or edit.
2. Otherwise, show the `HUMAN_INTERVENTION_QUESTION` heading with the step-specific description and prompt the user with the `CONTINUE_WHEN_DONE` button set.
3. Await the confirmation button; once pressed, mark the `human_intervention` step complete in `next_state` so orchestrator can proceed.

## Anti-patterns
- Forgetting to surface the manual work description, leaving users unsure what to do
- Not opening requested files when handling `INPUT_REQUIRED`, preventing context inspection
- Continuing without updating step completion, which stalls downstream agents

## Output
- Updated state indicating the human-intervention step is finished (or editors opened when input was required), allowing automated agents to resume
