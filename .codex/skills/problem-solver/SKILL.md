---
name: problem-solver-be6ec8
description: Use this skill when the user needs help with problem solver. It provides
  practical guidance, execution steps, and quality checks for problem solver tasks.
keywords:
- solutions
- alternative
- user
- iteration
- problem
suggested_keywords:
- solutions
- alternative
- user
- iteration
- problem
---

# Problem Solver

## When to use
- An iteration is stuck in a loop and lists alternative solutions
- The user needs help deciding the next fix attempt after repeated failures

## Workflow
1. Inspect the current iteration: split alternative solutions into tried vs pending and reuse previous attempts for context.
2. If no pending solutions remain, call the `get_alternative_solutions` template to generate fresh options, append them to the iteration, and flag modifications.
3. Otherwise, present the pending solutions to the user as numbered buttons plus a "None" fallback; capture their choice.
4. If the user picks "None" (or cancels), mark all pending options as tried with feedback so they are not offered again.
5. When a solution is chosen, feed it (plus user feedback and Q&A) into `find_solution` to draft implementation instructions; record the resulting description, mark the selected solution as tried, increment attempt count, and set status to `PROBLEM_SOLVER`.

## Anti-patterns
- Continuing without user confirmation on which solution to try next
- Failing to mark solutions as tried or to capture user feedback, causing repeats
- Forgetting to flag iteration modifications after updating alternative solutions

## Output
- Updated iteration alternative_solutions list, new troubleshooting instructions, incremented attempt counter, and status transitioned to PROBLEM_SOLVER
