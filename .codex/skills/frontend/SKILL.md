---
name: frontend-c0f2e7
description: Use this skill when the user needs help with frontend. It provides practical
  guidance, execution steps, and quality checks for frontend tasks.
keywords: []
source: partially-processed/agents/frontend.py
---

# Frontend

When to use
- To generate or continue building the frontend part of the project, including template application and UI iteration.

Workflow
1. Start frontend flow: clear logs, announce build, and call LLM template `build_frontend`.
2. Process returned code blocks, apply changes, optionally run auto-debug and iteration logic.
3. When finished, set frontend iteration flags and possibly move to backend steps.

Dependencies
- `core.llm.parser.DescriptiveCodeBlockParser`, `core.agents.git.GitMixin`, process manager for auto-debug.

Output
- Writes frontend files, updates `next_state.epics` messages and `fe_iteration_done` flags, and may update knowledge base.

## When to use

Use this skill when you need frontend automation or guidance.


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
