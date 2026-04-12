# ------------------------------------------------------------ #
# File: inplace_uf.py
# Date: 2026-04-02
# Author: Florentino
# Description: In-place `+=` / `-=` (no `++`); ufuncs `sin`, `sqrt`.
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    a = np.ones((2, 3), dtype=int)
    a += 3
    a -= 1
    print("After +=3, -=1:\n", a)

    b = np.array([0, np.pi / 2, np.pi])
    print("sin(b):", np.sin(b))
    print("sqrt([1,4,9]):", np.sqrt([1, 4, 9]))


if __name__ == "__main__":
    main()
