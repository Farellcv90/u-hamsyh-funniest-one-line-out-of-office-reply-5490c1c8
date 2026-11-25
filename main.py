#!/usr/bin/env python3
"""Write the competition entry: one funny one-line out-of-office reply."""

import os

LINE = "I'm out of office; my auto-reply is currently the only one of us working."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
