---
name: setup
description: First-run setup for the job search helper. Collects the user's CV and evidence, interviews them about target roles, then fills CLAUDE.md placeholders and builds reference/MEMORY.md and reference/index.md with a source pointer on every claim. Use when reference/MEMORY.md still says STATUS: TEMPLATE, or when the user says "set me up".
disable-model-invocation: true
---

You are setting up this workspace for a new user. Work in the order below. Ask one group of questions at a time and wait for the answers. Never invent a fact about the user.

## Step 0: Check state
Read `CLAUDE.md` and `reference/MEMORY.md`.
- If `reference/MEMORY.md` does not contain `STATUS: TEMPLATE`, setup was already done. Ask whether the user wants to redo it or add evidence instead. Redoing overwrites MEMORY.md, so confirm first.
- Otherwise continue.

## Step 1: Collect evidence
Tell the user to copy these into `reference/evidence/` (create subfolders if useful), and wait until they say they are done:
- Their current CV and any past resumes (required)
- Performance reviews, recommendation letters, awards
- Papers, patents, theses, portfolio pages, project READMEs
- Certificates and course transcripts

Then list `reference/evidence/`. For each PDF or Word file with no Markdown copy next to it, read the original directly or convert it (see `reference/CONTEXT.md`). If a file cannot be read, say so and ask for another format. Do not skip it silently.

## Step 2: Interview the user
Ask these in two or three short groups, not all at once:
1. Full name as it should appear on resumes. Location. Work mode (remote, hybrid, onsite) and relocation. Work authorization if relevant.
2. Target roles (2-4 role families), target sectors, seniority, and dealbreakers.
3. Which accomplishments they are proudest of that the documents may not show. Anything in the CV that is outdated or overstated.
4. Known gaps: skills job descriptions often ask for that they do not have.
5. Preferred tone for cover letters (formal, conversational, startup).

## Step 3: Fill CLAUDE.md placeholders
Replace in `CLAUDE.md`:
- `{{FULL_NAME}}` with the full name
- `[TARGET ROLES]` with the role families, e.g. "data analyst, analytics engineer or BI developer"
- `{{FILE_NAME_PREFIX}}` with the name using underscores, e.g. `Jane_Doe`

Show the user the resulting Overview and naming lines.

## Step 4: Build reference/MEMORY.md
Use the existing `reference/MEMORY.md` structure. Remove the `STATUS: TEMPLATE` line and the setup banner. Replace the title, description, tags and the example placeholders. Rules, all from the file's own "How to read and write this file" section:
- **Every claim carries a source pointer** `[evidence/<file>, <section>]`. A claim from the interview only is marked `[user statement, YYYY-MM-DD]`. A claim with no source is marked `[needs source]`, and is left out of anything written later.
- **Verb accuracy.** Use the verb the source supports. If the source says "used", "ran", "adapted" or "tuned", do not write "developed" or "built". Where the CV is vague about the user's role, ask rather than choose the stronger verb.
- **Keep qualifiers** ("pilot", "up to", "in testing").
- **No hard line breaks** inside a bullet or paragraph.
- Fill Target Roles, Known Gaps and Honest Framings from the interview.
- Where the CV and another document disagree, trust the document with more detail, say so to the user, and log it in the Corrections Log.

Show the user the draft in sections. Ask for corrections. Write the file only when they approve.

## Step 5: Build reference/index.md
Add one line per document in `reference/evidence/`: `* [evidence/<file>](evidence/<file>) - what it is, and what it can verify.`

## Step 6: Report
Summarise in a few lines: what was filled, which items are marked `[needs source]` or `[GAP]`, and what the user should do next. Suggest, in order:
1. Save a job description in `job_descriptions/YYYY-MM-DD_Company_Name/jd.md` and ask "analyze my fit for this job".
2. Ask for a resume, then a cover letter, for the same job.
3. Later: `/mock-interview`, LinkedIn improvement, onboarding plan.

Remind the user: the workspace now holds personal data. If they put it under Git, keep the repository private.
