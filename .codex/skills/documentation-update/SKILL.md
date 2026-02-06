---
name: documentation-update-24d570
description: Use this skill when the user needs help with documentation update. It
  provides practical guidance, execution steps, and quality checks for documentation
  update tasks.
keywords:
- documentation
- instructions
- README
- sync
- technical-debt
---

# Documentation Update Workflow

## 1. Trigger Identification
Documentation must be updated when:
- Internal logic changes (e.g., a new state variable is added).
- External APIs or dependencies are modified.
- User feedback indicates ambiguity in existing guides.

## 2. Sync Procedure
1. **Locate**: Identify all files referencing the changed feature (use `grep` / search).
2. **Review**: Compare current code behavior against documented behavior.
3. **Edit**: Standardize terminology and update code snippets to match the literal implementation.

## 3. Verification
- Follow the updated instructions from a "clean slate" to ensure no missed steps.
- Verify linked `README.md` or `.prompt.md` files still flow logically.

## Anti-Patterns
- Updating code logic but delaying the documentation update.
- Using vague language (e.g., "the settings file") instead of absolute paths.
