---
name: internal-overview-59b1d5
description: Use this skill when the user needs help with internal overview. It provides
  practical guidance, execution steps, and quality checks for internal overview tasks.
keywords:
- internal
- mocks
- helpers
- test
- repository
suggested_keywords:
- internal
- mocks
- helpers
- test
- repository
---

# Internal Overview

## When to use
- You need to run or extend unit tests, mocks, or local API simulators in `internal/`
- Understanding the repo's test scaffolding and mock servers for development

## Workflow
1. Inspect `internal/` for test helpers, mocks, and local round-trippers.
2. Run unit or integration tests using the repository's test harness; inspect mock implementations for expected behavior.
3. When adding tests, follow existing patterns for deterministic mocks and small surface-area fixtures.

## Output
- Clear mapping of internal test helpers and guidance to extend or run local mocks

## Anti-patterns (NEVER)
- Never use this skill when the request clearly belongs to a different domain skill.
- Never return unchecked placeholder text as final output.
- Never skip validation when the output drives edits, commands, or decisions.
