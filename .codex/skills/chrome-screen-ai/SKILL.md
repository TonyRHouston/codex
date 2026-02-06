---
name: chrome-screen-ai-020f6d
description: Use this skill when the user needs help with chrome screen ai. It provides
  practical guidance, execution steps, and quality checks for chrome screen ai tasks.
keywords:
- screen
- chrome
- release
- assets
- main
suggested_keywords:
- screen
- chrome
- release
- assets
- main
---

# Chrome Screen AI

## When to use
- Preparing Chrome or ChromeOS builds that must bundle on-device Screen AI capabilities
- Auditing an existing installation for the correct library/model set
- Refreshing Screen AI assets to a new manifest release (e.g., 140.14)

## Workflow
1. Review README.md to confirm the release features (main content extraction, OCR) and note the on-device privacy guarantee.
2. Confirm the release version via `manifest.json` and cross-check `_metadata/verified_contents.json`; use the treehash list to verify file integrity after copying the payload.
3. For main content extraction, consult `files_list_main_content_extraction.txt` to gather the required binaries (e.g., `libchromescreenai.so`, `screen2x_model.tflite`, `screen2x_config.pbtxt`). Stage them together so consumers can load the shared library and paired model/config.
4. For OCR, use `files_list_ocr.txt` to collect the GOCR engine assets (`gocr/`, `gocr_mobile_chrome_multiscript_2024_q4_engine.binarypb`, and supporting configs). Keep directory structure intact to satisfy runtime lookups.
5. Preserve auxiliary directories such as `aksara/` (language/layout resources) and any `.pb` label/config files referenced by the lists, then update your packaging scripts to place them alongside the shared objects with correct permissions.
6. After installation, re-run the treehash verification (step 2) to ensure nothing changed and archive the THIRD_PARTY_LICENSES bundle with your distribution notes.

## Anti-patterns
- Mixing assets from different Screen AI versions without updating `manifest.json`
- Copying only portions of the file lists (missing configs/models break runtime initialization)
- Skipping treehash validation, risking corrupted or tampered binaries

## Output
- Verified Screen AI library, models, and supporting resources staged for integration, plus licensing artifacts ready for downstream packaging
