# ------------------------------------------------------------ #
# File: transpose.py
# Date: 2026-04-01
# Author: Florentino
# Description: Matrix transpose (.T).
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    matrix = np.array([[1, 2], [3, 4]])
    print(matrix.T)


if __name__ == "__main__":
    main()
