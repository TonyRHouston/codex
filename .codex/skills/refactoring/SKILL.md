---
name: refactoring-540919
description: 'Plan and execute safe refactors with regression control. Use when changing
  structure without changing behavior.

  Keywords: refactor,architecture,tests'
---

# Refactoring

## When to use
- Structural code changes without feature additions
- High-risk areas that need cleanup or modularization

## Inputs to gather
- Behavioral contracts and acceptance criteria
- Existing tests and coverage gaps
- Dependencies and integration points

## Refactor workflow
1. Define invariants and add missing tests
2. Break the refactor into small, reversible steps
3. Run tests after each step and keep changes isolated
4. Validate behavior in production-like scenarios

## Safety rules
- Prefer rename/move before logic changes
- Keep commits small and rollbackable
- Use feature flags for risky structural shifts

## Anti-patterns (NEVER)
- Combine refactor with new features
- Large rewrites without tests
- Rename or move and change logic in one step

## Output expectations
- Stepwise refactor plan with checkpoints
- Test coverage additions and verification
- Rollback strategy if behavior shifts
