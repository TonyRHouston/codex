---
name: skills-mcp-filesystem-skill-6dc8db
description: Use this skill when the user needs help with skills mcp filesystem skill.
  It provides practical guidance, execution steps, and quality checks for skills mcp
  filesystem skill tasks.
source: skills/mcp-filesystem/SKILL.md
---

# MCP Filesystem Server

## When to use
- File read/write operations with MCP filesystem
- Troubleshooting allowed directories or roots updates

## Core workflow
1. Identify allowed roots or CLI args
2. Use list_allowed_directories before operations
3. Perform read/write/edit/search with explicit paths

## Anti-patterns (NEVER)
- Run without any allowed directories
- Assume roots are set when client lacks support
- Edit without dry-run when using edit_file

## Output expectations
- Allowed directories list
- File operations executed
- Any access control errors

## References
- Read references/filesystem.md
