# Roadmap

The main goal is for the skill to help its author learn. Publishing and growing it for others comes when there is time.

## Before going public

- [x] Separate the personal from the general: the learner profile lives in `~/.claude/learning-mentor/`, outside the repository; the live-coding weak spots are generic now.
- [x] Topic content is not part of the skill (2026-10-24): `topics/` removed; notes about a topic live in the learner's own track (`learning-mentor/TRACK_NOTES.md`). History was restarted from a single commit before publishing.
- [x] Commit email: the author is `74947150+Intention-man@users.noreply.github.com` (done before the first push).
- [x] A license: MIT.
- [x] An English README: what it is, one-command install, the first prompt.

## Vision: a framework, not a static skill

The learner configures how they learn; out of the box they get a configuration that already works well — the author's, proven on real tracks.

- [ ] Ship the author's settings as the defaults: `defaults.md` in the repo with every setting (detail, hints, plumbing, checks, new material, interface, gamification…) and a one-line *why* for each. A new learner starts from it; the settings form shows these values as "(Recommended)".
- [ ] Every rule in `SKILL.md` that is really a preference becomes a setting with the author's choice as the default, so a learner can switch it off instead of fighting the skill. Rules that make it work at all (one block at a time, the learner writes the logic, check before "done") stay fixed.
- [ ] One place that lists all settings and their values — `references/settings.md` is the start.
- [ ] Keep it simple: a new learner who answers nothing still gets a good track; the form is for changing, not for setting up.

## Later

- A dedicated slash command for settings, instead of the «настройки» / "settings" phrase.
- An HTML page with track progress — an option in the settings form.
- Short answer first, details on demand: after each comment on a learner's answer, a compact verdict, with the full explanation one click away. The Claude Code VS Code panel shows `<details>` as raw text (checked 2026-10-23), so it needs another way: an HTML page with collapsible blocks, clickable "More / Next" options, or a one-character signal such as `?` for "expand".
- A compact choice after each mentor message ("next part", "more details", "repeat in another way"), like buttons on a website, so the learner steers with a click. It must not clutter a narrow chat panel such as VS Code's.
- Day streaks and levels in the progress script — an option in the settings form.
- Package it as a Claude Code plugin so it installs via `/plugin`.
- If sharing topic packs (a stand plus experiments that worked) is ever needed — a separate content repository, not part of the skill.
- A LinkedIn article about the approach.
