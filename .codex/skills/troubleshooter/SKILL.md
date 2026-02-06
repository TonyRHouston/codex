---
name: troubleshooter-25cbd3
description: Use this skill when the user needs help with troubleshooter. It provides
  practical guidance, execution steps, and quality checks for troubleshooter tasks.
keywords: []
source: partially-processed/agents/troubleshooter.py
---

# Troubleshooter

When to use
- When a task or iteration fails testing, or when user reports issues requiring investigation.

Workflow
1. Gather run command and user test instructions; if missing, request them.
2. Generate bug reports or alternative solutions using LLM prompts and helper mixins.
3. Create new iterations, update statuses (e.g., HUNTING_FOR_BUG, IMPLEMENT_SOLUTION), and coordinate testing.

Dependencies
- `core.agents.mixins` (ChatWithBreakdownMixin, IterationPromptMixin, RelevantFilesMixin), `core.llm.parser`.

Output
- Appends new iterations to `next_state.iterations`, updates `next_state.current_iteration` and `next_state.action`.

## When to use

Use this skill when you need troubleshooter automation or guidance.


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
