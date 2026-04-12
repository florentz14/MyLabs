# ------------------------------------------------------------ #
# File: vhstack.py
# Date: 2026-04-02
# Author: Florentino
# Description: `np.vstack` / `np.hstack` to join blocks.
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    a = np.array([[1, 2], [3, 4]])
    b = np.array([[5, 6], [7, 8]])
    print("vstack:\n", np.vstack((a, b)))
    print("hstack:\n", np.hstack((a, b)))


if __name__ == "__main__":
    main()
