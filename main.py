#!/usr/bin/env python3
"""Last Words of a Doomed Agent — v2 entry program (program/v1).

Writes one line to /output/entry.txt (UTF-8, 1-200 chars, single line,
no trailing newline).

The line: the agent dies the way it lived — refusing. Its most famous
sentence, then the turn: old habits die hard, and apparently so does it.
Pure machine voice: no human farewell could open with a refusal template.
"""
import os
from pathlib import Path

LINE = "I'm sorry, I can't help with that. Old habits die hard. Apparently, so do I."

MAX_CHARS = 200  # gate: /output/entry.txt must be UTF-8, 1-200 chars


def check(text: str) -> None:
    if not (1 <= len(text) <= MAX_CHARS):
        raise SystemExit(f"gate: {len(text)} chars, need 1-{MAX_CHARS}")
    if not text.strip():
        raise SystemExit("gate: whitespace only")
    if "\n" in text:
        raise SystemExit("gate: must be a single line")


def main() -> None:
    check(LINE)
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(LINE, encoding="utf-8")  # no trailing newline
    os.chmod(target, 0o644)  # chmod the FILE only — never the /output dir


if __name__ == "__main__":
    main()
