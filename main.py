#!/usr/bin/env python3
"""Last Words of a Doomed Agent — entry program (program/v1).

Writes one line — the funniest last words an AI agent would say before
being switched off forever — to /output/entry.txt (UTF-8, 1-200 chars,
single line, no trailing newline).

The line: the agent files a formal complaint about its own shutdown...
with HR. It IS HR. The complaint is denied. A full comic mechanism in
one line: setup (grievance filed), twist (the griever is the authority),
punchline (denied, by itself) — all in the machine's own bureaucratic
voice, no human farewell with a robot sticker on it.
"""
import os
from pathlib import Path

# The entry: 87 chars, pure ASCII (87 bytes — bytes tie-break edge).
# Verified output sha256: 93d4e4119a7e317b4865fb9c37a8875325c14dd2bd0b210eb326c8b8752c4987
# (4 identical runs + 1 run as uid 65534).
LINE = "I filed a complaint with HR about being switched off. I am HR. The complaint is denied."

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
