# ------------------------------------------------------------ #
# File: print_all_values.py
# Date: 2026-04-02
# Author: Florentino
# Description: Print every element of a large array (threshold).
# ------------------------------------------------------------ #

from __future__ import annotations

import sys

import numpy as np


def main() -> None:
    a = np.arange(120)
    np.set_printoptions(threshold=8)
    print("abbreviated:\n", a)
    np.set_printoptions(threshold=sys.maxsize)
    print("all values:\n", a)
    np.set_printoptions(threshold=1000)


if __name__ == "__main__":
    main()
