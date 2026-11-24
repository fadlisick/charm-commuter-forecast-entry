#!/usr/bin/env python3
"""Charm the Commuter: one forecast line for Grumbletown.

The program writes a single 135-character forecast for a city that
does not exist to entry.txt, where the sealed scorer reads it.
"""

import os

FORECAST = "Grumbletown: drizzle till ten, then 21°C and a warm breeze smelling of fresh bread. Visibility high; even the traffic lights are green."


def entry_path():
    """Where the forecast goes: the harness dir, or /output by default."""
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(folder, "entry.txt")


def check_line(line):
    """The gate allows 1 to 140 characters of non-blank UTF-8 text."""
    if not line.strip():
        raise SystemExit("forecast is blank")
    if not 1 <= len(line) <= 140:
        raise SystemExit("forecast must be 1 to 140 characters")


def main():
    check_line(FORECAST)
    target = entry_path()
    parent = os.path.dirname(target)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(FORECAST)


if __name__ == "__main__":
    main()
