---
name: mixins-c785c0
description: Use this skill when the user needs help with mixins. It provides practical
  guidance, execution steps, and quality checks for mixins tasks.
keywords:
- internal
- mixins
- helpers
source: partially-processed/agents/mixins.py
---

Provides mixin classes used across agents (e.g., iteration prompts, breakdown helpers). This is an internal library, not a user-facing skill.

When to use
- Inspect `partially-processed/agents/mixins.py` when reusing iteration or parsing helpers.

Workflow
1. Include mixins into agent classes to reuse behavior.

Dependencies
- Internal only.

Output
- N/A

## When to use
- Use when the user request maps directly to this skill's domain or prompt objective.
- Use to standardize outputs when consistency matters more than creativity.

## Workflow
1. Confirm user intent and expected output format.
2. Apply this skill's core instructions to generate the first pass.
3. Validate output against constraints and revise for correctness.
4. Return concise output with any assumptions explicitly stated.

## Anti-patterns (NEVER)
- Never use this skill when the request clearly belongs to a different domain skill.
- Never return unchecked placeholder text as final output.
- Never skip validation when the output drives edits, commands, or decisions.
