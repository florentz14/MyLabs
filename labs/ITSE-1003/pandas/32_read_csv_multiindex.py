# ------------------------------------------------------------ #
# File: 32_read_csv_multiindex.py
# Date: 2026-04-15
# Author: Florentino
# Description: 32 read csv multiindex script.
# Explanation: It explains 32 read csv multiindex script and why it is useful in basic data analysis.
# ------------------------------------------------------------ #

from pathlib import Path

import pandas as pd


csv_path = Path(__file__).parent.parent / "data" / "color_status_metrics.csv"
multi_index_frame = pd.read_csv(csv_path, index_col=["color", "status"])

print("read_csv(..., index_col=['color', 'status']):")
print(multi_index_frame)
