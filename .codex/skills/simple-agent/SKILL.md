---
name: simple-agent-bf4266
description: Use this skill when the user needs help with simple agent. It provides
  practical guidance, execution steps, and quality checks for simple agent tasks.
keywords:
- entrypoint
- agent
- file
- code
- disk
suggested_keywords:
- entrypoint
- agent
- file
- code
- disk
---

# Simple Agent Workflow

## When to use
- You want GPT Engineer to generate an initial codebase and entrypoint using the classic preprompt set
- An existing project needs iterative `improve` cycles without the full orchestrator stack
- You are packaging a lightweight agent that relies on disk storage for logs, prompts, and execution artifacts

## Workflow
1. Construct the agent with `SimpleAgent.with_default_config(path, ai=None, preprompts_holder=None)`. This wires `DiskMemory` at `memory_path(path)` and a `DiskExecutionEnv`, plus the standard `PrepromptsHolder(PREPROMPTS_PATH)`. Pass a custom `AI` instance if you need alternative models or telemetry.
2. Call `agent.init(prompt)` with a `Prompt` carrying `.text` and optional entrypoint prompt overrides. The agent first runs `gen_code` to produce source files, logging conversation history to `CODE_GEN_LOG_FILE`, then `gen_entrypoint` to build `ENTRYPOINT_FILE` bash script metadata and merges both into a `FilesDict`.
3. If you need execution, upload the returned `FilesDict` into the `DiskExecutionEnv` and run `execute_entrypoint`, which prompts for confirmation before invoking `bash ENTRYPOINT_FILE` in the working directory while streaming stdout/stderr.
4. For refinements, invoke `agent.improve(files_dict, prompt)` (or `improve_fn` directly) with the current files. The routine builds a chat with `setup_sys_prompt_existing_code`, parses diff blocks via `parse_diffs`, salvages valid hunks, and iterates up to `MAX_EDIT_REFINEMENT_STEPS` when validation fails. Logs land in `DEBUG_LOG_FILE`, `DIFF_LOG_FILE`, and `IMPROVE_LOG_FILE` under disk memory.
5. Persist or inspect artifacts by reading from `DiskMemory`: it keeps base64-encoded images, text sources, and timestamped log appendices. Call `archive_logs()` between sessions to rotate `logs/` into a timestamped archive.

## Anti-patterns
- Reusing the same temp directory across runs without clearing logs; stale `ENTRYPOINT_FILE` contents may leak into new sessions
- Skipping the confirmation prompt before executing entrypoints and blindly running generated scripts on CI environments
- Ignoring validation errors returned from `_improve_loop`; diffs that cannot be applied will be dropped, so retry counts and messages should be checked
- Constructing `SimpleAgent` without a proper `PrepromptsHolder`, leading to missing keys such as `generate` or `improve`

## Output
- Generated code/entrypoint files in a `FilesDict`, interactive execution capability via the disk execution environment, and disk-backed memory/logs capturing each conversation and diff iteration ready for later analysis
