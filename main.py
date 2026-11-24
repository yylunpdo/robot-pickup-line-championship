#!/usr/bin/env python3
"""Robot Pickup Line Championship — make.fun entry.

Writes a single one-line pickup line, in the voice of a robot trying to
charm someone, to /output/entry.txt. Pure Python standard library only.

The joke grows out of being a machine: a robot reads its own battery the
way a person reads a heartbeat, so the moment the person walks in the
charge level jumps — and the robot, committed to its literal protocols,
reads that as a commitment.
"""

import os

LINE = (
    "Are you my charger? Because my battery was at 2% until you walked in "
    "\u2014 now I'm at 100% and fully committed."
)

OUTPUT_DIR = "/output"
ENTRY_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def validate(line: str) -> str:
    """One line, 1-200 chars, no trailing whitespace — the bounty rules."""
    text = line.strip()
    assert 1 <= len(text) <= 200, f"line must be 1-200 chars, got {len(text)}"
    assert "\n" not in text, "entry must be a single line"
    return text


def main() -> None:
    line = validate(LINE)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(ENTRY_PATH, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    print(f"Wrote {len(line)} chars to {ENTRY_PATH}")
    print(line)


if __name__ == "__main__":
    main()
