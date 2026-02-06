---
name: json-validation-2
description: Validate and work with JSON configuration files. Use this when asked to validate JSON, check configuration files, or work with JSON data.
license: MIT
source: tools/copilot-toolkit/skills/json-validation/SKILL.md
---

# JSON Validation Skill

This skill helps validate JSON files and configuration using shared validation scripts.

## Quick Validation

Use the shared validation script:

```bash
bash tools/scripts/validate-json.sh <file-path>
```

Returns:
- Exit code 0 if valid
- Exit code 1 if invalid with error details

## Process

### 1. Validate Syntax
```bash
# Single file
bash tools/scripts/validate-json.sh config.json

# Multiple files
for file in config/*.json; do
  bash tools/scripts/validate-json.sh "$file"
done
```

### 2. Check Structure
After syntax validation, verify the structure matches expectations:
- Required fields are present
- Data types are correct
- Values are within valid ranges
- References to other objects are valid

### 3. Validate Content
- Check for security issues (exposed secrets, credentials)
- Verify URLs and paths are correct
- Ensure environment-specific values are appropriate
- Validate against schema if available

## Common JSON Issues

### Syntax Errors
- Missing or extra commas
- Unclosed brackets or braces
- Unquoted keys
- Invalid escape sequences
- Trailing commas (not allowed in strict JSON)

### Structure Issues
- Duplicate keys (last value wins)
- Inconsistent nesting levels
- Missing required fields
- Incorrect data types

### Content Issues
- Invalid URLs or file paths
- Exposed secrets or credentials
- Incorrect environment references
- Out-of-range values

## Validation Patterns

### Using jq for Validation
```bash
# Validate and pretty-print
jq . config.json

# Extract specific field
jq '.database.host' config.json

# Validate structure
jq 'has("required_field")' config.json
```

### Schema Validation
```bash
# Using ajv-cli (if installed)
ajv validate -s schema.json -d config.json
```

### Custom Validation Script
```bash
#!/bin/bash
# Validate JSON and check required fields

file="$1"

# Check syntax
if ! jq empty "$file" 2>/dev/null; then
  echo "Invalid JSON syntax in $file"
  exit 1
fi

# Check required fields
required_fields=("name" "version" "description")
for field in "${required_fields[@]}"; do
  if ! jq -e ".$field" "$file" >/dev/null 2>&1; then
    echo "Missing required field: $field"
    exit 1
  fi
done

echo "Validation passed for $file"
```

## Best Practices

### Configuration Files
- Use consistent formatting (2 or 4 space indentation)
- Add comments in separate .md file (JSON doesn't support comments)
- Validate on save and in CI/CD
- Use environment-specific files (dev.json, prod.json)
- Never commit secrets in JSON files

### Large JSON Files
- Consider splitting into smaller files
- Use JSON Lines format for large datasets
- Validate in chunks if memory-constrained
- Use streaming parsers for very large files

### Schema Design
- Define clear schema for configuration
- Use JSON Schema standard
- Document required vs optional fields
- Specify data types and constraints
- Provide examples

## Integration with Tools

### In Git Hooks
```bash
# .git/hooks/pre-commit
#!/bin/bash
for file in $(git diff --cached --name-only | grep '.json$'); do
  bash tools/scripts/validate-json.sh "$file" || exit 1
done
```

### In CI/CD
```yaml
# GitHub Actions example
- name: Validate JSON files
  run: |
    for file in config/*.json; do
      bash tools/scripts/validate-json.sh "$file"
    done
```

### In Development
```bash
# Watch for changes and validate
fswatch -o config/*.json | xargs -n1 bash tools/scripts/validate-json.sh
```

## Example Usage

### Validate Configuration
```bash
# Validate package.json
bash tools/scripts/validate-json.sh package.json

# Validate all config files
find . -name "*.json" -exec bash tools/scripts/validate-json.sh {} \;
```

### Fix Common Issues
```bash
# Pretty-print and fix formatting
jq . config.json > config.json.tmp && mv config.json.tmp config.json

# Remove comments (if accidentally added)
jq . config.json > config.json.tmp && mv config.json.tmp config.json
```

## Error Handling

Reference error handling patterns from `tools/functions/error-handling.md`:

```javascript
// Example: Safe JSON parsing
function parseJsonFile(filePath) {
  try {
    const content = fs.readFileSync(filePath, 'utf8');
    return JSON.parse(content);
  } catch (error) {
    if (error.code === 'ENOENT') {
      throw new Error(`File not found: ${filePath}`);
    }
    if (error instanceof SyntaxError) {
      throw new Error(`Invalid JSON in ${filePath}: ${error.message}`);
    }
    throw error;
  }
}
```

## Resources

- JSON Specification: https://www.json.org/
- JSON Schema: https://json-schema.org/
- jq Manual: https://stedolan.github.io/jq/manual/
- Shared validation script: `tools/scripts/validate-json.sh`
- Validation patterns: `tools/functions/validation.md`
