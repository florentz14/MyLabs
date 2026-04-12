# ------------------------------------------------------------ #
# File: equidistant_path_samples.py
# Date: 2026-04-02
# Author: Florentino
# Description: Resample a polyline (X,Y) at equal arc-length spacing.
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    t = np.linspace(0, 2 * np.pi, 20)
    x = np.cos(t)
    y = np.sin(t)
    dx = np.diff(x)
    dy = np.diff(y)
    seg = np.hypot(dx, dy)
    u = np.concatenate([[0.0], np.cumsum(seg)])
    n = 12
    targets = np.linspace(0.0, u[-1], n)
    xp = np.interp(targets, u, x)
    yp = np.interp(targets, u, y)
    print(np.column_stack((xp, yp)))


if __name__ == "__main__":
    main()
