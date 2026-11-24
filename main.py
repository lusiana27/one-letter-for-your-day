#!/usr/bin/env python3
"""One Letter for Your Day — entry: the single letter G.

Writes exactly one byte, the letter G, to /output/entry.txt.
G stands for Gas — the word for the day.
"""

import os
import shutil


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # Clear only the folder's contents, never the folder itself.
    for name in os.listdir(out_dir):
        path = os.path.join(out_dir, name)
        if os.path.isdir(path) and not os.path.islink(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="ascii", newline="") as f:
        f.write("G")


if __name__ == "__main__":
    main()
