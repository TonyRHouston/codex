---
name: thinkpdf-6df01e
description: Use this skill when the user needs help with thinkpdf. It provides practical
  guidance, execution steps, and quality checks for thinkpdf tasks.
keywords:
- thinkpdf
- gui
- pdfs
- mcp
- markdown
suggested_keywords:
- thinkpdf
- gui
- pdfs
- mcp
- markdown
---

# thinkpdf

## When to use
- Extracting text, tables, or structure from PDFs for RAG pipelines or LLM context
- Batch converting folders of PDFs with progress reporting and caching
- Wiring PDF utilities into IDEs via the built-in MCP server or launching a lightweight GUI

## Workflow
1. Install the package (`pip install thinkpdf`) and add extras when required:
   - `thinkpdf[docling]` for higher-fidelity table extraction
   - `thinkpdf[gui]` to launch the desktop UI with `thinkpdf-gui`
2. Use the CLI (`thinkpdf`) for conversions:
   - Single file: `thinkpdf input.pdf [-o output.md]`
   - Batch: `thinkpdf folder --batch [--workers N]` with optional caching (`--no-cache` disables) and OCR toggles (`--ocr off|auto|force`)
   - Setup MCP config: `thinkpdf setup` prints the JSON block for Cursor/Antigravity
3. Programmatic usage: `from thinkpdf import convert; convert("document.pdf")` returns markdown. Adjust `thinkpdf.core.models.Options` for OCR mode or asset export as needed.
4. For GUI workflows, install the `[gui]` extra then run `thinkpdf-gui` to open the Qt interface (reads/writes markdown alongside assets).
5. To integrate with MCP-compatible editors, add the provided block to `mcp.json` so tools become available:
   - `read_pdf` streams PDF content
   - `convert_pdf` saves markdown outputs
   - `get_document_info` returns metadata
6. When running the CLI, include `--export-images` to collect embedded images into an `_assets` folder and `--password` for encrypted PDFs. Enable `-v/--verbose` to stream progress callbacks.
7. Review cached results stored by `CacheManager()` (default unless `--no-cache`) to avoid redundant conversions; clear cache manually if source PDFs change.

## Anti-patterns
- Forgetting to install the `[docling]` extra when table fidelity matters
- Running `--batch` on a single file path (requires a directory)
- Skipping MCP setup after printing the JSON block, leading to missing IDE tools
- Leaving cache enabled when source PDFs change (run with `--no-cache` or purge cache first)

## Output
- Markdown files (and optional assets) generated from PDFs, accessible via CLI, GUI, library calls, or MCP tools ready for downstream RAG ingestion
