# ------------------------------------------------------------ #
# File: swap_rows.py
# Date: 2026-04-02
# Author: Florentino
# Description: Swap two rows with fancy indexing.
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    a = np.arange(12).reshape(4, 3)
    i, j = 0, 3
    a[[i, j]] = a[[j, i]]
    print(a)


if __name__ == "__main__":
    main()
