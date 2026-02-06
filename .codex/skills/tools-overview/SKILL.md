---
name: tools-overview-fe85a1
description: Use this skill when the user needs help with tools overview. It provides
  practical guidance, execution steps, and quality checks for tools overview tasks.
keywords:
- scripts
- tool
- tools
- utility
- entrypoints
suggested_keywords:
- scripts
- tool
- tools
- utility
- entrypoints
---

# tools-overview

## When to use
- Use when the user request explicitly maps to **tools overview** outcomes.
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
# Tools Overview

## When to use
- You want a quick map of utility scripts, services, and invocation patterns in the repo
- Agents need to pick the right helper tool for tasks like fetching docs, running linters, or packaging assets

## Workflow
1. Scan `Tools/` and all `tools*` directories for executable scripts and tool manifests.
2. Record CLI signatures and environment expectations so agents can call them with correct flags.
3. Prefer documented entrypoints; if missing, add a short `--help` extraction step to the tool inventory.

## Output
- A curated index of scripts with sample invocations, expected inputs, and side effects for safe agent use
