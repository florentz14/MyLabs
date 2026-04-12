# ------------------------------------------------------------ #
# File: bcast.py
# Date: 2026-04-02
# Author: Florentino
# Description: Broadcasting: scalar + vector; row + matrix.
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    a = np.array([1, 2, 3])
    print("a + 2:", a + 2)

    m = np.ones((3, 3))
    row = np.array([1, 2, 3])
    print("ones(3,3) + row:\n", m + row)


if __name__ == "__main__":
    main()
