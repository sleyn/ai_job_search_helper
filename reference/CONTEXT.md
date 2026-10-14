---
type: Playbook
title: "Reference Materials Guide"
description: "How the user's evidence is stored, converted and summarised into MEMORY.md."
tags: [playbook, instructions]
timestamp: 2026-01-01T00:00:00Z
---
# Reference documents for job search

## Overview
Everything Claude may assert about the user comes from this workspace. `MEMORY.md` is the summary layer. `evidence/` holds the source documents.

## Directory structure
- `MEMORY.md` - Summary of career history, skills, achievements. Every claim has a source pointer.
- `index.md` - One line per document in `evidence/`: what it is and what it can verify.
- `evidence/` - Source documents. Suggested contents:
  - CV and past resumes
  - Performance reviews
  - Papers, patents, theses (with supplements)
  - Project write-ups, READMEs, portfolio pages
  - Certificates and course transcripts
  - Reference letters and recruiter notes

## Naming convention
Descriptive names with underscores, no spaces, and a year where it helps: `CV_2026.pdf`, `Performance_Review_FY2025.pdf`, `2023_Smith_Nature_Genetics.pdf`. A paper with supplements gets its own subfolder.

## Adding new evidence
1. Put the file in `evidence/`.
2. Convert PDFs and Word files to Markdown next to the original, so Claude can read them. Skip if a Markdown copy exists. Use any converter that is installed, for example:
   ```
   pip install markitdown
   markitdown file.pdf > file.md
   ```
   If no converter is available, Claude can read PDFs directly. Ask it to.
3. Add one line for the file to `index.md`.
4. Propose additions to `MEMORY.md` as a numbered list of before/after edits with source pointers. Apply only what the user approves.

## Rules for editing MEMORY.md
- Capture only what a source document or the user's own statement supports. If unsure of a number, ask before writing it.
- Source pointer on every claim.
- Keep the verb the source used. Do not upgrade "adapted" to "developed".
- No hard line breaks inside a bullet or paragraph.
- When a source document contradicts MEMORY.md, the document wins. Fix MEMORY.md, add a line to the Corrections Log, and tell the user.
