---
name: skills-database-design-skill-bdc874
description: 'Design data models, schemas, and storage strategies. Use when choosing
  databases, modeling entities, or optimizing queries.

  Keywords: database,schemas,queries,modeling

  '
source: skills/database-design/SKILL.md
---

# Database Design

## When to use
- New schema design or major query refactor
- Data growth or performance issues

## Inputs to gather
- Access patterns and query frequency
- Data volume, retention, and consistency needs
- Transaction and concurrency requirements

## Design workflow
1. Choose storage model aligned to access patterns
2. Model entities, relationships, and constraints
3. Define primary keys and indexing strategy
4. Plan migrations and backfill steps

## Design rules
- Normalize for integrity, denormalize for read performance
- Index to match real query filters and joins
- Validate migrations on production-like data

## Anti-patterns (NEVER)
- Index every column without query evidence
- Use JSON blobs for core relational data
- Skip migration rollback planning
- Store unbounded history without retention rules

## Output expectations
- Schema with keys, constraints, and indexes
- Migration plan and rollback strategy
- Query performance assumptions
