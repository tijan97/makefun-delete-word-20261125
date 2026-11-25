#!/usr/bin/env python3
"""make.fun entry: "The Word You'd Delete From the Dictionary".

Chosen word: floccinaucinihilipilification

Why this word, and why deleting it is the funniest deletion:
- It literally means "the act or habit of estimating something as
  worthless". Deleting it from the dictionary is therefore the most
  floccinaucinihilipilification thing anyone can do to a word: the
  dictionary itself finally estimates it as worthless. The deletion
  performs the very act the word describes.
- It is a 29-letter monstrosity that almost nobody can spell, pronounce,
  or has ever used in a real sentence, so nobody would even notice it
  was gone -- the perfect victim. Deleting the dictionary's longest
  punchline also leaves no word left to describe how worthless it was.
- The joke comes from the word itself, not from a setup: one look at the
  word and its meaning is the whole punchline.

The program prints ONLY the word (plus a trailing newline) to
<output_dir>/entry.txt, where <output_dir> is MAKEFUN_OUTPUT_DIR,
OUTPUT_DIR, or /output. Nothing else is written to the entry file.
"""

import os

WORD = "floccinaucinihilipilification"


def main() -> None:
    # Validate against the competition gate before writing anything:
    # exactly one word, 1-77 characters, not only whitespace.
    stripped = WORD.strip()
    assert stripped, "word must not be empty or only whitespace"
    assert stripped == WORD, "word must contain no surrounding whitespace"
    assert " " not in stripped and "\n" not in stripped, "entry must be a single word"
    assert 1 <= len(stripped) <= 77, "entry must be 1-77 characters"

    output_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(WORD + "\n")


if __name__ == "__main__":
    main()
