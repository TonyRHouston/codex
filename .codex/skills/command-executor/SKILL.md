---
name: command-executor-1488a5
description: Use this skill when the user needs help with command executor. It provides
  practical guidance, execution steps, and quality checks for command executor tasks.
keywords:
- command
- run
- step
- task
- completion
suggested_keywords:
- command
- run
- step
- task
- completion
---

# Command Executor

## When to use
- A task step includes a command to run (`step["command"]`)
- Needs human confirmation or command substitution before execution
- Capturing stdout/stderr analysis for later debugging

## Workflow
1. Ensure `self.step` is set (via orchestrator) and extract command text plus optional timeout; format TL question with RUN_COMMAND strings.
2. Ask the user for confirmation; allow them to edit/replace the command inline. If declined, log skip, set EX_SKIP_COMMAND, call `complete()`, and finish.
3. When approved, capture start time, run the command through `ProcessManager.run_command` (stream output chunks to dedicated CLI source).
4. After completion, invoke the `ran_command` template, providing task steps, current task, step index, command, timeout, and captured stdout/stderr/status; parse into `CommandResult` (analysis + success flag).
5. Call `complete()` to mark the step finished in the next state, set EX_RUN_COMMAND action, and persist an `ExecLog` entry with all metadata including duration and analysis.
6. If the LLM indicates failure, bubble up via `AgentResponse.error` with full context; otherwise finish successfully.

## Anti-patterns
- Executing without user confirmation or ignoring edited command text
- Forgetting to stream output to the CLI UI source
- Skipping ExecLog persistence or next_state completion updates
- Treating unsuccessful commands as success without raising an error response

## Output
- Command execution status (EX_RUN_COMMAND or EX_SKIP_COMMAND), captured stdout/stderr, `ExecLog` entry, and analysis summarizing success or required follow-up
