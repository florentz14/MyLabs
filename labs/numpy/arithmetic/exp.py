# ------------------------------------------------------------ #
# File: exp.py
# Date: 2026-04-01
# Author: Florentino
# Description: Natural exponential e^x for each element.
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    b = np.array([2, 5])
    print(np.exp(b))


if __name__ == "__main__":
    main()
