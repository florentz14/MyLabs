# ------------------------------------------------------------ #
# File: hstack.py
# Date: 2026-04-01
# Author: Florentino
# Description: Stack arrays horizontally (column-wise for 1-D inputs).
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    print(np.hstack(([1, 2], [3, 4])))


if __name__ == "__main__":
    main()
