---
name: mcp-remote
description: Configure and operate remote or service-backed MCP integrations, including auth, scopes, network transport, and hosted endpoints.
keywords:
- mcp
- remote
- auth
- oauth
- github
suggested_keywords:
- remote mcp
- hosted mcp
- mcp auth
---

# MCP Remote

## Router
Use this skill first when the user asks for hosted/service-backed MCP setup or auth.

### Trigger phrases
- "connect MCP to GitHub/service X"
- "MCP OAuth"
- "MCP token/scope issues"
- "hosted MCP endpoint"
- "SSE/HTTP MCP setup"

### Do not use when
- Work is fully local stdio/offline setup on this machine (use `mcp-local`).
- Failure source is unknown and needs cross-layer triage (use `mcp-troubleshooting`).

## When to use
- User needs MCP connected to hosted services/APIs.
- Work includes tokens, OAuth, scopes, remote endpoints, or networked transport.
- User wants GitHub MCP or other external-service MCP connectivity.

## Covers
- `github-mcp-server-cli`
- `mcp-integration`
- `mcp-fetch`
- `mcp-ftp`
- `mcp-git`
- `mcpcurl`

## Workflow
1. Identify transport and endpoint shape (stdio wrapper, SSE, HTTP, or service adapter).
2. Define auth requirements (PAT/OAuth/scopes) and environment variables.
3. Configure Codex MCP server entry and verify config parses.
4. Validate connectivity and scope coverage with service-specific diagnostics.
5. Confirm tools are reachable from Codex and test representative calls.

## Quick checks
- `codex mcp list`
- `codex mcp get <server>`
- `github-mcp-server list-scopes --output=summary`
- Service-specific health/tool listing commands

## Output
- Remote MCP integration that is authenticated, scoped correctly, and validated end-to-end.
