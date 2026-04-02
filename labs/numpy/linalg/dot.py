# ------------------------------------------------------------ #
# File: dot.py
# Date: 2026-04-01
# Author: Florentino
# Description: Matrix multiplication (np.dot / @).
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    a = np.array([[1, 2], [3, 4]])
    b = np.array([[5, 6], [7, 8]])
    print(np.dot(a, b))


if __name__ == "__main__":
    main()
