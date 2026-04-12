# ------------------------------------------------------------ #
# File: batched_matvec_sum.py
# Date: 2026-04-02
# Author: Florentino
# Description: Sum of p batched (n,n) @ (n,1) products → (n,1).
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    rng = np.random.default_rng(10)
    p, n = 5, 4
    mats = rng.standard_normal((p, n, n))
    vecs = rng.standard_normal((p, n, 1))
    out = (mats @ vecs).sum(axis=0)
    print(out.shape)


if __name__ == "__main__":
    main()
