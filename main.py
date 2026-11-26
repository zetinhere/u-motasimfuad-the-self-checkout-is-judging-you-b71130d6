#!/usr/bin/env python3
"""The Self-Checkout Is Judging You - make.fun entry.

Writes one funny line in the voice of a smug, judgmental self-checkout
machine to /output/entry.txt. Deterministic: no network, no input, no
randomness - the same line every run.

The line: the till has counted the basket (twelve yoghurts, nothing else)
and run the numbers on what will actually happen to them. The arithmetic
is the joke's engine - four eaten, six binned, two denied - and it adds
up to exactly twelve, because the machine counted.
"""

import os

LINE = "Twelve yoghurts. I ran the numbers. You will eat four, bin six, and pretend the other two never happened."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"line must be 1-200 chars, got {len(LINE)}"
    assert LINE.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    # Round-trip assert: what we wrote must be exactly what the judge reads.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE + "\n", "round-trip mismatch in entry.txt"
    assert 1 <= len(written.strip()) <= 200, "entry must be 1-200 chars"


if __name__ == "__main__":
    main()
