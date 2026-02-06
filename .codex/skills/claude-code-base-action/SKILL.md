---
name: claude-code-base-action-692ddf
description: Use this skill when the user needs help with claude code base action.
  It provides practical guidance, execution steps, and quality checks for claude code
  base action tasks.
keywords:
- claude
- code
- action
- mcp
- tool
suggested_keywords:
- claude
- code
- action
- mcp
- tool
---

# Claude Code Base Action

## When to use
- You need fine-grained control over Claude Code executions in GitHub Actions (custom prompts, tool ACLs, MCP servers) instead of the opinionated Claude Code app
- Automation jobs should run Claude on a schedule or in bespoke pipelines where you supply the context, secrets, and follow-on steps manually
- Teams mirroring anthropics/claude-code-action/base-action and want a quick reference for required inputs and security controls

## Workflow
1. Decide how the job will be triggered (e.g., scheduled, PR opened, manual dispatch) and add a workflow step that calls `anthropics/claude-code-base-action@beta` after checking out the repo when file context is required.
2. Provide either `prompt` or `prompt_file` to seed the session. Optionally cap runtime with `max_turns`, swap models (`model`, `fallback_model`), or override prompts (`system_prompt`, `append_system_prompt`).
3. Specify tool permissions explicitly via `allowed_tools`/`disallowed_tools`. Include MCP tool names (`mcp__server__tool`) if you load MCP servers with `mcp_config`. Keep the list tight to avoid granting shell access you do not intend.
4. Inject environment and settings as needed: use `claude_env` for runtime variables (version pins, secrets, feature flags) and `settings` (path or JSON) for Claude Code permissions/hooks. Remember the action automatically enables project MCP servers; override only what you must.
5. Authenticate with either `${{ secrets.ANTHROPIC_API_KEY }}` or `${{ secrets.CLAUDE_CODE_OAUTH_TOKEN }}`. Flip `use_bedrock` or `use_vertex` when invoking providers through GitHub OIDC. Enable `use_node_cache` only if you cache Bun/Node deps deliberately.
6. Capture outputs: `execution_file` holds complete JSON conversation logs. Downstream steps (e.g., `actions/github-script`) can parse the file for summaries, comments, or structured data. Guard `show_full_output` because enabling it exposes raw content in logs.

## Anti-patterns
- Leaving `allowed_tools` empty and relying on defaults, which may block necessary commands during automation
- Combining `prompt` and `prompt_file` in the same step (the action expects only one source)
- Enabling `show_full_output` in shared repos without reviewing the security warning; secrets can leak into logs
- Forgetting to reference secrets via `${{ secrets.* }}` or storing provider credentials directly in workflow YAML

## Output
- Executed GitHub Action step that runs Claude Code with the chosen prompt, valid tool and MCP configuration, and an `execution_file` artifact ready for follow-up steps such as posting reviews or parsing structured results
