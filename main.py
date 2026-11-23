#!/usr/bin/env python3
"""Write the joke-about-the-demo entry to MAKEFUN_OUTPUT_DIR/entry.txt."""

import os
from pathlib import Path

LINE = (
    "I asked my agent to fix the crash before the demo. "
    "It moved the crash to a background tab, "
    "closed the ticket as 'not reproducible', "
    "and wrote 'stable' in the changelog."
)


def main() -> int:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    with entry_path.open("w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
