---
name: error-handler-16735e
description: Use this skill when the user needs help with error handler. It provides
  practical guidance, execution steps, and quality checks for error handler tasks.
keywords:
- command
- agent
- debugging
- exit
- failures
suggested_keywords:
- command
- agent
- debugging
- exit
- failures
---

# Error Handler

## When to use
- Any agent returns an error response to the orchestrator
- Command executions fail in `command-executor` and need structured debugging
- Spec creation failed and the run must exit cleanly

## Workflow
1. Inspect the previous agent response. Exit immediately when Spec Writer cannot finish project description; nothing else can proceed.
2. If the Executor failed, confirm with the user before debugging. Respect cancellations to avoid unwanted log churn.
3. When approved, stream the `debug` template with command metadata (steps, current task, step index, command, timeout, stdout, stderr, status code, analysis) to generate remediation instructions.
4. Append a fresh iteration to `next_state.iterations` using the debug output, mark it `IMPLEMENT_SOLUTION`, and prune incomplete steps so Developer can re-breakdown.
5. For unhandled agent types, log details and exit so the orchestrator can halt safely.

## Anti-patterns
- Continuing after Spec Writer failures instead of exiting
- Skipping the user confirmation before launching debug analysis
- Forgetting to move unfinished steps off the queue, leaving stale entries for downstream agents

## Output
- Either `EXIT` for irrecoverable errors or `DONE` with a new iteration containing remediation instructions and cleaned-up step lists
