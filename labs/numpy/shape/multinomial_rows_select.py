# ------------------------------------------------------------ #
# File: multinomial_rows_select.py
# Date: 2026-04-02
# Author: Florentino
# Description: Rows of X that are nonnegative integers summing to n.
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    n = 5
    x = np.array(
        [
            [2.0, 1.0, 1.0, 1.0],
            [5.0, 0.0, 0.0, 0.0],
            [1.1, 2.0, 1.0, 0.9],
            [1.0, 1.0, 1.0, 2.0],
        ]
    )
    is_int = np.all(np.isclose(x, np.round(x)), axis=1)
    ok = is_int & (x.sum(axis=1) == n) & np.all(x >= 0, axis=1)
    print(x[ok])


if __name__ == "__main__":
    main()
