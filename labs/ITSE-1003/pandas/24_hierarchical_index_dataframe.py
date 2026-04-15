# ------------------------------------------------------------ #
# File: 24_hierarchical_index_dataframe.py
# Date: 2026-04-15
# Author: Florentino
# Description: 24 hierarchical index dataframe script.
# Explanation: It explains 24 hierarchical index dataframe script and why it is useful in basic data analysis.
# ------------------------------------------------------------ #

import numpy as np
import pandas as pd


frame = pd.DataFrame(
    np.arange(12).reshape((4, 3)),
    index=[
        ["group1", "group1", "group2", "group2"],
        ["row1", "row2", "row1", "row2"],
    ],
    columns=["A", "B", "C"],
)

print("DataFrame with hierarchical row index:")
print(frame)
print()

print("Select first-level group 'group1':")
print(frame.loc["group1"])
print()

print("Select single row ('group2', 'row1'):")
print(frame.loc[("group2", "row1")])
