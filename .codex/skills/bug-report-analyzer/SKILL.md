---
name: bug-report-analyzer-b256ff
description: Use this skill when the user needs help with bug report analyzer. It
  provides practical guidance, execution steps, and quality checks for bug report
  analyzer tasks.
keywords:
- bug-report
- triage
- reproduction
- quality-assurance
- root-cause
---

# bug-report-analyzer

## When to use
- Use when the user request explicitly maps to **bug report analyzer** outcomes.
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
# Bug Report Analysis Workflow

## 1. Input Validation
Check for mandatory fields in the report:
- **Environment**: OS, Version, Browser, etc.
- **Expected vs. Actual**: Is the defect clearly described?
- **Reproduction**: Are there specific, repeatable steps?

## 2. Technical Evaluation
- **Severity Rating**: Does this block core functionality or is it aesthetic?
- **Root Cause Hypothesis**: Based on logs or screenshots, which module is likely failing?
- **Reproduction Proof**: Attempt to script the failure locally.

## 3. Categorization
- **Confirmed**: Bug reproduced and understood.
- **Needs Info**: Insufficient data to reproduce.
- **Duplicate**: Already tracked in another issue.

## Principle
- A bug not reproducible is a bug not yet understood. Prioritize reproduction evidence over implementation guesses.
