# ------------------------------------------------------------ #
# File: subtract.py
# Date: 2026-04-01
# Author: Florentino
# Description: Element-wise subtraction.
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    a = np.array([10, 20])
    b = np.array([2, 5])
    print(a - b)


if __name__ == "__main__":
    main()
