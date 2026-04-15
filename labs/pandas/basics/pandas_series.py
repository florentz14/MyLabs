# ------------------------------------------------------------ #
# File: pandas_series.py
# Date: 2026-04-12
# Author: Florentino
# Description: Basic track — Series index, dtype, and element-wise ops.
# Explanation: It explains basic track — Series index, dtype, and element-wise ops and why it is useful in basic data analysis.
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd


def main() -> None:
    s = pd.Series([10, 20, 30], index=["a", "b", "c"])
    print("Series:\n", s)
    print("dtype:", s.dtype)
    print("index:", list(s.index))
    print("\ns * 2:\n", s * 2)
    print("\ns.loc['b']:", s.loc["b"])


if __name__ == "__main__":
    main()
