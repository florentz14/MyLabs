# ------------------------------------------------------------ #
# File: expand_dims.py
# Date: 2026-04-01
# Author: Florentino
# Description: Insert an axis (e.g. turn a vector into a row matrix).
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    m = np.array([1, 2, 3, 4, 5, 6])
    print(np.expand_dims(m, axis=0))


if __name__ == "__main__":
    main()
