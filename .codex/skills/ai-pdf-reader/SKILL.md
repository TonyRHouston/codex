---
name: ai-pdf-reader-3cf50a
description: Use this skill when the user needs help with ai pdf reader. It provides
  practical guidance, execution steps, and quality checks for ai pdf reader tasks.
keywords:
- pdfs
- markdown
- text
- pdf
- extract
suggested_keywords:
- pdfs
- markdown
- text
- pdf
- extract
---

# AI PDF Reader

## When to use
- You need to extract text or images from PDFs for RAG ingestion
- Converting scanned PDFs with OCR to searchable markdown
- Preprocessing manuals, specs, or research PDFs before indexing

## Workflow
1. Feed `AI-pdf-reader` with a PDF path or base64 payload. It runs OCR (when needed), extracts text and images, and normalizes output to markdown snippets.
2. Cache intermediate artifacts to speed repeat runs and store mapping from pages to extracted markdown for easy citation.
3. Optionally run a summarization pass to produce short abstracts per document or per page to accelerate retrieval.

## Anti-patterns
- Sending extremely large PDFs without chunking; split into page ranges before ingestion
- Treating image-only scans as text; ensure OCR is enabled for scanned sources

## Output
- Markdown fragments, page-level metadata, base64-encoded images, and optional summaries ready for RAG or archival ingestion
