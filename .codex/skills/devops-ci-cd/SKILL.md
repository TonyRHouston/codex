---
name: devops-ci-cd-c021f0
description: 'Design CI/CD pipelines and DevOps workflows. Use when automating builds,
  tests, deployments, or environment management.

  Keywords: devops,ci,cd,automation'
---

# DevOps and CI/CD

## When to use
- New pipelines, deployment automation, or release workflows
- Reliability issues in build or deploy stages

## Inputs to gather
- Environments, deployment targets, and rollback needs
- Test suites and build dependencies
- Security and compliance requirements

## Pipeline workflow
1. Define stages: lint, test, build, package, deploy
2. Use caching and artifacts to reduce runtime
3. Gate deploys with required checks and approvals
4. Plan rollback and verification steps

## Operational rules
- Use least-privilege secrets and rotate regularly
- Separate build and deploy permissions
- Prefer immutable artifacts per release

## Anti-patterns (NEVER)
- Deploy without passing tests or approvals
- Store secrets in logs or plaintext files
- Manual steps without auditability

## Output expectations
- Pipeline stages and triggers
- Deployment strategy and rollback plan
- Ownership and alerting for failures
