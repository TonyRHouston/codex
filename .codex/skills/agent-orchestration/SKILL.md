---
name: agent-orchestration-984e3f
description: Use this skill when the user needs help with agent orchestration. It
  provides practical guidance, execution steps, and quality checks for agent orchestration
  tasks.
keywords:
- agent
- agents
- based
- kode
- cli
source: partially-processed/Kode-cli/docs/agents-system.md
suggested_keywords:
- agent
- agents
- based
- kode
- cli
provenance: null
required_code: partially-processed/agents/executor.py (Load/Execute logic)
---

# agent-orchestration

## When to use
- Use when the user request explicitly maps to **agent orchestration** outcomes.
- Use when consistent, repeatable outputs are more important than ad-hoc responses.

## Decision Framework
Before acting, evaluate the **why**, trade-off, and risk profile:
- **Why now**: what user outcome or blocker is this skill resolving?
- **Trade-off**: what speed vs quality decision is acceptable for this turn?
- **Scope boundary**: what is in-scope for this skill vs another domain skill?
- **Verification strategy**: what concrete check proves the result is correct?

## Workflow
1. Confirm intent, constraints, and expected output format.
2. Apply this skill's domain logic to produce a first-pass result.
3. Validate the result against correctness, safety, and completeness checks.
4. Refine output and state assumptions, limitations, and next action clearly.

## Anti-patterns (NEVER)
- Never proceed when intent is ambiguous and high-impact decisions are involved.
- Never mix unrelated domain steps without an explicit decision to do so.
- Do not ship output that has not been validated against the requested constraints.
- Avoid placeholder text, guessed facts, or silent omissions in final output.
- Never use this skill when a more specific skill is clearly the better fit.
- Don't skip verification because an initial result "looks right".

## Output Expectations
- Clear, task-aligned result with explicit assumptions.
- Evidence of validation steps performed.
- Concise summary of what was done and what remains.

## Existing Notes
# Agent Orchestration Workflow

## 1. Agent Hierarchy
- Identify the **Primary Agent** (Task Lead).
- Assign **Sub-Agents** based on specialized domains (e.g., `git`, `tech_writer`).
- Apply the 5-tier priority system for model loading.

## 2. Dynamic Discovery
- Implement hot-reload triggers for new agent configurations.
- Map capability strings to available Python agent classes.

## 3. Communication Channel
- Maintain state shared between agents in `session_state.md`.
- Enforce strict hand-off protocols to prevent logic loops.

## Standalone Requirements
- Implementation of the `AgentExecutor` class (see `executor.py`).
- Config schema for `model_selection` and `tool_restriction`.
