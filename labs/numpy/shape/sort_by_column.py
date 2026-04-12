# ------------------------------------------------------------ #
# File: sort_by_column.py
# Date: 2026-04-02
# Author: Florentino
# Description: Sort rows by the n-th column.
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    rng = np.random.default_rng(2)
    a = rng.random((5, 4))
    n = 2
    order = a[:, n].argsort()
    print(a[order])


if __name__ == "__main__":
    main()
