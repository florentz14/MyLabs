# ------------------------------------------------------------ #
# File: view_copy.py
# Date: 2026-04-02
# Author: Florentino
# Description: Slice view shares memory; `.copy()` is independent.
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    a = np.array([1, 2, 3, 4])
    v = a[0:2]
    v[0] = 99
    print("after v[0]=99, base a:", a)

    c = a.copy()
    c[1] = 88
    print("after c[1]=88 on copy, base a:", a)


if __name__ == "__main__":
    main()
