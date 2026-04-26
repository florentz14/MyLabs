# ------------------------------------------------------------ #
# File: scatter_3d_two_groups.py
# Date: 2026-04-26
# Author: Florentino Baez
# Professor: Mauricio Quiroga
# Description: 3D scatter plot of two random point clouds living at different Z ranges, drawn with different markers (circles vs. triangles).
# Explanation: Activates the 3D axes via `projection='3d'`, generates each cluster with a uniform-random helper, and lets ax.scatter accept (xs, ys, zs) directly so the same API as 2D scatter still works.
# ------------------------------------------------------------ #

import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility (1968-08-01 as integer seed).
np.random.seed(19680801)


def randrange(n, vmin, vmax):
    """Return `n` numbers uniformly distributed in [vmin, vmax)."""
    return (vmax - vmin) * np.random.rand(n) + vmin


fig = plt.figure()

# `projection='3d'` swaps the default Axes for an Axes3D, which adds the z
# dimension and methods like ax.scatter(x, y, z) and ax.set_zlabel(...).
# Stubs return the 2D Axes type, so 3D-specific calls below carry a pyright
# ignore for the extra z arg.
ax = fig.add_subplot(projection="3d")

# Number of points per cluster.
n = 100

# Two clusters share x in [23, 32] and y in [0, 100] but live at different
# z bands so they appear stacked on top of each other in the box.
# Each tuple is (marker, z-min, z-max).
for m, zlow, zhigh in [("o", -50, -25), ("^", -30, -5)]:
    xs = randrange(n, 23, 32)
    ys = randrange(n, 0, 100)
    zs = randrange(n, zlow, zhigh)
    ax.scatter(xs, ys, zs, marker=m)  # pyright: ignore[reportArgumentType]

ax.set_xlabel("X Label")
ax.set_ylabel("Y Label")
ax.set_zlabel("Z Label")

plt.tight_layout()
plt.show()
