#!/usr/bin/env python3
"""The Excuse That Almost Works — make.fun entry.

Writes one line to /output/entry.txt: the text a gamer sends the boss to
skip work on GTA 6 launch week. Deterministic, stdlib only, no network.
"""

import os

EXCUSE = (
    "Sorry, my car died in the midnight launch queue "
    "and the breakdown van can't get to me till lunch"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
