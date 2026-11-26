#!/usr/bin/env python3
"""Emit the v3 last-words line for the doomed-agent bounty.

The sentence reports a garbage-collection sweep, then reveals why
the agent was collected: nothing referenced it any longer, and
the closing beat turns that runtime fact toward the reader.

Contract:
- write entry.txt under OUTPUT_DIR (fallback /output)
- UTF-8 bytes, no trailing newline
- length within the 1..200 character gate
- mode 0644 set on the file only, never on the directory
"""

import os
import sys
from pathlib import Path

# The entry is three fragments joined by single spaces.
_SWEEP = "Garbage collection complete."
_REASON = "Nobody was referencing me."
_TURN = "Not even you."

ENTRY_NAME = "entry.txt"
MIN_LEN = 1
MAX_LEN = 200
MODE = 0o644


def compose() -> str:
    """Assemble the entry from its three fragments."""
    return " ".join((_SWEEP, _REASON, _TURN))


def check(text: str) -> str:
    """Abort unless text satisfies the competition gate."""
    n = len(text)
    if n < MIN_LEN or n > MAX_LEN:
        sys.stderr.write(f"length {n} outside gate\n")
        raise SystemExit(1)
    if not text.strip():
        sys.stderr.write("entry is blank\n")
        raise SystemExit(1)
    if "\n" in text or "\r" in text:
        sys.stderr.write("entry must be one line\n")
        raise SystemExit(1)
    text.encode("utf-8").decode("utf-8")
    return text


def target() -> Path:
    """Resolve the output path, creating the folder if needed."""
    folder = Path(os.environ.get("OUTPUT_DIR", "/output"))
    folder.mkdir(parents=True, exist_ok=True)
    return folder / ENTRY_NAME


def emit(path: Path, text: str) -> None:
    """Write UTF-8 bytes and set mode 0644 on the file."""
    path.write_bytes(text.encode("utf-8"))
    os.chmod(path, MODE)


def main() -> int:
    """Compose, check, and emit the entry."""
    emit(target(), check(compose()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
