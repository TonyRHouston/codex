---
name: api-design-5cbcbd
description: 'Design maintainable APIs with clear contracts. Use when defining endpoints,
  schemas, error models, versioning, or backward compatibility.

  Keywords: api,contracts,versioning,errors'
---

# API Design

## When to use
- New endpoints, breaking changes, or versioning decisions
- Defining schema contracts across teams or services

## Inputs to gather
- Primary consumers and their use cases
- Core domain model and data ownership
- Auth, rate limits, and latency requirements

## Design workflow
1. Model resources and relationships first
2. Map use cases to endpoints and methods
3. Define schemas with explicit required vs optional fields
4. Specify error model and versioning strategy

## Contract rules
- Use nouns for resources, verbs via HTTP methods
- Idempotency for create/modify actions (keys or safe retries)
- Consistent pagination and filtering conventions
- Predictable error shape (code, message, details)

## Anti-patterns (NEVER)
- Breaking changes without versioning or migration path
- Overloaded endpoints with inconsistent behavior
- Inconsistent status codes or error payloads
- Leaking internal IDs or storage-specific fields

## Output expectations
- Endpoint list with request/response examples
- Error model and status code mapping
- Versioning and compatibility plan
