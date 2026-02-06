---
name: text-data-isolation-github-original-1bf365
description: Use this skill when the user needs help with text data isolation github
  original. It provides practical guidance, execution steps, and quality checks for
  text data isolation github original tasks.
license: MIT
---

# text-data-isolation-github-original

## When to use
- Use when the user request explicitly maps to **text data isolation github original** outcomes.
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
# Text Data Isolation Skill

A minimal skill for extracting and isolating text data from various sources including HTML logs, JSON, console output, and mixed-format files.

## Quick Start

Use the `isolate_text.py` CLI tool:

```bash
# Extract text from any source file
python3 isolate_text.py source.html

# Save isolated text to file
python3 isolate_text.py source.html --output clean_text.txt

# Specify format explicitly
python3 isolate_text.py data.json --format json --output text.txt

# Auto-detect format (default)
python3 isolate_text.py file.txt --output isolated.txt

# Generate analysis report
python3 isolate_text.py source.html --output text.txt --report analysis.json
```

## Supported Formats

- **HTML**: Extracts text from HTML files, removes tags, preserves structure
- **JSON**: Extracts text values from JSON objects/arrays
- **Console Output**: Cleans timestamp and log markers, preserves content
- **Plain Text**: Cleans whitespace and special characters
- **Auto-detect**: Automatically identifies format based on file content

## Process

### 1. Identify Source

- Determine input source type (HTML, JSON, console, text, etc.)
- Verify file exists and is readable
- Check file size and encoding

### 2. Parse and Extract

- Auto-detect or use specified format
- Parse according to format rules
- Extract text content while preserving meaning
- Remove markup, timestamps, and control characters

### 3. Clean and Isolate

- Normalize whitespace
- Remove redundant newlines
- Consolidate related text blocks
- Eliminate noise and artifacts

### 4. Export Results

- Output clean isolated text
- Optional analysis report with metrics
- Preserve original line structure if needed
- Support multiple output formats

## Features

- **Multi-format support**: HTML, JSON, console, plain text
- **Auto-detection**: Intelligent format recognition
- **Whitespace normalization**: Consistent formatting
- **Content preservation**: Maintains text meaning and structure
- **Analysis reports**: Detailed extraction metrics
- **Flexible output**: Text or structured formats

## Output

### Text Output (Default)
Clean isolated text, one item per line or consolidated blocks depending on source.

### Analysis Report
```json
{
  "source_file": "input.html",
  "format": "html",
  "total_chars": 15234,
  "total_lines": 342,
  "extracted_items": 156,
  "processing_time_ms": 234,
  "encoding": "utf-8"
}
```

## Examples

### Extract Text from HTML Log
```bash
python3 isolate_text.py workflow_logs.html --output clean_logs.txt
```

### Clean Console Output
```bash
python3 isolate_text.py console_output.txt --output text.txt --report metrics.json
```

### Extract from JSON
```bash
python3 isolate_text.py data.json --format json --output extracted.txt
```

## Use Cases

1. **Log Analysis**: Extract text from HTML/JSON logs for easier reading
2. **Data Cleaning**: Remove markup from mixed-format sources
3. **Text Mining**: Isolate meaningful content from structured data
4. **Content Extraction**: Pull text from various export formats
5. **Data Preparation**: Clean data before processing or analysis

## Integration

Use this skill in GitHub Copilot workflows:

```python
from isolate_text import TextIsolator

# Extract from file
isolator = TextIsolator("source.html")
text = isolator.extract()
print(text)

# Get analysis
isolator.extract()
report = isolator.get_report()
print(report)
```

## Performance

- **Speed**: <0.5s for typical files (< 10 MB)
- **Memory**: Efficient streaming for large files
- **Accuracy**: Format-specific parsing rules
- **Reliability**: Graceful handling of malformed input

---

**Status**: Production Ready
**Version**: 1.0.0
**Last Updated**: February 4, 2026
