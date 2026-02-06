---
name: system-architect-84e9e5
description: Use this skill when the user needs help with system architect. It provides
  practical guidance, execution steps, and quality checks for system architect tasks.
keywords:
- structural
- design
- system
- tools
- architecture
source: partially-processed/agents/architect.py
suggested_keywords:
- structural
- design
- system
- tools
- architecture
provenance: null
required_code: partially-processed/tools/complexity_scanner/ (Metrics logic)
---

# system-architect

## When to use
- Use when the user request explicitly maps to **system architect** outcomes.
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
# System Architecture Workflow

## 1. Structural Audit
- Map directory dependencies and cycles.
- Identify "God Classes" or overly coupled modules.

## 2. Design Pattern Proposal
- Select appropriate patterns (e.g., CQRS, Repository, Factory).
- Define interface boundaries between primary system components.

## 3. Scalability Mapping
- Plan for sharding, caching layers (Redis/Memcached), and async worker queues.
- Validate data flow against N-tier architecture standards.

## Standalone Requirements
- Architecture visualization tools found in `Coding_Tools/`.
- Complexity metric calculation scripts from `ai-logic/metrics/`.
