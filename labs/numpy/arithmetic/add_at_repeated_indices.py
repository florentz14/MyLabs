# ------------------------------------------------------------ #
# File: add_at_repeated_indices.py
# Date: 2026-04-02
# Author: Florentino
# Description: Add 1 at indices with repeats: use np.add.at.
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    z = np.zeros(8, dtype=np.int64)
    idx = np.array([1, 1, 2, 3, 3, 3])
    np.add.at(z, idx, 1)
    print(z)


if __name__ == "__main__":
    main()
