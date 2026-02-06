---
name: skills-observability-monitoring-skill-3f6753
description: 'Design observability and monitoring for systems. Use when adding metrics,
  logs, tracing, or SLOs.

  Keywords: observability,monitoring,metrics,tracing

  '
source: skills/observability-monitoring/SKILL.md
---

# Observability and Monitoring

## When to use
- New services or reliability gaps
- Unclear failure modes or slow incident response

## Inputs to gather
- User-facing SLOs and critical flows
- Existing metrics, logs, and tracing coverage

## Observability workflow
1. Define SLOs and error budgets
2. Instrument golden signals (latency, traffic, errors, saturation)
3. Add structured logs with correlation IDs
4. Configure alerts with clear thresholds and runbooks

## Monitoring rules
- Alert on symptoms, not just causes
- Prefer high-signal dashboards over noisy metrics
- Ensure traces link cross-service dependencies

## Anti-patterns (NEVER)
- Alert on every metric without context
- Logs without request or trace correlation
- Metrics that are not tied to user impact

## Output expectations
- Metrics, logs, and tracing plan
- Alert thresholds and response playbook
- Dashboard layout and ownership
