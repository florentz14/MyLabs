# ------------------------------------------------------------ #
# File: record_from_arrays.py
# Date: 2026-04-02
# Author: Florentino
# Description: Build a record array from column arrays.
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    x = np.array([1.0, 2.0, 3.0])
    y = np.array([4.0, 5.0, 6.0])
    r = np.rec.fromarrays([x, y], names="x,y")
    print(r.dtype)
    print(r.x, r.y)


if __name__ == "__main__":
    main()
