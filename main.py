#!/usr/bin/env python3
"""The Agent's Uh-Oh — make.fun bounty entry.

Writes exactly one word — the word an agent says when it has no idea
what to do — to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
"""

import os
import sys

# The entry word: an agent's lost-for-words reaction.
ENTRY_WORD = "segfault"


def validate(word: str) -> None:
    """The gate requires UTF-8 text of 1-99 characters, not only whitespace,
    and a single word (no spaces, no punctuation beyond the word itself)."""
    if not word:
        raise ValueError("entry word must not be empty")
    if len(word) > 99:
        raise ValueError("entry word must be at most 99 characters")
    if word != word.strip():
        raise ValueError("entry word must not have leading or trailing whitespace")
    if any(ch.isspace() for ch in word):
        raise ValueError("entry word must be exactly one word (no whitespace)")
    if not word.isalnum():
        raise ValueError("entry word must be one plain word (letters/digits only)")


def main() -> int:
    validate(ENTRY_WORD)

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)

    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY_WORD)

    # Round-trip check: what landed on disk must be byte-identical to the
    # validated word, so a stray newline or encoding slip can never pass.
    with open(path, "rb") as f:
        if f.read() != ENTRY_WORD.encode("utf-8"):
            print("error: entry.txt on disk does not match the validated word", file=sys.stderr)
            return 1

    print(f"wrote {len(ENTRY_WORD)}-character entry word to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
