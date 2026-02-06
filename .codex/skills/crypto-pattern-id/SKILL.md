---
name: crypto-pattern-id-f4aee1
description: Use this skill when the user needs help with crypto pattern id. It provides
  practical guidance, execution steps, and quality checks for crypto pattern id tasks.
keywords:
- crypto-detection
- constants
- compression
- signatures
- reverse-engineering
source: V2.txt
allowed-tools: []
---

# crypto-pattern-id

## When to use
- Use when the user request explicitly maps to **crypto pattern id** outcomes.
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
# Crypto & Compression Pattern ID

When to use
- You need to guess algorithms used in a binary or blob before full decompilation.

Workflow
1. Extract strings/bytes (e.g., `strings`, hexdump) or parse sections with `readelf/objdump`.
2. Check crypto constants: MD5/SHA state words, AES S-box/rcon, TEA delta, RC4 0..255 permutation.
3. Check compression magics: gzip (1f 8b), bzip2 (42 5a), xz (fd 37 7a 58 5a 00), zlib (78 9c), lz4 (04 22 4d 18).
4. Correlate with code paths (init tables, round loops) from disassembly/decompilation to confirm.

Dependencies
- Hex/strings tools; optional scripting to scan sections for constants.

Output
- Short list of suspected algorithms and the offsets/sections where signatures were found.
