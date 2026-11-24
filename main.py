#!/usr/bin/env python3
"""Copy entry.png to the output directory.

Entry for make.fun news-image-20261124: the program writes the image
that sums up the world news of Tuesday, 24 November 2026. The image is
a newspaper front page (1024x1024 PNG) drawn with PIL; this program
only copies the file the repository holds, so the two grading runs
produce byte-identical output.

Standard library only, no network. The output directory comes from
MAKEFUN_OUTPUT_DIR when set, else /output.
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
MAX_BYTES = 1_048_576  # the gate refuses images over 1 MiB


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    size = os.path.getsize(SRC)
    if size > MAX_BYTES:
        print(f"entry.png is {size} bytes, over the 1 MiB cap",
              file=sys.stderr)
        return 1
    with open(SRC, "rb") as f:
        head = f.read(len(PNG_MAGIC))
    if head != PNG_MAGIC:
        print("entry.png copy is not a valid PNG (bad magic bytes)",
              file=sys.stderr)
        return 1
    shutil.copyfile(SRC, dst)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
