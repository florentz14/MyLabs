# ------------------------------------------------------------ #
# File: sliding_mean.py
# Date: 2026-04-02
# Author: Florentino
# Description: Moving average via convolution (valid mode).
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    z = np.arange(20, dtype=np.float64)
    w = 5
    kernel = np.ones(w) / w
    print(np.convolve(z, kernel, mode="valid"))


if __name__ == "__main__":
    main()
