# ------------------------------------------------------------ #
# File: vstack.py
# Date: 2026-04-01
# Author: Florentino
# Description: Stack arrays vertically (row-wise).
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    print(np.vstack(([1, 2], [3, 4])))


if __name__ == "__main__":
    main()
