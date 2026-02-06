---
name: diff-validator-20835c
description: Use this skill when the user needs help with diff validator. It provides
  practical guidance, execution steps, and quality checks for diff validator tasks.
keywords:
- diff
- partially
- processed
- core
- hunks
suggested_keywords:
- diff
- partially
- processed
- core
- hunks
---

# Diff Validation Workflow

## When to use
- A downstream tool produced patch hunks that may be misaligned or contain hallucinated context
- You need to sanitize diffs before `FilesDict.apply()` or VCS patching to avoid corrupting the working tree
- An LLM returned review comments as additions and you must reclassify them without rerunning generation

## Workflow
1. Build `Hunk` instances with explicit `(label, line)` tuples and original offsets; the constructor tallies retain/add/remove counts so later length corrections stay consistent [partially-processed/core/diff.py#L44-L198](partially-processed/core/diff.py#L44-L198).
2. Call `Diff.validate_and_correct(lines_dict)` with a 1-indexed mapping of pristine lines. It walks hunks sequentially, trimming previously verified regions to keep search windows tight [partially-processed/core/diff.py#L312-L378](partially-processed/core/diff.py#L312-L378).
3. Inside each hunk, let `find_start_line` recover a trustworthy anchor if the incoming start offset is wrong; comment-only lines are downgraded to `ADD` so validation can continue [partially-processed/core/diff.py#L133-L199](partially-processed/core/diff.py#L133-L199).
4. Use `validate_lines` to auto-heal gaps: missing original lines are injected via `add_retained_line`, while spurious edits are dropped with `pop_line` based on rolling similarity ratios [partially-processed/core/diff.py#L200-L286](partially-processed/core/diff.py#L200-L286).
5. Fall back to the lightweight similarity helpers when tuning thresholds; both `is_similar` and `count_ratio` ignore whitespace and case, making them robust against formatter drift [partially-processed/core/diff.py#L381-L419](partially-processed/core/diff.py#L381-L419).

## Anti-patterns
- Feeding zero-retain hunks from new files into legacy patches; mark the whole diff as new instead of forcing validation
- Passing raw file strings without converting to ordered, 1-indexed dictionaries; validation logic assumes that structure
- Overriding `forward_block_len` to tiny sizes—similarity scoring collapses and produces false removals
- Ignoring the returned `problems` list; discarded hunks are removed from the diff silently otherwise

## Output
- Cleaned diff hunks ready for patch application, with corrected offsets, balanced retain/add/remove counts, and a diagnostics trail identifying any hunks that were unsalvageable
