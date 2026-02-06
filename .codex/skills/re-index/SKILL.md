---
name: re-index
description: Index and router skill for reverse-engineering tasks. Selects the correct RE sub-skill for static analysis, dynamic analysis, memory/syscall triage, or packed binaries.
keywords:
- reverse-engineering
- binary-analysis
- disassembly
- debugging
- triage
suggested_keywords:
- re
- reverse engineering
- binary triage
---

# RE Index

## Purpose
Use this skill as the first stop for reverse-engineering requests. Route to one focused sub-skill.

## Route to
- `reverse-engineering-cffe6d` or `skills-reverse-engineering-skill-23ec3c`: broad legacy/system behavior inference.
- `re-toolkit-53597e`: general tooling workflow for RE tasks.
- `binary-analysis-playbook-2c9c00`: structured static binary analysis.
- `cfg-disassembly-mapper-7b3133`: control-flow/disassembly mapping tasks.
- `dynamic-instrumentation-3d0d90`: runtime behavior instrumentation.
- `gdb-memory-dumper-8046da`: memory extraction and dump workflows.
- `syscall-io-triage-0a2e58`: syscall and I/O behavior triage.
- `packer-compression-triage-5b663c`: packed/compressed binary triage.

## Quick routing rules
- Unknown behavior in legacy binary/app -> `reverse-engineering` / `skills-reverse-engineering-skill`
- Need a practical tool chain first -> `re-toolkit`
- Static reverse-engineering path -> `binary-analysis-playbook`
- CFG graph or disassembly structure focus -> `cfg-disassembly-mapper`
- Runtime hooks/tracing/instrumentation -> `dynamic-instrumentation`
- Memory capture requirement -> `gdb-memory-dumper`
- Syscall/file/network behavior debugging -> `syscall-io-triage`
- Suspected packed/protected sample -> `packer-compression-triage`

## Trigger phrases
- "reverse engineer this"
- "analyze this binary"
- "map disassembly/cfg"
- "instrument runtime behavior"
- "dump process memory"
- "triage packed executable"

## Output
- Deterministic selection of one RE sub-skill and a focused execution path with minimal overlap.
