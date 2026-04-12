# ------------------------------------------------------------ #
# File: unravel_100th.py
# Date: 2026-04-02
# Author: Florentino
# Description: (x,y,z) index of the 100th element in C order for shape (6,7,8).
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    shape = (6, 7, 8)
    # 0-based: "100th element" → linear index 99
    idx = np.unravel_index(99, shape)
    print(idx)


if __name__ == "__main__":
    main()
