# ------------------------------------------------------------ #
# File: idx_flat.py
# Date: 2026-04-02
# Author: Florentino
# Description: Slicing, slice assignment, row iteration vs `.flat`.
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    a = np.arange(10) ** 3
    print("a[2:5]:", a[2:5])
    a[:6:2] = -1000
    print("after a[:6:2] = -1000:\n", a)

    b = np.arange(12).reshape(4, 3)
    print("rows:")
    for row in b:
        print(" ", row)
    print("flat:", end=" ")
    for x in b.flat:
        print(x, end=" ")
    print()


if __name__ == "__main__":
    main()
