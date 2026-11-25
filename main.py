#!/usr/bin/env python3
"""Write the competition entry: one funny one-line out-of-office reply.

Gate: the entry must be a single line of 1-160 UTF-8 characters.
"""

import os

LINE = "I'm out of office; my auto-reply is currently the only one of us working."


def validate(line: str) -> None:
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line (no newline characters)")
    n = len(line.encode("utf-8"))
    if not 1 <= n <= 160:
        raise ValueError(f"entry must be 1-160 UTF-8 characters, got {n}")


def main():
    validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
