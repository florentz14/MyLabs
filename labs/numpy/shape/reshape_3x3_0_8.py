# ------------------------------------------------------------ #
# File: reshape_3x3_0_8.py
# Date: 2026-04-02
# Author: Florentino
# Description: 3×3 matrix with values 0…8.
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    print(np.arange(9).reshape(3, 3))


if __name__ == "__main__":
    main()
