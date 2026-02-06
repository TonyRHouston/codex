---
name: mcpcurl-7ca7ef
description: Use this skill when the user needs help with mcpcurl. It provides practical
  guidance, execution steps, and quality checks for mcpcurl tasks.
keywords:
- tool
- mcpcurl
- server
- json
- stdio
suggested_keywords:
- tool
- mcpcurl
- server
- json
- stdio
---

# mcpcurl CLI

## When to use
- You want to exercise an MCP server from the shell without wiring a full IDE integration
- QA needs to verify tool schemas or try specific tool invocations end-to-end using the same stdio transport Claude uses
- You are debugging tool arguments, enum validation, or JSON payload shapes before updating formal clients

## Workflow
1. Build or install the `mcpcurl` binary. Every command requires `--stdio-server-cmd`, a shell string that launches your MCP server in stdio mode (for example `"github-mcp-server stdio"` or `"bun run server.ts"`). Flags are parsed with Cobra so wrap multi-word commands in quotes.
2. Inspect available tools with `mcpcurl schema --stdio-server-cmd="..."`. The command sends a JSON-RPC `tools/list` request and prints the raw response so you can confirm tool names, descriptions, and parameter schemas.
3. Invoke a tool via dynamically generated subcommands under `mcpcurl tools <tool-name>`. mcpcurl binds flags based on the schema: strings, enums (validated in `PreRunE`), numeric ranges, booleans (only sent when explicitly set), and arrays (either `--flag value --flag value` or `--flag-json` for object arrays). Required properties are marked via `MarkFlagRequired`.
4. Provide arguments on the CLI or through environment variables named after the tool (`<TOOL>_<FLAG>=value`, with hyphens converted to underscores). mcpcurl merges flag and env sources before building the JSON-RPC payload.
5. Review responses using pretty printing (default `--pretty=true`). The CLI pretty prints JSON/JSONL outputs; disable with `--pretty=false` to see raw payloads. Errors from the MCP server bubble to stderr with full text content.

## Anti-patterns
- Omitting quotes around `--stdio-server-cmd` when it contains spaces, causing Cobra to interpret shell fragments as separate arguments
- Forgetting to set optional array/object flags using the `--flag-json` variant, leading to JSON unmarshal errors before the request is sent
- Assuming schema is cached permanently; mcpcurl fetches tools at startup only, so restart the process if the server’s schema changes mid-session
- Ignoring enum validation failures; mcpcurl guards client-side but the server will still reject invalid strings if bypassed

## Output
- JSON-RPC request/response cycles against the target MCP server, schema dumps for inspection, and human-friendly tool execution output suitable for reproducing bugs or validating new tools
