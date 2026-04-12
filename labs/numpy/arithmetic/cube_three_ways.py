# ------------------------------------------------------------ #
# File: cube_three_ways.py
# Date: 2026-04-02
# Author: Florentino
# Description: Z**3 via `*`, `**`, and np.power.
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    rng = np.random.default_rng(14)
    z = rng.random(6)
    print(z * z * z)
    print(z**3)
    print(np.power(z, 3))


if __name__ == "__main__":
    main()
