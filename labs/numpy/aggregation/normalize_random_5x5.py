# ------------------------------------------------------------ #
# File: normalize_random_5x5.py
# Date: 2026-04-02
# Author: Florentino
# Description: Min–max normalize a 5×5 random matrix to [0, 1].
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    rng = np.random.default_rng(0)
    x = rng.random((5, 5))
    lo, hi = x.min(), x.max()
    n = (x - lo) / (hi - lo)
    print(n)


if __name__ == "__main__":
    main()
