---
name: actions-debugging-722487
description: Use this skill when the user needs help with actions debugging. It provides
  practical guidance, execution steps, and quality checks for actions debugging tasks.
license: MIT
source: tools/copilot-toolkit/skills/actions-debugging/SKILL.md
---

# Actions Debugging Skill

Systematic approach to debugging GitHub Actions workflow failures.

## Process

### 1. Identify Failed Workflows

- Locate the failed workflow run
- Extract logs (use log-extraction skill: `python3 extract_logs.py`)
- Identify specific failed steps

### 2. Get Failure Information

Use `bash tools/scripts/validate-json.sh summary.json` on extracted data to validate structure.

Review the JSON summary:
```json
{
  "steps": [
    {
      "number": 11,
      "name": "Processing Request (Linux)",
      "conclusion": "success|failure|skipped",
      "duration_human": "mm:ss",
      "attrs": { "data-name": "...", ... }
    }
  ]
}
```

### 3. Analyze Common Failure Patterns

**Dependency Issues**:
- Check step names for "download", "install", "setup"
- Failed download steps → network or availability issue
- Missing tool steps → version or compatibility issue

**Environment Problems**:
- OS-specific step skipped → wrong runner OS
- Validation steps failed → environment config issue
- Tool version mismatches → dependency conflict

**Test Failures**:
- Look for test step duration and conclusion
- No completion time → timeout or hang
- Check for data availability

**Permissions and Auth**:
- Early authentication steps → token or credentials issue
- API call failures → permission or rate limiting

### 4. Common Solutions

Following error handling patterns (`tools/functions/error-handling.md`):

**Add Debug Logging**:
```bash
# In workflow
- name: Debug Info
  run: |
    echo "Node: $(node --version)"
    echo "PWD: $(pwd)"
    echo "Files: $(ls -la)"
```

**Fix Caching**:
```yaml
- uses: actions/cache@v3
  with:
    path: ~/.npm
    key: ${{ runner.os }}-${{ hashFiles('**/package-lock.json') }}
```

**Matrix Strategy**:
```yaml
strategy:
  matrix:
    os: [ubuntu-latest]
    node: [16, 18, 20]
  fail-fast: false
```

### 5. Verify Solution

- Re-run workflow
- Extract logs: `python3 extract_logs.py <new-html>`
- Validate: `bash tools/scripts/validate-json.sh summary.json`
- Compare step results with previous run

## Best Practices

Following validation patterns (`tools/functions/validation.md`):

- **Validate Input**: Check log file validity and structure
- **Fail Fast**: Stop investigation on invalid data
- **Check Requirements**: Verify OS, tool versions, dependencies
- **Test Boundaries**: Test with edge cases (missing deps, old versions)

## Workflow Design

- Use specific action versions (not @main)
- Cache dependencies appropriately
- Add timeout-minutes to prevent hangs
- Use if: always() for cleanup steps
- Test workflow changes in a branch

## Related Skills

- **Log Extraction**: Extract and parse log files
- **JSON Validation**: Validate extracted data
- **Bug Investigation**: Systematic root cause analysis
