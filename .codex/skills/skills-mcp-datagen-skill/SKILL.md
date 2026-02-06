---
name: skills-mcp-datagen-skill-3229cc
description: 'Operate the Data Generation MCP server for synthetic data creation.
  Use when generating tables or predefined datasets.

  Keywords: mcp,datagen,synthetic-data,faker,numpy

  '
source: skills/mcp-datagen/SKILL.md
---

# MCP Data Generation Server

## When to use
- Generate synthetic datasets for testing
- Build custom schema-driven tables

## Core workflow
1. Define schema and row counts
2. Choose generator per field (faker/numpy/mimesis)
3. Validate outputs and correlations

## Anti-patterns (NEVER)
- Use synthetic data as production data
- Skip schema validation

## Output expectations
- Schema, row counts, and sample output

## References
- Read references/datagen.md
