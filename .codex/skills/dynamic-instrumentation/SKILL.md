---
name: dynamic-instrumentation-3d0d90
description: Use this skill when the user needs help with dynamic instrumentation.
  It provides practical guidance, execution steps, and quality checks for dynamic
  instrumentation tasks.
keywords:
- dynamic-analysis
- instrumentation
- gdb
- strace
- ltrace
- frida
- memory-dump
source: V2.txt
allowed-tools: []
---

# dynamic-instrumentation

## When to use
- Use when the user request explicitly maps to **dynamic instrumentation** outcomes.
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
# Dynamic Instrumentation

When to use
- You need runtime visibility into a binary: syscalls, library calls, memory contents, or inline function hooks.

Workflow
1. Baseline tracing: `strace -o trace.log target` (focus: `-e trace=network|file`); `ltrace -o ltrace.log target` (libcalls, demangle with `-C`, include syscalls with `-S`).
2. Debug + inspect: run under GDB/GEF/pwndbg; set breakpoints (e.g., `break main`), inspect regs/stack (`info registers`, `x/20x $rsp`), and disassemble around IP.
3. Memory forensics in GDB: use a helper to dump regions, extract printable strings, and compute entropy; flag high-entropy regions (>7.5 bits/byte) for possible crypto/compression.
4. Frida hooks: attach to exported functions (e.g., `open`) with `Interceptor.attach`, log args/returns, and patch behavior at runtime.
5. Iterate: tighten filters to noisy traces, add targeted breakpoints, and re-run with sample inputs.

Dependencies
- strace, ltrace, gdb (with GEF/pwndbg optional), Frida (node/python host + frida-server/remote target if needed).
- Target binary runnable in the current environment; symbols optional but helpful.

Output
- Collected traces (syscalls/libcalls), runtime notes (registers/stack observations), memory string/entropy findings, and any Frida hook logs for further reverse-engineering.
