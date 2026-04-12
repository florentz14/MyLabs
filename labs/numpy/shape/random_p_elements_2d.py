# ------------------------------------------------------------ #
# File: random_p_elements_2d.py
# Date: 2026-04-02
# Author: Florentino
# Description: Place p random entries in a 2-D array.
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    rng = np.random.default_rng(0)
    h, w, p = 8, 10, 7
    a = np.zeros((h, w), dtype=np.float64)
    flat = np.arange(h * w)
    pick = rng.choice(flat, size=p, replace=False)
    a.ravel()[pick] = 1.0
    print(a)


if __name__ == "__main__":
    main()
