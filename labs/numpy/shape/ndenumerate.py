# ------------------------------------------------------------ #
# File: ndenumerate.py
# Date: 2026-04-02
# Author: Florentino
# Description: Like enumerate for arrays: np.ndenumerate / np.ndindex.
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    a = np.arange(6).reshape(2, 3)
    for idx, val in np.ndenumerate(a):
        print(idx, val)
    print("---")
    for idx in np.ndindex(a.shape):
        print(idx, a[idx])


if __name__ == "__main__":
    main()
