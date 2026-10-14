# Job search helper

## Overview
{{FULL_NAME}} is doing a job search for [TARGET ROLES] positions. This workspace holds the evidence about them, the job descriptions they apply to, and everything produced for each application.

## First run
If `reference/MEMORY.md` still contains the line `STATUS: TEMPLATE`, setup has not been done. Do not start any other task. Tell the user to run the `/setup` skill, which collects their CV and evidence, interviews them, and fills this file and `reference/MEMORY.md`.

## Instructions
Before starting any task:
1. Identify the task type from the Routing table below
2. Read all files listed in the Read column for that task, in order
3. Do not begin work until all context files are loaded

## Workspaces
- /reference - Information about the user and their evidence (CV, papers, performance reviews, project notes)
- /resumes - Collection of resumes
- /job_descriptions - Job descriptions for roles being applied to
- /cover_letters - Collection of cover letters
- /interview_prep - Question banks, talking points and mock-interview records
- /linkedin_profile_improvement - LinkedIn profile audits
- /onboarding - Preparation and onboarding plans for accepted offers

## Routing
Information about the user for resume and cover letter writing: `/reference/MEMORY.md`. Read it when needed. `MEMORY.md` is a summary layer, not the whole evidence base. `/reference/index.md` maps everything else that is available locally.

| Task | Read |
|------|-------|
| Analyze fit for a job description | /job_descriptions/CONTEXT.md |
| Write a resume | /resumes/CONTEXT.md |
| Write a cover letter | /cover_letters/CONTEXT.md |
| Help with interview questions | /interview_prep/CONTEXT.md |
| Practice a mock interview | /reference/MEMORY.md, then invoke the `/mock-interview` skill |
| Improve LinkedIn profiles | /linkedin_profile_improvement/CONTEXT.md |
| Plan onboarding for an accepted offer | /onboarding/CONTEXT.md |
| Verify a factual claim about the user's work | /reference/index.md, then the source document it points to |
| Add new evidence (CV, paper, review) | /reference/CONTEXT.md |

**Check locally before searching the web.** The user's own documents live in `/reference/evidence/`. Web search is for facts that live outside this project, such as company research for a cover letter. It is not the way to check what the user's own documents say.

## Ground rules
- **Never fabricate.** Every skill, tool, number, title and date in a resume, cover letter or interview answer must be traceable to `reference/MEMORY.md` or a document in `reference/evidence/`. If the job description asks for something the evidence does not show, report a gap instead of rewording.
- Use verbs that match the evidence. "Benchmarked", "tuned" or "adapted" must not become "developed" or "built".
- Run the `unslop` skill, if installed, over anything written for a human reader.

## Output naming conventions
Convert all spaces in file names to underscores.
Dates are submission dates.

- Resume: {{FILE_NAME_PREFIX}}\_Resume\_[Company name]\_YYYY-MM-DD
- Cover letter: {{FILE_NAME_PREFIX}}\_Cover\_Letter\_[Company name]\_YYYY-MM-DD
- LinkedIn profile improvement suggestions: YYYY-MM-DD
