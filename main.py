#!/usr/bin/env python3
"""Entry for make.fun 'The Passport Page of a Country That Isn't There'.

Copies the repo-held passport spread image to /output/entry.png.
Standard library only; no network.
"""
import os
import shutil
import sys


MAX_BYTES = 1_048_576


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    if not os.path.isfile(src):
        print(f"missing entry image: {src}", file=sys.stderr)
        return 1
    if os.path.getsize(src) > MAX_BYTES:
        print("entry image exceeds the 1 MiB gate", file=sys.stderr)
        return 1
    out_dir = "/output"
    dst = os.path.join(out_dir, "entry.png")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(src, dst)
    return 0


if __name__ == "__main__":
    sys.exit(main())
