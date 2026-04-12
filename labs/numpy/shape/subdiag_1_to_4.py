# ------------------------------------------------------------ #
# File: subdiag_1_to_4.py
# Date: 2026-04-02
# Author: Florentino
# Description: 5×5 matrix with 1,2,3,4 on the first sub-diagonal.
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    a = np.diag(np.arange(1, 5), k=-1)
    print(a)


if __name__ == "__main__":
    main()
