---
name: git-d65bc5
description: Use this skill when the user needs help with git. It provides practical
  guidance, execution steps, and quality checks for git tasks.
keywords:
- internal
- git
- tools
source: partially-processed/agents/git.py
---

Helper wrappers for Git operations used by agents. Not a user-facing skill; exposes safe git operations for agent tooling.

When to use
- When an agent needs to inspect or operate on the repository via Git helpers.

Workflow
1. Provide abstractions for git status, diffs, and apply patches.

Dependencies
- `git` CLI and repository access.

Output
- Structured results for git operations.

## When to use
- Use when the user request maps directly to this skill's domain or prompt objective.
- Use to standardize outputs when consistency matters more than creativity.

## Workflow
1. Confirm user intent and expected output format.
2. Apply this skill's core instructions to generate the first pass.
3. Validate output against constraints and revise for correctness.
4. Return concise output with any assumptions explicitly stated.

## Anti-patterns (NEVER)
- Never use this skill when the request clearly belongs to a different domain skill.
- Never return unchecked placeholder text as final output.
- Never skip validation when the output drives edits, commands, or decisions.
