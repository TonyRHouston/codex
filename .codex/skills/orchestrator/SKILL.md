---
name: orchestrator-829a76
description: Use this skill when the user needs help with orchestrator. It provides
  practical guidance, execution steps, and quality checks for orchestrator tasks.
keywords:
- agent
- project
- git
- initialization
- each
suggested_keywords:
- agent
- project
- git
- initialization
- each
---

# Orchestrator

## When to use
- Running the full Pythagora flow from specification through completion
- Responding to agent outputs, user interrupts, and project state changes

## Workflow
1. Bootstrap shared services: create an Executor (and reuse its ProcessManager), initialize UI channels, check for offline file changes, install dependencies, and apply project scaffolding tweaks (frontend script, package.json/vite updates, favicon, debugger).
2. If Git is enabled, detect installation and optionally initialize the repo before work starts.
3. Enter the main loop:
   - Handle redo flags by loading prior project states and restoring files.
   - Update telemetry stats and choose the next agent based on current state (spec writer, architect, developer, troubleshooter, problem solver, etc.).
   - Run the agent (or parallel agents when appropriate), gracefully handling user interrupts.
4. After each agent finishes:
   - On DONE, commit next_state to the database, refresh knowledge base artifacts, and emit project info if the spec writer just ran.
   - On INPUT_REQUIRED, bubble context to the UI.
   - On EXIT, break the loop and finalize.
5. Keep helper routines ready for dependency installation, script injection, debugging support, and legacy UI updates.

## Anti-patterns
- Neglecting offline change detection, which can overwrite user edits
- Forgetting to propagate ProcessManager/UI references to secondary agents
- Ignoring agent responses (e.g., not handling EXIT or INPUT_REQUIRED)
- Skipping Git initialization checks when orchestrator is instructed to use Git

## Output
- Coordinated sequence of agent invocations with committed project states, refreshed knowledge base info, and optional Git commits or scaffolding updates
