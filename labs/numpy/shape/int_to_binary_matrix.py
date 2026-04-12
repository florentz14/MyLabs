# ------------------------------------------------------------ #
# File: int_to_binary_matrix.py
# Date: 2026-04-02
# Author: Florentino
# Description: Int vector → binary matrix (bits as columns).
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    z = np.array([1, 2, 3, 4], dtype=np.int64)
    width = 8
    bits = ((z[:, None] & (1 << np.arange(width))) != 0).astype(np.uint8)
    print(bits)


if __name__ == "__main__":
    main()
