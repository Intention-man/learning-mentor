# Settings

How the learner wants to learn, set by clicking rather than by writing paragraphs. Two levels:

| Level | Where | What |
|---|---|---|
| Profile — how this learner usually learns | `~/.claude/learning-mentor/profile.md`, only if the learner agreed (see "Consent"). Personal, outside the skill's repository | detail, hints, plumbing, checks, interface, gamification, language, search |
| Track — what is special about one topic | the settings table at the top of "Track rules" in the track's `PLAN.md` | goal, deadline, depth, block length, and any profile key this topic needs differently |

The track wins over the profile; the profile wins over the defaults below. `PLAN.md` holds only the keys that differ from the profile plus goal, depth and block length — so a priority topic can be "in depth, interview questions" while a side topic is "brief, no questions", and neither leaks into the other.

## Consent

Writing outside the learner's project needs their consent. The first time settings are saved and `~/.claude/learning-mentor/` doesn't exist, ask one clickable question:

- "Keep my settings for all projects" (Recommended) — create `~/.claude/learning-mentor/` with `profile.md`; the known-tracks list `tracks.txt` is kept there too, so tracks are found from any folder.
- "Only in this project" — create nothing outside the project. All answers go to the track's `PLAN.md` and apply only there; write `shared settings: declined` into its settings table, so this track never asks again. A next track will ask again.

## When

| Moment | Do |
|---|---|
| Any session on an existing track (found by `scripts/find_tracks.py`, see "Finding the track" in `SKILL.md`) | Show one line with the effective settings and "to change them, say «настройки» / settings". No questions |
| Existing track, but no `profile.md` (a fresh clone on a new laptop, a friend's copy) | Form 1 only, to create `profile.md`; the track's own settings stay as they are in `PLAN.md` |
| New track, no `profile.md` yet | The consent question, then the full form (both forms below). Style answers go to `profile.md` (or to `PLAN.md` if declined), goal/depth/block length to `PLAN.md` |
| New track, `profile.md` exists | One line with the effective settings, then the short form: goal, depth, block length, and "As usual (<one-line summary of the profile>)" vs "Customize for this track". "Customize" opens form 1 with profile values as defaults; differing answers go to `PLAN.md` |
| The learner says «настройки» / "settings" / «давай перенастроим» | Show the effective settings, ask what to change, then ask where: "Only this track" (→ `PLAN.md`) or "Make it my default" (→ `profile.md`) |

Skip any question already answered in the prompt. Answered means stated in so many words. "As usual / Customize" is never inferred: "like the last track" or "take into account what worked" is context for the plan, not a choice — still ask it.

## Forms

Use the `AskUserQuestion` tool: up to 4 questions per form, 2–4 options each. It adds an "Other" free-text field to every question automatically, so don't add your own. Ask in the learner's language; put the current value first and mark it "(Recommended)".

**Form 1 — style (profile)**

| Key | Question | Options, default first |
|---|---|---|
| detail | How detailed should explanations be? | Short, with tables · With analogies and examples · In depth, with internals |
| hints | How should hints work? | Only on request · A leading question when I make a mistake · Show the reference solution after 2–3 attempts |
| plumbing | How should plumbing steps come? | The mentor does them, I think only at 🧠 · I do everything myself · Everything ready except the logic |
| checks | How should solutions be checked? | Questions as in a code review · Questions as in an interview · Just a check, no questions |

**Form 2 — format**

| Key | Question | Options, default first |
|---|---|---|
| goal | What is the goal? (track) | Work with it in production · An interview (when?) · Refresh what I forgot · Curiosity |
| depth | How far should the tasks go? (track) | Up to middle/senior-level tasks at the end · Working level: the core topics with practice · Basics and an overview |
| interface | Which interface? (profile) | Terminal only · An HTML page with progress · Decide later |
| gamification | How much gamification? (profile) | Progress bar · Plus day streaks and levels · None |

Block length (track) goes into the short form; in the full form ask it in the chat if it matters, otherwise use about 45 minutes.

Some options are not built yet (the HTML page, streaks and levels — see `ROADMAP.md`). If the learner picks one, record it, say plainly that it isn't available yet, and use the closest thing that works now.

If `AskUserQuestion` is not available, ask the same questions in the chat as a numbered list with lettered options, so the learner can answer like "1a 2b 3a".

## Formats

`~/.claude/learning-mentor/profile.md`:

```markdown
# Learner profile

| Key | Value |
|---|---|
| search | allowed (may walk the home folder to find tracks, read-only) / denied / not asked |
| language | Russian |
| detail | Short, with tables |
| hints | Only on request |
| plumbing | The mentor does them, I think only at 🧠 |
| checks | Questions as in a code review |
| interface | Terminal only |
| gamification | Progress bar |
| new_material | Explain first, then ask |
```

`new_material` is not in the forms, to keep them short: the default is "Explain first, then ask"; set "Let me look it up in the docs" only if the learner says so.

Settings in `learning-mentor/PLAN.md`, at the top of "Track rules" (a table, not checkboxes, so the progress script ignores it):

```markdown
## Track rules

| Setting | Value |
|---|---|
| goal | Work with it in production |
| depth | Priority topic, in depth |
| block | ~45 min |
| checks | Questions as in an interview |

- <free-form rules specific to this track>
```

An older track may have only free-form "Track rules" without the table: read the settings from the bullets and fill in the table the next time settings change.
