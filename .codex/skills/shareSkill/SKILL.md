---
name: shareskill
description: Use this skill when the user needs help with shareSkill. It provides
  practical guidance, execution steps, and quality checks for shareSkill tasks.
---

# Copilot instructions for shareAI-skills

## Build, test, lint
- No build/lint/test commands are defined in this repository. There are no package managers or CI configs present.

## High-level architecture
- This repository is a collection of **agent skills**. Each skill lives in `skills/<skill-name>/` and is primarily defined by a `SKILL.md` file with YAML frontmatter (`name`, `description`) and a body of domain guidance.
- Skill content can be layered:
  - Core instructions in `SKILL.md`
  - Deep-dive references in `references/`
  - Optional scripts in `scripts/` (e.g., `skills/agent-builder/scripts/init_agent.py`)
  - Optional assets/templates in `assets/`
- The `.claude-plugin/plugin.json` declares plugin metadata and lists available skill directories; this repo is intended to be consumed by agent CLIs (Kode, Claude Code, Cursor) as skill packages.

## Key conventions
- **Skills are knowledge, not code**: keep `SKILL.md` focused on expert-only knowledge and decision frameworks, not tutorials or obvious basics.
- **Use YAML frontmatter** at the top of each `SKILL.md` with `name` and a trigger-rich `description` that helps the agent decide when to load the skill.
- **Progressive disclosure**: put heavyweight guidance in `references/` and load it only when the task matches the scenario.
- **NEVER lists** and anti-patterns are expected in skill content to encode expert pitfalls.
- New skills should follow the documented structure in README: `skills/<name>/SKILL.md` plus optional `references/`, `scripts/`, `assets/`.
