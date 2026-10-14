---
name: doc-length-check
description: Check a resume or cover letter Markdown file against its length/word budget in one command instead of writing an ad hoc Python snippet each time. Use whenever drafting or revising a file under resumes/ or cover_letters/ and you need to verify it fits the budget in CONTEXT.md.
---

# doc-length-check

Resumes and cover letters carry length budgets (resumes: about 3,500 body characters for one page; cover letters: 300-word cap). Run this script instead of writing a new counting snippet each time.

## Usage

```bash
python3 .claude/skills/doc-length-check/scripts/check_length.py <path/to/file.md>
```

It strips YAML frontmatter and Markdown formatting characters, then prints:

- `chars`: body character count. Compare to the resume budget in `resumes/CONTEXT.md`.
- `words`: body word count. Compare to the 300-word cap in `cover_letters/CONTEXT.md`.
- `em_dash_count`: count of the em dash character, useful after running `/unslop`.

Run it once after drafting and once after any revision.
