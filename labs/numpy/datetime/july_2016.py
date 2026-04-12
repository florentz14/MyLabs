# ------------------------------------------------------------ #
# File: july_2016.py
# Date: 2026-04-02
# Author: Florentino
# Description: All calendar dates in July 2016.
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    d = np.arange("2016-07", "2016-08", dtype="datetime64[D]")
    print(d)


if __name__ == "__main__":
    main()
