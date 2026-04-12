# ------------------------------------------------------------ #
# File: named_ndarray.py
# Date: 2026-04-02
# Author: Florentino
# Description: ndarray subclass with a `name` attribute.
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


class NamedArray(np.ndarray):
    def __new__(cls, input_array, name=""):
        obj = np.asarray(input_array).view(cls)
        obj.name = name
        return obj

    def __array_finalize__(self, obj):
        if obj is None:
            return
        self.name = getattr(obj, "name", "")


def main() -> None:
    x = NamedArray([1, 2, 3], name="signal")
    print(type(x), x.name, x)


if __name__ == "__main__":
    main()
