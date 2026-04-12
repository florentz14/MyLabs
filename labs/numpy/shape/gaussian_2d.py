# ------------------------------------------------------------ #
# File: gaussian_2d.py
# Date: 2026-04-02
# Author: Florentino
# Description: 2-D Gaussian bump on a grid.
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    n = 31
    x = np.linspace(-3.0, 3.0, n)
    y = np.linspace(-3.0, 3.0, n)
    X, Y = np.meshgrid(x, y, indexing="xy")
    sigma = 1.0
    Z = np.exp(-(X**2 + Y**2) / (2 * sigma**2))
    print(Z.shape, Z.min(), Z.max())


if __name__ == "__main__":
    main()
