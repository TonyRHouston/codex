---
name: files-aed20c
description: Use this skill when the user needs help with files. It provides practical
  guidance, execution steps, and quality checks for files tasks.
---

# Telemetry & Observability

## When to use
- You need to capture usage metrics, error traces, or Kusto-style queries for dashboards

## Workflow
1. Hook telemetry emitters at key agent boundaries (start, finish, error) and include contextual tags (run-id, agent).
2. Emit structured events to the local telemetry collector or Kusto-friendly CSVs for ingestion.
3. Use dashboards or ad-hoc queries to spot regressions or hotspots.

## Anti-patterns
- Emitting full prompt contents to telemetry; trim or hash sensitive fields

## Output
- Structured telemetry events, CSV exports, and queryable dashboards for run analysis
