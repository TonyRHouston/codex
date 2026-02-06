---
name: re-toolkit-53597e
description: Use this skill when the user needs help with re toolkit. It provides
  practical guidance, execution steps, and quality checks for re toolkit tasks.
keywords:
- reverse-engineering
- binary-analysis
- gdb
- strace
- frida
- crypto-detection
- memory-analysis
- objdump
- radare2
- ghidra
- upx
- assetripper
- android-studio
- unitex
source: V2.txt
allowed-tools: []
---

# re-toolkit

## When to use
- Use when the user request explicitly maps to **re toolkit** outcomes.
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
# Reverse Engineering Toolkit

When to use
- You need a one-stop entry to the RE skills set (static triage, runtime tracing, crypto/compression signatures, memory forensics).

Workflow
1. Static triage via `binary-analysis-playbook` (format ID, readelf/objdump/r2, Ghidra/RetDec).
2. Runtime tracing via `dynamic-instrumentation` (strace/ltrace, GDB/GEF, Frida hooks).
3. Algorithm hints via `crypto-pattern-id` (crypto constants, compression magics).
4. Memory forensics via `gdb-memory-dumper` (strings + entropy in target regions).
5. Summarize findings (format, hot functions, syscalls/libcalls, suspected algorithms, memory hotspots) before deeper decomp.

Dependencies
- Same as underlying skills: readelf/objdump, radare2, gdb/GEF/pwndbg, strace/ltrace, Frida, optional Ghidra/RetDec.

Output
- A concise RE plan or report referencing results from the underlying skills.
