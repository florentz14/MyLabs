# ------------------------------------------------------------ #
# File: inplace_negate_sign.py
# Date: 2026-04-02
# Author: Florentino
# Description: In-place `logical_not` on bool; `negative` on float.
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    b = np.array([True, False, True])
    np.logical_not(b, out=b)
    print(b)
    f = np.array([1.0, -2.0, 3.0])
    np.negative(f, out=f)
    print(f)


if __name__ == "__main__":
    main()
