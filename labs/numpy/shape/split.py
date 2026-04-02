# ------------------------------------------------------------ #
# File: split.py
# Date: 2026-04-01
# Author: Florentino
# Description: Split array into equal parts (np.split).
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    m = np.array([1, 2, 3, 4, 5, 6])
    print(np.split(m, 2))


if __name__ == "__main__":
    main()
