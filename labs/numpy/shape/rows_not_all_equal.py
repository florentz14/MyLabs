# ------------------------------------------------------------ #
# File: rows_not_all_equal.py
# Date: 2026-04-02
# Author: Florentino
# Description: Rows where not all entries are equal.
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    rng = np.random.default_rng(16)
    m = rng.integers(0, 3, size=(10, 3))
    m[0] = [2, 2, 2]
    sel = np.ptp(m, axis=1) > 0
    print(m[sel])


if __name__ == "__main__":
    main()
