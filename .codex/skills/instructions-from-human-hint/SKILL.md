---
name: instructions-from-human-hint-4a9f01
description: Use this skill when the user needs help with instructions from human
  hint. It provides practical guidance, execution steps, and quality checks for instructions
  from human hint tasks.
---

When to use
- Use when you need the prompt at partially-processed/prompts/bug-hunter/instructions_from_human_hint.prompt as guidance.

Workflow
1. Open the prompt file and read its instructions.
2. Apply the prompt to the current task, filling any placeholders.
3. Produce the response in the format the prompt requests.

Output
- A response consistent with the referenced prompt.

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
