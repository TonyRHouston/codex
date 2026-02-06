---
name: files-dict-manager-638444
description: Use this skill when the user needs help with files dict manager. It provides
  practical guidance, execution steps, and quality checks for files dict manager tasks.
keywords:
- dict
- files
- partially
- processed
- core
suggested_keywords:
- dict
- files
- partially
- processed
- core
---

# FilesDict Handling

## When to use
- You must marshal generated files between agents and disk while guaranteeing filename/content typing
- A reviewer needs numbered source listings inside a chat transcript without running external formatters
- Logs should capture the raw body of each file in a deterministic, append-only layout

## Workflow
1. Populate `FilesDict` just like a dict, but rely on its overridden `__setitem__` to reject non-string filenames and payloads; pass `Path` objects when you want OS-safe conversions handled automatically [partially-processed/core/files_dict.py#L29-L53](partially-processed/core/files_dict.py#L29-L53).
2. Call `to_chat()` to generate a triple-backticked listing that iterates line numbers via `file_to_lines_dict`, ideal for system prompts or post-run summaries [partially-processed/core/files_dict.py#L55-L73](partially-processed/core/files_dict.py#L55-L73).
3. Use `to_log()` when you need verbatim dumps in artifacts—each file is prefixed with its name and followed by raw contents, enabling quick diffing later [partially-processed/core/files_dict.py#L74-L89](partially-processed/core/files_dict.py#L74-L89).
4. When constructing the numbered views yourself, reuse `file_to_lines_dict` to split content into an `OrderedDict`, keeping stable ordering even if filenames repeat [partially-processed/core/files_dict.py#L92-L115](partially-processed/core/files_dict.py#L92-L115).

## Anti-patterns
- Stuffing binary blobs into `FilesDict`; the type guard expects UTF-8 strings and will raise otherwise
- Feeding already formatted chat strings back into `to_chat()`—the helper double-wraps them and breaks downstream parsing
- Mutating the dict with `update()` on foreign mappings containing non-string values, which bypasses the type check
- Enumerating with `sorted()` before logging; you lose deliberate ordering that `OrderedDict` preserves for review

## Output
- Strongly typed file bundles ready for agent prompts, log uploads, or diff application, with consistent numbering and formatting helpers
