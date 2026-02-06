---
name: frontend-builder-b89a6f
description: Use this skill when the user needs help with frontend builder. It provides
  practical guidance, execution steps, and quality checks for frontend builder tasks.
keywords:
- frontend
- run
- iteration
- template
- auto
suggested_keywords:
- frontend
- run
- iteration
- template
- auto
---

# Frontend Builder

## When to use
- The frontend epic needs initial scaffolding or follow-up iterations
- User feedback or auto-debugging must be folded into subsequent UI updates
- Swagger projects require replacing mocked endpoints with real API hooks

## Workflow
1. On the first pass, clear UI logs, announce frontend build start, stream the `build_frontend` template, and store the conversation history on the epic; wait for async template tasks to finish before processing code blocks.
2. For continued work, replay the stored convo, request further implementation (or `DONE`), and process each block: replace files or run npm commands (skipping missing scripts) while tracking retry counts and the `fe_iteration_done` flag.
3. When iterations begin, attempt auto-debug (kill dev servers, run `npm run start`, curl the UI, capture logs); surface failures for implementation or ask the user for change/bug descriptions. Gather relevant documentation via RAG when swagger-only and user input warrants it.
4. Apply relace-based edits first; if they fail, fall back to standard `build_frontend`. Mark conversation state, whether relace succeeded, and if manual iteration is in effect. Queue swagger mock removals when API files change and invoke removal flow before continuing.
5. On completion requests, finalize the epic, emit telemetry/UI logs, optionally run git commit, and prepare backend setup (logs, run command). If unfinished, continue iterating with updated messages and auto-debug attempt counters.

## Anti-patterns
- Ignoring unfinished async template tasks before saving files
- Leaving `file_paths_to_remove_mock` uncleared after processing swagger mocks
- Forgetting to guard npm scripts against missing entries or relace errors
- Ending an iteration without updating `fe_iteration_done`, conversation history, or run command

## Output
- Updated frontend files, executed npm commands, new run command/app link, iteration flags (`fe_iteration_done`, `use_relace`), and UI log streams marking progress or completion
