---
name: project-configurator-7b6bca
description: Use this skill when the user needs help with project configurator. It
  provides practical guidance, execution steps, and quality checks for project configurator
  tasks.
keywords:
- config
- project
- partially
- processed
- core
suggested_keywords:
- config
- project
- partially
- processed
- core
---

# Project Config Management

## When to use
- A workspace needs to bootstrap or mutate `gpt-engineer.toml` without hand-editing TOML
- You want validation around optional `gptengineer-app` settings before syncing to the hosted service
- Automation must surface default build/test/lint commands while only persisting overrides

## Workflow
1. Model paths, run scripts, and optional app metadata with the provided dataclasses; `Config` wires them together with sensible defaults [partially-processed/core/project_config.py#L34-L110](partially-processed/core/project_config.py#L34-L110).
2. Use `Config.from_toml(path)` to read the existing document via `read_config`, returning a fully typed structure ready for inspection or mutation [partially-processed/core/project_config.py#L80-L110](partially-processed/core/project_config.py#L80-L110).
3. When mutating, call `to_dict()` to obtain a serialization-ready payload with `None` values stripped, keeping the TOML writer from emitting empty sections [partially-processed/core/project_config.py#L111-L121](partially-processed/core/project_config.py#L111-L121).
4. Persist updates through `to_toml(config_file, save=True)`; it merges only changed keys back into the on-disk document while preserving unrelated settings [partially-processed/core/project_config.py#L122-L151](partially-processed/core/project_config.py#L122-L151).
5. For fresh projects, seed the file with `example_config` or `default_config_filename` constants, then iterate with the same load/mutate/save cycle [partially-processed/core/project_config.py#L11-L31](partially-processed/core/project_config.py#L11-L31).

## Anti-patterns
- Calling `to_toml` on a non-existent path; always create or copy a template so `read_config` passes its existence assertion
- Bypassing `filter_none` by writing raw dicts—tomlkit will choke on `None` and you will lose sparse sections
- Omitting `project_id` when populating `gptengineer-app`; the constructor asserts its presence and will halt automation
- Treating `openapi` as a plain list of strings; it expects dictionaries that hydrate `_OpenApiConfig`

## Output
- A validated TOML document on disk plus structured config objects you can reuse across CLI invocations or CI jobs
