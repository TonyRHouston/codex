---
name: backend-services-e79f62
description: Use this skill when the user needs help with backend services. It provides
  practical guidance, execution steps, and quality checks for backend services tasks.
---

# Backend Services

## When to use
- New service design or service split decisions
- Reliability, latency, or integration challenges

## Inputs to gather
- Data ownership and consistency needs
- Latency budgets and throughput targets
- Upstream and downstream dependencies

## Service design workflow
1. Define service boundaries and owned data
2. Specify API contracts and idempotency behavior
3. Plan retries, timeouts, and backoff
4. Add resilience patterns (circuit breakers, fallbacks)

## Reliability rules
- All external calls must have timeouts
- Retries must be bounded and idempotent
- Prefer async for long-running workflows

## Anti-patterns (NEVER)
- Shared database across multiple services
- Unbounded retries that amplify load
- Hidden dependencies without observability
- Long synchronous chains in critical paths

## Output expectations
- Service contract with error and retry policy
- Failure mode analysis and mitigation
- Observability hooks to validate behavior
