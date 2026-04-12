# ------------------------------------------------------------ #
# File: structured_xy_rgb.py
# Date: 2026-04-02
# Author: Florentino
# Description: Structured dtype: position (x,y) and color (r,g,b).
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    dt = np.dtype(
        [
            ("x", np.float32),
            ("y", np.float32),
            ("r", np.uint8),
            ("g", np.uint8),
            ("b", np.uint8),
        ]
    )
    p = np.array((1.0, 2.0, 200, 40, 80), dtype=dt)
    print(p.dtype)
    print(p)


if __name__ == "__main__":
    main()
