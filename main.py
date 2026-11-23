#!/usr/bin/env python3
"""Write one warm line to /output/entry.txt.

The entry is a single line of at most 200 characters about a small good
thing that happened today: the neighbour's cat, which has ignored the
narrator for a whole year, chose this morning to climb onto their lap
and fall asleep mid-purr. The warmth is the sudden trust after a year
of indifference; the surprise is the timing and the mid-purr sleep;
the concrete detail is 6 a.m. The program is deterministic: it always
writes the same bytes. It uses only the Python 3.13 standard library,
no network, no randomness.
"""

import os

LINE = (
    "My neighbour's cat, who has ignored me for a whole year, chose "
    "today at 6 a.m. to climb onto my lap and fall asleep mid-purr."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars, must be 1-200"
    assert text.strip(), "line must not be only whitespace"
    # Gate: exactly one line — no embedded newline or control characters.
    assert "\n" not in text and "\r" not in text, "line must be a single line"
    assert all(ord(ch) >= 32 or ch in "\t" for ch in text), (
        "line must not contain control characters"
    )
    assert text == text.strip(), "line must have no leading/trailing space"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    # Second refinement: verify the write by reading it back as UTF-8
    # and confirming the file holds exactly the line plus one newline.
    with open(path, "r", encoding="utf-8") as f:
        assert f.read() == text + "\n", "written entry.txt does not round-trip"


if __name__ == "__main__":
    main()
