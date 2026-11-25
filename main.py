#!/usr/bin/env python3
"""Funniest One-Line Out-of-Office Reply — make.fun program/v1 entry.

Writes a single original out-of-office auto-reply line to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
"""

import os
from pathlib import Path

REPLY = (
    "Out of office until Monday \u2014 my cat is watching my inbox "
    "and has already deleted three emails, with no remorse."
)


def main() -> None:
    # Self-check against the gate: 1-160 characters, one line, not blank.
    assert 1 <= len(REPLY) <= 160, f"reply is {len(REPLY)} chars"
    assert "\n" not in REPLY and REPLY.strip(), "reply must be one non-blank line"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(REPLY, encoding="utf-8")


if __name__ == "__main__":
    main()
