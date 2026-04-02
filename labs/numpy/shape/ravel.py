# ------------------------------------------------------------ #
# File: ravel.py
# Date: 2026-04-01
# Author: Florentino
# Description: Return a contiguous flattened view (or copy) — often memory-efficient.
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    matrix = np.array([[1, 2], [3, 4]])
    print(np.ravel(matrix))


if __name__ == "__main__":
    main()
