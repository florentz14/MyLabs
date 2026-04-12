# ------------------------------------------------------------ #
# File: negate_between_3_8.py
# Date: 2026-04-02
# Author: Florentino
# Description: Negate in place elements strictly between 3 and 8.
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    a = np.arange(11, dtype=float)
    m = (a > 3) & (a < 8)
    a[m] *= -1
    print(a)


if __name__ == "__main__":
    main()
