---
name: bug-hunter-3d6e09
description: Use this skill when the user needs help with bug hunter. It provides
  practical guidance, execution steps, and quality checks for bug hunter tasks.
keywords: []
source: partially-processed/agents/bug_hunter.py
---

# Bug Hunter

When to use
- When an iteration is in a bug-hunting state or user reports failing behavior; for log aggregation and reproduction instructions.

Workflow
1. If needed, request bug reproduction instructions via LLM (`get_bug_reproduction_instructions`).
2. Check logs using a dedicated LLM check (`check_logs`) and stream breakdowns to UI.
3. Decide whether more logs are needed or a fix is identified; update iteration status accordingly.
4. Coordinate user testing and pair programming flows when required.

Dependencies
- `core.agents.mixins.ChatWithBreakdownMixin`, `core.llm.parser.JSONParser`, telemetry and UI helpers.

Output
- Updates `next_state.current_iteration` statuses, `next_state.action`, and may append `bug_hunting_cycles` with instructions.

## When to use

Use this skill when you need bug-hunter automation or guidance.


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
