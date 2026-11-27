#!/usr/bin/env python3
"""Entrypoint: copy the finished front-page image to the output dir.

Standard library only, no network, deterministic: the same bytes are
written on every run. The image (entry.png, drawn at build time by
draw.py with PIL) sums up the world news of Thursday 26 November 2026.
"""
import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(src, os.path.join(out_dir, "entry.png"))


if __name__ == "__main__":
    sys.exit(main())
