# ------------------------------------------------------------ #
# File: linspace_open_0_1.py
# Date: 2026-04-02
# Author: Florentino
# Description: Length 10, values strictly between 0 and 1.
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    v = np.linspace(0.0, 1.0, 12)[1:-1]
    print(v, v.shape)


if __name__ == "__main__":
    main()
