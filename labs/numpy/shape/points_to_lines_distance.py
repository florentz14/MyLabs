# ------------------------------------------------------------ #
# File: points_to_lines_distance.py
# Date: 2026-04-02
# Author: Florentino
# Description: Distances from each point P[j] to each line (P0[i],P1[i]).
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    p0 = np.array([[0.0, 0.0], [1.0, 0.0]])
    p1 = np.array([[1.0, 0.0], [2.0, 1.0]])
    pts = np.array([[0.5, 0.5], [1.5, 0.5], [2.0, 2.0]])
    v = p1[:, np.newaxis, :] - p0[:, np.newaxis, :]
    w = pts[np.newaxis, :, :] - p0[:, np.newaxis, :]
    cross = v[..., 0] * w[..., 1] - v[..., 1] * w[..., 0]
    dist = np.abs(cross) / np.linalg.norm(v, axis=-1, keepdims=True)[..., 0]
    print(dist)


if __name__ == "__main__":
    main()
