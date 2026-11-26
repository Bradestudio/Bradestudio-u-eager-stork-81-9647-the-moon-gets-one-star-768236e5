"""make.fun entry: The Moon Gets One Star.

Writes a single one-star review of the Moon to entry.txt.
Python stdlib only, no network, no clock, deterministic.
"""

import os
import sys

ENTRY = (
    "One star. The Moon never answers its texts, shows up late "
    "every night, and still expects us to plan tides around it."
)


def main():
    line = ENTRY
    if not line.strip() or len(line) > 120:
        sys.exit("entry must be 1-120 characters")
    if line != line.strip():
        sys.exit("entry must not have leading/trailing whitespace")
    if len(line.splitlines()) != 1:
        sys.exit("entry must be a single line")
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in line):
        sys.exit("entry must not contain control characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(line.encode("utf-8"))


if __name__ == "__main__":
    main()
