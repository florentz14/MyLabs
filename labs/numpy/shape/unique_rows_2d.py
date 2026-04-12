# ------------------------------------------------------------ #
# File: unique_rows_2d.py
# Date: 2026-04-02
# Author: Florentino
# Description: Unique rows of a 2-D array.
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    a = np.array([[1, 2, 3], [4, 5, 6], [1, 2, 3], [1, 1, 1]])
    print(np.unique(a, axis=0))


if __name__ == "__main__":
    main()
