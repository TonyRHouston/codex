---
name: tech-lead-planner-078185
description: Use this skill when the user needs help with tech lead planner. It provides
  practical guidance, execution steps, and quality checks for tech lead planner tasks.
keywords:
- epics
- epic
- tasks
- feature
- task
suggested_keywords:
- epics
- epic
- tasks
- feature
- task
---

# Tech Lead Planner

## When to use
- After specification to spin up the first development plan and tasks
- When a feature epic is active and needs sub-epics/tasks
- When the user asks for a new feature or quick implementation

## Workflow
1. On first run with only the bootstrap epic, clear mocked data, clone the spec, and add the initial "Build frontend" epic; reset relevant/modified file markers.
2. If templates exist and the project just started, optionally apply project templates (respect summaries, maintain relevant files empty afterward).
3. When an epic is active:
   - For feature epics, fetch relevant files in parallel before planning.
   - Use TECH_LEAD_PLANNING to draft the epic-level development plan; choose sub-epics depending on feature vs app complexity.
   - For each sub-epic, call TECH_LEAD_EPIC_BREAKDOWN to form tasks, concatenating descriptions, related API endpoints, and testing instructions.
   - Append generated tasks to next state, emit epics/tasks to the UI twice (before and after update), flag modifications, and log telemetry.
4. When no epic remains, prompt the user for next work:
   - If the user wants a new feature, create a feature epic, set TL_START_FEATURE action, and hand control back to orchestrator.
   - For quick implementations, resurrect the previous state epics/tasks, trim old logs, append a new task under the last sub-epic, and flag tasks/epics modified before notifying the UI.
5. Whenever auth is enabled on the initial app, inject the login/register hard-coded task at the front, prime log streams, and emit starting task/project-stage signals.

## Anti-patterns
- Leaving mocked data intact after bootstrapping
- Skipping relevant-file gathering for feature planning
- Forgetting to flag tasks/epics as modified after mutating lists
- Dropping template summaries or telemetry updates when templates are applied
- Adding quick implementation tasks without trimming previous logs

## Output
- Updated epics, sub-epics, and task lists (with descriptions, API endpoints, testing instructions)
- Project stage/action updates (TL_CREATE_PLAN, TL_START_FEATURE, etc.) and telemetry events reflecting the plan creation
