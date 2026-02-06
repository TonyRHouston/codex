---
name: mcp-local
description: Configure, run, and troubleshoot local MCP servers (stdio) for offline and workstation-hosted workflows.
keywords:
- mcp
- local
- stdio
- offline
- codex
suggested_keywords:
- mcp local
- stdio server
- offline mcp
---

# MCP Local

## Router
Use this skill first when the user asks for local MCP setup or fixes.

### Trigger phrases
- "set up MCP locally"
- "offline MCP"
- "stdio MCP server"
- "make this MCP server work on this machine"
- "configure `.codex/config.toml` for MCP"

### Do not use when
- Primary issue is remote auth/scopes/OAuth/hosted endpoint behavior.
- User is troubleshooting unknown failures across both local and remote servers (use `mcp-troubleshooting`).

## When to use
- User wants MCP to work on the current machine with local binaries/scripts.
- Task is about stdio-based MCP setup in `.codex/config.toml` or `~/.codex/config.toml`.
- User needs offline/local-first server operation and validation.

## Covers
- `thinkpdf-offline-mcp`
- `mcp-builder`
- `mcp-cli`
- `mcp-click`
- `mcp-datagen`
- `mcp-everything`
- `mcp-filesystem`
- `mcp-memory`
- `mcp-sequentialthinking`
- `mcp-time`

## Workflow
1. Discover local server command/path and required env vars.
2. Add or update `[mcp_servers.<name>]` blocks in Codex config with `command`, `args`, and timeouts.
3. Verify server process starts without immediate failure.
4. Confirm Codex registration with `codex mcp list` and `codex mcp get <name>`.
5. Validate tool calls via `mcp-cli` or Codex tool discovery after session restart.

## Quick checks
- `codex mcp list`
- `codex mcp get <server>`
- `timeout 2s <server command...>`
- `mcp-cli`

## Output
- Working local MCP server entries in Codex config and a validated startup path for each server.
