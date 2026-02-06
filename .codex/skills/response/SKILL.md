---
name: response-1023be
description: Use this skill when the user needs help with response. It provides practical
  guidance, execution steps, and quality checks for response tasks.
keywords:
- internal
- response
- parser
source: partially-processed/agents/response.py
---

Utilities for parsing LLM responses and extracting structured data. Internal library; not a standalone skill.

When to use
- When implementing response parsing or JSON extraction helpers.

Workflow
1. Parse model outputs into structured shapes and validate them.

Dependencies
- Internal parsing utilities.

Output
- Structured Python objects or JSON.

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
