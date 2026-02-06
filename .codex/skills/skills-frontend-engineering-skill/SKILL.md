---
name: skills-frontend-engineering-skill-8bea46
description: Use this skill when the user needs help with skills frontend engineering
  skill. It provides practical guidance, execution steps, and quality checks for skills
  frontend engineering skill tasks.
source: skills/frontend-engineering/SKILL.md
---

# Frontend Engineering

## When to use
- New UI flows, performance issues, or accessibility gaps
- Architecture decisions for state or data fetching

## Inputs to gather
- User journeys and target devices
- Design system constraints and branding
- Performance budgets and a11y requirements

## Engineering workflow
1. Map user flows to component hierarchy
2. Define state boundaries and data ownership
3. Optimize rendering and bundle size early
4. Validate accessibility with semantic structure

## Frontend rules
- Prefer server data normalization and caching
- Minimize global state; colocate state by component
- Use ARIA only when semantics are insufficient

## Anti-patterns (NEVER)
- Unbounded re-renders from global state misuse
- Rely on client-side rendering for all content
- Ignore keyboard navigation and focus management
- Ship large bundles without code splitting

## Output expectations
- Component tree and state/data flow notes
- Performance risks and mitigation plan
- Accessibility checklist with concrete fixes
