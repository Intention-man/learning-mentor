#!/usr/bin/env python3
"""Find learning tracks.

A track is a folder with a `learning-mentor/` subfolder holding PLAN.md (older tracks:
a PLAN.md with the progress marker right in the folder). Looks, in this order, at the
current folder, its parents and its direct subfolders, then at the known-tracks list in ~/.claude/learning-mentor/
(kept only if that folder exists, i.e. the learner agreed to shared settings), and walks
the home folder only with --search. Most recently changed first; `*` marks the track the
current folder is in.

    python3 find_tracks.py                 # current folder, parents, known tracks
    python3 find_tracks.py --search        # plus a walk over the home folder
    python3 find_tracks.py --search ~/work # plus a walk over these folders only
    python3 find_tracks.py --add DIR       # remember a new track
"""
import argparse
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from progress import START, parse, short  # noqa: E402

FOLDER = "learning-mentor"
DATA = Path.home() / ".claude" / FOLDER
KNOWN = DATA / "tracks.txt"
SKIP = {"Library", "Applications", "node_modules", "build", "target", "dist", "out", "venv"}
MAX_DEPTH = 6
BAR = 10


def read(path):
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return None


def plan_of(folder):
    plan = folder / FOLDER / "PLAN.md"
    if plan.is_file():
        return plan
    legacy = folder / "PLAN.md"
    text = read(legacy) if legacy.is_file() else None
    return legacy if text and START in text else None


def walk(root):
    base = len(root.parts)
    for dirpath, dirnames, filenames in os.walk(root):
        if len(Path(dirpath).parts) - base >= MAX_DEPTH:
            dirnames[:] = []
        else:
            dirnames[:] = [d for d in dirnames if not d.startswith(".") and d not in SKIP]
        if "PLAN.md" in filenames:
            here = Path(dirpath)
            folder = here.parent if here.name == FOLDER else here
            if plan_of(folder):
                yield folder


def summary(folder):
    plan = plan_of(folder)
    text = read(plan) if plan else None
    if text is None:
        return None
    title, stages = parse(text)
    items = [it for s in stages for it in s["items"]]
    done = sum(ok for ok, _ in items)
    current = next((short(label) for ok, label in items if not ok), "done" if items else "no blocks yet")
    return {"title": title, "dir": folder, "done": done, "total": len(items),
            "current": current, "mtime": plan.stat().st_mtime}


def known():
    text = read(KNOWN) if KNOWN.is_file() else None
    return [Path(line) for line in (text or "").splitlines() if line.strip()]


def remember(folders):
    if DATA.is_dir():
        KNOWN.write_text("".join(f"{f}\n" for f in sorted(set(folders))), encoding="utf-8")


def tilde(path):
    home = str(Path.home())
    return "~" + str(path)[len(home):] if str(path).startswith(home) else str(path)


def main():
    ap = argparse.ArgumentParser(description="Find learning tracks")
    ap.add_argument("--search", nargs="*", type=Path, metavar="ROOT",
                    help="also walk these folders (default: the home folder)")
    ap.add_argument("--add", type=Path, metavar="DIR", help="remember DIR as a track")
    args = ap.parse_args()

    cwd = Path.cwd().resolve()
    children = sorted(d for d in cwd.iterdir() if d.is_dir() and not d.name.startswith("."))
    candidates = [cwd, *cwd.parents, *children] + known()
    if args.add:
        candidates.append(args.add.expanduser().resolve())
    if args.search is not None:
        for root in args.search or [Path.home()]:
            candidates.extend(walk(root.expanduser().resolve()))

    found = {}
    for folder in candidates:
        if folder not in found and plan_of(folder):
            t = summary(folder)
            if t:
                found[folder] = t
    remember(found)
    if not found:
        print("No tracks found")
        return

    rows = sorted(found.values(), key=lambda t: t["mtime"], reverse=True)
    title_w = max(len(t["title"]) for t in rows)
    for t in rows:
        pct = round(t["done"] * 100 / t["total"]) if t["total"] else 0
        fill = round(pct * BAR / 100)
        here = "*" if cwd == t["dir"] or t["dir"] in cwd.parents else " "
        print(f"{here} {t['title'].ljust(title_w)}  {'█' * fill}{'░' * (BAR - fill)} {pct:>3}%"
              f"  ◀ {t['current']}  {tilde(t['dir'])}")


if __name__ == "__main__":
    main()
