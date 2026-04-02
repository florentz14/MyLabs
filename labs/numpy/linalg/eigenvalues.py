# ------------------------------------------------------------ #
# File: eigenvalues.py
# Date: 2026-04-01
# Author: Florentino
# Description: Eigenvalues of a square matrix (np.linalg.eigvals).
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    a = np.array([[1, 2], [3, 4]])
    print(np.linalg.eigvals(a))


if __name__ == "__main__":
    main()
