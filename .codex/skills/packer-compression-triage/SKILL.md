---
name: packer-compression-triage-5b663c
description: Use this skill when the user needs help with packer compression triage.
  It provides practical guidance, execution steps, and quality checks for packer compression
  triage tasks.
keywords:
- packer-detection
- compression
- entropy
- triage
- upx
source: V2.txt
allowed-tools: []
---

# packer-compression-triage

## When to use
- Use when the user request explicitly maps to **packer compression triage** outcomes.
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
# Packer & Compression Triage

When to use
- You suspect a binary or blob is packed or compressed and need quick confirmation and next steps.

Workflow
1. Check magic bytes/signatures: gzip (1f 8b), bzip2 (42 5a), xz (fd 37 7a 58 5a 00), zlib (78 9c), lz4 (04 22 4d 18), UPX headers, PE section names.
2. Measure entropy on sections/blobs; high entropy (>7.5 bits/byte) suggests packing/encryption.
3. Try first-stage unpack: UPX (`upx -d target`), or dump/decompress blob with matching tool.
4. Re-run static triage on unpacked output.

Dependencies
- Strings/hexdump tools; entropy calculator; UPX (for common packer), decompression tools for detected formats.

Output
- Verdict on likely packing/compression and the recommended initial unpack/decompress step.
