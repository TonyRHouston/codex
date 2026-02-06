---
name: tpilotx-cli-89a761
description: Use this skill when the user needs help with tpilotx cli. It provides
  practical guidance, execution steps, and quality checks for tpilotx cli tasks.
keywords:
- cli
- project
- tpilotx
- config
- orchestrator
suggested_keywords:
- cli
- project
- tpilotx
- config
- orchestrator
---

# TpilotX CLI

## When to use
- You need to start a full Pythagora/TpilotX session from the command line, either for new builds or to resume saved projects
- Operators must list, inspect, or delete stored projects/branches before re-running the orchestrator
- You are packaging the CLI for desktop extensions or remote IPC clients and must configure logging, telemetry, and API endpoints correctly

## Workflow
1. Parse command arguments (`helpers.parse_arguments`) so flags like `--project`, `--list`, `--llm-endpoint`, or `--no-auto-confirm-breakdown` are available. The parser also exposes feature toggles for IPC (`--enable-api-server`), custom config paths, and explicit stack prompts.
2. Load configuration via `helpers.load_config`, allowing `.env` fallbacks. Apply CLI overrides for log level, DB URL, IPC host/port, and provider base URLs/keys. Validate with `Config.model_validate`; bail out early if parsing fails.
3. Initialize logging and choose the UI adapter: IPC client, scripted `VirtualUI`, or default `PlainConsoleUI`. Run `run_migrations` against the configured database and create a `SessionManager` bound to the parsed args.
4. Call `async_main` (through `run_tpilotx`) to dispatch control flow: quick-return for listing (`--list`, `--list-json`), config display, legacy imports, or project deletes. Otherwise instantiate `StateManager`, optional `IPCServer`, apply access tokens, telemetry, and Sentry if enabled.
5. For fresh sessions, `start_new_project` walks the UI question flow (stack selection, prompt capture). For resumptions, `load_project` restores the requested project/branch/step and rehydrates FE/BE logs plus conversations before handing off to the `Orchestrator`.
6. Register signal handlers and `atexit` cleanup to flush telemetry and shut down the UI. On teardown, call `cleanup(ui)`, stop any API server, and ensure the UI closes cleanly before exiting the process.

## Anti-patterns
- Skipping `run_migrations`, which leaves the orchestrator working against stale schemas
- Providing both `--project` and `--branch` without matching IDs, causing confusing "not found" errors instead of checking `--list`
- Forgetting to run with `--no-auto-confirm-breakdown` when testing human-in-the-loop flows, leading to unintended auto approvals
- Ignoring the need to call `capture_exception`/`send_error`; unhandled exceptions bypass UI notifications and telemetry crash reports

## Output
- A running CLI session with the selected UI, database migrations applied, telemetry and optional API server active, and orchestrator control handed over to manage tasks or project resumptions
