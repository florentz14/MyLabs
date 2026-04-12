# ------------------------------------------------------------ #
# File: rgba_dtype.py
# Date: 2026-04-02
# Author: Florentino
# Description: Structured dtype for RGBA as four unsigned bytes.
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    rgba = np.dtype([("r", "u1"), ("g", "u1"), ("b", "u1"), ("a", "u1")])
    print(rgba)
    c = np.array((255, 128, 0, 255), dtype=rgba)
    print(c)


if __name__ == "__main__":
    main()
