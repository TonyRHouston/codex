---
name: kode-cli-bf39e7
description: Use this skill when the user needs help with kode cli. It provides practical
  guidance, execution steps, and quality checks for kode cli tasks.
keywords:
- cli
- kode
- run
- skill
- agent
suggested_keywords:
- cli
- kode
- run
- skill
- agent
---

# kode-cli

## When to use
- Use when the user request explicitly maps to **kode cli** outcomes.
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
# Kode CLI

## When to use
- You need to install or manage skill packs with the Kode CLI
- Automating agent workflows that rely on `Kode-cli` manifest files

## Workflow
1. Discover `Kode-cli` manifests and supported commands in the directory; inspect example invocations.
2. Run the CLI in a sandbox (or with `--dry-run`) to validate changes prior to applying them to a repo.
3. Use Kode CLI to produce reproducible environment setup scripts consumed by agents or CI.

## Output
- Standardized install scripts, manifest interpretations, and reproducible environment steps
