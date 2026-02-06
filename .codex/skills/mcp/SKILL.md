---
name: mcp
description: Index and router skill for MCP work. Selects the right MCP sub-skill for local setup, remote integration, or troubleshooting.
keywords:
- mcp
- router
- index
- local
- remote
suggested_keywords:
- mcp setup
- mcp debug
- mcp integration
---

# MCP Index

## Purpose
Use this skill as the first stop for any MCP request. Route immediately to one sub-skill.

## Route to
- `mcp-local`: local/offline/stdio server setup and validation.
- `mcp-remote`: hosted/service-backed MCP integration, auth, scopes, and endpoints.
- `mcp-troubleshooting`: ambiguous failures or cross-layer MCP debugging.

## Quick routing rules
- Local machine + stdio + config edits -> `mcp-local`
- Tokens/OAuth/scopes/hosted endpoint -> `mcp-remote`
- "Not working", unknown cause, or mixed symptoms -> `mcp-troubleshooting`

## Trigger phrases
- "set up MCP"
- "configure MCP server"
- "connect MCP to service"
- "MCP not showing up"
- "debug MCP"

## Output
- Deterministic selection of one MCP sub-skill and a focused workflow with minimal overlap.
