#!/usr/bin/env python3
"""Notes From a Passive-Aggressive Fridge — entry program.

Writes one passive-aggressive note from a smart fridge to /output/entry.txt.
Pure standard library, no network.
"""

import os

ENTRY = (
    "You opened me 14 times today and took nothing. "
    "The yogurt expired Tuesday \u2014 I kept it anyway. "
    "It has more commitment than you do."
)


def main():
    # Gate check: the bounty requires UTF-8 text of 1-200 characters,
    # a single line, and more than whitespace.
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
