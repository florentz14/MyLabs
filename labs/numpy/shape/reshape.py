# ------------------------------------------------------------ #
# File: reshape.py
# Date: 2026-04-01
# Author: Florentino
# Description: Change array shape (here: 1-D length 6 -> 2x3).
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    m = np.array([1, 2, 3, 4, 5, 6])
    print(m.reshape(2, 3))


if __name__ == "__main__":
    main()
