# ------------------------------------------------------------ #
# File: 31_read_table_with_sep.py
# Date: 2026-04-15
# Author: Florentino
# Description: 31 read table with sep script.
# Explanation: It explains 31 read table with sep script and why it is useful in basic data analysis.
# ------------------------------------------------------------ #

from pathlib import Path

import pandas as pd


csv_path = Path(__file__).parent.parent / "data" / "store_inventory.csv"
table_frame = pd.read_table(csv_path, sep=",")

print("read_table(..., sep=','):")
print(table_frame)
