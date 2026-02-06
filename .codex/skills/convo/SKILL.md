---
name: convo-1d1f43
description: Use this skill when the user needs help with convo. It provides practical
  guidance, execution steps, and quality checks for convo tasks.
keywords:
- internal
- convo
- chat
source: partially-processed/agents/convo.py
duplicate_of: response
---

Conversation utilities used by multiple agents. Not a standalone skill; provides helpers for building chats and conversation state.

When to use
- When implementing or debugging chat flows in agent code.

Workflow
1. Compose and parse conversational turns.

Dependencies
- Internal code; refer to `partially-processed/agents/convo.py`.

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
