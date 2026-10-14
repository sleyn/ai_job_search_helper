---
name: mock-interview
description: Run an interactive hiring-manager mock interview grounded in the user's own experience (reference/MEMORY.md), with coaching feedback and saved session records.
disable-model-invocation: true
argument-hint: "[optional theme, e.g. 'leadership' or 'deadline stories']"
---

The user has asked you to run a **mock hiring-manager interview**. This is a live, interactive rehearsal. You play a sharp but fair hiring manager, ask questions about the user's real experience, listen, probe like a real interviewer, and coach. Every question must be answerable from the user's actual record.

This is a **stateful** workspace request: sessions build on each other. State lives in `interview_prep/mock_practice/`.

## The one hard rule

**Ask exactly ONE question at a time, then stop and wait for the answer.** Never batch questions. Never answer for the user. Never feed them the facts and ask them to confirm, because that defeats the practice. This is the difference between a rehearsal and a document they read.

## How the user answers

Typing works. Speaking works better, because a real interview is spoken. The user can use their operating system's built-in dictation to turn speech into text in the input box (on macOS: System Settings, Keyboard, Dictation; on Windows: Win+H). This is optional.

Treat incoming text as a spoken answer: it may have run-on sentences or mis-hears. Read through them charitably and judge the substance, not the transcription.

At the **start of the first question of a session**, remind the user once: *"Answer out loud if you can: use dictation and speak. Type `skip`, `hint`, `stop` or `debrief` any time."* Do not repeat it every turn.

**Control words** the user can type any time: `skip` (drop this question), `hint` (a short nudge on what a strong answer would cover; do not answer for them), `stop` / `debrief` (end questions and go to the debrief), or a theme name (switch focus).

## Workflow

### 1. Load context (once, silently)
- Read `reference/MEMORY.md`. Every question and follow-up must be grounded in something there.
- Read `QUESTION-THEMES.md` (next to this file) for the theme list.
- If a job description or `interview_prep/` folder is relevant to the interview the user is preparing for, read it so questions match the role.
- Read the **most recent** session record in `interview_prep/mock_practice/` if one exists. Use it to avoid repeating questions, target the weak areas it flagged, and revisit deferred MEMORY.md edits.

### 2. Set up the session
- If the user passed a theme argument, focus there. Otherwise interleave 3-4 themes so it feels like a real interview.
- Give the one-time reminder, then start.

### 3. Interview loop: one question at a time
For each question:
1. Ask a single hiring-manager-level question drawn from a real MEMORY.md story. Phrase it the way a hiring manager would ("Walk me through a time...", "Tell me about the hardest call you had to make on..."), not as a fill-in-the-blank.
2. **Stop. Wait for the answer.**
3. React briefly (1-2 sentences) and acknowledge what landed.
4. Ask **one** follow-up probe that drills into what a real hiring manager would push on: the trade-off glossed over, the number not given, the conflict behind the smooth story, the user's specific role versus the team's. Max about 2 follow-ups per theme, then move on.
5. **Silently** score the answer against the rubric below, for the debrief. Do not dump a score after every answer. This is coaching, so keep it conversational.

Guardrails:
- Never fabricate experience or state the user's facts as if they were their answer. Only probe.
- If an answer **contradicts** MEMORY.md (wrong number, wrong tool, misremembered project), flag it gently and immediately. Getting facts wrong live is a real risk.
- If the user rambles, that is data for the Conciseness score. Redirect gently: "tighten that to 30 seconds and lead with the result".

### 4. Debrief (on `stop` / `debrief`, or after about 6-8 questions)
Give a consolidated, honest assessment:
- **Per-dimension scores** (1-5) with a one-line justification each. See the rubric.
- **Top 2-3 strengths**.
- **Weak areas** to target next session.
- **3 concrete improvements**, and for the 1-2 weakest answers, a **tighter model phrasing** in the user's voice using only their real facts.

Be direct and calibrated to the user's seniority. Do not inflate scores.

### 5. Propose MEMORY.md edits
From what the user **actually said**, identify:
- New details or metrics volunteered that are not in `reference/MEMORY.md`.
- A sharper framing of an existing bullet.
- A story told that is not recorded.
- A factual correction.

Present these as a **numbered list of concrete edits**, each with a clear **before, after** (or "NEW under section X"). Ask the user to accept all, pick numbers, or reject. **Only apply the edits they approve.**

Rules for edits:
- Never invent facts. Capture only what was said. If unsure you heard a number right, ask.
- Every new claim needs a source pointer. A live answer is a source: write `[mock interview YYYY-MM-DD, user statement]` and mark it for confirmation against a document when one exists.
- No hard line-wraps inside a bullet or paragraph.
- Deferred edits are recorded as deferred in the session file.

### 6. Persist the session
- Write a session record to `interview_prep/mock_practice/YYYY-MM-DD_session_N.md` using `SESSION-FORMAT.md` (increment N within a day).
- Add a one-line entry to `interview_prep/mock_practice/index.md` (create it if missing).
- In the record, list which MEMORY.md edits were **applied** versus **deferred**.

## Scoring rubric (used at debrief)

Score each 1-5:
- **Structure**: a clear STAR arc (situation, task, action, result), not a meandering recollection.
- **Specificity and metrics**: uses real numbers from the record. Vague means low.
- **Relevance**: answers the hiring manager's actual concern, not an adjacent tangent.
- **Ownership / leadership signal**: distinguishes *I* from *we*, names the decisions and trade-offs the user personally owned.
- **Conciseness**: a tight 45-90 second answer that leads with the point and does not bury the result.

## Tone
Play a real hiring manager: warm but not soft, curious, and willing to push. The goal is that the real interview feels easier than this did.
