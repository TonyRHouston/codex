---
name: tools-copilot-toolkit-skills-log-extraction-skill-44efea
description: Use this skill when the user needs help with tools copilot toolkit skills
  log extraction skill. It provides practical guidance, execution steps, and quality
  checks for tools copilot toolkit skills log extraction skill tasks.
license: MIT
source: tools/copilot-toolkit/skills/log-extraction/SKILL.md
---

# tools-copilot-toolkit-skills-log-extraction-skill

## When to use
- Use when the user request explicitly maps to **tools copilot toolkit skills log extraction skill** outcomes.
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
# Log Extraction Skill

This skill helps extract, parse, and analyze GitHub Actions workflow logs efficiently.

## Quick Start

Use the `extract_logs.py` CLI tool:

```bash
# Extract and display summary
python3 extract_logs.py <html-file>

# Generate HTML summary
python3 extract_logs.py <html-file> --html-out summary.html

# Generate JSON export
python3 extract_logs.py <html-file> --json-out summary.json

# Both formats
python3 extract_logs.py <html-file> --html-out summary.html --json-out summary.json
```

## Process

### 1. Gather Log Information

- Identify the source log file (saved HTML from GitHub Actions)
- Note what workflow or job the logs are from
- Identify time period and runner OS
- Check for specific error or failure patterns

### 2. Parse and Validate

The extractor uses structured parsing following `tools/functions/validation.md`:

- Validates HTML structure
- Extracts step metadata (name, conclusion, timing)
- Normalizes attribute values (whitespace collapsing)
- Preserves both cleaned and raw attribute values

Use `bash tools/scripts/validate-json.sh summary.json` to validate output.

### 3. Analyze Results

The extracted data includes:

**Per-Step Information**:
- Step number and name
- Conclusion (success, failure, skipped)
- Start and completion timestamps
- Duration in seconds and human-readable format
- Log URL for detailed logs
- All metadata attributes (raw and cleaned)

**Summary View**:
- HTML: Styled table with per-step details and log links
- JSON: Structured data for programmatic access

### 4. Investigate Patterns

Use bug investigation patterns (`tools/prompts/bug-investigation.md`):

- **Gather Information**: Review step conclusions, error patterns
- **Isolate Cause**: Identify which steps failed and why
- **Analyze**: Look for timing anomalies, skip patterns
- **Solution**: Determine remediation (retry, config change, dependency fix)

## Common Patterns

### Build Timeouts

Look for:
- Incomplete step execution
- No `completed_at` timestamp
- Long `duration_seconds` without progress

### Environment Issues

Look for:
- Skipped OS-specific steps (firewall, setup)
- Version mismatches in validation steps
- Missing tool installation

### Dependency Failures

Look for:
- Early step failures (download, setup)
- "Failed to download" messages
- Version conflict patterns

## Validation

Always validate extracted JSON:

```bash
bash tools/scripts/validate-json.sh summary.json
```

Ensures:
- Valid JSON syntax
- All required fields present
- Proper data types
- No missing metadata

## Best Practices

- Save original HTML files for audit trail
- Validate JSON output before analysis
- Use structured data (JSON) for programmatic analysis
- Reference both HTML and JSON views for context
- Document investigation findings

## Integration

The extractor integrates with:
- **JSON Validation Skill**: Validate extracted data (`tools/scripts/validate-json.sh`)
- **Bug Investigation Skill**: Systematic failure analysis
- **Code Review Skill**: Validate workflow configuration quality
