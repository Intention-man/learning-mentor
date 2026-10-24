# PLAN.md template

The plan lives at `<track folder>/learning-mentor/PLAN.md`, next to `tasks/` and `CHEATSHEET.md`. Keep only the sections you need, and write the plan in the learner's language. The progress script counts `- [ ]` / `- [x]` checkboxes under `## ` headings, so don't use checkboxes in other sections ("Later", "Track rules") — they would be counted as blocks.

~~~markdown
# Plan: <topic>

<!-- progress -->
<!-- /progress -->

Goal: <work with X in production / interview at Y, date>. Budget: <hours per week or deadline>.
Stand: <language, build tool, how and where it is installed, constraints — e.g. no Docker>.

## Track rules

| Setting | Value |
|---|---|
| goal | <from the settings form> |
| depth | <…> |
| block | <~45 min> |
| <any profile key that differs for this track> | <…> |

- <free-form rules specific to this track: who writes CHEATSHEET.md, "no Google",
  which idioms to watch in reviews…>

## Stage 1. <name>

- [ ] 1.1 <block>: <what we do, one line>
- [ ] 1.2 <block>: <…>

## Stage 2. <name>

- [ ] 2.1 <…>

## Later

- <detours to come back to — plain bullets, no checkboxes>

## Out of scope

| What | Why |
|---|---|
~~~

A closed block looks like this: `- [x] 1.1 Stand: install the tools — 2026-10-21`. The script shows the label before the colon as the current step, so keep it short.

For interview prep, add a "What they check" section with a source (the company's page, what the recruiter said): the plan is built from it, not from a textbook. Order stages by how likely the topic is to come up, so that the most important ones are done if the interview comes early.
