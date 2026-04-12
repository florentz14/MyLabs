# ------------------------------------------------------------ #
# File: nditer_sum_broadcast.py
# Date: 2026-04-02
# Author: Florentino
# Description: Sum (1,3) and (3,1) with np.nditer.
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    a = np.arange(3).reshape(1, 3)
    b = np.arange(3).reshape(3, 1)
    out = np.empty((3, 3))
    it = np.nditer(
        [a, b, out],
        flags=["external_loop"],
        op_flags=[["readonly"], ["readonly"], ["writeonly"]],
    )
    for x, y, z in it:
        z[...] = x + y
    print(out)


if __name__ == "__main__":
    main()
