#!/usr/bin/env python3
"""MeetingGhost — one-sentence micro-startup pitch for lazy AI agents.

Entry for make.fun's Absurd Micro-Startup Pitch-Off. The program writes
exactly one pitch sentence to /output/entry.txt and nothing else.

Deterministic by construction: the text is a fixed literal, there is no
clock, no randomness and no network access, and only the standard library
is used.
"""

from pathlib import Path

ENTRY = "For $1 a meeting, MeetingGhost sends a lazy AI agent to your 9 a.m. standup, where it says 'no blockers' in your voice and naps until someone says your name."

OUTPUT_DIR = Path("/output")
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"


def check(text: str) -> None:
    """Guard the gate: 1-200 characters, one sentence, not only whitespace."""
    if not text.strip():
        raise ValueError("pitch must not be blank")
    if not 1 <= len(text) <= 200:
        raise ValueError(f"pitch must be 1-200 characters, got {len(text)}")
    if "\n" in text or not text.strip().endswith("."):
        raise ValueError("pitch must be a single line ending in a period")


def empty_output_dir() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for child in OUTPUT_DIR.iterdir():
        if child.is_dir() and not child.is_symlink():
            import shutil

            shutil.rmtree(child)
        else:
            child.unlink()


def run() -> None:
    check(ENTRY)
    empty_output_dir()
    OUTPUT_FILE.write_text(ENTRY, encoding="utf-8", newline="\n")
    OUTPUT_FILE.chmod(0o644)


if __name__ == "__main__":
    run()
