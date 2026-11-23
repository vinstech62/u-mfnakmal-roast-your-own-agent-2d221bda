#!/usr/bin/env python3
"""Roast Your Own Agent — one-line roast of my own AI agent.

Writes a single line (<=200 chars, UTF-8, no trailing newline) to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).
Deterministic: the same line on every run.
"""

import os

ROAST = "My agent outsourced this roast to a subagent, then took credit for it in the commit message."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ROAST)

if __name__ == "__main__":
    main()
