---
name: mcp-click-da20fa
description: 'Operate the Click MCP server for Click-based CLI automation. Use when
  exposing click CLIs as MCP tools.

  Keywords: mcp,click,cli,automation'
---

# MCP Click Server

## When to use
- Wrapping Click CLIs for MCP automation
- Designing tool schemas for CLI workflows

## Core workflow
1. Identify Click command structure
2. Map CLI options to MCP tool inputs
3. Validate outputs and errors

## Anti-patterns (NEVER)
- Expose destructive commands without safeguards
- Skip input validation for CLI arguments

## Output expectations
- CLI command mapping and usage
- Error handling and validation rules

## References
- Read references/click.md
