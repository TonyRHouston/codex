---
name: frontend-wizard-231434
description: Use this skill when the user needs help with frontend wizard. It provides
  practical guidance, execution steps, and quality checks for frontend wizard tasks.
keywords:
- frontend
- swagger
- knowledge
- base
- epic
suggested_keywords:
- frontend
- swagger
- knowledge
- base
- epic
---

# Frontend Wizard

## When to use
- Starting a new project state that needs the initial frontend scaffolding
- Importing a Swagger/OpenAPI definition and configuring auth before work begins

## Workflow
1. Set the next_state action to FE_INIT and reset the in-memory template cache.
2. If the project type is `swagger`:
   - Loop until valid docs are provided; prompt the user, attempt upload via `rag/upload`, and retry on errors (refresh tokens on 403).
   - Once accepted, store returned `external_api_url` and type metadata.
   - Ask for the backend authentication method; for API key, validate availability, capture the key, and persist; for unsupported auth, collect telemetry opt-in.
3. For non-swagger projects, default auth to `login`.
4. Create a KnowledgeBase ORM instance with user options and attach it to the next state (ensure session association).
5. Seed `next_state.epics` with a single "Build frontend" epic (frontend source, open state) and clear additional structures as needed.
6. Return `AgentResponse.create_specification` if initialization succeeded; otherwise exit gracefully.

## Anti-patterns
- Proceeding without validating Swagger docs or repeating the upload on failure
- Ignoring token refresh prompts when uploads return 403
- Forgetting to persist authentication choices into knowledge base options
- Starting without creating the initial epic or knowledge base record

## Output
- Initialized knowledge base and epic list, stored Swagger metadata and auth options, and an action log indicating frontend setup
