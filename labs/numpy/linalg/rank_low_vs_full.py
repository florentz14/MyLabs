# ------------------------------------------------------------ #
# File: rank_low_vs_full.py
# Date: 2026-04-02
# Author: Florentino
# Description: Rank of full-rank vs rank-deficient matrix. See `matrix_rank.py`.
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    rng = np.random.default_rng(8)
    full = rng.standard_normal((4, 4))
    low = np.outer(rng.standard_normal(4), rng.standard_normal(4))
    print(np.linalg.matrix_rank(full), np.linalg.matrix_rank(low))


if __name__ == "__main__":
    main()
