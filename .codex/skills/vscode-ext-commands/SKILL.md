---
name: vscode-ext-commands-1a8c10
description: Use this skill when the user needs help with vscode ext commands. It
  provides practical guidance, execution steps, and quality checks for vscode ext
  commands tasks.
---

# vscode-ext-commands

## When to use
- Use when the user request explicitly maps to **vscode ext commands** outcomes.
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
# VS Code extension command contribution

This skill helps you to contribute commands in VS Code extensions

## When to use this skill

Use this skill when you need to:
- Add or update commands to your VS Code extension

# Instructions

VS Code commands must always define a `title`, independent of its category, visibility or location. We use a few patterns for each "kind" of command, with some characteristics, described below:

* Regular commands: By default, all commands should be accessible in the Command Palette, must define a `category`, and don't need an `icon`, unless the command will be used in the Side Bar.

* Side Bar commands: Its name follows a special pattern, starting with underscore (`_`) and suffixed with `#sideBar`, like `_extensionId.someCommand#sideBar` for instance. Must define an `icon`, and may or may not have some rule for `enablement`. Side Bar exclusive commands should not be visible in the Command Palette. Contributing it to the `view/title` or `view/item/context`, we must inform _order/position_ that it will be displayed, and we can use terms "relative to other command/button" in order to you identify the correct `group` to be used. Also, it's a good practice to define the condition (`when`) for the new command is visible.
