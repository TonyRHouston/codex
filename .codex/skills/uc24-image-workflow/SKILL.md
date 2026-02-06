---
name: uc24-image-workflow-b060d5
description: Ubuntu Core 24 image creation workflow guidance. Use when asked to build
  a UC24 image, edit/sign model assertions, choose required snaps, or optimize the
  workflow for LLM-friendly, repeatable steps.
---

# uc24-image-workflow

## When to use
- Use when the user request explicitly maps to **uc24 image workflow** outcomes.
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
# Ubuntu Core 24 image workflow

## Workflow

- Collect target hardware and architecture.
- Use a model assertion JSON as the source of truth and keep it in `models/`.
- Edit model fields: `authority-id`, `brand-id`, `timestamp`, and required `snaps`.
- Sign the model to produce a `.model` assertion.
- Build the image with `ubuntu-image`.

## Required snaps (baseline)

- Gadget snap for the target device
- Kernel snap for the target device
- `core24` (base)
- `snapd`
- `console-conf`

## Optimize for LLM usage

- Prefer deterministic, stepwise commands with explicit filenames and paths.
- Ask for missing inputs (device, architecture, IDs, key name) before executing commands.
- If a user request is ambiguous, propose a default (Raspberry Pi arm64) and confirm.

## References

- For concrete command sequences and examples, read `references/uc24-image-workflow.md`.
