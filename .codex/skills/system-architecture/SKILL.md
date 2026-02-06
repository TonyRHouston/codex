---
name: system-architecture-8934c1
description: 'Architect systems and components with scalability, reliability, and
  cost trade-offs. Use when designing new systems or major refactors.

  Keywords: architecture,scalability,trade-offs,design'
---

# System Architecture

## When to use
- New system design or major platform refactor
- Scaling, reliability, or cost trade-off decisions

## Inputs to gather
- Functional requirements and success metrics
- Quality attributes (latency, availability, consistency)
- Traffic patterns, data volume, and growth

## Architecture workflow
1. Define top 3 quality attributes and constraints
2. Choose architecture style (monolith, modular, services)
3. Define components, ownership, and data flow
4. Model failure modes and resilience tactics

## Key decisions
- Data ownership and boundaries
- Sync vs async communication
- Consistency model and recovery strategy

## Anti-patterns (NEVER)
- Distributed architecture by default without need
- Hidden shared state across teams or services
- Long synchronous dependency chains without timeouts
- Scaling assumptions without load estimates

## Output expectations
- Component map with responsibilities
- Data flow and dependency diagram (text is fine)
- Trade-off summary and risks
