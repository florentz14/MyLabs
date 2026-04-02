# ------------------------------------------------------------ #
# File: total.py
# Date: 2026-04-01
# Author: Florentino
# Description: Sum of all elements (np.sum).
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    data = np.array([1, 5, 10, 15, 20])
    print(np.sum(data))


if __name__ == "__main__":
    main()
