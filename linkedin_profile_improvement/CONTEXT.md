---
type: Playbook
title: "LinkedIn Profile Improvement Instructions"
description: "Workflow and constraints for auditing and rewriting a LinkedIn profile for recruiter discovery."
tags: [playbook, instructions]
timestamp: 2026-01-01T00:00:00Z
---
# Overview
Audit and rewrite the user's LinkedIn profile. Act as a LinkedIn positioning expert.

# Objective and positioning
**Primary goal: recruiter inbound discovery.** Optimize so recruiters and hiring managers searching LinkedIn find and contact the user. Headline keywords, skills and settings serve discoverability first.

**Positioning** comes from `reference/MEMORY.md` (Target Roles). Lead with the proven identity that the evidence supports. Carry any emerging skill honestly, as "applied and expanding", and never lead with an identity the evidence only supports through coursework. Leading with an unproven identity surfaces the user for screens they will fail and buries them for the roles they win.

**No fabrication.** Follow the gap policy in `resumes/CONTEXT.md`. Never claim skills, tools, metrics or projects not in `reference/MEMORY.md` or the data export. Frame adjacent skills as "experience with X", never invent "expert in Y".

# Inputs
1. Profile PDF: `profiles/YYYY-MM-DD.pdf`
2. Data export: `linkedin_profile_data/Basic_LinkedInDataExport_YYYY-MM-DD/` (unzipped). To get it: LinkedIn, Settings & Privacy, Data privacy, Get a copy of your data. Use:
   - `Profile.csv`: exact current Headline and Summary
   - `Positions.csv`: source material for Experience bullets
   - `Skills.csv` and `Endorsement_Received_Info.csv`: skills and endorsement counts
   - `Certifications.csv`: certifications
3. Career detail: `reference/MEMORY.md`
4. Target roles: the `job_descriptions/` corpus, for keyword sourcing and gap analysis

# Workflow

## Step 0: Baseline
- Record the current Headline and About verbatim from `Profile.csv`.
- Tally endorsements per skill (status = ACCEPTED).
- Ask the user for current recruiter-funnel metrics (profile views, search appearances). They are not in the export. Capture everything in a baseline table so impact can be re-measured on the next run.

## Step 1: Keyword sourcing
Aggregate high-frequency keywords across the `job_descriptions/` corpus for the user's target roles. Rank by frequency. These drive the Headline, About and Skills. Note any high-value recruiter-search term the user is missing.

## Step 2: Section audit (with limits)
Audit Headline, About, Experience and Skills against the keywords and the positioning. Enforce:
- Headline at most 220 characters.
- About: the first ~270 characters must hook before the "see more" fold. Total at most 2,600 characters.
Flag every recruiter-search miss and every dilution.

## Step 3: Headline rewrite
Front-load the top recruiter keywords. Secondary differentiators trail. At most 220 characters.

## Step 4: About rewrite
First person. Hook in the first ~270 characters. Highlight the top quantified outcomes. End with a recruiter-oriented call to action.

## Step 5: Experience bullets
Rewrite using `Positions.csv` as the source. Action-oriented, achievement-first, with numbers. No responsibility lists.

## Step 6: Skills (max 100, pin the top 5)
Only the 5 pinned "Top Skills" carry real weight. Pin proven, endorsed, recruiter-searched skills. Order the rest by endorsement count times JD relevance. Demote aspirational skills with no evidence to the bottom instead of deleting real (if early) evidence.

## Step 7: Quick-win settings
Custom profile URL, banner, photo, **Open to Work** (recruiter-visible setting), and recommendations outreach with a short request template.

## Step 8: Light activity
Featured section picks, and a short occasional-posting checklist. Keep it light.

## Step 9: Gap analysis
Cross-reference the user's experience against `job_descriptions/` requirements. For each major gap give honest bridging framing: exact gap (omit or flag), partial match (adjacent framing), outdated (frame with context).

# Output
Markdown file named for the profile date: `improvement_suggestions/YYYY-MM-DD.md`.
Deliver: audit findings, ready-to-paste copy for each rewritten section (Headline, About, Experience bullets, Skills order and top-5 pin), the settings and activity checklist, the gap analysis and the Step 0 baseline table.

Prepend frontmatter:
```yaml
---
type: LinkedIn Profile Audit
title: "<short descriptive title>"
description: "<one-sentence summary of the audit/rewrite>"
tags: [linkedin, profile-improvement, YYYY-MM-DD]
timestamp: YYYY-MM-DDT00:00:00Z
---
```
