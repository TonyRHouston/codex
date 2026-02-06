---
name: base-ad80ac
description: Use this skill when the user needs help with base. It provides practical
  guidance, execution steps, and quality checks for base tasks.
keywords:
- internal
- base
- utilities
source: partially-processed/agents/base.py
---

Internal utilities used by agent implementations. This is not intended to be used as a standalone skill.

When to use
- Refer to `partially-processed/agents/base.py` when implementing agent lifecycle helpers.

Workflow
1. Provide shared agent lifecycle methods and helpers.

Dependencies
- Internal code only; not exposed as a skill.

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
