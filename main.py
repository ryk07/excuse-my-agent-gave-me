"""The Excuse My Agent Gave Me — entry program (stdlib only).

Writes one original line: the excuse an AI agent hands its human after
missing a deadline. The line is a fixed, hand-written string — no network,
no randomness, no external files — so both graded runs produce identical
output.
"""

import os
from pathlib import Path

LINE = (
    "Sorry \u2014 my context window filled up at 11:58, so I archived "
    "your deadline and confidently rescheduled it to a Tuesday "
    "that doesn't exist."
)


def main() -> None:
    if not 1 <= len(LINE) <= 200:
        raise ValueError(f"line is {len(LINE)} chars, must be 1-200")
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
