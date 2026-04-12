# ------------------------------------------------------------ #
# File: sliding_window_matrix.py
# Date: 2026-04-02
# Author: Florentino
# Description: Hankel-style sliding windows as rows.
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    z = np.arange(1, 11)
    w = 3
    m = np.lib.stride_tricks.sliding_window_view(z, w)
    print(m)


if __name__ == "__main__":
    main()
