# ------------------------------------------------------------ #
# File: point_to_line_distance.py
# Date: 2026-04-02
# Author: Florentino
# Description: Distance from one point to many 2-D segments P0→P1.
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    p0 = np.array([[0.0, 0.0], [1.0, 0.0], [0.0, 1.0]])
    p1 = np.array([[1.0, 0.0], [2.0, 1.0], [1.0, 2.0]])
    p = np.array([0.5, 0.5])
    v = p1 - p0
    w = p - p0
    cross = v[:, 0] * w[:, 1] - v[:, 1] * w[:, 0]
    dist = np.abs(cross) / np.linalg.norm(v, axis=1)
    print(dist)


if __name__ == "__main__":
    main()
