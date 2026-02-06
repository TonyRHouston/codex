---
name: mcp-troubleshooting
description: Diagnose MCP discovery, startup, auth, and tool invocation failures across both local and remote MCP servers.
keywords:
- mcp
- troubleshooting
- diagnostics
- discovery
- auth
suggested_keywords:
- mcp not showing
- mcp server failing
- mcp auth error
---

# MCP Troubleshooting

## Router
Use this skill first when the failure location is unclear or spans multiple layers.

### Trigger phrases
- "MCP not showing up"
- "MCP configured but no tools/resources"
- "server starts then exits"
- "MCP works sometimes"
- "help debug MCP end-to-end"

### Use over other MCP skills when
- You cannot tell whether the issue is config, startup, auth, session state, or tool invocation.
- Local and remote servers are both affected.

## When to use
- MCP servers are configured but not appearing.
- Tool/resource discovery is empty or inconsistent.
- Server process exits early, times out, or returns auth errors.

## Scope
- Applies to both `mcp-local` and `mcp-remote`.

## Triage order
1. Config integrity: validate `.codex/config.toml` or `~/.codex/config.toml` parses and contains expected `[mcp_servers.*]`.
2. Registration: run `codex mcp list` and `codex mcp get <server>`.
3. Startup: run a short `timeout` launch for the server command and inspect stderr.
4. Auth/env: verify required env vars exist and are visible to server process.
5. Session state: restart/reconnect Codex session and retest discovery.
6. Tool-level checks: invoke representative tools through `mcp-cli` or native server diagnostics.

## Common fixes
- Correct binary/script path in `command` and `args`.
- Set missing env vars (for example service tokens).
- Increase `startup_timeout_sec` for slower servers.
- Remove stale duplicate server names and restart Codex.

## Output
- Root cause summary, exact failing layer, and concrete fix with verification commands.

## Quick decision matrix
- Local stdio/offline setup request -> `mcp-local`
- Hosted/auth/scope/endpoint request -> `mcp-remote`
- Ambiguous failure/debug request -> `mcp-troubleshooting`
