# ------------------------------------------------------------ #
# File: dot_product_diagonal.py
# Date: 2026-04-02
# Author: Florentino
# Description: Diagonal of A @ B with einsum.
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    rng = np.random.default_rng(5)
    m = 4
    a = rng.random((m, 3))
    b = rng.random((3, m))
    diag = np.einsum("ij,ji->i", a, b)
    print(np.allclose(diag, (a @ b).diagonal()))


if __name__ == "__main__":
    main()
