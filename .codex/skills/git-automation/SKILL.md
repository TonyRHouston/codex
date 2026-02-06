---
name: git-automation-d9340b
description: Use this skill when the user needs help with git automation. It provides
  practical guidance, execution steps, and quality checks for git automation tasks.
keywords:
- git
- user
- commit
- availability
- initialize
suggested_keywords:
- git
- user
- commit
- availability
- initialize
---

# Git Automation

## When to use
- Before orchestrator-driven runs that may need version control
- Right before task completion when changes should be committed

## Workflow
1. Check whether Git is installed via `git --version`; cache availability on the state manager.
2. Inspect the workspace for an existing `.git` folder; if missing, prompt the user to initialize.
   - On approval, run `git init`, write a default .gitignore, stage files, and create an initial commit when changes exist.
3. Before committing work, re-check for staged diffs using `git status --porcelain`. If clean, exit silently.
4. Ask the user if they want to commit; if yes, stage all changes and fetch a diff to seed a commit message via the LLM when none is provided.
5. Confirm or edit the suggested message with the user, then run `git commit -m` to persist. Update `state_manager.git_used` accordingly.

## Anti-patterns
- Running Git commands without verifying availability or initialization
- Writing .gitignore without handling filesystem errors
- Committing without user confirmation or ignoring clean working trees

## Output
- Initialized repository state, optional initial commit, and subsequent commits with user-verified messages
