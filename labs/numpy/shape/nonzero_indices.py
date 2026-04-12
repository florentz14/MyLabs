# ------------------------------------------------------------ #
# File: nonzero_indices.py
# Date: 2026-04-02
# Author: Florentino
# Description: Indices of non-zero entries.
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    a = np.array([1, 2, 0, 0, 4, 0])
    print(np.nonzero(a)[0])


if __name__ == "__main__":
    main()
