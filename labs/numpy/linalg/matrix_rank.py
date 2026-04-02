# ------------------------------------------------------------ #
# File: matrix_rank.py
# Date: 2026-04-01
# Author: Florentino
# Description: Rank of a matrix (linearly independent columns).
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    a = np.array([[1, 2], [3, 4]])
    print(np.linalg.matrix_rank(a))


if __name__ == "__main__":
    main()
