# ------------------------------------------------------------ #
# File: structured_grid_xy.py
# Date: 2026-04-02
# Author: Florentino
# Description: Structured array of (x,y) on a grid over [0,1]×[0,1].
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    n = 4
    xs = np.linspace(0.0, 1.0, n)
    ys = np.linspace(0.0, 1.0, n)
    gx, gy = np.meshgrid(xs, ys)
    dt = np.dtype([("x", np.float64), ("y", np.float64)])
    pts = np.empty(gx.size, dtype=dt)
    pts["x"] = gx.ravel()
    pts["y"] = gy.ravel()
    print(pts[:5], "... len", len(pts))


if __name__ == "__main__":
    main()
