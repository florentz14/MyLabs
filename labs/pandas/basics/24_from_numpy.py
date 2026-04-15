# ------------------------------------------------------------ #
# File: from_numpy.py
# Date: 2026-04-01
# Author: Florentino
# Description: Create a DataFrame from a NumPy array.
# Explanation: It explains create a DataFrame from a NumPy array and why it is useful in basic data analysis.
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np
import pandas as pd


def main() -> None:
    arr = np.array([[1, 2], [3, 4], [5, 6]])
    df = pd.DataFrame(arr, columns=["X", "Y"])
    print(df)


if __name__ == "__main__":
    main()
