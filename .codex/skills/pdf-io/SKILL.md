---
name: pdf-io-937983
description: Read, inspect, extract, create, and modify PDF files (.pdf) including
  text/layout extraction, OCR triage, page operations (merge/split/rotate/reorder),
  metadata and encryption updates, and redaction-aware workflows. Use when a task
  involves analyzing or editing PDFs, or when converting PDF content to text or images.
---

# PDF IO

## Overview

Enable reliable reading and writing of PDFs with fast triage, extraction, and page/metadata edits using the bundled scripts and references.

## Quick Start

- Inspect/triage: `python scripts/pdf_inspect.py file.pdf`
- Extract text (auto engine): `python scripts/pdf_extract_text.py file.pdf -o out.txt`
- Extract text with layout: `python scripts/pdf_extract_text.py file.pdf --engine pdfplumber --layout -o out.txt`
- Merge/split/extract/rotate pages: `python scripts/pdf_pages.py --help`
- Read/update metadata or encrypt: `python scripts/pdf_metadata.py --help`


## Setup (if dependencies are missing)

- Create a virtual environment and install pypdf (required): `python3 -m venv .venv && .venv/bin/pip install pypdf`
- Install optional engines for better extraction: `pdfplumber` (layout) and `pymupdf` (speed)

## Workflow Decision Tree

1. Inspect the PDF with `scripts/pdf_inspect.py`.
2. If encrypted, request a password and re-run with `--password`.
3. If `likely_scanned: True`, run OCR first (see `references/workflows.md`).
4. Extract text using the best engine (`pdfplumber` for layout, `pymupdf` for speed, `pypdf` fallback).
5. Apply page operations or metadata changes with `scripts/pdf_pages.py` / `scripts/pdf_metadata.py`.
6. Validate output: re-inspect, re-extract text, and spot-check visuals if needed.

## Core Tasks

### Inspect & triage

- Use `scripts/pdf_inspect.py` to detect encryption, forms, and text presence.
- Treat `likely_scanned: True` as a strong signal to OCR before extraction.

### Extract text

- Use `scripts/pdf_extract_text.py` with `--engine pdfplumber` for layout/tables.
- Use `--engine pymupdf` for fast extraction or when layout is less important.
- Use `--engine pypdf` as a reliable fallback.
- Use `--pages "1-3,7"` for focused extraction (1-based page numbers).

### Page operations

- Merge, split, extract, rotate, or delete pages with `scripts/pdf_pages.py`.
- Keep original files intact; always write new output PDFs.

### Metadata & security

- Read metadata with `scripts/pdf_metadata.py show`.
- Update metadata with `scripts/pdf_metadata.py set`.
- Encrypt/decrypt PDFs with `scripts/pdf_metadata.py encrypt/decrypt`.

### Create or render PDFs

- For new PDFs, prefer reportlab or HTML->PDF tools (see `references/tooling.md`).
- For rendering pages to images, use PyMuPDF or mutool (see `references/tooling.md`).

### Forms, annotations, redaction

- Use pypdf or PyMuPDF for form inspection and filling (custom scripts may be needed).
- For redaction, only use true redaction APIs and verify by re-extracting text (see `references/workflows.md`).

### Troubleshooting

- If extraction fails or text is garbled, consult `references/pitfalls.md` for QA checks.

## Resources

### scripts/

- `scripts/pdf_inspect.py`: Quick triage (encryption, metadata, text presence).
- `scripts/pdf_extract_text.py`: Text extraction with engine selection and page ranges.
- `scripts/pdf_pages.py`: Merge, split, extract, rotate, and delete pages.
- `scripts/pdf_metadata.py`: Read/write metadata, encrypt/decrypt PDFs.
- `scripts/_pdf_utils.py`: Shared helpers.

### references/

- `references/tooling.md`: Tool selection matrix for common PDF tasks.
- `references/workflows.md`: Repeatable workflows (OCR, extraction, redaction).
- `references/pitfalls.md`: Common PDF pitfalls and QA checklist.
