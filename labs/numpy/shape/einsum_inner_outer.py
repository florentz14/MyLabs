# ------------------------------------------------------------ #
# File: einsum_inner_outer.py
# Date: 2026-04-02
# Author: Florentino
# Description: einsum idioms: inner, outer, sum, mul.
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    a = np.arange(1, 4)
    b = np.arange(4, 7)
    print("inner", np.einsum("i,i->", a, b), np.inner(a, b))
    print("outer\n", np.einsum("i,j->ij", a, b))
    print("sum  ", np.einsum("i->", a), a.sum())
    print("mul  ", np.einsum("i,i->i", a, b), a * b)


if __name__ == "__main__":
    main()
