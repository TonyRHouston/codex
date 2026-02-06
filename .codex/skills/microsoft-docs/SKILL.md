---
name: microsoft-docs-6e3f98
description: Use this skill when the user needs help with microsoft docs. It provides
  practical guidance, execution steps, and quality checks for microsoft docs tasks.
compatibility: Requires Microsoft Learn MCP Server (https://learn.microsoft.com/api/mcp)
---

# microsoft-docs

## When to use
- Use when the user request explicitly maps to **microsoft docs** outcomes.
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
# Microsoft Docs

## Tools

| Tool | Use For |
|------|---------|
| `microsoft_docs_search` | Find documentation—concepts, guides, tutorials, configuration |
| `microsoft_docs_fetch` | Get full page content (when search excerpts aren't enough) |

## When to Use

- **Understanding concepts** — "How does Cosmos DB partitioning work?"
- **Learning a service** — "Azure Functions overview", "Container Apps architecture"
- **Finding tutorials** — "quickstart", "getting started", "step-by-step"
- **Configuration options** — "App Service configuration settings"
- **Limits & quotas** — "Azure OpenAI rate limits", "Service Bus quotas"
- **Best practices** — "Azure security best practices"

## Query Effectiveness

Good queries are specific:

```
# ❌ Too broad
"Azure Functions"

# ✅ Specific
"Azure Functions Python v2 programming model"
"Cosmos DB partition key design best practices"
"Container Apps scaling rules KEDA"
```

Include context:
- **Version** when relevant (`.NET 8`, `EF Core 8`)
- **Task intent** (`quickstart`, `tutorial`, `overview`, `limits`)
- **Platform** for multi-platform docs (`Linux`, `Windows`)

## When to Fetch Full Page

Fetch after search when:
- **Tutorials** — need complete step-by-step instructions
- **Configuration guides** — need all options listed
- **Deep dives** — user wants comprehensive coverage
- **Search excerpt is cut off** — full context needed

## Why Use This

- **Accuracy** — live docs, not training data that may be outdated
- **Completeness** — tutorials have all steps, not fragments
- **Authority** — official Microsoft documentation
