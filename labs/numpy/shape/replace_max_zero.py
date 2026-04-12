# ------------------------------------------------------------ #
# File: replace_max_zero.py
# Date: 2026-04-02
# Author: Florentino
# Description: Random length-10 vector; set the maximum to 0.
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    rng = np.random.default_rng(5)
    v = rng.random(10)
    v[v.argmax()] = 0.0
    print(v)


if __name__ == "__main__":
    main()
