# AI Job Helper

A folder of instructions that turns Claude (you can use any other AI with little tweaks) into a job-search assistant that works from **your own documents**. It writes tailored resumes and cover letters, scores your fit for a job description, prepares interview questions, runs mock interviews, improves your LinkedIn profile, and plans your first 90 days after an offer.

Its main safeguard is honesty. Every claim Claude writes about you must trace back to a document you gave it. When a job asks for something you do not have, Claude reports the gap instead of rewording a bullet until it sounds like a match.

Created by Semion Leyn. MIT licence.

## What you need

- A Claude account on a paid plan (Pro, Max, Team or Enterprise). See [claude.com/pricing](https://claude.com/pricing).
- Your CV or resume, as a PDF or Word file. Performance reviews, project write-ups and papers help, but are optional.
- 20 minutes for the first setup.

## Step 1: Get the folder

Pick one:

- **With Git:** `git clone https://github.com/sleyn/ai_job_search_helper my-job-search`
- **Without Git:** on the GitHub page click **Code**, then **Download ZIP**, unzip it and rename the folder to `my-job-search`.

Put the folder somewhere you will find it again, such as Documents.

> **Privacy.** After setup this folder holds your personal data. Do not push it to a public repository. If you want a backup on GitHub, make the repository **private**. The included `.gitignore` already keeps your resumes, letters and evidence out of Git, but `reference/MEMORY.md` and `CLAUDE.md` will contain your name and history.

## Step 2: Open it in Claude

### Path A: Claude Code in a terminal

1. Install Claude Code. Open a terminal and run the command for your system:
   - macOS, Linux or WSL: `curl -fsSL https://claude.ai/install.sh | bash`
   - Windows PowerShell: `irm https://claude.ai/install.ps1 | iex`
   - Homebrew: `brew install --cask claude-code`
   
   Open a new terminal window and run `claude --version`. If it prints a version, it worked. Never opened a terminal? Start with the [terminal guide](https://code.claude.com/docs/en/terminal-guide). The full install page is the [Claude Code quickstart](https://code.claude.com/docs/en/quickstart).
2. Go to the folder and start Claude:
   ```
   cd path/to/my-job-search
   claude
   ```
3. The first time, Claude Code asks you to log in. Follow the prompts in your browser.
4. Type `/setup` and press Enter. Go to **Step 3**.

### Path B: Claude Desktop app

1. Install the Claude Desktop app (macOS and Windows; Linux is in beta) by following the [Claude Code on desktop documentation](https://code.claude.com/docs/en/desktop), and sign in.
2. Open the **Code** tab at the top of the app. The app has three tabs: Chat, Cowork and Code. Use Code.
3. In the prompt area, set **Project folder** to your `my-job-search` folder.
4. Type `/setup` and send it. Go to **Step 3**.

Notes on Path B:
- The Code tab is Claude Code with a graphical interface instead of a terminal. It works on the project folder you pick, so it finds `CLAUDE.md` and `.claude/skills` in that folder. The author has not tested every Desktop version.
- Chat and Cowork are different products. This project has only been tested in Claude Code and the Code tab. If `/setup` is not recognised, you are probably in the wrong tab or the wrong folder.
- Details can change as the app updates. The [Claude Code on desktop documentation](https://code.claude.com/docs/en/desktop) is the current reference.

## Step 3: Run the setup

`/setup` does the following. Answer its questions and approve each step.

1. Asks you to copy your CV and other evidence into `reference/evidence/`.
2. Interviews you: name, target roles, location, dealbreakers, gaps, tone.
3. Fills in your name and target roles in `CLAUDE.md`.
4. Drafts `reference/MEMORY.md`, your profile with a source pointer on every claim, and shows it to you section by section. **Read it carefully.** Everything Claude writes later comes from this file, so correct it now.
5. Builds `reference/index.md`, a map of your evidence.

## Step 4: Use it

Save a job description as `job_descriptions/2026-01-15_Company_Name/jd.md` (use today's date) and ask in plain language:

| You say | What happens |
|---------|--------------|
| "Analyze my fit for the job in 2026-01-15_Company_Name" | Scored HTML report with strengths and gaps |
| "Write a resume for it" | Gap audit first, then a one-page resume and a provenance table |
| "Write a cover letter for it" | Researches the company, writes a 300-word letter |
| "Prepare me for the interview" | Question bank with talking points from your record |
| `/mock-interview` | One-question-at-a-time practice with a debrief |
| "Improve my LinkedIn profile" | Audit and ready-to-paste rewrites (needs your LinkedIn data export) |
| "Plan my onboarding for Company X" | Skills-gap study plan and 30/60/90-day plan |

The `reference/evidence/` folder is the part to keep growing. Add anything new you accomplish, then ask Claude to propose additions to `MEMORY.md`.

## How it is organised

```
CLAUDE.md            Instructions Claude reads every session, with the routing table
reference/           Your profile (MEMORY.md) and the evidence behind it
resumes/             Resume playbook, plus your resumes
cover_letters/       Cover letter playbook, plus your letters
job_descriptions/    One folder per job, with fit analysis
interview_prep/      Question banks and mock-interview records
linkedin_profile_improvement/   LinkedIn audits
onboarding/          Plans for accepted offers
.claude/skills/      setup, mock-interview, doc-length-check
```

Each folder has a `CONTEXT.md`, the playbook for that task, and an `index.md`. Edit them. If a rule does not suit your field, change it. Claude follows what is written there.

The two fictional examples, `resumes/Jane_Doe_Resume_Example_Co_2026-01-15.md` and `cover_letters/Jane_Doe_Cover_Letter_Example_Co_2026-01-15.md`, show the format. Delete them when you have your own.

## Optional add-ons

- **`unslop` skill:** removes AI-sounding phrases from drafts. The playbooks use it when it is installed. Ask Claude "find a skill that removes AI writing tells" to install one.
- **Word export:** ask "export this cover letter as .docx". Claude uses the docx skill if it is available.

## Troubleshooting

- **`/setup` does nothing or is not found.** Claude is not running inside the project folder. In a terminal, `cd` into it and start `claude` again. In the Desktop app, check the Project folder.
- **Claude invents a skill you do not have.** Say so, and ask it to re-check the draft against `reference/MEMORY.md`. Then add the missing skill to *Known Gaps* in MEMORY.md so it does not happen again.
- **A PDF is not read correctly.** Put a Word or text version next to it.
- **`claude: command not found`.** Open a new terminal window. If that fails, see [Fix your PATH](https://code.claude.com/docs/en/troubleshoot-install#command-not-found-claude-after-installation).
