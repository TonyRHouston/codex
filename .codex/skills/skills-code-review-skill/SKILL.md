---
name: skills-code-review-skill-78ea68
description: 'Perform high-signal code reviews with focus on correctness, security,
  and maintainability. Use when reviewing PRs or diffs.

  Keywords: code-review,quality,correctness

  '
source: skills/code-review/SKILL.md
---

# Code Review

## When to use
- Reviewing PRs or design changes
- Assessing risk for production changes

## Review workflow
1. Understand intent and scope before the diff
2. Check correctness, security, and data handling
3. Validate tests and coverage for changed paths
4. Assess maintainability and operational impact

## Review focus areas
- Data integrity and edge cases
- Error handling and retries
- Backward compatibility and migrations

## Anti-patterns (NEVER)
- Approve without understanding the change intent
- Focus only on style or minor nits
- Ignore tests or skip running them when needed

## Output expectations
- Summary of risk and confidence level
- Blocking issues vs suggestions
- Follow-up tasks or tests to add
