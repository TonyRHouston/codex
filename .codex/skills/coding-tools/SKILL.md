---
name: coding-tools-d1f49b
description: Use this skill when the user needs help with coding tools. It provides
  practical guidance, execution steps, and quality checks for coding tools tasks.
keywords:
- tools
- coding
- developer
- helper
- scripts
suggested_keywords:
- tools
- coding
- developer
- helper
- scripts
---

# coding-tools

## When to use
- Use when the user request explicitly maps to **coding tools** outcomes.
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
# Coding Tools

## When to use
- You want to run small utilities (formatters, generators, test runners) bundled with the repository
- A troubleshooting step needs reproducible helper commands present in `Coding_Tools` or `tools/`

## Workflow
1. Inspect `Coding_Tools` for README entries and discover available scripts.
2. Prefer invoking helpers via the provided wrapper (if present) to maintain environment consistency.
3. When adding new utilities, include short usage docs and a test harness so agents can call them safely.

## Output
- A known inventory of small, testable developer helpers with documented invocations for agent usage
