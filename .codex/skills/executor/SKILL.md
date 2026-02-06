---
name: executor-9b6688
description: Use this skill when the user needs help with executor. It provides practical
  guidance, execution steps, and quality checks for executor tasks.
keywords: []
source: partially-processed/agents/executor.py
---

# Executor

When to use
- When a task step includes a `command` to run locally as part of implementation or debugging.

Workflow
1. Confirm command with user (ask_question), optionally edit.
2. Run command via `ProcessManager.run_command`, stream stdout/stderr to UI.
3. Evaluate command output with an LLM (`ran_command` prompt) and return `CommandResult` analysis.
4. Log execution and record `ExecLog` via state manager.

Dependencies
- `core.proc.process_manager.ProcessManager`, `core.llm.parser.JSONParser`, `core.proc.exec_log.ExecLog`.

Output
- Persists `ExecLog` entries, sets `next_state.action` and may return AgentResponse.done or AgentResponse.error with details.

## When to use

Use this skill when you need executor automation or guidance.


## Workflow

1. Validate inputs.
2. Run core logic.
3. Return structured output.


## Dependencies

- Repository prompts and templates (check `prompt` paths).
- Access to repo filesystem.


## Output

Structured JSON or markdown describing the result.

## Anti-patterns (NEVER)
- Never use this skill when the request clearly belongs to a different domain skill.
- Never return unchecked placeholder text as final output.
- Never skip validation when the output drives edits, commands, or decisions.
