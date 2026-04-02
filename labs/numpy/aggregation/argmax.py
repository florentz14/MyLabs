# ------------------------------------------------------------ #
# File: argmax.py
# Date: 2026-04-01
# Author: Florentino
# Description: Index of the maximum value.
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    data = np.array([1, 5, 10, 15, 20])
    print(np.argmax(data))


if __name__ == "__main__":
    main()
