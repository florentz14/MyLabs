# ------------------------------------------------------------ #
# File: error_band_along_curve.py
# Date: 2026-04-26
# Author: Florentino Baez
# Professor: Mauricio Quiroga
# Description: Draw a 2D error band around a parametric curve by offsetting each point along its local normal, illustrated with constant vs. variable error magnitudes.
# Explanation: Builds normals via centred finite differences (forward at the first point, backward at the last), then constructs a closed Path that goes outward along (x + n*err) and back along (x - n*err) so the band hugs the curve in 2D regardless of orientation.
# Source pattern: matplotlib gallery (lines_bars_and_markers / curve_error_band).
# ------------------------------------------------------------ #

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import PathPatch
from matplotlib.path import Path


def draw_error_band(ax, x, y, err, **kwargs):
    """Shade a band of half-width `err` around the (x, y) curve on `ax`.

    The band is built by walking each point in the direction perpendicular
    to the local tangent, so the band stays aligned with the curve even when
    it loops or doubles back on itself.
    """
    # Calculate normals via centered finite differences (except the first point
    # which uses a forward difference and the last point which uses a backward
    # difference).
    dx = np.concatenate([[x[1] - x[0]], x[2:] - x[:-2], [x[-1] - x[-2]]])
    dy = np.concatenate([[y[1] - y[0]], y[2:] - y[:-2], [y[-1] - y[-2]]])
    l = np.hypot(dx, dy)
    nx = dy / l
    ny = -dx / l

    # End points of the error: positive normal (xp, yp) and negative (xn, yn).
    xp = x + nx * err
    yp = y + ny * err
    xn = x - nx * err
    yn = y - ny * err

    # Build a closed polygon: forward along the positive offset, then backward
    # along the reversed negative offset.
    vertices = np.block([[xp, xn[::-1]],
                         [yp, yn[::-1]]]).T
    codes = np.full(len(vertices), Path.LINETO)
    codes[0] = codes[len(xp)] = Path.MOVETO
    path = Path(vertices, codes)
    ax.add_patch(PathPatch(path, **kwargs))


# Parametric "cardioid-like" curve used as the demo path: r(t) = 0.5 + cos(t).
N = 400
t = np.linspace(0, 2 * np.pi, N)
r = 0.5 + np.cos(t)
x = r * np.cos(t)
y = r * np.sin(t)

# Two side-by-side panels sharing axes so the bands are visually comparable.
_, axs = plt.subplots(1, 2, layout="constrained", sharex=True, sharey=True)

errs = [
    (axs[0], "constant error", 0.05),
    (axs[1], "variable error", 0.05 * np.sin(2 * t) ** 2 + 0.04),
]

for i, (ax, title, err) in enumerate(errs):
    # `aspect=1` keeps circles round; ticks hidden because the values are
    # arbitrary parametric coords and would only add visual noise.
    ax.set(title=title, aspect=1, xticks=[], yticks=[])
    ax.plot(x, y, "k")
    draw_error_band(
        ax, x, y, err=err,
        facecolor=f"C{i}",  # default cycle colour C0/C1 per panel
        edgecolor="none",
        alpha=0.3,
    )

plt.show()
