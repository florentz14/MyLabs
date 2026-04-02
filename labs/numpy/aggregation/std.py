# ------------------------------------------------------------ #
# File: std.py
# Date: 2026-04-01
# Author: Florentino
# Description: Standard deviation.
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    data = np.array([1, 5, 10, 15, 20])
    print(np.std(data))


if __name__ == "__main__":
    main()
