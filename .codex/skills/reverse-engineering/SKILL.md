---
name: reverse-engineering-cffe6d
description: 'Analyze existing systems, binaries, or legacy code to infer behavior
  and structure. Use when documentation is missing or incomplete.

  Keywords: reverse-engineering,legacy,analysis'
---

# Reverse Engineering

## When to use
- Legacy systems with missing documentation
- Opaque binaries or black-box services

## Inputs to gather
- Access level (source, binary, logs, runtime)
- Known inputs/outputs and constraints
- Test harness or sandbox environment

## Analysis workflow
1. Map observable inputs to outputs (black-box tests)
2. Trace execution paths (logs, instrumentation, tracing)
3. Build a behavior model and validate with new cases
4. Document inferred contracts and assumptions

## Techniques
- Binary search behaviors with controlled inputs
- Compare environment variables and flags
- Use diffing on outputs between versions

## Anti-patterns (NEVER)
- Modify the target system before understanding baseline
- Assume undocumented behavior is stable
- Skip documentation of assumptions and evidence

## Output expectations
- Inferred spec and behavior model
- Evidence-backed assumptions and gaps
- Suggested experiments to close unknowns
