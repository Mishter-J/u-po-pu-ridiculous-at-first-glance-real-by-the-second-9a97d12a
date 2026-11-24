#!/usr/bin/env python3
"""Ridiculous at First Glance, Real by the Second - make.fun entry.

Writes one sentence (185 chars, under the 200-character cap) pitching a
bizarre startup idea that sounds absurd until you realise it would
actually sell, to /output/entry.txt.

Deterministic: the same fixed sentence every run. No randomness, no
network, no input besides this file.
"""

import os

ENTRY = (
    "Dear judge, our actors apologize for you: $30 buys a stranger who "
    "takes the blame and cries on cue, so you keep the friendship \u2014 "
    "your last words are \"thank you, I'll take it from here.\""
)


def validate_entry(text: str) -> None:
    """Gate self-check (RULES.txt): UTF-8, 1-200 chars, non-blank."""
    try:
        text.encode("utf-8")
    except UnicodeEncodeError as exc:
        raise ValueError(f"entry is not valid UTF-8: {exc}") from exc
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 chars, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be blank")


def main() -> None:
    validate_entry(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
