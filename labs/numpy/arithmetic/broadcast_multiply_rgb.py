# ------------------------------------------------------------ #
# File: broadcast_multiply_rgb.py
# Date: 2026-04-02
# Author: Florentino
# Description: (5,5,3) * (5,5) via broadcast on last axis.
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    rng = np.random.default_rng(6)
    rgb = rng.random((5, 5, 3))
    g = rng.random((5, 5))
    print((rgb * g[..., np.newaxis]).shape)


if __name__ == "__main__":
    main()
