---
name: token-usage-monitor-df2629
description: Use this skill when the user needs help with token usage monitor. It
  provides practical guidance, execution steps, and quality checks for token usage
  monitor tasks.
keywords:
- token
- usage
- partially
- processed
- core
suggested_keywords:
- token
- usage
- partially
- processed
- core
---

# Token Accounting

## When to use
- You need observability into prompt/completion totals while orchestrating multi-step conversations
- A run mixes text and vision payloads and you must estimate the combined OpenAI usage cost
- CI should emit CSV summaries of token consumption after each agent stage

## Workflow
1. Initialize `TokenUsageLog(model_name)` to seed cumulative counters and a tokenizer tuned to the target model [partially-processed/core/token_usage.py#L195-L207](partially-processed/core/token_usage.py#L195-L207).
2. For each step, call `update_log(messages, answer, step_name)`; it tallies prompt and completion counts via the tokenizer, accumulates totals, and appends a `TokenUsage` snapshot [partially-processed/core/token_usage.py#L208-L239](partially-processed/core/token_usage.py#L208-L239).
3. Behind the scenes, `Tokenizer.num_tokens_from_messages` handles both plain text and base64 image payloads, pricing tiled images per OpenAI's vision rules [partially-processed/core/token_usage.py#L82-L192](partially-processed/core/token_usage.py#L82-L192).
4. Retrieve structured records with `log()` or emit a CSV using `format_log()` when you need artifacts for dashboards [partially-processed/core/token_usage.py#L241-L265](partially-processed/core/token_usage.py#L241-L265).
5. To estimate spend, call `usage_cost()`; it looks up per-model pricing and sums prompt/completion costs when the model string contains `gpt` [partially-processed/core/token_usage.py#L266-L312](partially-processed/core/token_usage.py#L266-L312).

## Anti-patterns
- Passing messages that skip the framing tokens (e.g., raw strings); wrap them in LangChain `AIMessage` or `HumanMessage` so token counting stays accurate
- Feeding non-base64 image URLs; the tokenizer expects inline data to measure resolution tiles
- Mixing multiple models inside one log; instantiate a new `TokenUsageLog` per model to keep pricing correct
- Suppressing cost calculation errors silently; piping stdout to logs keeps pricing anomalies visible

## Output
- Step-by-step token usage records, CSV exports, and optional USD cost projections that inform rate-limited planning
