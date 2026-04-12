# ------------------------------------------------------------ #
# File: interleave_three_zeros.py
# Date: 2026-04-02
# Author: Florentino
# Description: [1,2,…,5] with three zeros between successive values.
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    v = np.arange(1, 6)
    out = np.zeros(len(v) + (len(v) - 1) * 3, dtype=int)
    out[::4] = v
    print(out)


if __name__ == "__main__":
    main()
