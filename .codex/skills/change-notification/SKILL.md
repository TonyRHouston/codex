---
name: change-notification-844064
description: Use this skill when the user needs help with change notification. It
  provides practical guidance, execution steps, and quality checks for change notification
  tasks.
keywords:
- notify
- slack
- alerts
- code-change
- update
---

# Change Notification Workflow

## 1. Significance Assessment
Determine the "Blast Radius":
- **Low**: Local refactor, no API change (Log only).
- **Medium**: UI change, dependency update (Internal notify).
- **High**: Breaking API change, DB schema migration (Critical notify).

## 2. Notification Composition
- **Summary**: Concise description of *what* changed.
- **Rationale**: The *why* behind the change.
- **Action Required**: Clear instructions for other developers (e.g., "Run `npm install`").

## 3. Propagation Channels
- Update internal `changelog` or `notices.md`.
- Trigger webhook-based channel alerts (Slack/Discord/Email).

## Anti-Patterns
- Notifying for every commit (Notification Fatigue).
- Forgetting to mention breaking changes until after deployment.
