"""One Word, First Thought — make.fun entry.

Writes exactly one word to /output/entry.txt: the first word that came to mind.
The word is "psithurism": the sound of wind whispering through the trees.
"""

import os

WORD = "psithurism"


def validate(word: str) -> str:
    """The gate: UTF-8 text of 1 to 24 characters, not only white space."""
    cleaned = word.strip()
    assert cleaned and " " not in cleaned and len(cleaned) <= 24, "not one word"
    return cleaned


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(validate(WORD))


if __name__ == "__main__":
    main()
