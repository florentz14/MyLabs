# ------------------------------------------------------------ #
# File: integer_part_four_ways.py
# Date: 2026-04-02
# Author: Florentino
# Description: Integer part of positive floats: four methods.
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    rng = np.random.default_rng(1)
    z = rng.random(6) * 100
    print("z:", z)
    print("floor:       ", np.floor(z))
    print("trunc:       ", np.trunc(z))
    print("astype int:  ", z.astype(np.int64))
    print("modf integer:", np.modf(z)[1])


if __name__ == "__main__":
    main()
