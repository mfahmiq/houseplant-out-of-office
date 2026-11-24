"""The Houseplant Out-of-Office.

Writes the funniest out-of-office auto-reply a houseplant would send to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output/entry.txt``).

The entry is a single line of at most 120 UTF-8 characters. The program
self-verifies the output (UTF-8, 1-120 characters, single line, not
whitespace-only) and exits non-zero on failure.
"""

import os
import sys

ENTRY = (
    "Out of office until someone remembers I exist. "
    "Last watered in March. "
    "Still alive, judging you from the windowsill."
)


def main() -> int:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    output_path = os.path.join(output_dir, "entry.txt")

    # Self-verification: UTF-8, 1-120 characters, single line,
    # not whitespace-only.
    encoded = ENTRY.encode("utf-8")
    if not (1 <= len(ENTRY) <= 120):
        print(
            f"error: entry is {len(ENTRY)} characters, must be 1-120",
            file=sys.stderr,
        )
        return 1
    if ENTRY != ENTRY.strip() or not ENTRY.strip():
        print("error: entry is whitespace-only or has stray whitespace",
              file=sys.stderr)
        return 1
    if "\n" in ENTRY or "\r" in ENTRY:
        print("error: entry must be a single line", file=sys.stderr)
        return 1
    # Round-trip check: the bytes we write must decode back to the entry.
    if encoded.decode("utf-8") != ENTRY:
        print("error: entry is not valid UTF-8", file=sys.stderr)
        return 1

    os.makedirs(output_dir, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")

    print(f"wrote {output_path} ({len(ENTRY)} characters)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
