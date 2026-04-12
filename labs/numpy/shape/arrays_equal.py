# ------------------------------------------------------------ #
# File: arrays_equal.py
# Date: 2026-04-02
# Author: Florentino
# Description: Compare two arrays: array_equal vs allclose.
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    rng = np.random.default_rng(3)
    a = rng.random((2, 3))
    b = a.copy()
    print("equal copies:", np.array_equal(a, b))
    b[0, 0] += 1e-9
    print("equal tiny diff:", np.array_equal(a, b))
    print("allclose tiny diff:", np.allclose(a, b))


if __name__ == "__main__":
    main()
