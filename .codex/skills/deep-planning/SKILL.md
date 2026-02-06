---
name: deep-planning-0f20a0
description: Use this skill when the user needs help with deep planning. It provides
  practical guidance, execution steps, and quality checks for deep planning tasks.
keywords:
- ambiguous
- complex-architecture
- multi-step
- clarify
- plan
---

# Deep Planning Workflow

## Phase 1: Clarification
Identify and resolve all logical gaps before committing to a plan.
1. **Ambiguity Scan**: List all undefined variables, missing requirements, or technical unknowns.
2. **Clarification Requests**: Phrase specific questions for the user to minimize "guesswork."
3. **Consensus Check**: Ensure user confirms the inferred constraints.

## Phase 2: Structural Planning
1. **Dependency Analysis**: Map the critical path of implementation.
2. **Failure Analysis**: Identify potential edge cases and mitigation strategies.
3. **Iterative Breakdown**: Create a task list where each item is verifiable and scoped to < 1 hour.

## Anti-Patterns
- Starting implementation with unresolved "must-fix" questions.
- Ignoring third-party library constraints until execution.
