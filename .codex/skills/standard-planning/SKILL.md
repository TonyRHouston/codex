---
name: standard-planning-b39ad7
description: Use this skill when the user needs help with standard planning. It provides
  practical guidance, execution steps, and quality checks for standard planning tasks.
keywords:
- feature
- maintenance
- roadmap
- enhancement
---

# standard-planning

## When to use
- Use when the user request explicitly maps to **standard planning** outcomes.
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
# Standard Planning Workflow

## Steps
1. **Context Assessment**: Review existing related modules and documentation.
2. **Logical Mapping**: Outline the flow of data or control between components.
3. **Preparation Checklist**:
   - Environment variables needed?
   - New dependencies required?
   - Test coverage plan?
4. **Task Decomposition**: Create a linear todo list in the workspace state.

## Rules of Engagement
- Every plan must include a definition of "Done."
- Every plan must specify which existing files will be modified vs. created.
