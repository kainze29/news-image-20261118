"""Emit the 18 November 2026 front page for the make.fun grader.

The repository carries news.png: one 1024x1024 front page summing up
Wednesday 18 November 2026 in 35 stories (six illustrated top stories
plus a numbered list of the other 29). The grader runs this program
twice in a sandbox with no network, so all it does is copy the bytes
already shipped in the repository to the output path, after checking
the file is really a whole PNG inside the competition's size limit.
Both runs therefore write identical bytes.
"""

import hashlib
import os
import sys

SOURCE = "news.png"
TARGET = "entry.png"
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
MAX_BYTES = 1048576


def read_front_page():
    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(here, SOURCE)
    with open(path, "rb") as handle:
        return handle.read()


def guard_png(blob):
    if len(blob) > MAX_BYTES:
        sys.exit(f"{SOURCE} is {len(blob)} bytes, over the 1 MiB limit")
    if len(blob) < 4096:
        sys.exit(f"{SOURCE} is only {len(blob)} bytes, looks truncated")
    if blob[:8] != PNG_MAGIC:
        sys.exit(f"{SOURCE} does not start with PNG magic bytes")
    width = int.from_bytes(blob[16:20], "big")
    height = int.from_bytes(blob[20:24], "big")
    if width > 1024 or height > 1024:
        sys.exit(f"{SOURCE} is {width}x{height}, over the 1024x1024 limit")
    return hashlib.sha256(blob).hexdigest()


def emit(blob):
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, TARGET)
    with open(dest, "wb") as handle:
        handle.write(blob)
    return dest


def main():
    blob = read_front_page()
    digest = guard_png(blob)
    dest = emit(blob)
    print(f"wrote {dest} ({len(blob)} bytes, sha256 {digest})")


if __name__ == "__main__":
    main()
