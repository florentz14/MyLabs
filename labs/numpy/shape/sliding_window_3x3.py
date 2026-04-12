# ------------------------------------------------------------ #
# File: sliding_window_3x3.py
# Date: 2026-04-02
# Author: Florentino
# Description: All contiguous 3×3 blocks from a 10×10 matrix.
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    rng = np.random.default_rng(9)
    a = rng.random((10, 10))
    w = np.lib.stride_tricks.sliding_window_view(a, (3, 3))
    print(w.shape)


if __name__ == "__main__":
    main()
