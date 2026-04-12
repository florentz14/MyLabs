# ------------------------------------------------------------ #
# File: cartesian_product_many.py
# Date: 2026-04-02
# Author: Florentino
# Description: Cartesian product of any number of 1-D vectors.
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    a = np.array([1, 2, 3])
    b = np.array([10, 20])
    c = np.array([100])
    grids = np.meshgrid(a, b, c, indexing="ij")
    prod = np.stack(grids, axis=-1).reshape(-1, 3)
    print(prod)


if __name__ == "__main__":
    main()
