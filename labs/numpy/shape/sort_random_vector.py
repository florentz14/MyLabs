# ------------------------------------------------------------ #
# File: sort_random_vector.py
# Date: 2026-04-02
# Author: Florentino
# Description: Random length-10 vector, sorted.
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    rng = np.random.default_rng(2)
    v = rng.random(10)
    print(np.sort(v))


if __name__ == "__main__":
    main()
