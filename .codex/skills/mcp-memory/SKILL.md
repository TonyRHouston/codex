---
name: mcp-memory-256f36
description: Use this skill when the user needs help with mcp memory. It provides
  practical guidance, execution steps, and quality checks for mcp memory tasks.
---

# MCP Memory Server

## When to use
- Persisting user knowledge across sessions
- Managing entities, relations, and observations
- Configuring Google Drive storage backend

## Core workflow
1. Choose storage backend (filesystem or googledrive)
2. Create/update entities and relations
3. Add/remove observations with atomic facts
4. Search/open nodes for retrieval

## Anti-patterns (NEVER)
- Store secrets in observations
- Use googledrive without secure credentials handling
- Create non-atomic observations

## Output expectations
- Storage config used
- Graph updates performed
- Retrieval results

## References
- Read references/memory.md
- Read references/google-drive-setup.md
- Read references/security-google-drive.md
