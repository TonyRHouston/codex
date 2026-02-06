---
name: tui-exit-shutdown-b94549
description: 'Guide exit, shutdown, and interrupt flows for the Copilot TUI. Use when
  modifying quit behavior or testing shutdown logic.

  Keywords: tui,exit,shutdown,interrupt,codex'
---

# tui-exit-shutdown

## When to use
- Use when the user request explicitly maps to **tui exit shutdown** outcomes.
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
# TUI Exit and Shutdown

## When to use
- Modifying quit behavior in the TUI
- Debugging shutdown/interrupt regressions

## Core model
- Exit modes: ShutdownFirst vs Immediate
- Shutdown completes before exit when using ShutdownFirst

## Key flows
- Ctrl+C: first press arms quit; second press triggers shutdown-first
- Ctrl+D: only when composer empty and no modal is active
- Slash commands: /quit, /exit, /logout trigger shutdown-first immediately

## Anti-patterns (NEVER)
- Use Immediate exit for normal user flows
- Skip interrupt for active work
- Allow modal to leak Ctrl+C into quit flow

## Output expectations
- Clear change summary and affected flows
- Test plan covering Ctrl+C/Ctrl+D and slash commands

## References
- Read references/exit-shutdown-flow.md
