# learning-mentor

A [Claude Code](https://claude.com/claude-code) skill that turns Claude into a mentor for learning a technology hands-on. Instead of writing code for you, Claude sets up a learning track: a plan of small blocks, a local stand, tasks with done criteria, code-review style questions, a cheat sheet with your own measurements — and a progress bar every time you close a block.

```text
Example track
████░░░░░░░░░░░░░░░░  18%  blocks: 3/17  · today +2

Stage 1. Basics                        ■■■□□  3/5  ◀ 1.4 Failure modes
Stage 2. A small real service          □□□    0/3
Stage 3. Under load                    □□□    0/3
```

## How it works

1. **A track.** Tell Claude what you want to learn. The first time, a clickable form lets you pick how detailed explanations are, how hints work, how solutions are checked and more — that becomes your profile. Next tracks only ask about the goal and depth, plus "as usual or customize". Say "settings" any time to change them. Claude shows the plan as a map of the topic — what is in, what is left out and why — and creates a folder with a `PLAN.md`: stages split into blocks of 20–60 minutes, each with a verifiable result. Basics first, realistic tasks towards the end if you want that depth.
2. **One part at a time.** Each block comes in small parts: short theory (anything new is explained first, with diagrams where they help), then a task in problem terms ("a feed of the last 5 events"), then a question — usually "what do you expect to see?" before you run it.
3. **Claude does the plumbing.** Installs, builds, test data and boilerplate code are on Claude, and anything slow runs in the background while you read. In code you fill in only the key lines, with an example of the same shape and the syntax you need next to them; there are also read-and-predict and find-the-bug tasks.
4. **Learning through breakage.** Every block has something to break so it becomes visible: a race, an OOM, data lost after `kill -9`. You predict the result first, then run it, and the gap is what sticks.
5. **Review.** At the end of a block, 2–3 questions as in a code review or an interview. A short verdict first, details when you ask.
6. **Your own numbers.** After each stage Claude writes `CHEATSHEET.md` from your measurements, to refresh the topic later.
7. **Progress.** Each closed block moves the progress bar.

## Install

The skill is the folder `~/.claude/skills/learning-mentor/`; Claude Code picks it up in any project.

```bash
git clone https://github.com/Intention-man/learning-mentor ~/.claude/skills/learning-mentor
```

`python3` is needed for the progress script. On macOS it comes with the Xcode Command Line Tools.

## Use

- Start a track: "I want to learn Cassandra hands-on. Be my mentor, don't write the code for me."
- Continue: "where did we stop", "done", "show progress", or call `/learning-mentor` explicitly.
- Progress by hand: `python3 ~/.claude/skills/learning-mentor/scripts/progress.py <track>/learning-mentor/PLAN.md`.
- All tracks at once: `python3 ~/.claude/skills/learning-mentor/scripts/find_tracks.py`.

## Keep it growing

After a stage or a track, ask Claude to update the skill. It runs a short retrospective, adds general lessons to `SKILL.md` and notes about the topic to the track's `learning-mentor/TRACK_NOTES.md`, shows the diff and commits. Pushing happens only after you confirm.

## Design principles

- **Simple for the learner first.** Claude does the extra work — searching the file system, reading files, checking — rather than making the learner configure paths or think through details that don't matter to them. The learner answers only what only they can answer, by clicking.
- **Simple for development too.** No registries or config files when the file system already knows the answer: a track is just a folder with a `learning-mentor/` subfolder, found by looking around, not by a list you maintain.
- **The learner writes the solution.** Claude gives plumbing as ready commands and marks with 🧠 where to think.

## What goes where

| Where | What |
|---|---|
| `<your project>/learning-mentor/` | everything about one track: `PLAN.md`, `tasks/`, `CHEATSHEET.md`, `NOTES.md`. Nothing else in your project is touched |
| `~/.claude/learning-mentor/` | your profile and the list of known tracks, shared by all projects — created only if you agree |
| `~/.claude/skills/learning-mentor/` | this repository: the method and scripts, no personal data |

## Layout

| Path | What's inside |
|---|---|
| `SKILL.md` | the method: new track, block cycle, hints, breakage, progress, style |
| `references/settings.md` | settings: the profile, per-track overrides, the clickable forms |
| `references/plan-template.md` | `PLAN.md` template for a new track |
| `references/livecoding-mode.md` | mode for live-coding interview prep |
| `scripts/progress.py` | progress bar from the `PLAN.md` checkboxes |
| `scripts/find_tracks.py` | finds your tracks anywhere in the home folder — no registry, folders can move |
| `ROADMAP.md` | plans, including what to do before going public |

## License

MIT — see [LICENSE](LICENSE).
