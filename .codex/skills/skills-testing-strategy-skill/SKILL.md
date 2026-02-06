---
name: skills-testing-strategy-skill-2abea4
description: 'Design robust test strategies, coverage plans, and test suites. Use
  when deciding what to test, which layers to cover, or how to prevent regressions.

  Keywords: testing,unit,integration,e2e,coverage

  '
source: skills/testing-strategy/SKILL.md
---

# Testing Strategy

## When to use
- New features, major refactors, or missing coverage
- Flaky tests or unclear test ownership
- Choosing between unit, integration, and end-to-end coverage

## Inputs to gather
- Critical user flows and system invariants
- Existing tests and known gaps
- Failure modes and risk areas

## Strategy framework
- Build a test matrix: risks x layers (unit, integration, e2e)
- Keep unit tests dominant; use integration for boundaries
- Keep e2e minimal and focused on critical paths only
- Add property or contract tests for invariant-heavy logic

## Design rules
- One logical assertion per test when possible
- Control nondeterminism (time, randomness, concurrency)
- Prefer clear fixtures and data builders over ad-hoc setup

## Anti-patterns (NEVER)
- Make e2e the default for every behavior
- Tests that require order or shared global state
- Sleep-based timing without deterministic synchronization
- Snapshot tests for logic-heavy behavior

## Output expectations
- Coverage plan by layer and risk
- Concrete test cases to add or update
- Regression guardrails for high-risk paths
