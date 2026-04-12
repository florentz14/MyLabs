# ------------------------------------------------------------ #
# File: pairwise_distances.py
# Date: 2026-04-02
# Author: Florentino
# Description: Consecutive Euclidean distances for (100,2) coordinates.
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    rng = np.random.default_rng(7)
    p = rng.random((100, 2))
    d = np.linalg.norm(np.diff(p, axis=0), axis=1)
    print(d.shape)
    print(d[:5], "...")


if __name__ == "__main__":
    main()
