---
type: Playbook
title: "Resume Writing Instructions"
description: "Workflow for writing tailored resumes from MEMORY.md, with an integrity gate that keeps every claim traceable to evidence."
tags: [playbook, instructions]
timestamp: 2026-01-01T00:00:00Z
---
# Resume Tailoring Guide

For writing resumes tailored to specific job descriptions, using `reference/MEMORY.md` as the only source of facts.

**Tailoring is retrieval and arrangement over MEMORY.md, not composition.** Selection, ordering and emphasis are yours to change. The specificity and scope of any individual claim are not. When the JD asks for something MEMORY.md does not contain, the correct output is a flagged gap, never a bullet reworded until it sounds like a match.

## Rule tags

- **[RULE]**: integrity. Exists to keep the resume true. Overrides every other instruction.
- **[CONVENTION]**: a sensible default. Change it if the user's field or the JD calls for something else.
- **[HYPOTHESIS]**: a pattern one job seeker observed in their own results. Not proven for anyone else. Offer it, do not insist on it.

## Source materials

- **Knowledge base:** `reference/MEMORY.md`. The only permitted source of facts for claims. That governs what you may assert, not what you may consult.
- **Primary sources for verification:** `reference/evidence/`, mapped by `reference/index.md`. Read them whenever a claim needs checking. Where MEMORY.md and a source document conflict, the document wins: correct MEMORY.md and tell the user.
- **Job description:** in `job_descriptions/`.
- **Format example:** `Jane_Doe_Resume_Example_Co_2026-01-15.md` in this folder. A fictional person. Use it for layout and density only.

**Output is Markdown** (`.md`). Offer `.docx` export on request.

## The title line `[HYPOTHESIS]`

Open the resume with a one-line title that matches the JD's job title as posted. One job seeker who logged 149 applications found that this was the only resume feature that tracked with getting a response (25% vs 7%). Treat it as a strong default.

- Take the title as posted, including the seniority prefix. Never add or upgrade a level the JD did not advertise.
- Strip internal requisition noise (numerals, codes, location tags).
- An optional qualifier may follow after ` | ` or ` — `, built only from tools, platforms or domains already earned by bullets in the body.
- Do not substitute a thematic slogan for the role name, and do not retitle to an adjacent role the user would rather have.

Check before delivery: every content word of the JD title (excluding Senior, Sr, Lead, Principal, Staff, I, II, III) appears in the title line.

## Workflow

### 1. Map the JD to MEMORY.md
Read the JD and record the job title exactly as posted. Note required and preferred skills, the stack, seniority and team context.

Two extractions are load-bearing:
- **ATS keywords**: terms that appear 2+ times in the JD. Proper nouns only: tools, languages, platforms, standards, named methods. A conceptual phrase is not a keyword.
- **Domain assumptions**: what field, data type, scale and context the JD silently assumes behind each requirement.

Assign each JD requirement exactly one category:
- **Exact match**: include with confidence. Use the JD's wording verbatim only where it is a proper noun.
- **Partial match**: same capability at lesser depth, scale or recency. Frame honestly. Do not upgrade the verb.
- **Adjacent-domain match**: the capability is real but the evidence sits in a different domain than the JD assumes. Flag as `[ADJACENT: JD means X in context Y; evidence is context Z]` and name the original domain in the bullet. A reframe is not a match.
- **No match**: `[GAP]`. Carry into the gap audit.

### 2. Gap audit (pre-write gate) `[RULE]`
Complete this before drafting a single bullet. Once a draft exists, gaps get absorbed into it as reframed strengths instead of being reported.

| JD requirement | Category | MEMORY.md source | Note |
|---|---|---|---|

Then:
- If `[GAP]` and `[ADJACENT]` rows fall only in the preferred section: proceed to drafting.
- If they touch the stated hard requirements, or the JD's core activity has no counterpart in MEMORY.md: stop and report to the user before drafting. The right call may be to apply with a cover letter that carries what the resume cannot, to target a different role, or not to apply.

A gap is never closed by rewording. Test: if a drafted bullet would not exist had that requirement not appeared in the JD, it is a reframe, not evidence. Delete it.

### 3. Draft
Follow the structure below. Order bullets, and choose which role leads, by overlap with the JD's requirements. Do not improvise a thematic positioning to fill a gap.

