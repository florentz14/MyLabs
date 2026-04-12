# ------------------------------------------------------------ #
# File: closest_to_scalar.py
# Date: 2026-04-02
# Author: Florentino
# Description: Value in a vector closest to a given scalar.
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    rng = np.random.default_rng(6)
    v = rng.random(12)
    z = 0.33
    i = np.abs(v - z).argmin()
    print("v", v)
    print("scalar", z, "-> closest", v[i])


if __name__ == "__main__":
    main()
