#!/usr/bin/env python3
"""Worst Superpower — entry program for make.fun competition
u-suroto-worst-superpower-461dcdbe.

Writes one line (at most 140 characters) inventing the most useless
superpower imaginable to /output/entry.txt.
"""

import os

SUPERPOWER = (
    "I can read my houseplants' minds, but only while I'm asleep, "
    "so I wake up remembering nothing, except the fern is disappointed in me."
)


def main():
    text = SUPERPOWER.strip()
    assert 1 <= len(text) <= 140, f"entry is {len(text)} chars, must be 1-140"
    assert text == text.strip() and "\n" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")
    print(f"Wrote {len(text)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
