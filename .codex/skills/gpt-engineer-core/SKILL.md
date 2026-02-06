---
name: gpt-engineer-core-438553
description: Use this skill when the user needs help with gpt engineer core. It provides
  practical guidance, execution steps, and quality checks for gpt engineer core tasks.
keywords:
- gpt
- engineer
- core
- cli
- helpers
suggested_keywords:
- gpt
- engineer
- core
- cli
- helpers
---

# gpt-engineer-core

## When to use
- Use when the user request explicitly maps to **gpt engineer core** outcomes.
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
# GPT Engineer Core

## When to use
- You need to interact with `gpt_engineer/` code, run its CLI, or adapt core helpers like `SimpleAgent` and `DiskExecutionEnv`

## Workflow
1. Locate the `gpt_engineer/` directory and identify CLI entrypoints and config files.
2. Use the provided helpers for generating code, running entrypoints, and persisting artifacts to disk.
3. Wire any custom AI backends by supplying compatible `AI` instances to agent constructors for local testing.

## Output
- Guidance for running GPT Engineer CLI flows and integrating core helpers into higher-level orchestration
