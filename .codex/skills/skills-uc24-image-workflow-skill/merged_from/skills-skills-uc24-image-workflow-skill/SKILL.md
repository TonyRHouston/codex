---
name: skills-skills-uc24-image-workflow-skill
description: Ubuntu Core 24 image creation workflow guidance. Use when asked to build
  a UC24 image, edit/sign model assertions, choose required snaps, or optimize the
  workflow for LLM-friendly, repeatable steps.
source: skills/skills/uc24-image-workflow/SKILL.md
---

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
