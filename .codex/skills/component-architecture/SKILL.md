---
name: component-architecture-eba386
description: Use this skill when the user needs help with component architecture.
  It provides practical guidance, execution steps, and quality checks for component
  architecture tasks.
keywords:
- react
- components
- modular
- interface
- props
---

# component-architecture

## When to use
- Use when the user request explicitly maps to **component architecture** outcomes.
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
# Component Architecture Workflow

## 1. Logical Scoping
- **Atomicity**: Can this be broken down further?
- **Responsibility**: Should this component handle state, or just render it?

## 2. Interface Definition
- Set strict prop/input types (no `any`).
- Define clear events/outputs.
- Ensure "Single Source of Truth" for state management.

## 3. Isolation & Verification
- **Visual/Unit Logic**: Verify in isolation (e.g., Storybook or Component Tests).
- **Theming**: Ensure no hard-coded styles; use design tokens.

## Rules
- Components must be "pure" where possible.
- Side effects must be contained in hooks or dedicated controllers.
