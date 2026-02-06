---
name: code-linting-4079e5
description: Use this skill when the user needs help with code linting. It provides
  practical guidance, execution steps, and quality checks for code linting tasks.
keywords:
- linting
- files
- partially
- processed
- core
suggested_keywords:
- linting
- files
- partially
- processed
- core
---

# Linting Pipeline

## When to use
- You want every generated Python asset formatted with Black before execution or diffing
- A project needs a pluggable lint registry that can grow beyond Python without rewriting call sites
- Automated runs must degrade gracefully when Black is unavailable or when code is already compliant

## Workflow
1. Instantiate `Linting()` to seed the extension map that points `.py` files at `lint_python`; additional linters can be attached to `self.linters` for other suffixes [partially-processed/core/linting.py#L33-L63](partially-processed/core/linting.py#L33-L63).
2. Call `lint_files(files_dict, config)` with a `FilesDict` bundle; the method walks each filename, normalizes the extension, and dispatches to the registered handler while preserving untouched files [partially-processed/core/linting.py#L117-L178](partially-processed/core/linting.py#L117-L178).
3. Inside the Python handler, rely on `black.format_str` to format content using any `config` overrides (like `line_length`); NothingChanged and generic exceptions fall back to the original text with informative prints [partially-processed/core/linting.py#L66-L115](partially-processed/core/linting.py#L66-L115).
4. Inspect stdout to see which files changed—`lint_files` emits per-file status so CI logs reveal formatter activity without extra hooks [partially-processed/core/linting.py#L162-L178](partially-processed/core/linting.py#L162-L178).

## Anti-patterns
- Passing `None` configs expecting defaults from Black; supply `{}` explicitly when you plan to mutate it later
- Registering async or long-running linters without adjusting the loop; `lint_files` is synchronous and will block execution
- Feeding binary or non-UTF content through Black; ensure upstream steps keep `FilesDict` text-only
- Wrapping `lint_python` in additional try/except that hides formatter failures; the handler already swallows recoverable errors

## Output
- A sanitized `FilesDict` with Python files auto-formatted, non-target files untouched, and console feedback documenting each lint decision
