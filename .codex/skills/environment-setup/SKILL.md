---
name: environment-setup-d662c2
description: Use this skill when the user needs help with environment setup. It provides
  practical guidance, execution steps, and quality checks for environment setup tasks.
keywords:
- init
- bootstrap
- environment
- config
- dependencies
---

# Environment Setup Workflow

## Phase 1: Dependency Audit
- Check required runtimes (Node, Python, Go) and versions.
- Verify presence of package managers (`npm`, `poetry`, `pip`).

## Phase 2: Configuration 
- **Secret Management**: Create `.env.template` if missing; verify required keys.
- **Toolchain**: Initialize linting/testing configs if not present.

## Phase 3: Validation
1. Install base dependencies.
2. Execute a "smoke test" (e.g., `npm run build` or `python check_deps.py`).
3. Confirm working directory `cwd` matches expected project root.

## Anti-Patterns
- Installing global packages instead of project-local dev-dependencies.
- Checking `.env` files with secrets into git.
