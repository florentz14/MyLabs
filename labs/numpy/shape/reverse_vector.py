# ------------------------------------------------------------ #
# File: reverse_vector.py
# Date: 2026-04-02
# Author: Florentino
# Description: Reverse a 1-D array.
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    v = np.arange(12)
    print("original:", v)
    print("reversed:", v[::-1])


if __name__ == "__main__":
    main()
