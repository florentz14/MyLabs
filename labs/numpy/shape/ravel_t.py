# ------------------------------------------------------------ #
# File: ravel_t.py
# Date: 2026-04-02
# Author: Florentino
# Description: `reshape`, `ravel`, transpose `.T`.
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    rng = np.random.default_rng(0)
    a = np.floor(10 * rng.random((3, 4)))
    print("Original:\n", a)
    print("reshape(6, 2):\n", a.reshape(6, 2))
    print("ravel:", a.ravel())
    print("transpose:\n", a.T)


if __name__ == "__main__":
    main()
