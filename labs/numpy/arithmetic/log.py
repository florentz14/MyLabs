# ------------------------------------------------------------ #
# File: log.py
# Date: 2026-04-01
# Author: Florentino
# Description: Natural logarithm (base e) of each element.
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    a = np.array([10, 20])
    print(np.log(a))


if __name__ == "__main__":
    main()
