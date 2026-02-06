---
name: legacy-handler-d1e75a
description: Use this skill when the user needs help with legacy handler. It provides
  practical guidance, execution steps, and quality checks for legacy handler tasks.
keywords:
- legacy
- review
- steps
- task
- step
suggested_keywords:
- legacy
- review
- steps
- task
- step
---

# Legacy Handler

## When to use
- Orchestrator encounters leftover `review_task` steps from older project states
- Need to maintain backward compatibility while migrating to newer agents

## Workflow
1. Inspect `self.data` for the legacy invocation context.
2. When `type` equals `review_task`, mark the corresponding step complete in `next_state` and return done.
3. Surface unexpected types via exceptions so new legacy cases are noticed quickly.

## Anti-patterns
- Silently ignoring unknown legacy types (hides migration issues)
- Performing additional mutations on state beyond completing the targeted step

## Output
- Updated step status for the legacy review task; no other state changes
