---
name: tech-writer-929a43
description: Use this skill when the user needs help with tech writer. It provides
  practical guidance, execution steps, and quality checks for tech writer tasks.
keywords:
- task
- tasks
- readme
- milestones
- documented
suggested_keywords:
- task
- tasks
- readme
- milestones
- documented
---

# Tech Writer

## When to use
- After Troubleshooter marks a task as reviewed and documentation should follow
- At key milestones (halfway, final task) to keep users informed and motivated

## Workflow
1. Count total tasks and unfinished tasks (minus the current one) to locate milestones; when halfway or one task remains, send a celebration update and summarize progress stats.
2. When triggered, stream a README draft via the `create_readme` template and save it to README.md.
3. Set TW_WRITE action, update current task status to DOCUMENTED, and allow orchestrator to proceed.

## Anti-patterns
- Emitting congratulations without verifying task counts (avoids division by zero)
- Forgetting to decrement unfinished tasks before milestone checks
- Skipping README generation when required

## Output
- Updated task status (documented), optional celebratory message, and fresh README content stored in the repo
