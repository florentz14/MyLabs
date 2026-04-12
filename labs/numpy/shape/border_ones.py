# ------------------------------------------------------------ #
# File: border_ones.py
# Date: 2026-04-02
# Author: Florentino
# Description: 2-D array: 1 on border, 0 inside.
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    n = 7
    a = np.ones((n, n))
    a[1:-1, 1:-1] = 0
    print(a)


if __name__ == "__main__":
    main()
