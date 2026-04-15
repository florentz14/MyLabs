import numpy as np
import pandas as pd


frame = pd.DataFrame(
    np.arange(16).reshape((4, 4)),
    index=["red", "blue", "yellow", "white"],
    columns=["ball", "pen", "pencil", "paper"],
)

f_lambda = lambda x: x.max() - x.min()


def f(x):
    return x.max() - x.min()


print("Original DataFrame:")
print(frame)
print()

print("Apply lambda by column (default axis=0):")
print(frame.apply(f_lambda))
print()

print("Apply def function by column (default axis=0):")
print(frame.apply(f))
print()

print("Apply function by row (axis=1):")
print(frame.apply(f, axis=1))
