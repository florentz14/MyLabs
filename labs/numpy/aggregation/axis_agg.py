# ------------------------------------------------------------ #
# File: axis_agg.py
# Date: 2026-04-02
# Author: Florentino
# Description: Global `sum`/`max` vs `axis=` (e.g. column sums).
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    data = np.array([[1, 2], [3, 4]])
    print("sum():", data.sum())
    print("max():", data.max())
    print("sum(axis=0) (column sums):", data.sum(axis=0))


if __name__ == "__main__":
    main()
