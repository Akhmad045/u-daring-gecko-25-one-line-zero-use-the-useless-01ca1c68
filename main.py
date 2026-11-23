"""One Line, Zero Use: The Useless Superpower Sprint.

Assembles a single original line describing a hilariously useless
superpower and writes it to /output/entry.txt. Stdlib only, deterministic.
"""

import os

LINES = [
    "I can stop time — but only in the split second my phone slips from my hand.",
]

LINE = LINES[0]


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"line must be 1-200 chars, got {len(LINE)}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(f"entry ({len(LINE)} chars): {LINE}")


if __name__ == "__main__":
    main()
