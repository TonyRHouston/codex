---
name: type-safety-enforcer-f3b4d5
description: Use this skill when the user needs help with type safety enforcer. It
  provides practical guidance, execution steps, and quality checks for type safety
  enforcer tasks.
keywords:
- typescript
- type-safety
- any
- interfaces
- types
---

# type-safety-enforcer

## When to use
- Use when the user request explicitly maps to **type safety enforcer** outcomes.
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
# Type Safety Enforcement

## The "Zero Any" Policy
- Use of `any` is a failure condition unless mandated by a specific library limitation.
- Use `unknown` with type guards if the type is truly dynamic.

## Workflow
1. **Interface Mapping**: Define the shape of all inputs and outputs before writing logic.
2. **Generics Implementation**: Use generics for reusable utility functions to maintain end-to-end safety.
3. **Type Narrowing**: Implement custom type guards (`isType`) for complex union types.

## Verification
- Run `tsc --noEmit` to confirm no hidden regressions.
- Ensure all external API responses are cast to validated interfaces.
