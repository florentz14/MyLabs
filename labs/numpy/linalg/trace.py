# ------------------------------------------------------------ #
# File: trace.py
# Date: 2026-04-01
# Author: Florentino
# Description: Sum of diagonal elements.
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    a = np.array([[1, 2], [3, 4]])
    print(np.trace(a))


if __name__ == "__main__":
    main()
