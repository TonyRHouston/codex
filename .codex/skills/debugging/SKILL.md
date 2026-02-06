---
name: debugging-56a102
description: 'Expert debugging for complex failures across languages, stacks, and
  environments. Use when root cause is unclear, tests are flaky, or logs show contradictory
  signals.

  Keywords: debugging,root-cause,triage,logs'
---

# Debugging

## When to use
- Intermittent failures, flaky tests, or environment-specific bugs
- Logs contradict each other or symptoms do not match the hypothesis
- Regressions without an obvious code change

## Inputs to gather
- Reproduction steps and minimal failing input
- Recent code/config changes (diff or deploy history)
- Logs, metrics, and traces around the failure window
- Environment details (versions, flags, data samples)

## Debugging workflow
1. Reproduce reliably, then minimize the failing case
2. Isolate: binary search changes, dependencies, and configs
3. Form a single hypothesis, run one experiment, record results
4. Confirm root cause with evidence, then fix and verify

## Decision framework
- Flaky tests: check timing, shared state, parallelism, and nondeterminism
- Environment-only failures: inspect config, secrets, feature flags, or OS differences
- Data-dependent bugs: capture the exact input and trace the transformation path
- Race conditions: add deterministic synchronization or single-threaded repro

## Anti-patterns (NEVER)
- Shotgun changes that alter multiple variables at once
- Rely on print-debugging without time-bounding experiments
- Stop after symptom relief without proving the root cause
- Ignore warnings or error logs that do not match the theory

## Output expectations
- Root cause statement with evidence
- Minimal fix plan and verification steps
- Any new guardrails (test, alert, or regression check)
