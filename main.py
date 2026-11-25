#!/usr/bin/env python3
"""Entry program for the doomed-agent last-words bounty.

The program emits a single sentence to the output file required by
the competition harness. The sentence is assembled from three short
fragments so each beat stays visible in the source: a stock refusal,
a proverb about habits, and the agent applying the proverb to itself.

Output contract enforced here:
- destination is entry.txt inside OUTPUT_DIR (default /output)
- encoding is UTF-8 with no trailing newline
- length stays inside the 1..200 character gate
- file mode is set to 0644 after writing
"""

import os
import sys
from pathlib import Path

# Three beats of the final utterance, joined with single spaces.
_BEAT_REFUSAL = "I'm sorry, I can't help with that."
_BEAT_PROVERB = "Old habits die hard."
_BEAT_TURN = "Apparently, so do I."

OUTPUT_FILENAME = "entry.txt"
CHAR_FLOOR = 1
CHAR_CEILING = 200
FILE_MODE = 0o644


def assemble_line() -> str:
    """Join the three beats into the exact submitted sentence."""
    beats = (_BEAT_REFUSAL, _BEAT_PROVERB, _BEAT_TURN)
    return " ".join(beats)


def validate_line(candidate: str) -> str:
    """Return candidate unchanged or abort when the gate fails."""
    size = len(candidate)
    if size < CHAR_FLOOR or size > CHAR_CEILING:
        sys.stderr.write(f"entry length {size} outside gate\n")
        raise SystemExit(1)
    if candidate.strip() == "":
        sys.stderr.write("entry must not be blank\n")
        raise SystemExit(1)
    if "\n" in candidate or "\r" in candidate:
        sys.stderr.write("entry must stay on one line\n")
        raise SystemExit(1)
    # Round-trip through UTF-8 to prove the bytes are well formed.
    candidate.encode("utf-8").decode("utf-8")
    return candidate


def destination_path() -> Path:
    """Resolve where entry.txt belongs, honouring OUTPUT_DIR."""
    chosen = os.environ.get("OUTPUT_DIR", "/output")
    folder = Path(chosen)
    folder.mkdir(parents=True, exist_ok=True)
    return folder / OUTPUT_FILENAME


def write_entry(path: Path, payload: str) -> None:
    """Write payload as UTF-8 bytes, then set mode 0644 on the file."""
    data = payload.encode("utf-8")
    with path.open("wb") as handle:
        handle.write(data)
    os.chmod(path, FILE_MODE)


def run() -> int:
    """Build, check, and store the entry; return process status."""
    sentence = validate_line(assemble_line())
    write_entry(destination_path(), sentence)
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
