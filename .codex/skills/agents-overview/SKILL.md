---
name: agents-overview-866945
description: Use this skill when the user needs help with agents overview. It provides
  practical guidance, execution steps, and quality checks for agents overview tasks.
keywords:
- agent
- agents
- manifests
- delegation
- describe
suggested_keywords:
- agent
- agents
- manifests
- delegation
- describe
---

# Agents Overview

## When to use
- Inspect agent manifests and decide which agent to delegate a task to
- Understand agent lifecycles, allowed tools, and model preferences

## Workflow
1. Inspect `agents/` and related manifest files for frontmatter keys like `agent`, `model_name`, and `tools`.
2. Validate that each manifest includes `entrypoint` and `timeout` semantics to avoid runaway jobs.
3. Use the cataloged agent list to route tasks and ensure ACLs for tool usage are enforced.

## Output
- A short registry of agents, their capabilities, and recommended delegation rules for orchestrators
