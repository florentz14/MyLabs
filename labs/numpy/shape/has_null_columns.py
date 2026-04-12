# ------------------------------------------------------------ #
# File: has_null_columns.py
# Date: 2026-04-02
# Author: Florentino
# Description: Detect columns that are all NaN ("null").
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    a = np.array([[1.0, np.nan, 3.0], [4.0, np.nan, 6.0]])
    null_cols = np.isnan(a).all(axis=0)
    print("null columns:", null_cols)


if __name__ == "__main__":
    main()
