# ------------------------------------------------------------ #
# File: rolling_windows_1d.py
# Date: 2026-04-02
# Author: Florentino
# Description: Sliding windows of width 4 on Z → R rows.
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    z = np.arange(1, 15)
    r = np.lib.stride_tricks.sliding_window_view(z, 4)
    print(r)


if __name__ == "__main__":
    main()
