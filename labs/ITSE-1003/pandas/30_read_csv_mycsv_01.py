# ------------------------------------------------------------ #
# File: 30_read_csv_mycsv_01.py
# Date: 2026-04-15
# Author: Florentino
# Description: 30 read csv mycsv 01 script.
# Explanation: It explains 30 read csv mycsv 01 script and why it is useful in basic data analysis.
# ------------------------------------------------------------ #

from pathlib import Path

import pandas as pd


csv_path = Path(__file__).parent.parent / "data" / "people_basic.csv"
csvframe = pd.read_csv(csv_path)

print("csvframe:")
print(csvframe)
