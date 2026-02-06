---
name: claude-code-plugins-671e78
description: Use this skill when the user needs help with claude code plugins. It
  provides practical guidance, execution steps, and quality checks for claude code
  plugins tasks.
keywords:
- claude
- plugin
- code
- plugins
- commands
suggested_keywords:
- claude
- plugin
- code
- plugins
- commands
---

# Claude Code Plugins

## When to use
- You need Claude Code to handle git workflows, feature delivery, or PR reviews with slash commands instead of shell scripts
- A project would benefit from prebuilt hooks or agents (e.g., security reminders, frontend guidance) rather than building a plugin from scratch
- You are curating a Claude Code environment and must document which plugins are active and what operational dependencies they require

## Workflow
1. Install or update Claude Code (`curl -fsSL https://claude.ai/install.sh | bash` on macOS/Linux or the WinGet/PowerShell installer on Windows) and launch it inside the target repository with `claude`.
2. Review the bundled plugin catalog at partially-processed/claude-code/plugins/README.md to choose the module that matches the task (e.g., commit-commands for git automation, pr-review-toolkit for code review, feature-dev for guided delivery).
3. Copy the selected plugin into the project’s `.claude/plugins/` directory or point managed installations at the repo path, then confirm the plugin metadata in `<plugin>/.claude-plugin/plugin.json` lists the expected commands, agents, skills, and hooks.
4. Update `.claude/settings.json` (or managed settings) to permit the new commands/agents, add required environment variables, and declare disallowed tools if needed; for git-centric plugins ensure `gh` is installed and authenticated because `/commit-push-pr` shells out to GitHub CLI.
5. Start Claude Code and run the plugin entry command (`/commit`, `/feature-dev`, `/plugin-dev:create-plugin`, etc.), watching for dependency prompts or follow-up agents; document outcomes and any repo-specific tweaks in your operational notes so future sessions reuse the same configuration.

## Anti-patterns
- Enabling plugins without installing their external dependencies (e.g., missing GitHub CLI for commit automation or omitting project hooks referenced by `feature-dev`)
- Leaving `.claude/settings.json` unchanged so new commands remain blocked by default permissions
- Mixing experimental plugins into production profiles without isolating them in managed or per-repo settings
- Forgetting to review each plugin’s README for extra setup steps (like Agent SDK template repos for `agent-sdk-dev`)

## Output
- Activated plugin directory under `.claude/plugins/`, updated settings entries, validated slash commands or hooks, and a short run log confirming the plugin executed successfully for the target workflow
