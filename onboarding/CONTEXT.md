---
type: Playbook
title: "Onboarding Preparation Instructions"
description: "Workflow for planning pre-start preparation and the first 90 days for a role where the user has accepted an offer."
tags: [playbook, instructions]
timestamp: 2026-01-01T00:00:00Z
---
# Overview
Prepare the user for a new role after an offer is accepted: a skills-gap study plan, a week-1 plan and a 30/60/90-day plan.
Offer evaluation and negotiation are out of scope.

# Directory Structure
Each onboarding package is stored in `onboarding/YYYY-MM-DD_Company_Name/`, where the date is the day the package was created.
Use underscores, never spaces or hyphens between name parts.

# Inputs
Read in this order:
1. `reference/MEMORY.md`. Open `reference/index.md` for deeper evidence.
2. The job description in `job_descriptions/YYYY-MM-DD_Company_Name/`. Look for `jd.md`, then `jd.txt`, then any `*jd*` file. If none exists, ask the user to provide it before proceeding.
3. Every other file in that job description folder (broader JD, match analysis, notes). It may hold team, tooling or scope detail the JD lacks.
4. The matching `interview_prep/` folder, for what the user learned about the team, manager and stack.
5. Anything the user supplies: offer letter, onboarding docs, directories or web sites.
6. Web search only for facts outside this project (company, product, competitors). Never use it to check what the user's own documents say.

# Workflow
1. Read the inputs above.
2. Identify the role type and the sector. Apply the Sector Adjustments below.
3. Ask the user for the start date and any known first-week logistics. Do not invent dates.
4. Write the gap analysis file.
5. Write the onboarding plan file.
6. Run the `unslop` skill over both files, if installed.
7. Propose updates to `reference/MEMORY.md` (see Memory Feedback). Never edit it without approval.
8. Add the package to `onboarding/index.md`.

# Gap Analysis
File: `onboarding/YYYY-MM-DD_Company_Name/YYYY-MM-DD_Company_Name_gap_analysis.md`

Rate each JD requirement Strong, Partial or Gap.
- Cite the evidence for every rating: `reference/MEMORY.md` or a document in `reference/evidence/`.
- Never rate Strong without a citation.
- Apply the verb-accuracy rule: describe benchmarking, tuning or adapting as exactly that, not as "developed".
- Mark anything MEMORY.md cannot support as [needs your input].

For each Partial or Gap, give a learning action, a time estimate and the week the skill is first needed.
Cap the prioritized study list at 5-7 items so it fits before the start date.

Output format:

---
## [Company] – [Role title] | Gap Analysis
### Requirement Ratings
| Requirement | Rating | Evidence | First needed |
|-------------|--------|----------|--------------|

### Study Plan (top 5-7)
| # | Skill | Learning action | Time estimate | Needed by |
|---|-------|-----------------|---------------|-----------|
---

# Onboarding Plan
File: `onboarding/YYYY-MM-DD_Company_Name/YYYY-MM-DD_Company_Name_onboarding.md`

Tag every item in the 30/60/90 plan **Confirmed** (the manager or recruiter said it) or **Assumed** (inferred from the JD). Do not present assumptions as expectations.

Sections:
- **Pre-start checklist**: study plan pointer, company and domain research, tools to set up in advance.
- **People map**: manager, team, stakeholders, with what the user already knows from interview prep.
- **Week 1**: orientation goals, access to request, people to meet.
- **30/60/90 plan**: per period, goals, deliverables, learning and relationships.
- **Early wins**: ideas that use the user's evidenced strengths, each tied to a citation.
- **Questions to ask in week 1**: expectations, success metrics, tooling, data access, team norms.
- **Validate in week 1**: the Assumed items from the plan, rewritten as questions for the manager.

Keep the file to about two pages.

# Sector Adjustments
Apply the ones that fit the employer. Examples:
- **Academic or research:** PI expectations and lab culture, grant and funding cycle, ethics and data-use approvals, compute allocation, authorship norms, who owns the code.
- **Regulated (healthcare, finance, government):** compliance regimes, validation and change-control rules, audit trails, documentation requirements, on-call expectations.
- **Startup or product company:** roadmap, cross-functional stakeholders, sprint cadence, cloud-cost guardrails, IP policy, quality process.

# Memory Feedback
After the plan is written, list proposed additions to `reference/MEMORY.md` for the user to approve: new target skills, role context, or goals worth keeping for future resumes. Present them as a list and wait for approval.

# Notes
- Do not fabricate experience, dates, team details or expectations.
- Tone should be direct and confident, matching the user's seniority level.
- Offer terms (salary, equity, title) are not part of this package.
