# ------------------------------------------------------------ #
# File: bool_mask.py
# Date: 2026-04-02
# Author: Florentino
# Description: Boolean masks: filter with `a[mask]`, assign `a[cond] = …`.
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    data = np.array([[1, 7], [3, 9], [8, 2]])
    mask = data > 5
    print("mask:\n", mask)
    print("data[mask]:", data[mask])
    data[data > 5] = 0
    print("after data[data > 5] = 0:\n", data)


if __name__ == "__main__":
    main()
