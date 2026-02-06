---
name: binary-analysis-playbook-2c9c00
description: Use this skill when the user needs help with binary analysis playbook.
  It provides practical guidance, execution steps, and quality checks for binary analysis
  playbook tasks.
keywords:
- binary-analysis
- reverse-engineering
- static-analysis
- dynamic-analysis
- gdb
- strace
- readelf
- objdump
- radare2
- ghidra
source: V2.txt
allowed-tools: []
---

# binary-analysis-playbook

## When to use
- Use when the user request explicitly maps to **binary analysis playbook** outcomes.
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
# Binary Analysis Playbook

When to use
- You need a concise checklist to triage and analyze binaries (ELF/PE/Mach-O) via static and dynamic techniques.

Workflow
1. Identify format and symbols: `readelf -h/-l/-S/-s`, `objdump -x/-d -M intel`, or platform equivalents (`pefile`, `otool`).
2. Disassemble and map functions: `r2 -A` (`pdf`, `afl`) or `objdump -d`; follow branches/jumps; optionally script Capstone for recursive descent.
3. Decompile for structure: Ghidra or r2ghidra (`pdg @ sym.main`); RetDec/IDA if available.
4. Pattern-match algorithms: scan for crypto constants (MD5/SHA/AES/TEA/RC4) and compression magics (gzip/bzip2/xz/zlib/lz4).
5. Dynamic tracing: run under GDB/GEF/Pwntools helpers; set breakpoints, inspect regs/stack; trace syscalls with `strace -e trace=network|file` and libc calls with `ltrace -C/-S`.
6. Instrument memory: in GDB, dump regions, extract strings, and check entropy (high entropy suggests encryption/compression).

Dependencies
- CLI tools: readelf/objdump, gdb (+GEF/pwndbg optional), strace, ltrace, radare2, Ghidra/RetDec (optional GUI/CLI installs).
- Target binary accessible locally; for Windows/Mach-O use pefile/otool equivalents.

Output
- A short report or notes covering: file format/security features, key functions/CFG hotspots, suspected algorithms (crypto/compression), observable syscalls/IO, and any high-entropy or sensitive regions for deeper review.
