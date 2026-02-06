---
name: skills-mcp-time-skill-88ea48
description: 'Operate the Time MCP server for current time and timezone conversions.
  Use when handling timezone logic or time conversions.

  Keywords: mcp,time,timezone,conversion

  '
source: skills/mcp-time/SKILL.md
---

# MCP Time Server

## When to use
- Current time in specific timezone
- Convert between timezones

## Core workflow
1. Use IANA timezone names
2. Call get_current_time or convert_time

## Anti-patterns (NEVER)
- Use invalid timezone identifiers
- Assume system timezone without checking

## Output expectations
- Time results and timezone context

## References
- Read references/time.md
