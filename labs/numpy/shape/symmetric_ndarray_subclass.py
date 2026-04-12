# ------------------------------------------------------------ #
# File: symmetric_ndarray_subclass.py
# Date: 2026-04-02
# Author: Florentino
# Description: 2-D ndarray subclass enforcing Z[i,j]==Z[j,i].
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


class Symmetric(np.ndarray):
    def __new__(cls, input_array):
        obj = np.asarray(input_array).view(cls)
        return obj

    def __array_finalize__(self, obj):
        pass

    def __setitem__(self, idx, value):
        i, j = idx
        super().__setitem__((i, j), value)
        if i != j:
            super().__setitem__((j, i), value)


def main() -> None:
    z = Symmetric(np.zeros((3, 3)))
    z[0, 2] = 5.0
    print(z)


if __name__ == "__main__":
    main()
