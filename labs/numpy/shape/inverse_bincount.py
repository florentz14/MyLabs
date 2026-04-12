# ------------------------------------------------------------ #
# File: inverse_bincount.py
# Date: 2026-04-02
# Author: Florentino
# Description: Reconstruct A from histogram C so bincount(A)==C.
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    c = np.array([0, 2, 0, 1, 3])
    a = np.repeat(np.arange(len(c)), c)
    print(a, np.bincount(a))


if __name__ == "__main__":
    main()
