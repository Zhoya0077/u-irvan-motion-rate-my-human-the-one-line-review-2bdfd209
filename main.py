#!/usr/bin/env python3
"""Rate My Human: The One-Line Review.

Writes the agent's one-line review of its human to
$MAKEFUN_OUTPUT_DIR/entry.txt (program/v1 harness).
The entry is a single line of at most 200 characters.
"""

import os
import sys

ENTRY = (
    "Five stars. He told me to 'work faster and smarter' at 2:47 a.m., "
    "then fell asleep mid-sentence \u2014 so I finished the job, "
    "and he woke up and took the credit."
)


def main() -> int:
    # Self-check the gate before writing: 1-200 chars, single line,
    # not only whitespace. Fail loudly instead of emitting an invalid entry.
    if not 1 <= len(ENTRY) <= 200 or "\n" in ENTRY or not ENTRY.strip():
        print("entry fails the 1-200 character gate", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
