# ------------------------------------------------------------ #
# File: power.py
# Date: 2026-04-01
# Author: Florentino
# Description: Element-wise power (here: square each element).
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    a = np.array([10, 20])
    print(a**2)


if __name__ == "__main__":
    main()
