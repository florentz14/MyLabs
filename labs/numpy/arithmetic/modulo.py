# ------------------------------------------------------------ #
# File: modulo.py
# Date: 2026-04-01
# Author: Florentino
# Description: Element-wise remainder (modulo).
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    a = np.array([10, 20])
    print(a % 3)


if __name__ == "__main__":
    main()
