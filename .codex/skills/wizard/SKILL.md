---
name: wizard-7d510f
description: Use this skill when the user needs help with wizard. It provides practical
  guidance, execution steps, and quality checks for wizard tasks.
keywords: []
source: partially-processed/agents/wizard.py
---

# Wizard

When to use
- During initial project setup to initialize templates, frontend epics, and project knowledge base.

Workflow
1. If project type is `swagger`, request OpenAPI/Swagger docs and upload them; otherwise set default options.
2. Initialize knowledge base and create initial frontend epic.
3. Return `AgentResponse.create_specification` to trigger Spec Writer flow.

Dependencies
- `core.db.models.KnowledgeBase`, `core.ui.base`, HTTP upload to RAG service (`PYTHAGORA_API`).

Output
- Initializes `next_state.epics`, `next_state.knowledge_base`, and may set template options.

## When to use

Use this skill when you need wizard automation or guidance.


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
