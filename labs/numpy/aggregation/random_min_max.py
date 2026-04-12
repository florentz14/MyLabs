# ------------------------------------------------------------ #
# File: random_min_max.py
# Date: 2026-04-02
# Author: Florentino
# Description: 10×10 random array; global min and max.
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    rng = np.random.default_rng(1)
    a = rng.random((10, 10))
    print("min:", a.min(), " max:", a.max())


if __name__ == "__main__":
    main()
