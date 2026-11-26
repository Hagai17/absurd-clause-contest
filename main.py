#!/usr/bin/env python3
"""The Absurd Clause Contest — entry program (program/v1).

Writes one absurd terms-of-service clause to /output/entry.txt.
The clause is a deadpan indemnification provision. Revision 2 of the
text: the absurd item (one raccoon) is buried in the middle of the
hold-harmless list instead of sitting at its end, and dry boilerplate
("and assigns") continues after it, so the register never breaks and
the joke ambushes the reader a beat late — a clause hidden deep inside
the list, the way fine print actually hides things.
"""

import os

# The indemnified parties, in order. The raccoon is item four of six.
INDEMNIFIED = [
    "the Company",
    "its officers",
    "directors",
    "employees",
    "one (1) raccoon of its choosing",
    "and assigns",
]

ENTRY = (
    "You agree to indemnify, defend, and hold harmless "
    + ", ".join(INDEMNIFIED)
    + ", from any claims arising from your use of the Service."
)


def main() -> None:
    # Gate self-check: 1-200 characters, a single sentence, not blank.
    assert 1 <= len(ENTRY) <= 200, "entry outside the 200-character gate"
    assert ENTRY.strip() == ENTRY and ENTRY.strip(), "entry must not be blank"
    assert ENTRY.count(".") == 1 and ENTRY.endswith("."), "entry must be one sentence"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
