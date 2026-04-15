# ------------------------------------------------------------ #
# File: 26_stack_unstack_leveling.py
# Date: 2026-04-15
# Author: Florentino
# Description: 26 stack unstack leveling script.
# Explanation: It explains 26 stack unstack leveling script and why it is useful in basic data analysis.
# ------------------------------------------------------------ #

import numpy as np
import pandas as pd


frame = pd.DataFrame(
    np.arange(8).reshape((2, 4)),
    index=["row1", "row2"],
    columns=[
        ["groupA", "groupA", "groupB", "groupB"],
        ["x", "y", "x", "y"],
    ],
)

print("DataFrame with hierarchical columns:")
print(frame)
print()

stacked = frame.stack()
print("frame.stack():")
print(stacked)
print()

print("stacked.unstack():")
print(stacked.unstack())
