# ------------------------------------------------------------ #
# File: elem_matmul.py
# Date: 2026-04-02
# Author: Florentino
# Description: Element-wise `+`/`-`/`*`/`**` vs matrix product `@` (not `*`).
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    a = np.array([10, 20, 30, 40])
    b = np.array([1, 2, 3, 4])
    print("a + b:", a + b)
    print("a - b:", a - b)
    print("b**2:", b**2)

    a2 = np.array([[1, 1], [0, 1]])
    b2 = np.array([[2, 0], [3, 4]])
    print("A * B (element-wise):\n", a2 * b2)
    print("A @ B (matmul):\n", a2 @ b2)


if __name__ == "__main__":
    main()
