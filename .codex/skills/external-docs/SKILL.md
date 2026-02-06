---
name: external-docs-482eb9
description: Use this skill when the user needs help with external docs. It provides
  practical guidance, execution steps, and quality checks for external docs tasks.
keywords:
- docs
- docsets
- external
- documentation
- task
suggested_keywords:
- docs
- docsets
- external
- documentation
- task
---

# External Docs

## When to use
- A task could benefit from framework/library references beyond local files
- The current task has no stored docs in project state `docs`
- Example projects are not in play (they already encode documentation choices)

## Workflow
1. Skip doc collection when the spec references an example project; otherwise list docsets via `GET {EXTERNAL_DOCUMENTATION_API}/docsets` with the retried `httpx` client.
2. Ask the LLM (streaming) to run the `select_docset` template with available docsets and the current task, parsing the JSON reply with `SelectedDocsets`.
3. For each chosen docset, call the `create_docs_queries` template to gather targeted search phrases, again parsing with `DocQueries`.
4. Issue parallel `GET {EXTERNAL_DOCUMENTATION_API}/query` requests (AsyncClient) supplying docset keys and query lists; keep up to three snippets per query.
5. Store results on `next_state.docs` as dictionaries containing docset key, description, and snippet payload so downstream agents can cite them; also persist the full list of available docsets for transparency.

## Anti-patterns
- Attempting to fetch docsets when the API is unavailable without handling exceptions
- Writing documentation multiple times for the same task when `docs` already exists
- Dropping docset descriptions, leaving snippets without context for later agents

## Output
- Updated `next_state.docs` populated with docset metadata and snippets, ready for developer or writer agents to reference
