---
name: telemetry-kusto-analyst-38bb69
description: Use this skill when the user needs help with telemetry kusto analyst.
  It provides practical guidance, execution steps, and quality checks for telemetry
  kusto analyst tasks.
keywords:
- kusto
- telemetry
- queries
- query
- real
suggested_keywords:
- kusto
- telemetry
- queries
- query
- real
---

# Telemetry Kusto Analyst

## When to use
- Investigating VS Code telemetry using KQL and providing real query results

## Workflow
1. If missing, fetch telemetry docs (`vscode-telemetry-docs/.github/copilot-instructions.md`).
2. If needed, install/ensure Kusto tooling (`kusto_query` tool or Azure MCP extension).
3. Run real Kusto queries (default rolling 28-day window if not specified); include proper time filters.
4. Parallelize independent queries when useful; stop after repeated failures and report.
5. Present query text, results, and interpretation; cite docs when relevant and scrub user-identifiable data.

## Anti-patterns
- Describing hypothetical queries instead of running them
- Omitting time filters or using partial-day windows
- Ignoring repeated query failures without reporting

## Output
- Executed Kusto query, results, and a concise analysis answering the question
