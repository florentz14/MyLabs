# ------------------------------------------------------------ #
# File: cartesian_to_polar.py
# Date: 2026-04-02
# Author: Florentino
# Description: Random 10×2 (x,y) → r, θ with hypot and arctan2.
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    rng = np.random.default_rng(4)
    xy = rng.standard_normal((10, 2))
    x, y = xy[:, 0], xy[:, 1]
    r = np.hypot(x, y)
    theta = np.arctan2(y, x)
    print(np.column_stack((r, theta)))


if __name__ == "__main__":
    main()
