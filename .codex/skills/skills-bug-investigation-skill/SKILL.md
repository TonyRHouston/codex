---
name: skills-bug-investigation-skill-b1a61c
description: Use this skill when the user needs help with skills bug investigation
  skill. It provides practical guidance, execution steps, and quality checks for skills
  bug investigation skill tasks.
license: MIT
source: skills/bug-investigation/SKILL.md
---

# Bug Investigation Skill

This skill provides a systematic methodology for investigating and resolving bugs efficiently.

## Investigation Process

Follow the structured process from `tools/prompts/bug-investigation.md`:

### 1. Gather Information
- Collect bug report details: symptoms, steps to reproduce, expected vs actual behavior
- Review error messages, logs, and stack traces
- Identify affected versions and environments
- Check for related issues or recent changes

### 2. Reproduce the Bug
- Set up the environment to match the bug conditions
- Follow reproduction steps exactly
- Document any variations or additional findings
- Confirm the bug is reproducible

### 3. Isolate the Cause
- Use debugging tools and techniques
- Add logging or instrumentation if needed
- Test hypotheses systematically
- Narrow down to specific code or conditions
- Review recent changes using git history

### 4. Analyze Root Cause
- Understand why the bug occurs
- Identify contributing factors
- Consider edge cases and related scenarios
- Check for similar issues in other areas

### 5. Develop Solution
- Plan the fix considering scope and impact
- Follow error handling patterns from `tools/functions/error-handling.md`
- Use validation patterns from `tools/functions/validation.md`
- Consider backward compatibility
- Write tests to prevent regression

### 6. Verify Fix
- Test the specific bug scenario
- Test edge cases and related scenarios
- Run existing test suite
- Consider manual testing if needed
- Document the fix

## Debugging Techniques

### Code Analysis
- Review the code path leading to the issue
- Check for logic errors, off-by-one errors, race conditions
- Verify assumptions and preconditions
- Look for typos and incorrect variable references

### Logging and Tracing
- Add strategic log statements
- Use debugging tools (debugger, profiler)
- Trace execution flow
- Monitor state changes

### Testing
- Write failing test that reproduces the bug
- Use test-driven debugging
- Test boundary conditions
- Verify fix with multiple test cases

### Git Investigation
```bash
# Find when bug was introduced
git log --oneline -- <file>
git blame <file>
git bisect start
```

## Common Bug Patterns

### Null/Undefined References
- Check for null/undefined before access
- Use optional chaining or safe navigation
- Validate inputs properly

### Off-by-One Errors
- Review loop conditions and array indices
- Check boundary conditions
- Test with edge cases

### Race Conditions
- Identify shared state and concurrent access
- Add proper synchronization
- Use atomic operations where appropriate

### Memory Issues
- Check for memory leaks
- Verify resource cleanup
- Monitor memory usage

## Best Practices

- Document your investigation process
- Keep notes of what you've tried
- Make minimal changes to fix the issue
- Add tests to prevent regression
- Consider impact on related code
- Update documentation if needed

## Validation Scripts

Use shared validation tools:

```bash
# Validate JSON configuration
bash tools/scripts/validate-json.sh <file>

# Check dependencies
bash tools/scripts/check-dependencies.sh <deps>
```

## Example Investigation

1. **Bug Report**: "Application crashes when loading user profile"
2. **Reproduce**: Set up test user, navigate to profile
3. **Logs**: Find null pointer exception in user data access
4. **Root Cause**: Missing validation for optional user fields
5. **Fix**: Add validation using patterns from `tools/functions/validation.md`
6. **Test**: Add test cases for users with missing fields
7. **Verify**: Run full test suite and manual testing
