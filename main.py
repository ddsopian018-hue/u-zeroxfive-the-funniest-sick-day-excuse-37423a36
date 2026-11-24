"""The Funniest Sick-Day Excuse — make.fun bounty entry.

Writes one line (under 200 characters) to $MAKEFUN_OUTPUT_DIR/entry.txt:
a funny reason to call in sick, and nothing else.

The line: one vivid scene, a half-believable excuse, with the twist
landing on the last word — a neighbour's toddler has taken the author
hostage on a balcony and will only release them for biscuits.
"""

import os

LINE = (
    "Hi, can't make it in today \u2014 my neighbour's toddler locked me "
    "on the balcony in my dressing gown and now I'm negotiating my "
    "release with a four-year-old who only accepts payment in biscuits."
)


def main():
    # Gate check first: the scorer counts the file's characters, so the
    # file must hold exactly the line — no trailing newline, no extra
    # whitespace — and stay inside the 1-200 character gate.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars"
    assert LINE.count(".") == 1 and LINE.endswith("."), "must be one sentence"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "./output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
