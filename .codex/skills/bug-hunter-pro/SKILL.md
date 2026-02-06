---
name: bug-hunter-pro-9c00cc
description: Use this skill when the user needs help with bug hunter pro. It provides
  practical guidance, execution steps, and quality checks for bug hunter pro tasks.
keywords:
- bug
- user
- test
- status
- reproduction
suggested_keywords:
- bug
- user
- test
- status
- reproduction
---

# Bug Hunter Pro

## When to use
- Active iterations that need bug reproduction and structured debugging
- Cases where logs or user testing are required before fixing
- Sessions that might escalate to pair programming for guidance

## Workflow
1. Ensure reproduction steps exist: if missing, start a background LLM task to generate detailed test steps from current task context and user feedback, then store them.
2. Branch by iteration status:
   - Hunting for bug: build the conversation from iteration history, stream a breakdown, classify whether the problem is identified or more logs are needed, then update bug-hunting cycles and set status to either awaiting fix or awaiting logging.
   - Awaiting user test/reproduction: send test instructions (and run command if present), collect user feedback on fix status, allow pair-programming opt-in, capture additional feedback, bump attempts, and mark iteration status accordingly.
   - Start pair programming: provide an initial explanation and structured log data, then loop on user prompts (questions, tell me more, hints, done). If the user offers a solution hint, draft instructions, get approval, and queue the next fix cycle.
3. After each branch, flag iteration modifications, update project stage/status signals, and clear any pending async reproduction task once consumed.

## Anti-patterns
- Continuing without reproduction steps or ignoring the async reproduction task completion
- Failing to update bug-hunting cycles, status, or attempt counters
- Implementing human hints without explicit approval during pair programming
- Letting long conversations proceed without trimming context when needed

## Output
- Updated iteration status (awaiting fix/logging/test/pair programming), human-readable instructions or logging steps, communicated test instructions, and any user feedback captured

---

# Bug Hunter Pro Workflow

## 1. Deep Trace Collection
- Aggregate logs from across the stack (frontend, middleware, DB).
- Use regex-based filtering to isolate the specific request ID/Correlation ID.

## 2. Differential Debugging
- Compare system state between "Success Case" and "Failure Case".
- Isolate non-deterministic inputs (timing, random seeds, external API latency).

## 3. Root Cause Synthesis
- Trace logic back through the call stack until the first erroneous state mutation.
- Categorize as: Memory leak, Race condition, Logic error, or Environmental drift.

## Standalone Requirements
- Log-stream processing logic from `agents/error_handler.py`.
- Regression test suite generator from `tools/test_gen.py`.
