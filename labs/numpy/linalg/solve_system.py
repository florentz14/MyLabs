# ------------------------------------------------------------ #
# File: solve_system.py
# Date: 2026-04-01
# Author: Florentino
# Description: Solve A @ x = b for x (square A).
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    a = np.array([[1, 2], [3, 4]])
    b = np.array([5, 11])
    print(np.linalg.solve(a, b))


if __name__ == "__main__":
    main()
