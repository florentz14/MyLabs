# ------------------------------------------------------------ #
# File: zeros_fifth_one.py
# Date: 2026-04-02
# Author: Florentino
# Description: Length-10 null vector; fifth element = 1.
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    z = np.zeros(10)
    z[4] = 1
    print(z)


if __name__ == "__main__":
    main()
