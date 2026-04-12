# ------------------------------------------------------------ #
# File: random_mean_30.py
# Date: 2026-04-02
# Author: Florentino
# Description: Random length-30 vector; mean.
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    rng = np.random.default_rng(2)
    v = rng.random(30)
    print(np.mean(v))


if __name__ == "__main__":
    main()
