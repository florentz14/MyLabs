# ------------------------------------------------------------ #
# File: matmul_5x3_3x2.py
# Date: 2026-04-02
# Author: Florentino
# Description: Real matrix product 5×3 @ 3×2. See also `dot.py`.
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    rng = np.random.default_rng(1)
    a = rng.random((5, 3))
    b = rng.random((3, 2))
    print(a @ b)


if __name__ == "__main__":
    main()
