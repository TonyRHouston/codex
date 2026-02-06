---
name: mcp-git-a8911a
description: Use this skill when the user needs help with mcp git. It provides practical
  guidance, execution steps, and quality checks for mcp git tasks.
---

# MCP Git Server

## When to use
- Git status, diff, log, branch, or commit via MCP
- Repository automation in MCP clients

## Core workflow
1. Confirm repo_path and access permissions
2. Use git_status and git_diff* to inspect
3. Apply git_add/commit/reset as needed

## Anti-patterns (NEVER)
- Commit without confirming repo_path
- Assume branch context without git_status
- Use destructive operations without validation

## Output expectations
- Repo path and commands used
- Diffs and summaries
- Commit hashes when applicable

## References
- Read references/git.md
