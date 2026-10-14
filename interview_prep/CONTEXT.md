---
type: Playbook
title: "Interview Preparation Instructions"
description: "Workflow for generating targeted interview question banks and talking points for specific roles."
tags: [playbook, instructions]
timestamp: 2026-01-01T00:00:00Z
---
# Overview
Prepare targeted interview question banks and talking points for a specific role.

# Directory Structure
Each interview prep session is stored in `YYYY-MM-DD_Company_Name/`.
The job description is read from `job_descriptions/YYYY-MM-DD_Company_Name/jd.md`.
If it is not found, ask the user to provide the job description before proceeding.

# Workflow
1. Read `reference/MEMORY.md`
2. Read the job description
3. Identify the role type from the JD and `reference/MEMORY.md` target roles
4. Generate the question bank per the Output section
5. Write it to `interview_prep/YYYY-MM-DD_Company_Name/YYYY-MM-DD_Company_Name_prep.md`
6. Add the folder to `interview_prep/index.md`

# Question Categories

## Behavioral (all roles)
Generate 8-10 STAR-format questions drawn from the JD's stated values, team context and seniority level. Pre-fill the Situation and Task fields from MEMORY.md where a strong match exists. Leave Action and Result as prompts for the user to complete.

## Technical
Choose categories from the JD itself: the tools, methods, systems and domain knowledge it names. Include the questions a technical screen for this role would plausibly ask.

## Role-specific deep dives
Identify 3-5 topics from the JD that represent likely technical-screen questions. For each, provide the question, key concepts to cover and a talking point seeded from MEMORY.md.

## Questions to ask the interviewer
Generate 5 thoughtful questions tailored to the role and company context.

# Gap Flagging
If the JD requires skills not present in MEMORY.md, list them under "Preparation gaps" with a suggested one-sentence honest framing the user can use if asked.

# Output Format
Markdown:

---
## [Company]: [Role title] | Interview Prep
### Behavioral Questions
| # | Question | Situation/Task (from your experience) | Action | Result |
|---|----------|--------------------------------------|--------|--------|

### Technical Questions
[by subcategory]

### Role-specific Deep Dives
[question, concepts, your talking point]

### Questions to Ask
[numbered list]

### Preparation Gaps
[skill, honest framing]
---

# Notes
- Do not fabricate experience. Only seed talking points from MEMORY.md.
- If MEMORY.md lacks relevant detail for a question, mark the talking point `[needs your input]` rather than guessing.
- Tone: direct and confident, matching the user's seniority.
- For live practice, use the `/mock-interview` skill.
