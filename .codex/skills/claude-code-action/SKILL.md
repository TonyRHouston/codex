---
name: claude-code-action-217885
description: Use this skill when the user needs help with claude code action. It provides
  practical guidance, execution steps, and quality checks for claude code action tasks.
keywords:
- claude
- github
- code
- app
- action
suggested_keywords:
- claude
- github
- code
- app
- action
---

# Claude Code Action

## When to use
- You need Claude to react to `@claude` mentions, issue assignments, or labels inside GitHub without manual intervention
- A repository wants structured automation (reviews, doc sync, flaky-test triage) using Claude Code on self-hosted GitHub runners
- Security or compliance teams require clarity on authentication, permissions, and provider setup before enabling the action

## Workflow
1. Install Claude Code locally with `claude` and run `/install-github-app` for the quickest setup, or follow docs/setup.md to install the official GitHub App manually. For organizations that cannot install third-party apps, generate a custom app from github-app-manifest.json and capture its `APP_ID` and private key.
2. Add authentication secrets under Settings → Secrets → Actions: either `ANTHROPIC_API_KEY` for direct API usage or `CLAUDE_CODE_OAUTH_TOKEN` from `claude setup-token`. If you created a custom GitHub App, also add `APP_ID` and `APP_PRIVATE_KEY`, and plan to mint a runtime token with actions/create-github-app-token.
3. Copy examples/claude.yml (or a tailored workflow) into `.github/workflows/`. Enable the events you expect (issue comments, PR reviews, issue assignment/label) so the action can detect tag, automation, or assignment modes automatically.
4. In the workflow step, reference the action `anthropics/claude-code-action@v1` and wire secrets through inputs. Use `prompt` for automation tasks, and pass advanced switches through `claude_args` (e.g., `--model`, `--max-turns`, `--json-schema`, plugin installs). Plug in cloud flags `use_bedrock` or `use_vertex` when routing through AWS or Google, and point to `.claude/settings.json` if you need custom tool or environment policy.
5. Optional hardening: configure `additional_permissions`, commit signing (either `use_commit_signing` or `ssh_signing_key` plus bot identity), and restrict actors via `allowed_bots` or `allowed_non_write_users`. Enable plugin marketplace entries or explicit plugins (e.g., `code-review@claude-code-plugins`) when the workflow must load curated skills before running.
6. Test by commenting `@claude` on a PR or triggering the automation job. Watch the run for dependency prompts (GitHub CLI, Bun, Claude binary). Document any repository-specific prompts or claude_args so future maintainers can extend the workflow without re-discovery.

## Anti-patterns
- Committing API keys or private keys directly into the workflow instead of referencing `${{ secrets.* }}`
- Leaving deprecated inputs (`mode`, `direct_prompt`, `allowed_tools`, etc.) in migrated workflows, which causes ignored configuration or failure
- Installing plugins via the `plugins` input without granting matching permissions or ensuring GitHub CLI access for commands like `/commit-push-pr`
- Allowing non-writers or bots without reviewing the elevated risk outlined in docs/security.md

## Output
- Verified `.github/workflows/claude.yml` (or equivalent) that references anthropics/claude-code-action@v1, configured secrets, optional custom app token creation, and a run log that shows Claude reacting correctly to repository triggers
