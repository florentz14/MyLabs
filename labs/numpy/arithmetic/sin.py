# ------------------------------------------------------------ #
# File: sin.py
# Date: 2026-04-01
# Author: Florentino
# Description: Sine of each element (radians).
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    a = np.array([10, 20])
    print(np.sin(a))


if __name__ == "__main__":
    main()
