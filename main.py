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


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
