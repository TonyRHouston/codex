---
name: disk-execution-env-76d7d8
description: Use this skill when the user needs help with disk execution env. It provides
  practical guidance, execution steps, and quality checks for disk execution env tasks.
keywords:
- stdout
- working
- stderr
- disk
- commands
suggested_keywords:
- stdout
- working
- stderr
- disk
- commands
---

# Disk Execution Environment

## When to use
- GPT Engineer or supporting tools must run generated entrypoints or tests inside an isolated working directory
- You want a reusable helper for pushing/pulling `FilesDict` data before executing shell commands
- Interactive sessions need live stdout/stderr streaming with timeout handling and graceful interruption

## Workflow
1. Construct `DiskExecutionEnv(path=None)`. When `path` is omitted it creates a temporary working dir via `FileStore`; providing a path reuses an existing tree.
2. Call `.upload(files_dict)` to push the current `FilesDict` snapshot into the working directory. Subsequent pulls via `.download()` return the on-disk state so you can persist command-side edits.
3. Use `.popen(command)` when you need a raw `subprocess.Popen` handle (for long-running commands you manage manually). stdout/stderr are pipe-attached for downstream reading.
4. For managed runs, use `.run(command, timeout=None)`. The helper prints `--- Start of run ---`, echoes the command, then streams stdout/stderr line-by-line until completion. Set `timeout` in seconds to auto-abort long tasks; a `TimeoutError` is raised and the process is killed.
5. If the user hits Ctrl+C, the loop catches `KeyboardInterrupt`, kills the subprocess, prints a stop message, and exits cleanly without crashing the caller.

## Anti-patterns
- Uploading large `FilesDict` blobs repeatedly instead of reusing the working tree; use `.download()` and mutate files in place when possible
- Forgetting to set `text=True` on custom `popen` usage when expecting string output (the convenience `.run` already sets it)
- Ignoring return code from `.run`; the helper returns `(stdout, stderr, returncode)` so callers should inspect `returncode` before assuming success
- Running interactive shell commands that require stdin; this environment does not forward user input beyond Ctrl+C

## Output
- A working directory populated from the latest `FilesDict`, streaming command logs to stdout, and collected `(stdout, stderr, returncode)` tuples for subsequent decision-making
