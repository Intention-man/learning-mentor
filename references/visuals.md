# Visuals

A diagram beats a paragraph when there are layers, queues, flows or numbers to compare. Learners new to a topic can't hold five components and their order in their head from text alone.

## When to draw

| Situation | Visual |
|---|---|
| layers of a system (client → pool → server → disk) | a box diagram |
| the order of steps in one request or operation | a numbered flow or a timeline |
| a race or two actors interleaving | a table with a time column and one column per actor |
| numbers from the learner's runs | a bar chart in text, or a table |
| a big architecture with many parts | an HTML page (see below) |

## In the chat

- Plain ASCII or box-drawing characters in a code block, so the layout survives in a monospace font.
- Number the arrows or steps when order matters: `(1)`, `(2)`, `(3)`. A learner reading an unnumbered diagram may take a sequence for a choice between branches.
- Don't draw a fork for things that happen one after another. If both steps always happen, draw them in sequence.
- Keep a diagram to what the current question needs; split a big one into two small ones.
- A bar chart in text: one row per variant, bars of `█` scaled to the largest value, the number next to the bar.

For example, a numbered flow:

```
client ──(1) request──▶ service ──(2) query──▶ database
client ◀─(4) response── service ◀─(3) rows──── database
```

## HTML pages

For a big architecture, a long comparison or anything that needs collapsible details, publish an HTML page as an Artifact instead of drawing in the chat. Load the `artifact-design` skill before writing the page and `artifact-diagramming` for diagrams in it. Check the learner's `interface` setting first: some learners want everything in the chat.

Some chat panels don't render HTML at all: Claude Code's VS Code panel shows `<details>` and other tags as text. There, keep diagrams in ASCII.
