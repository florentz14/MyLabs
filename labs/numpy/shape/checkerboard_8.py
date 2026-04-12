# ------------------------------------------------------------ #
# File: checkerboard_8.py
# Date: 2026-04-02
# Author: Florentino
# Description: 8×8 checkerboard via (i+j)%2.
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    i = np.arange(8)[:, None]
    j = np.arange(8)
    a = (i + j) % 2
    print(a)


if __name__ == "__main__":
    main()
