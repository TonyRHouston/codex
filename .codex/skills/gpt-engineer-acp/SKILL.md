---
name: gpt-engineer-acp-e1d639
description: Use this skill when the user needs help with gpt engineer acp. It provides
  practical guidance, execution steps, and quality checks for gpt engineer acp tasks.
keywords:
- acp
- gpt
- engineer
- mcp
- server
suggested_keywords:
- acp
- gpt
- engineer
- mcp
- server
---

# GPT Engineer ACP

## When to use
- Integrating gpt-engineer with ACP-compatible clients (GitHub Copilot, Zed/Toad, custom IDEs)
- Registering gpt-engineer as an MCP server for other agents
- Running the multi-stage validation pipeline before shipping generated code
- Exercising example clients or smoke-testing ACP endpoints

## Workflow
1. **Install & configure**: use Poetry within the repo (`poetry install`) and export provider keys (e.g., `OPENAI_API_KEY`). Optional env overrides include `GPT_ENGINEER_MODEL`, `GPT_ENGINEER_TEMPERATURE`, and `GPT_ENGINEER_DEBUG`.
2. **Start the ACP server**: run `gpte-acp --model <model> --project-path <dir>` (or `python -m gpt_engineer.acp.server --stdio`). The server manages sessions, JSON-RPC messaging, tool execution, and multimodal prompts.
3. **Exercise endpoints**: pipe JSON-RPC payloads (initialize, session/create, prompt/send, tools/execute) directly into `gpte-acp` or use the example scripts in `acp (2)`:
   - `basic_client.py` for a minimal text workflow
   - `multimodal_client.py` to send base64-encoded images alongside text
   - `streaming_client.py` to observe progress and file creation events
   - `test_acp.sh` for a shell-based regression script
4. **Generate MCP configuration**: import `create_mcp_config` from `gpt_engineer.acp.mcp_tools`, passing a target directory to emit `mcp-config.json` (or copy `acp/mcp-config.json`). Register the generated block under `mcpServers` so other agents can call `gpte-acp` via MCP.
5. **Integrate with Copilot**: copy `acp/copilot-config.json` into `.copilot/config.json`, then launch Copilot with `--acp --stdio` to bridge commands through the ACP server.
6. **Run validation pipeline**: invoke `gpte-validate` (or `python -m gpt_engineer.acp.validation <paths>`) to execute syntax checks, ruff linting, mypy type checks, and pytest tests. Review the summarized results before finalizing changes.
7. **Automate/testing**: incorporate the ACP tooling into pre-commit by copying the provided config (`.pre-commit-config-acp.yaml`) and running `pre-commit install`.

## Anti-patterns
- Launching the ACP server without setting `OPENAI_API_KEY`, leading to silent provider failures
- Forgetting to destroy sessions, leaving clients blocked on stale IDs
- Skipping the validation step after generation, allowing regressions to ship
- Copying configs without updating paths, causing MCP clients to point at invalid binaries

## Output
- Running ACP server ready for clients, generated MCP/copilot configs, executed example clients for smoke tests, and validation reports confirming code quality
