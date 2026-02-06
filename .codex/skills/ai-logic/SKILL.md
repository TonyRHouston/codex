---
name: ai-logic-8ac66a
description: Use this skill when the user needs help with ai logic. It provides practical
  guidance, execution steps, and quality checks for ai logic tasks.
keywords:
- prompt
- reusable
- helpers
- response
- pipelines
suggested_keywords:
- prompt
- reusable
- helpers
- response
- pipelines
---

# ai-logic

## When to use
- Use when the user request explicitly maps to **ai logic** outcomes.
- Use when consistent, repeatable outputs are more important than ad-hoc responses.

## Decision Framework
Before acting, evaluate the **why**, trade-off, and risk profile:
- **Why now**: what user outcome or blocker is this skill resolving?
- **Trade-off**: what speed vs quality decision is acceptable for this turn?
- **Scope boundary**: what is in-scope for this skill vs another domain skill?
- **Verification strategy**: what concrete check proves the result is correct?

## Workflow
1. Confirm intent, constraints, and expected output format.
2. Apply this skill's domain logic to produce a first-pass result.
3. Validate the result against correctness, safety, and completeness checks.
4. Refine output and state assumptions, limitations, and next action clearly.

## Anti-patterns (NEVER)
- Never proceed when intent is ambiguous and high-impact decisions are involved.
- Never mix unrelated domain steps without an explicit decision to do so.
- Do not ship output that has not been validated against the requested constraints.
- Avoid placeholder text, guessed facts, or silent omissions in final output.
- Never use this skill when a more specific skill is clearly the better fit.
- Don't skip verification because an initial result "looks right".

## Output Expectations
- Clear, task-aligned result with explicit assumptions.
- Evidence of validation steps performed.
- Concise summary of what was done and what remains.

## Existing Notes
# AI Logic

## When to use
- You need to compose multi-step prompt pipelines or reuse common LLM utilities
- Normalizing prompt templates, response parsing, or structured output extraction

## Workflow
1. Identify reusable prompt fragments and parameterize them for safety and reuse.
2. Use provided helpers to build messages, sanitize inputs, and parse structured responses (JSON, YAML).
3. Centralize retry/backoff and error-handling policies for calls to external models.

## Output
- Reusable prompt components, sanitizers, and parsers ready for agent orchestration
