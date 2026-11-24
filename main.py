#!/usr/bin/env python3
"""Absurd Micro-Startup Pitch-Off entry.

Writes a single one-sentence pitch (<200 chars) to /output/entry.txt.
Stdlib only, no network.
"""

import os
from pathlib import Path

ENTRY = (
    "SubjectSnooze: lazy AI agents rewrite the same tired 'quick question?' "
    "subject line for Etsy sellers of crocheted hats for anxious dogs, "
    "charging $1 per rewritten subject that actually gets opened."
)


def main() -> None:
    line = ENTRY.strip()
    # Gate: 1 to 200 characters, not only whitespace, single line.
    assert 1 <= len(line) <= 200, f"entry length {len(line)} out of range"
    assert line == line.strip() and "\n" not in line
    out = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(line + "\n", encoding="utf-8")
    print(f"Wrote {len(line)} chars to {out}")


if __name__ == "__main__":
    main()
