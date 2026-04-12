# ------------------------------------------------------------ #
# File: add_reduce_sum.py
# Date: 2026-04-02
# Author: Florentino
# Description: Sum a small 1-D array via np.add.reduce (ufunc path).
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    a = np.arange(8)
    print(np.add.reduce(a), np.sum(a))


if __name__ == "__main__":
    main()
