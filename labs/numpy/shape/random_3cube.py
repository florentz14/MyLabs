# ------------------------------------------------------------ #
# File: random_3cube.py
# Date: 2026-04-02
# Author: Florentino
# Description: Random 3×3×3 array.
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    rng = np.random.default_rng(0)
    print(rng.random((3, 3, 3)))


if __name__ == "__main__":
    main()
