#!/usr/bin/env python3
"""Entry program for make.fun news-image-20261122.

Copies the entry image (entry.png, beside this file) to the output
directory as entry.png. Deterministic: the same bytes on every run.
No network, no randomness, standard library only.
"""

import os
import shutil


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    if not os.path.isfile(src):
        raise SystemExit("entry.png not found beside main.py")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(src, os.path.join(out_dir, "entry.png"))


if __name__ == "__main__":
    main()
