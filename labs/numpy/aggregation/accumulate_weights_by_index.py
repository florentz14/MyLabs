# ------------------------------------------------------------ #
# File: accumulate_weights_by_index.py
# Date: 2026-04-02
# Author: Florentino
# Description: Scatter X into bins I with np.add.at / bincount.
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    x = np.array([1.0, 2.0, 3.0, 4.0])
    i = np.array([0, 1, 0, 1])
    f = np.zeros(3)
    np.add.at(f, i, x)
    print(f)
    print(np.bincount(i, weights=x, minlength=3))


if __name__ == "__main__":
    main()
