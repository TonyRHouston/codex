---
name: code-review-structured-abc390
description: Use this skill when the user needs help with code review structured.
  It provides practical guidance, execution steps, and quality checks for code review
  structured tasks.
license: MIT
---

# Structured Code Review Skill

This skill provides a systematic approach to code reviews using shared tools and templates.

## Process

When reviewing code, follow this structured workflow:

1. **Understand the Change**
   - Read PR description and linked issues
   - Identify affected files and components
   - Note the scope and impact of changes

2. **Apply Code Review Template**
   - Follow the checklist in `tools/prompts/code-review.md`
   - Review functionality, quality, testing, security, and performance
   - Use the structured template format

3. **Validate Code Quality**
   - Check error handling patterns (reference `tools/functions/error-handling.md`)
   - Verify input validation (reference `tools/functions/validation.md`)
   - Run validation scripts when applicable

4. **Run Validation Scripts**
   ```bash
   # Validate JSON files
   bash tools/scripts/validate-json.sh <file-path>
   
   # Check dependencies
   bash tools/scripts/check-dependencies.sh node npm git
   ```

5. **Provide Structured Feedback**
   - Group issues by severity: Critical Issues, Suggestions, Questions
   - Include specific file:line references
   - Suggest concrete fixes with code examples
   - Highlight positive aspects and good practices

## Review Categories

### Functionality
- Does the code implement the intended feature correctly?
- Are edge cases handled appropriately?
- Is error handling comprehensive?

### Code Quality
- Is the code readable and maintainable?
- Are naming conventions consistent?
- Is there unnecessary duplication?
- Are functions appropriately sized?

### Testing
- Are there sufficient tests for the changes?
- Do tests cover edge cases and error conditions?
- Are tests clear and maintainable?

### Security
- Are there any security vulnerabilities?
- Is user input properly validated and sanitized?
- Are secrets or sensitive data handled correctly?

### Performance
- Are there obvious performance issues?
- Are resources managed efficiently?
- Could algorithms be optimized?

## Example Usage

When reviewing a PR that adds JSON configuration:

1. Use `bash tools/scripts/validate-json.sh config.json` to validate syntax
2. Check error handling against patterns in `tools/functions/error-handling.md`
3. Follow the review checklist from `tools/prompts/code-review.md`
4. Provide structured feedback organized by severity

## Best Practices

- Be constructive and specific in feedback
- Focus on important issues, avoid nitpicking
- Provide examples and alternatives
- Consider the context and constraints
- Acknowledge good practices
- Reference relevant documentation and patterns
