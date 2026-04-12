# ------------------------------------------------------------ #
# File: introduction.py
# Date: 2026-04-12
# Author: Florentino
# Description: Basic track — what pandas is and verify the install.
# ------------------------------------------------------------ #

from __future__ import annotations

import pandas as pd


def main() -> None:
    print("Pandas is a library for tabular data: Series (1D) and DataFrame (2D).")
    print("It builds on NumPy and fits CSV, Excel, SQL, and JSON workflows.")
    print(f"pandas version: {pd.__version__}")


if __name__ == "__main__":
    main()
