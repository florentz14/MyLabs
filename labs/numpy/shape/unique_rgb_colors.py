# ------------------------------------------------------------ #
# File: unique_rgb_colors.py
# Date: 2026-04-02
# Author: Florentino
# Description: Count unique RGB colors in a (h,w,3) ubyte image.
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    rng = np.random.default_rng(3)
    img = rng.integers(0, 5, size=(8, 8, 3), dtype=np.uint8)
    flat = img.reshape(-1, 3)
    uniq = np.unique(flat, axis=0)
    print(len(uniq))


if __name__ == "__main__":
    main()
