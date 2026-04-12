# ------------------------------------------------------------ #
# File: mode_most_frequent.py
# Date: 2026-04-02
# Author: Florentino
# Description: Most frequent value via unique + counts.
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    z = np.array([1, 2, 2, 3, 2, 4, 1])
    vals, counts = np.unique(z, return_counts=True)
    print(vals[counts.argmax()])


if __name__ == "__main__":
    main()
