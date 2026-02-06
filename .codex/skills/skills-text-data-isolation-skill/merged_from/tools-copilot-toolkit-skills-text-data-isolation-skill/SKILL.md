---
name: tools-copilot-toolkit-skills-text-data-isolation-skill
description: Extract text data from URLs, Chrome browser tabs, VS Code console, and
  file formats. Use this when asked to scrape websites, extract browser content, parse
  logs, or clean mixed-format text sources.
license: MIT
source: tools/copilot-toolkit/skills/text-data-isolation/SKILL.md
---

# Text Data Isolation Skill

Extract and isolate text data from **three independent sources**:

1. **🌐 URLs** - Web scraping and page content extraction
2. **💻 Chrome Tabs** - Browser content via extension + HTTP server  
3. **🖥️ VS Code Console** - Console output parsing and cleaning

Plus support for file formats: HTML, JSON, console output, plain text with auto-detection.

## Quick Start - Three Sources

### Source 1: URL Scraping
```bash
# Scrape a website
python3 unified_extractor.py "https://example.com" -o output.txt

# With metadata
python3 unified_extractor.py "https://example.com" -o output.txt --show-info
```

### Source 2: Chrome Tab Extraction
```bash
# Start server to receive from Chrome extension
python3 unified_extractor.py --serve

# Then use Chrome extension (load via chrome://extensions/)
# Click extraction button on any webpage
```

### Source 3: VS Code Console
```bash
# Extract from console file
python3 unified_extractor.py console.log -o output.txt

# With cleanup options
python3 unified_extractor.py console.log \
  --remove-ansi \
  --remove-timestamps \
  -o clean_output.txt
```

## Key Features

✅ **Three Data Sources** - URLs, Chrome tabs, VS Code console  
✅ **Auto-Detection** - Automatically identifies source type  
✅ **Safe Buffering** - 8KB chunks, handles 500MB+ files  
✅ **No Dependencies** - Pure Python stdlib, no external packages  
✅ **Multiple Formats** - HTML, JSON, console, plain text  
✅ **Metadata Reporting** - Extract metrics and timing info  
✅ **Flexible Cleaning** - Selective ANSI, timestamp, log level removal  

## Supported Formats

| Format | Detection | Source | Example |
|--------|-----------|--------|---------|
| **URL** | Starts with `http://`, `https://`, `www.` | Web scraping | https://example.com |
| **HTML** | Starts with `<` | Files, web responses | `<html>...</html>` |
| **JSON** | Valid JSON structure | Files, API responses | `{"key": "value"}` |
| **VS Code Console** | Timestamps, log levels, ANSI codes | Console files | `[14:23:45] [INFO] message` |
| **Plain Text** | Default fallback | Any text file | Regular text content |

## Process

### For URL Scraping

```
1. Validate URL
2. Fetch HTML via HTTP request
3. Parse HTML content
4. Remove scripts, styles, tags
5. Decode HTML entities
6. Normalize whitespace
7. Output clean text
```

### For Chrome Tab Extraction

```
1. Extension extracts page content
2. Chunks data (8KB each)
3. POSTs to local HTTP server (localhost:9999)
4. Server reconstructs full content
5. Saves to timestamped file
6. Returns success response
```

### For VS Code Console

```
1. Detect console patterns (timestamps, log levels, ANSI codes)
2. Apply requested cleaning
3. Normalize whitespace
4. Output clean text
```

## Process- Normalize whitespace
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
