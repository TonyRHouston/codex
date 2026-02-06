---
name: build-triage-master-1f9ebd
description: Use this skill when the user needs help with build triage master. It
  provides practical guidance, execution steps, and quality checks for build triage
  master tasks.
keywords:
- build-failure
- ci-cd
- triage
- compiler-error
- logs
---

# Build Triage Workflow

## 1. Evidence Collection
- **Log Isolation**: Extract the specific error block from the build output.
- **Context Search**: Identify if the failure is in source code, configuration (tsconfig/package.json), or environment.

## 2. Categorization
- **Syntax/Type Error**: Immediate fix required in source.
- **Dependency Drift**: Check `node_modules` or lockfile consistency.
- **Environmental**: Check pathing, environment variables, or toolchain versions.

## 3. Resolution Path
1. **Minimal Reproduction**: Attempt to trigger the error with a targeted command.
2. **Delta Analysis**: Review recent changes in the `diff` that preceded the failure.
3. **Cache Invalidation**: If the error logic is sound, attempt `clean` builds.

## Anti-Patterns
- Blindly changing code without locating the specific log line of failure.
- Ignoring "Warning" cascades that precede the "Error".
