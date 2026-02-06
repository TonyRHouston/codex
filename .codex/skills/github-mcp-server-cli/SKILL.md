---
name: github-mcp-server-cli-29b7f0
description: Use this skill when the user needs help with github mcp server cli. It
  provides practical guidance, execution steps, and quality checks for github mcp
  server cli tasks.
keywords:
- github
- server
- mcp
- stdio
- inventory
suggested_keywords:
- github
- server
- mcp
- stdio
- inventory
---

# GitHub MCP Server CLI

## When to use
- You need to spin up the GitHub MCP server over stdio for local tooling or editor integration and must set toolset/feature flags correctly
- Security or IT teams want to audit which GitHub OAuth scopes are required for a chosen toolset before provisioning a PAT
- Documentation owners must refresh README and remote-server tables after tool or toolset changes land in the repository

## Workflow
1. Build or download the `github-mcp-server` binary and expose configuration through env vars prefixed with `GITHUB_` (for example `GITHUB_PERSONAL_ACCESS_TOKEN`, `GITHUB_TOOLSETS`, `GITHUB_FEATURES`). Launch the stdio transport with `github-mcp-server stdio` once the token and optional flags (`--toolsets`, `--tools`, `--features`, `--read-only`, `--dynamic-toolsets`, `--lockdown-mode`, etc.) are set.
2. When composing the flag list, remember Cobra + Viper normalization: hyphenated flags map to underscores for env overrides, and `--repo-access-cache-ttl` accepts Go duration strings (`5m`, `0s`). Leave `--toolsets` unset to accept the default bundle, or provide a comma separated list to constrain inventory.
3. To preview OAuth scope requirements without starting the server, run `github-mcp-server list-scopes` with the same flags you plan for production. Choose `--output=text` for human summaries, `--output=json` for programmatic pipelines, or `--output=summary` to emit unique scopes only.
4. Regenerate documentation after inventory updates with `github-mcp-server generate-docs`. The command rewrites README toolset/tool tables, docs/remote-server tables (including remote-only listings), and docs/tool-renaming alias tables by harvesting metadata from `pkg/github` inventory helpers.
5. Use `github-mcp-server --help` or `--version` when distributing the binary to verify the build metadata (ldflags set commit/date) and surface the shared persistent flag list to downstream operators.

## Anti-patterns
- Forgetting to set `GITHUB_PERSONAL_ACCESS_TOKEN`; the stdio command exits immediately with "GITHUB_PERSONAL_ACCESS_TOKEN not set"
- Supplying both `--toolsets=all` and specific `--tools` unintentionally; inventory narrowing may hide required tools for your workflow
- Running `generate-docs` in a dirty tree without committing upstream edits—tables will be rewritten and can conflict with manual changes
- Treating the list-scopes JSON output as authoritative without matching the flag configuration you intend to deploy

## Output
- Running stdio server session with the requested toolsets/features, scoped PAT, command logging, and cache TTL in effect; scope audit reports in text/JSON; regenerated documentation files updated to reflect the latest inventory metadata
