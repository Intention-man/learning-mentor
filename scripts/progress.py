#!/usr/bin/env python3
"""Track progress from PLAN.md.

Blocks are `- [ ]` / `- [x]` checkboxes under `## ` headings; sections without checkboxes are skipped.
A YYYY-MM-DD date on a closed block's line counts towards "today".

    python3 progress.py PLAN.md            # print
    python3 progress.py PLAN.md --write    # also update the block between the markers in PLAN.md
"""
import argparse
import datetime
import re
import sys
from pathlib import Path

ITEM = re.compile(r"^\s*[-*] \[([ xX])\]\s+(.+)$")
DATE = re.compile(r"\s*—?\s*\d{4}-\d{2}-\d{2}\s*$")
START, END = "<!-- progress -->", "<!-- /progress -->"
WIDTH = 20


def parse(text):
    title, stages = None, []
    for line in text.splitlines():
        if line.startswith("# ") and title is None:
            title = re.sub(r"^(Plan|План):\s*", "", line[2:].strip())
        elif line.startswith("## "):
            stages.append({"name": line[3:].strip(), "items": []})
        else:
            m = ITEM.match(line)
            if m and stages:
                stages[-1]["items"].append((m.group(1) != " ", m.group(2).strip()))
    return title or "Progress", [s for s in stages if s["items"]]


def short(item):
    return re.split(r":| — ", DATE.sub("", item), maxsplit=1)[0].strip()


def render(title, stages, today):
    items = [it for s in stages for it in s["items"]]
    total, done = len(items), sum(ok for ok, _ in items)
    today_count = sum(1 for ok, text in items if ok and today in text)
    fill = round(done * WIDTH / total)
    head = f"{'█' * fill}{'░' * (WIDTH - fill)}  {round(done * 100 / total)}%  blocks: {done}/{total}"
    if today_count:
        head += f"  · today +{today_count}"

    lines = [title, head, ""]
    name_w = max(len(s["name"]) for s in stages)
    box_w = max(len(s["items"]) for s in stages)
    current_shown = False
    for s in stages:
        n, k = len(s["items"]), sum(ok for ok, _ in s["items"])
        row = f"{s['name'].ljust(name_w)}  {('■' * k + '□' * (n - k)).ljust(box_w)}  {k}/{n}"
        if k == n:
            row += "  ✓"
        elif not current_shown:
            row += "  ◀ " + short(next(text for ok, text in s["items"] if not ok))
            current_shown = True
        lines.append(row)
    if done == total:
        lines += ["", "Track complete!"]
    return "\n".join(lines)


def write(path, text, block):
    if START not in text or END not in text:
        sys.exit(f"\n{path} has no {START} and {END} markers — add them under the plan title")
    before, rest = text.split(START, 1)
    after = rest.split(END, 1)[1]
    path.write_text(f"{before}{START}\n```text\n{block}\n```\n{END}{after}", encoding="utf-8")


def main():
    ap = argparse.ArgumentParser(description="Progress bar for a learning track's PLAN.md")
    ap.add_argument("plan", type=Path)
    ap.add_argument("--write", action="store_true", help="update the block between the markers in PLAN.md")
    args = ap.parse_args()

    text = args.plan.read_text(encoding="utf-8")
    title, stages = parse(text)
    if not stages:
        sys.exit("No blocks in the plan: expected `- [ ]` checkboxes under `## ` headings")
    block = render(title, stages, datetime.date.today().isoformat())
    print(block)
    if args.write:
        write(args.plan, text, block)


if __name__ == "__main__":
    main()
