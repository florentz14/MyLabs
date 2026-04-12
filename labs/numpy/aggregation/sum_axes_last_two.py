# ------------------------------------------------------------ #
# File: sum_axes_last_two.py
# Date: 2026-04-02
# Author: Florentino
# Description: Sum a 4-D array over the last two axes at once.
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    rng = np.random.default_rng(4)
    a = rng.random((2, 3, 4, 5))
    s = a.sum(axis=(-2, -1))
    print(s.shape)


if __name__ == "__main__":
    main()
