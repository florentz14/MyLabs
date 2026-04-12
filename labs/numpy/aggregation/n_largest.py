# ------------------------------------------------------------ #
# File: n_largest.py
# Date: 2026-04-02
# Author: Florentino
# Description: n largest values via argpartition.
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    rng = np.random.default_rng(13)
    z = rng.random(20)
    n = 5
    idx = np.argpartition(z, -n)[-n:]
    print(np.sort(z[idx]))


if __name__ == "__main__":
    main()
