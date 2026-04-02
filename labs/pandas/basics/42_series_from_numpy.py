# ------------------------------------------------------------ #
# File: series_from_numpy.py
# Date: 2026-04-01
# Author: Florentino
# Description: Create a Series from a NumPy array.
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np
import pandas as pd


def main() -> None:
    np_array = np.array([1.1, 2.2, 3.3, 4.4, 5.5])
    np_series = pd.Series(np_array)
    print("Series from a NumPy array:")
    print(np_series)


if __name__ == "__main__":
    main()
