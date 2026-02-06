---
name: mcp-ftp-3d3e8e
description: 'Operate the FTP MCP server, including gcloud-ftp Google Drive integration.
  Use when listing, uploading, downloading, or troubleshooting FTP MCP operations.

  Keywords: mcp,ftp,gcloud-ftp,google-drive'
---

# MCP FTP Server

## When to use
- File operations via FTP MCP (list/download/upload/rename)
- Google Drive FTP bridge setup or troubleshooting

## Core workflow
1. Confirm FTP or gcloud-ftp mode
2. Validate credentials and port settings
3. Execute FTP tool calls with explicit paths
4. Verify results and handle errors

## Anti-patterns (NEVER)
- Use gcloud-ftp without credentials configured
- Assume FTP root mappings without validating
- Upload secrets without encryption

## Output expectations
- Tool calls used and paths
- Verification steps and results
- Any failures with root cause hints

## References
- Read references/ftp-server.md
- Read references/gcloud-ftp-bridge.md
