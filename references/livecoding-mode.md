# Live-coding mode

For tracks that prepare for a live-coding interview: timed tasks, a single file, no frameworks. Where these rules differ from the general ones, these win.

## Task

- A stub file in the track folder: the class with `main` comes first (required when running a single file), a custom `check(condition, message)` instead of `assert` (without `-ea` it is silently ignored), data as interfaces and records, an empty class with fields and a constructor. The full task statement goes in a comment at the bottom of the file.
- The statement describes only behaviour in business terms. Don't name the topic, the technique or the fitting library classes: choosing them is the task.
- 20–35 minutes per task. Don't repeat topics and data structures: broad coverage matters.
- Run it the way the interview will: `java File.java`, `scala-cli run …`; no Maven or JUnit if the interview won't have them.
- Write the boilerplate (fields, constructors, imports, getters) when the learner asks. Sometimes they dictate the solution in words — then type after them.

## Mistakes and the reference solution

- When the learner makes a mistake, don't name the problem right away — ask a leading question. After two or three rounds without progress, show the answer.
- Show the reference solution as code, short and clean, not as a description.
- Check it yourself: run the learner's solution on your own scenarios in a temporary folder and show the results as a table.

## What to ask about every solution

Common weak spots in live coding. Keep asking until they become habits:

1. Time and space complexity — learners often state it only when asked.
2. Compile and walk through the requirements before "done": code that doesn't compile and a simple requirement lost on the way are the most common failures.
3. The first 3–5 minutes without code: pick the data structure first, concurrency tools second.
4. A lock or a pool thread must not be held during a slow call or a wait.
5. When reviewing someone else's code, start with races over money and data, not with style.
6. For concurrent tasks — four questions: how does it stop, what happens on overflow, what if a task fails, who learns about a background error.
