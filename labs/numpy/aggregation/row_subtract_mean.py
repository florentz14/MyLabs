# ------------------------------------------------------------ #
# File: row_subtract_mean.py
# Date: 2026-04-02
# Author: Florentino
# Description: Subtract each row's mean (keepdims).
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    rng = np.random.default_rng(1)
    a = rng.random((4, 5))
    b = a - a.mean(axis=1, keepdims=True)
    print(b.mean(axis=1))


if __name__ == "__main__":
    main()
