# ------------------------------------------------------------ #
# File: cauchy_matrix.py
# Date: 2026-04-02
# Author: Florentino
# Description: Cauchy matrix C_ij = 1/(x_i - y_j) with broadcasting.
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    x = np.arange(5.0)
    y = np.arange(5.0, 10.0)
    c = 1.0 / (x[:, None] - y[None, :])
    print(c)


if __name__ == "__main__":
    main()