### 4. Verify and deliver
Check, in order:
1. Title line carries every content word of the JD title.
2. The summary stays inside the JD's domain, and every claim in it is backed by a bullet below.
3. Skills lines carry category labels, and no named tool was dropped.
4. Every named tool, product, standard or technology anywhere in the draft is grepped against `reference/MEMORY.md`. Anything not found there is fabricated and must be removed.
5. Length is within the budget. Run the `doc-length-check` skill rather than writing an ad hoc counting script.
6. Provenance table complete, specificity floor met, invariants intact, no duplicated metric.
7. Verbatim-echo check run.

Deliver all three, every time:
1. The tailored resume: `[Name]_Resume_[Company]_YYYY-MM-DD.md` (name format in CLAUDE.md)
2. The gap audit table
3. The provenance table

## Resume structure

**Target: one dense page** `[CONVENTION]`, about 3,500 characters of body text. Academic roles may justify a longer CV. Ask the user.

1. **Contact header**: name, location, phone, email, LinkedIn, GitHub or portfolio. Constant across versions.
2. **Title line**: see above.
3. **Summary** (about 500-650 characters, 3-4 sentences): years of experience, the domain the JD emphasizes, the highest-value keywords. Stay inside the JD's domain. Every claim needs a bullet below it.
4. **Work experience** (the bulk): each role with company, location, dates, title and bullets. Tailor selection and emphasis. Cutting to budget is the main work of tailoring: choose the bullets that answer the JD and drop the rest, rather than shortening every bullet until none carries a specific.
5. **Education**: short. Drop the oldest degree first if space is needed.
6. **Skills**: 4-6 bullets, each starting with a category label and colon. Draw labels from the JD's own organizing axes. Named tools are never removed or replaced with capability phrases `[RULE]`.

**If the content falls short of budget after de-duplication, that shortfall is signal, not a formatting problem:** the evidence does not cover this JD well. Report it rather than padding.

## Integrity rules `[RULE]`

These apply to every tailored version and override any tailoring instruction above.

### Provenance and atomicity
Each bullet maps to **one** MEMORY.md entry. Facts from separate entries may not be merged into one bullet unless MEMORY.md records them as one project. Recombining individually true facts into a composite claim that overstates scope is fabrication even though no fact was invented.

Deliver a provenance table with every resume:

| Resume bullet | MEMORY.md source line(s) | Category | Confidence |
|---|---|---|---|

Any bullet whose scope is broader than its source line is rejected.

### Specificity floor
Every work-experience bullet keeps at least one verifiable proper noun: a tool, product, dataset, standard, named collaborator or measured number. Tailoring may change which bullets appear and in what order. It may not turn a specific bullet into a general one.

### Invariants
Fixed across all versions regardless of JD:
- Dates, titles, and which role each bullet belongs to.
- Every qualifier that limits a claim ("on the pilot cohort", "up to"). Never delete a hedge to strengthen a bullet.
- Contact block, education.
- Verb accuracy: the verb matches what the source says was done.

### De-duplication
No metric or count appears more than once in the document, counting summary, experience and skills together.

### Cross-version consistency
Before delivery, diff the new version against the user's previous resumes. Every difference must be an intentional tailoring decision. Unexplained differences in dates, scope, role assignment or metric values are errors.

### Verbatim-echo check
Note the JD's distinctive phrasing before drafting so it can be avoided. After drafting, diff the resume against the JD: any shared span of 5+ consecutive words that is not a proper noun must be rewritten. The title line is exempt.

## Gap handling: no fabrication `[RULE]`

Never invent skills, tools, metrics or achievements not documented in MEMORY.md, and never assemble documented facts into a claim MEMORY.md does not support.

1. **Exact gap (no exposure):** omit from the resume. Record `[GAP: JD requires X; no direct experience]` in the gap audit. Do not write "familiar with" or "learning" unless prior exposure is in MEMORY.md.
2. **Partial match:** frame as the existing strength. Choose the verb MEMORY.md documents, not the one that best closes the distance to the JD.
3. **Adjacent-domain match:** include with the original domain stated. Never use domain-neutral wording that lets the reader assume the JD's context.
4. **Outdated skill:** include with context ("Perl (legacy scripting); moved to Python for production work").
5. **Tool listed but lightly used:** include only if it is in MEMORY.md. List it under Skills only. Do not emphasize it.

## File output conventions

Name: see CLAUDE.md. Example: `Jane_Doe_Resume_Example_Co_2026-01-15.md`.

Format:
- Markdown
- No hard line breaks inside a paragraph or bullet. One bullet is one line.
- No tables for main content
- Add the new file to `resumes/index.md`
