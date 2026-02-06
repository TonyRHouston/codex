---
name: thinkpdf-offline-mcp
description: Create a Codex-ready offline MCP server configuration for ThinkPDF and run it locally over stdio without network dependencies.
keywords:
- thinkpdf
- mcp
- offline
- codex
- stdio
suggested_keywords:
- thinkpdf
- mcp
- offline
- codex
- stdio
---

# ThinkPDF Offline MCP

## When to use
- You want Codex to use ThinkPDF tools locally without depending on remote MCP services.
- You need a concrete `[mcp_servers.<name>]` block for `~/.codex/config.toml`.
- You want a stable launcher that starts ThinkPDF MCP over stdio from this workspace.

## Workflow
1. Generate a Codex MCP config block:
   - `python3 scripts/emit_codex_mcp_config.py`
   - Optional custom server name: `python3 scripts/emit_codex_mcp_config.py --name thinkpdf_offline`
2. Paste the emitted TOML block into `~/.codex/config.toml` (or `.codex/config.toml` for workspace-local config).
3. Restart Codex so it reconnects MCP servers.
4. Validate by checking MCP tools from the configured server:
   - `read_pdf`
   - `convert_pdf`
   - `get_document_info`

## Notes
- The launcher script resolves the local `thinkpdf/` directory in this repo and starts `thinkpdf.mcp_server` over stdio.
- This setup is offline in architecture: it runs fully local process-to-process and does not require a hosted MCP endpoint.
- If your environment is missing PDF dependencies, install them for your Python environment before use.

## Output
- A copy/paste-ready Codex MCP TOML block and a local stdio launcher path that Codex can dispatch to later.
