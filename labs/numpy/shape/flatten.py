# ------------------------------------------------------------ #
# File: flatten.py
# Date: 2026-04-01
# Author: Florentino
# Description: Collapse N-D array to 1-D (copy).
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    matrix = np.array([[1, 2], [3, 4]])
    print(matrix.flatten())


if __name__ == "__main__":
    main()
