# ------------------------------------------------------------ #
# File: checkerboard_tile_8.py
# Date: 2026-04-02
# Author: Florentino
# Description: 8×8 checkerboard built with np.tile.
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    cell = np.array([[0, 1], [1, 0]])
    a = np.tile(cell, (4, 4))
    print(a)


if __name__ == "__main__":
    main()
