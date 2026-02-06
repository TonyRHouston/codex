---
name: vscode-ext-localization-ee0d1c
description: Use this skill when the user needs help with vscode ext localization.
  It provides practical guidance, execution steps, and quality checks for vscode ext
  localization tasks.
---

# vscode-ext-localization

## When to use
- Use when the user request explicitly maps to **vscode ext localization** outcomes.
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
# VS Code extension localization

This skill helps you localize every aspect of VS Code extensions

## When to use this skill

Use this skill when you need to:
- Localize new or existing contributed configurations (settings), commands, menus, views or walkthroughs
- Localize new or existing messages or other string resources contained in extension source code that are displayed to the end user

# Instructions

VS Code localization is composed by three different approaches, depending on the resource that is being localized. When a new localizable resource is created or updated, the corresponding localization for all currently available languages must be created/updated.

1. Configurations like Settings, Commands, Menus, Views, ViewsWelcome, Walkthrough Titles and Descriptions, defined in `package.json`
  -> An exclusive `package.nls.LANGID.json` file, like `package.nls.pt-br.json` of Brazilian Portuguese (`pt-br`) localization
2. Walkthrough content (defined in its own `Markdown` files)
  -> An exclusive `Markdown` file like `walkthrough/someStep.pt-br.md` for Brazilian Portuguese localization
3. Messages and string located in extension source code (JavaScript or TypeScript files)
  -> An exclusive `bundle.l10n.pt-br.json` for Brazilian Portuguese localization
