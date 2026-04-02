# ------------------------------------------------------------ #
# File: determinant.py
# Date: 2026-04-01
# Author: Florentino
# Description: Determinant of a square matrix.
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    a = np.array([[1, 2], [3, 4]])
    print(np.linalg.det(a))


if __name__ == "__main__":
    main()
