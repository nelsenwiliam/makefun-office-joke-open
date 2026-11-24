#!/usr/bin/env python3
"""Write one original office joke to /output/entry.txt.

Pure standard library. The joke is a single line, well under the
200-character limit, with the payoff landing in the last few words:
the office printer — the most reliably broken machine in any
workplace — answers an email with an out-of-office reply of its own.
The output file holds that one line plus a trailing newline.
"""

import os

JOKE = (
    "Our printer jammed again, so I emailed IT a photo of it "
    "\u2014 and the printer replied with an out-of-office message."
)


def main() -> None:
    text = JOKE.strip()
    # Gate: exactly one line, 1-200 characters, nothing but the joke.
    assert 1 <= len(text) <= 200, f"joke must be 1-200 characters, got {len(text)}"
    assert "\n" not in text and "\r" not in text, "joke must be a single line"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
