"""Worst Superpower — make.fun entry.

Writes exactly one line to /output/entry.txt: the most useless
superpower imaginable. Standard library only.
"""

import os
import sys

ENTRY = "The power to always know exactly what time it is \u2014 in a timezone nobody lives in."
MAX_CHARS = 140


def validate(text):
    """Return an error string, or None if the entry is valid."""
    if not text or not text.strip():
        return "entry is empty or whitespace-only"
    if len(text) > MAX_CHARS:
        return "entry exceeds 140 characters"
    if "\n" in text or "\r" in text:
        return "entry must be a single line"
    for ch in text:
        if ord(ch) < 0x20:
            return "entry contains a control character"
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        return "entry is not UTF-8 encodable"
    return None


def main():
    err = validate(ENTRY)
    if err:
        print("invalid entry: " + err, file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
