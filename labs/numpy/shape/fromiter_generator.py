# ------------------------------------------------------------ #
# File: fromiter_generator.py
# Date: 2026-04-02
# Author: Florentino
# Description: Build array from a generator with np.fromiter.
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def ten_ints():
    for i in range(10):
        yield i * i


def main() -> None:
    a = np.fromiter(ten_ints(), dtype=np.int64, count=10)
    print(a)


if __name__ == "__main__":
    main()
