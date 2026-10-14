---
type: Playbook
title: "Job Description Analysis Instructions"
description: "Workflow for analyzing job fit, scoring rubric and HTML output format for job description match reports."
tags: [playbook, instructions]
timestamp: 2026-01-01T00:00:00Z
---
# Overview
Analyze fit between the user and a job description.

# Directory Structure
Each job description is stored in `YYYY-MM-DD_Company_Name/jd.md`. The date is the day the JD was saved.

If only a `jd.txt` is found, convert it to `jd.md` before proceeding:
1. Read the `jd.txt` content
2. Extract the role title (usually the first line) and a one-sentence description
3. Write `jd.md` with frontmatter prepended and the original content unchanged:
   ```yaml
   ---
   type: Job Description
   title: "<Role Title> - <Company>"
   description: "<one-sentence role summary>"
   tags: [job-description, <company-lowercase-hyphenated>, <YYYY-MM-DD>]
   timestamp: <YYYY-MM-DD>T00:00:00Z
   ---
   ```
4. Delete the original `jd.txt`
5. Add the JD folder to `index.md`

If neither `jd.md` nor `jd.txt` exists, ask the user to paste the job description.

# Workflow
1. Read `reference/MEMORY.md`
2. Read the job description
3. Analyze fit and produce the output below

# Scoring Rubric
Score out of 100, weighted:
- Core skills match: 40 pts
- Domain or industry fit: 20 pts
- Tooling and stack overlap: 20 pts
- Seniority and scope alignment: 20 pts

Every point must be backed by evidence in MEMORY.md. Where the evidence is missing, score it as a gap. Do not score generously.

# Output
HTML file written to `YYYY-MM-DD_Company_Name/YYYY-MM-DD_Company_Name_match.html`
Use `job_descriptions/_template.html` as the visual template.

Sections:
- Score: n/100
- Competency fit breakdown
- Keyword match
- Strengths to highlight
- Critical gaps and resume suggestions
- Bottom line: apply, apply only if unusually well matched, or skip, with one sentence of reasoning

After writing the HTML file, append a row `YYYY-MM-DD_Company_Name,n` to `job_descriptions/job_scores.csv` (create it with header `Name,Score` if it does not exist). Add the folder to `job_descriptions/index.md`.

# Optional: learn from your own results
Keep a simple log of where you applied and what happened (no reply, screen, interview, offer). After 30-50 applications, ask Claude to compare scores and role families against outcomes. That tells you which kinds of roles actually respond to you. The score is a flag, not a block. The user decides whether to apply.
