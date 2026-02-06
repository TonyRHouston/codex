---
name: task-troubleshooter-09cadc
description: Use this skill when the user needs help with task troubleshooter. It
  provides practical guidance, execution steps, and quality checks for task troubleshooter
  tasks.
keywords:
- feedback
- task
- iteration
- instructions
- status
suggested_keywords:
- feedback
- task
- iteration
- instructions
- status
---

# Task Troubleshooter

## When to use
- After a developer completes implementation and the task needs testing feedback
- When iterations must gather user bug reports, change requests, or quick redoes

## Workflow
1. If an iteration is already in FIND_SOLUTION, reuse stored feedback and call `find_solution` to draft implementation instructions, then set status to IMPLEMENT_SOLUTION.
2. Otherwise, bootstrap a new iteration:
   - Determine (or infer) the run command, fetching via `get_run_command` when missing.
   - If task lacks testing instructions, generate them from route files and save them before requesting feedback.
   - Present test instructions to the user, along with rerun/run-command hooks.
3. Solicit user feedback using TS prompts: Everything works, There is an issue, I want to change spec, or Redo task.
   - Handle redo requests by capturing additional human instructions and exiting so the orchestrator reloads earlier state.
   - For change/bug paths, gather detailed feedback, fetch relevant files, and classify iteration status (NEW_FEATURE_REQUESTED vs HUNTING_FOR_BUG).
4. Detect loops using iteration counts; set status to PROBLEM_SOLVER when loops recur and trace telemetry events.
5. Append the new iteration to next_state with proper metadata (user_feedback, attempts, status, bug_hunting_cycles) and flag modifications. When no further work is required, mark the task reviewed, set TS_TASK_REVIEWED, and end the loop.

## Anti-patterns
- Skipping run command discovery, leaving users without execution instructions
- Failing to store test instructions or relevant files for subsequent iterations
- Ignoring loop detection, starving ProblemSolver of alternative solutions
- Leaving iteration status unset when user requests a spec change or reports a bug

## Output
- Updated iterations list (feedback, status, attempts), task test instructions, run command, and UI actions such as TS_TASK_REVIEWED or TS_ALT_SOLUTION
