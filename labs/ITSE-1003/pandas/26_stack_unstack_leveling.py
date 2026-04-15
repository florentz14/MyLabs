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
