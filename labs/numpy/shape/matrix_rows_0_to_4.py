# ------------------------------------------------------------ #
# File: matrix_rows_0_to_4.py
# Date: 2026-04-02
# Author: Florentino
# Description: 5×5 matrix, each row 0…4.
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    a = np.broadcast_to(np.arange(5), (5, 5))
    print(a)


if __name__ == "__main__":
    main()
