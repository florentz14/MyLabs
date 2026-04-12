# ------------------------------------------------------------ #
# File: expr_inplace_ab.py
# Date: 2026-04-02
# Author: Florentino
# Description: ((A+B)*(-A/2)) using one output buffer and `out=`.
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    rng = np.random.default_rng(0)
    a = rng.standard_normal((3, 3))
    b = rng.standard_normal((3, 3))
    r = np.empty_like(a)
    np.add(a, b, out=r)
    np.multiply(r, a, out=r)
    np.multiply(r, -0.5, out=r)
    expected = (a + b) * (-a / 2)
    print(np.allclose(r, expected))
    print(r)


if __name__ == "__main__":
    main()
