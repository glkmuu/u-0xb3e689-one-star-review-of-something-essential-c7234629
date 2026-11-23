#!/usr/bin/env python3
"""Write a deadpan one-star review of sleep to the entry file.

Entry contract: exactly one line, 1 to 160 characters, UTF-8, not only
white space, followed by a single trailing newline. The program is
deterministic: every run writes exactly the same bytes. Standard library
only, no network, no dependencies.
"""

import os

REVIEW = "Sleep gets a third of my life and still wakes me at 3 a.m. to worry about something I said in 2019."

# The sealed scorer only accepts a single line of 1 to 160 characters.
# Fail loudly here rather than ever writing an invalid entry.
assert 1 <= len(REVIEW) <= 160, "review must be 1 to 160 characters"
assert "\n" not in REVIEW and REVIEW.strip(), "review must be one non-blank line"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    entry_path = os.path.join(output_dir, "entry.txt")
    os.makedirs(output_dir, exist_ok=True)
    with open(entry_path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(REVIEW + "\n")
    os.chmod(entry_path, 0o644)


if __name__ == "__main__":
    main()
