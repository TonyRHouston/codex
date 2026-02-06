---
name: agent-configuration-78bcf6
description: Use this skill when the user needs help with agent configuration. It
  provides practical guidance, execution steps, and quality checks for agent configuration
  tasks.
keywords:
- agent
- tools
- name
- model
- scope
suggested_keywords:
- agent
- tools
- name
- model
- scope
---

# Agent Configuration

## When to use
- Creating or editing agent definitions for Kode/Claude-compatible runtimes

## Workflow
1. Author agent Markdown with explicit frontmatter:
   - `agent` (identifier), `name`, `description`, `tools` (list or `*`), `model_name` (preferred over deprecated `model`).
2. Place configs by priority (low→high): built-in < .claude user < .kode user < .claude project < .kode project.
3. Hot-reload or `/agents` to apply changes; ensure fs.watch invalidation works.
4. Limit tools per agent for safety; set model_name per agent when needed.

## Anti-patterns
- Using deprecated `model` field
- Omitting tool restrictions when security matters
- Forgetting scope/priority when overlapping names

## Output
- Agent definition summary (path, tools, model_name, scope) and reload confirmation
