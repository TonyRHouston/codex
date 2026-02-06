---
name: mcp-everything-639ad4
description: 'Operate the Everything MCP server for testing MCP capabilities (tools,
  prompts, resources). Use when validating client integrations.

  Keywords: mcp,everything,test,capabilities'
---

# MCP Everything Server

## When to use
- Testing MCP client capabilities
- Validating prompts/resources/annotations support

## Core workflow
1. Call tools like echo/add/annotatedMessage
2. Validate resources and prompts behavior
3. Use listRoots to inspect roots support

## Anti-patterns (NEVER)
- Treat as production server
- Skip logging/cleanup validation

## Output expectations
- Tools exercised and results
- Any client compatibility gaps

## References
- Read references/everything.md
- Read references/oauth-auth.md
