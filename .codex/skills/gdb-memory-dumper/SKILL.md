---
name: gdb-memory-dumper-8046da
description: Use this skill when the user needs help with gdb memory dumper. It provides
  practical guidance, execution steps, and quality checks for gdb memory dumper tasks.
keywords:
- gdb
- memory-dump
- entropy
- strings
- reverse-engineering
source: V2.txt
allowed-tools: []
---

# gdb-memory-dumper

## When to use
- Use when the user request explicitly maps to **gdb memory dumper** outcomes.
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
# GDB Memory Dumper

When to use
- You need quick insight into runtime memory contents (strings, entropy) while debugging a binary.

Workflow
1. Attach or run under GDB/GEF/pwndbg; identify region (heap/stack/mmap) to inspect.
2. Use a helper command (e.g., custom `memdump`) to read bytes, extract printable strings (len >= 4), and compute Shannon entropy; flag high-entropy regions.
3. Iterate: move to adjacent regions, dump more bytes, and log offsets/addresses for later deep RE.

Dependencies
- gdb with Python support (for custom commands) and access to the target process.

Output
- Strings and entropy observations for the inspected region, with addresses to revisit in deeper analysis.
