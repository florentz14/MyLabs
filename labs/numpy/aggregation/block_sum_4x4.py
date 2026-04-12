# ------------------------------------------------------------ #
# File: block_sum_4x4.py
# Date: 2026-04-02
# Author: Florentino
# Description: 4×4 block sums of a 16×16 array.
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    rng = np.random.default_rng(11)
    a = rng.integers(0, 10, size=(16, 16))
    blocks = a.reshape(4, 4, 4, 4).sum(axis=(1, 3))
    print(blocks.shape)


if __name__ == "__main__":
    main()
