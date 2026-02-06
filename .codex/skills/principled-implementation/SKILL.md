---
name: principled-implementation-4db55e
description: Use this skill when the user needs help with principled implementation.
  It provides practical guidance, execution steps, and quality checks for principled
  implementation tasks.
keywords:
- quality-code
- implementation
- clean-code
- logic-rigor
---

# Principled Implementation Workflow

## Rules of Execution
1. **Logic Alignment**: Verify that the code being written maps directly to an approved `plan`.
2. **Minimal Surface Area**: Modify the fewest lines necessary to achieve the requirement.
3. **Side-Effect Audit**: Check if changes impact downstream modules or exported APIs.

## Implementation Steps
- **Scaffold**: Insert comments as placeholders for complex logic.
- **Core Logic**: Implement the primary algorithm or data flow.
- **Validation**: Add error handling and edge-case checks.
- **Clean-up**: Remove debug logs and ensure naming consistency.

## Definition of Done
- No `TODO` comments left in the modified segment.
- Code matches the project's existing style and linting rules.
