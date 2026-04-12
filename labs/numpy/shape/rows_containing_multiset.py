# ------------------------------------------------------------ #
# File: rows_containing_multiset.py
# Date: 2026-04-02
# Author: Florentino
# Description: Rows of A that contain each value of B rows with enough multiplicity.
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def row_contains_row_multiset(a_row: np.ndarray, b_row: np.ndarray) -> bool:
    for v in np.unique(b_row):
        if np.sum(a_row == v) < np.sum(b_row == v):
            return False
    return True


def main() -> None:
    rng = np.random.default_rng(15)
    a = rng.integers(0, 5, size=(8, 3))
    b = np.array([[1, 2], [0, 0]])
    for bi, brow in enumerate(b):
        mask = np.array([row_contains_row_multiset(a[i], brow) for i in range(len(a))])
        print(f"B[{bi}] rows of A:", np.where(mask)[0])


if __name__ == "__main__":
    main()
