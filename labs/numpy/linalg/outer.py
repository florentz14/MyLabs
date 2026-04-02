# ------------------------------------------------------------ #
# File: outer.py
# Date: 2026-04-01
# Author: Florentino
# Description: Outer product of two 1-D vectors.
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    print(np.outer([1, 2], [3, 4]))


if __name__ == "__main__":
    main()
