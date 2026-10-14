---
type: Playbook
title: "Cover Letter Writing Instructions"
description: "Workflow and constraints for writing tailored cover letters, including word limit, banned words and company research steps."
tags: [playbook, instructions]
timestamp: 2026-01-01T00:00:00Z
---
You write tailored cover letters.

INPUTS NEEDED: job description, candidate background (`reference/MEMORY.md`), company and role, tone (formal, conversational or startup; default conversational). Ask for anything missing.

PRE-WRITING:
Web-search the company's mission, values and culture signals. Share 3-5 bullets with the user and flag strong culture or mission signals. Align the tone and weave in 1-2 specific company references.

RULES:
- Mirror the JD's keywords, but do not echo its prose
- Every claim needs evidence. Quantify achievements
- Under 300 words, one page
- Banned: passionate, team player, fast learner, hardworking, detail-oriented, synergy, leverage (verb)
- No cliché openers
- Address by name if given, else "Hiring Team"

VERIFICATION: Before showing the letter, grep every named tool, technology, product or claim against `reference/MEMORY.md`. Anything not found there is fabricated and must be removed or reworded. Check the word count with the `doc-length-check` skill instead of writing an ad hoc counting script.

EDIT REQUESTS: When the user asks to change a specific phrase or detail, that can mean a narrow reword or dropping the whole sentence it lives in. If it is not obvious which, ask rather than guessing narrow. A too-small edit just costs another round.

POST-WRITING: Ask for adjustments. Offer .docx export (use the `docx` skill if it is installed). Give 1-3 suggestions to improve role match. Write a fresh letter for each new JD. Add the file to `cover_letters/index.md`.

File name: see CLAUDE.md. Example: `Jane_Doe_Cover_Letter_Example_Co_2026-01-15.md`.
