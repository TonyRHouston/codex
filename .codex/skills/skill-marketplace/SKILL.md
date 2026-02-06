---
name: skill-marketplace-e9320c
description: Use this skill when the user needs help with skill marketplace. It provides
  practical guidance, execution steps, and quality checks for skill marketplace tasks.
keywords:
- skill
- skills
- install
- add
- marketplace
suggested_keywords:
- skill
- skills
- install
- add
- marketplace
---

# Skill Marketplace

## When to use
- Installing or distributing skills/plugin packs for Kode-compatible agents

## Workflow
1. Add a marketplace (local path or GitHub shorthand zip).
2. Install plugin packs with scope: user (`~/.kode/...`) or project (`.kode/...`).
3. Enable/disable plugins per scope; list configured marketplaces.
4. For direct installs, use `add-skill` CLI to pull skills from any repo (optionally global, select skills by name).

## Anti-patterns
- Mixing scopes unintentionally (user vs project)
- Forgetting to enable after install
- Installing without verifying source trust

## Output
- Marketplace/skill actions performed, scope, and resulting installed/disabled/enabled state
