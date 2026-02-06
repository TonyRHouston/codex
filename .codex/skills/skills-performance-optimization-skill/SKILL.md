---
name: skills-performance-optimization-skill-29eb47
description: 'Identify and fix performance bottlenecks in code or systems. Use when
  latency, throughput, or resource usage regress.

  Keywords: performance,profiling,latency,throughput

  '
source: skills/performance-optimization/SKILL.md
---

# Performance Optimization

## When to use
- Latency regressions, throughput drops, or high resource usage
- Performance SLOs are missed or trending downward

## Inputs to gather
- SLO/SLI targets and baseline metrics
- Representative load profile and data shape
- Profiling data (CPU, memory, IO, network)

## Optimization workflow
1. Measure and reproduce under realistic load
2. Identify top 1-2 bottlenecks (avoid long tail guesswork)
3. Apply targeted fixes, then re-measure
4. Add regression guardrails (benchmarks or alerts)

## Bottleneck taxonomy
- CPU-bound: algorithmic complexity, hot loops
- IO-bound: chatty calls, slow storage, large payloads
- Lock/contension: shared resources or serialization points
- Network-bound: retries, latency amplification, N+1 calls

## Anti-patterns (NEVER)
- Optimize before profiling or without baseline metrics
- Micro-optimize while ignoring the primary bottleneck
- Cache without invalidation or TTL strategy
- Change multiple variables in one performance test

## Output expectations
- Bottleneck analysis with evidence
- Before/after metrics and trade-offs
- Follow-up actions for regressions
