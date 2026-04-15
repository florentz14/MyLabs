# ------------------------------------------------------------ #
# File: 10_statistics_describe.py
# Date: 2026-04-15
# Author: Florentino
# Description: 10 statistics describe script.
# Explanation: It explains 10 statistics describe script and why it is useful in basic data analysis.
# ------------------------------------------------------------ #

import numpy as np
import pandas as pd


frame = pd.DataFrame(
    np.arange(16).reshape((4, 4)),
    index=["red", "blue", "yellow", "white"],
    columns=["ball", "pen", "pencil", "paper"],
)

print("frame.describe():")
print(frame.describe())
