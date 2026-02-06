---
name: issue-triage-bb8d48
description: Use this skill when the user needs help with issue triage. It provides
  practical guidance, execution steps, and quality checks for issue triage tasks.
keywords:
- issue
- triage
- priority
- labels
- backlog
---

# issue-triage

## When to use
- Use when the user request explicitly maps to **issue triage** outcomes.
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
# Issue Triage Workflow

## 1. First Response
- Acknowledge receipt of the issue/feature request.
- Assign initial labels based on domain (e.g., `bug`, `enhancement`, `security`).

## 2. Priority Alignment
Use a weighted matrix:
- **Critical (P0)**: System down, security vulnerability.
- **High (P1)**: Major feature broken, no workaround.
- **Medium (P2)**: Feature sub-optimal, workaround exists.
- **Low (P3)**: Minor polish, technical debt.

## 3. Lifecycle Routing
- **Unconfirmed**: Awaiting triage.
- **Backlog**: Approved but not scheduled.
- **Ready**: Scoped and ready for developer assignment.

## Best Practice
- Ensure every issue has a "Clear Problem Statement" before it moves to "Ready."
