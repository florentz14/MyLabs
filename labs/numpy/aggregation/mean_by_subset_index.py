# ------------------------------------------------------------ #
# File: mean_by_subset_index.py
# Date: 2026-04-02
# Author: Florentino
# Description: Mean of D per label in S via bincount.
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    d = np.arange(10, dtype=np.float64)
    s = np.array([0, 0, 0, 1, 1, 2, 2, 2, 2, 2])
    sums = np.bincount(s, weights=d)
    counts = np.bincount(s)
    means = sums / np.maximum(counts, 1)
    print(means)


if __name__ == "__main__":
    main()
