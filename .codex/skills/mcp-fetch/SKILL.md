---
name: mcp-fetch-d6e812
description: Use this skill when the user needs help with mcp fetch. It provides practical
  guidance, execution steps, and quality checks for mcp fetch tasks.
---

# MCP Fetch Server

## When to use
- Retrieve web content as markdown
- Paginate content with start_index

## Core workflow
1. Fetch URL with max_length
2. Use start_index for pagination
3. Use raw when HTML is needed

## Anti-patterns (NEVER)
- Fetch sensitive internal URLs without approval
- Ignore robots.txt when required

## Output expectations
- URL, ranges fetched, and content summary

## References
- Read references/fetch.md
