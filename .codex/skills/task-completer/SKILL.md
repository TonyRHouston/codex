---
name: task-completer-4772da
description: Use this skill when the user needs help with task completer. It provides
  practical guidance, execution steps, and quality checks for task completer tasks.
keywords:
- task
- git
- completion
- commit
- status
suggested_keywords:
- task
- git
- completion
- commit
- status
---

# Task Completer

## When to use
- A development task reaches the end of its iteration and needs to be marked done
- Git commits should be created before transitioning to the next task

## Workflow
1. If Git is configured and used, trigger `git_commit()` via the GitMixin to capture work-in-progress before closing the task.
2. Calculate the 1-based index for the current task and set the next_state action using `TC_TASK_DONE`.
3. Call `next_state.complete_task()` and log completion through the state manager to persist history/telemetry.
4. Send task progress to the UI (task index, total tasks, description, source, status, and list of tasks) and emit telemetry `task-end` with project metadata.
5. When the final task within an epic finishes, notify the UI with either `send_app_finished` or `send_feature_finished` depending on epic source.

## Anti-patterns
- Skipping the Git commit before closing when repository tracking is active
- Forgetting to log task completion or update telemetry
- Failing to notify UI of completion, leaving inconsistent task state indicators

## Output
- Updated task status, logged completion, optional Git commit, UI progress message, and final completion signals when epics conclude
