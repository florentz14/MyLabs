# ------------------------------------------------------------ #
# File: inv.py
# Date: 2026-04-01
# Author: Florentino
# Description: Matrix inverse (square, non-singular).
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    a = np.array([[1, 2], [3, 4]])
    print(np.linalg.inv(a))


if __name__ == "__main__":
    main()
