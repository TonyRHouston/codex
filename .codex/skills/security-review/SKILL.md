---
name: security-review-757015
description: Use this skill when the user needs help with security review. It provides
  practical guidance, execution steps, and quality checks for security review tasks.
---

# Security Review

## When to use
- New auth flows, data exposure, or external integrations
- Reviewing PRs that touch security-sensitive areas

## Inputs to gather
- Assets, entry points, and trust boundaries
- Authn/authz model and data classification
- Third-party dependencies and secrets handling

## Review workflow
1. Threat model: assets, actors, attack surface
2. Validate input handling and output encoding
3. Review authz checks and session lifecycle
4. Verify secrets storage, logging, and access controls

## Common risk areas
- Injection and deserialization
- Privilege escalation and missing authz
- Secret leakage in logs or configs

## Anti-patterns (NEVER)
- Rely on client-side validation alone
- Store secrets in source code or configs
- Allow broad access without audit trails

## Output expectations
- Findings with severity and evidence
- Remediation steps and test coverage
- Residual risk notes
