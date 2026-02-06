---
name: syscall-io-triage-0a2e58
description: Use this skill when the user needs help with syscall io triage. It provides
  practical guidance, execution steps, and quality checks for syscall io triage tasks.
keywords:
- syscall
- strace
- ltrace
- triage
- network
- file-io
source: V2.txt
allowed-tools: []
---

# syscall-io-triage

## When to use
- Use when the user request explicitly maps to **syscall io triage** outcomes.
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
# Syscall & IO Triage

When to use
- You need a quick view of what a binary touches (network, files, processes) without full debugging.

Workflow
1. Run with focused tracing:
   - Network: `strace -e trace=network -o trace.net target`
   - File IO: `strace -e trace=file -o trace.file target`
   - Summary: `strace -c target`
   - Libcalls: `ltrace -o ltrace.log target` (demangle with `-C`, include syscalls with `-S`).
2. Review logs: find connect/open/read/write/execve patterns and unexpected endpoints/paths.
3. Refine filters and rerun for noisy programs.

Dependencies
- strace, ltrace; runnable target binary.

Output
- Short summary of network endpoints, file paths, and notable process actions observed in the traces.
