---
name: tools-copilot-toolkit-skills-github-actions-debugging-skill
description: Debug failing GitHub Actions workflows efficiently. Use this when asked
  to investigate CI failures, workflow issues, or GitHub Actions problems.
license: MIT
source: tools/copilot-toolkit/skills/github-actions-debugging/SKILL.md
---

# GitHub Actions Debugging Skill

This skill helps debug failing GitHub Actions workflows and CI/CD pipeline issues.

## Process

Follow this systematic approach to debug GitHub Actions failures:

### 1. Identify Failed Workflows
Use GitHub CLI or web interface to find failed runs:
```bash
gh run list --workflow=<workflow-name> --limit=10
gh run view <run-id>
```

### 2. Get Failure Information
Download and examine logs:
```bash
gh run view <run-id> --log
gh run view <run-id> --log-failed
```

### 3. Analyze Common Failure Patterns

#### Dependency Issues
- Check if dependencies are correctly specified
- Verify package versions and compatibility
- Look for missing system dependencies
- Review lock file consistency

#### Environment Problems
- Verify environment variables are set correctly
- Check secrets availability and format
- Validate matrix configurations
- Confirm runner compatibility (ubuntu, windows, macos)

#### Test Failures
- Identify specific failing tests
- Check for flaky tests
- Verify test data and fixtures
- Review test environment setup

#### Build Errors
- Check compilation errors
- Verify build scripts and configurations
- Review path issues
- Confirm required tools are installed

#### Permissions and Auth
- Verify token permissions (GITHUB_TOKEN)
- Check repository permissions
- Validate authentication for external services
- Review security settings

### 4. Common Solutions

#### Update Dependencies
```yaml
- name: Install dependencies
  run: npm ci  # Use ci instead of install for lock file
```

#### Fix Caching
```yaml
- name: Cache dependencies
  uses: actions/cache@v3
  with:
    path: ~/.npm
    key: ${{ runner.os }}-node-${{ hashFiles('**/package-lock.json') }}
```

#### Add Debug Logging
```yaml
- name: Debug Info
  run: |
    echo "Node version: $(node --version)"
    echo "NPM version: $(npm --version)"
    echo "Working directory: $(pwd)"
    ls -la
```

#### Matrix Strategy
```yaml
strategy:
  matrix:
    os: [ubuntu-latest, windows-latest]
    node: [16, 18, 20]
  fail-fast: false  # Continue other jobs if one fails
```

## Debugging Techniques

### Enable Debug Logging
Add these secrets to get detailed logs:
- `ACTIONS_RUNNER_DEBUG`: true
- `ACTIONS_STEP_DEBUG`: true

### Reproduce Locally
Use act to run workflows locally:
```bash
gh extension install nektos/gh-act
gh act -j <job-name>
```

### Check Workflow Syntax
```bash
# Validate workflow file
gh workflow view <workflow-name>
```

### Review Recent Changes
```bash
git log --oneline -- .github/workflows/
git diff HEAD~1 .github/workflows/<workflow-file>
```

## Best Practices

### Workflow Design
- Use specific action versions (not @main or @master)
- Cache dependencies appropriately
- Use fail-fast: false for matrix builds when investigating
- Add timeout-minutes to prevent hanging jobs
- Use if: always() for cleanup steps

### Error Handling
- Check exit codes properly
- Use continue-on-error sparingly
- Add meaningful error messages
- Implement retry logic for flaky operations

### Testing
- Test workflow changes in a branch first
- Use workflow_dispatch for manual testing
- Consider using reusable workflows
- Test on multiple platforms if needed

### Maintenance
- Keep actions up to date
- Review security advisories
- Document workflow purpose
- Clean up old workflow files

## Common Issues and Solutions

### "Resource not accessible by integration"
- Check GITHUB_TOKEN permissions in workflow
- Add required permissions to job or workflow

### "Node.js version mismatch"
- Specify exact Node.js version in setup-node
- Match local development version

### "npm ERR! 404 Not Found"
- Check package name spelling
- Verify package registry
- Check authentication for private packages

### "timeout waiting for connection"
- Add retry logic
- Check external service availability
- Increase timeout values

### "Tests pass locally but fail in CI"
- Check environment differences
- Review timezone settings
- Verify file system case sensitivity
- Check for race conditions

## Example Workflow Debugging Session

1. **Failure**: Test suite fails in CI but passes locally
2. **Check Logs**: Download logs with `gh run view <run-id> --log-failed`
3. **Identify**: Tests fail due to missing test database
4. **Root Cause**: Database setup script not running in CI
5. **Fix**: Add database setup step to workflow
6. **Verify**: Push changes and monitor new run
7. **Success**: All tests pass

## Validation

After fixing:
- Verify all jobs succeed
- Check that changes don't affect other workflows
- Test on all matrix configurations
- Update documentation if needed
