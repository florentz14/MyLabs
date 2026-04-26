# ------------------------------------------------------------ #
# File: wireframe_animated_phase.py
# Date: 2026-04-26
# Author: Florentino Baez
# Professor: Mauricio Quiroga
# Description: Animated 3D wireframe of a radial cosine ripple whose phase advances over 100 frames; prints the average FPS at the end.
# Explanation: Manual frame loop pattern -- remove the previous wireframe, recompute Z = cos(2*pi*X + phi) * (1 - hypot(X, Y)), redraw, then plt.pause(0.001) to let the GUI repaint. Z-limits are pinned so the camera doesn't auto-rescale every frame.
# Note: requires an INTERACTIVE backend (TkAgg, QtAgg, MacOSX, ...). Headless backends like Agg won't render the animation; run with the project venv.
# ------------------------------------------------------------ #

import time

import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(projection="3d")

# Make the X, Y meshgrid: 50x50 grid covering [-1, 1] x [-1, 1].
xs = np.linspace(-1, 1, 50)
ys = np.linspace(-1, 1, 50)
X, Y = np.meshgrid(xs, ys)

# Set the z axis limits up front so the auto-scale doesn't jitter the camera
# as the surface morphs frame to frame.
ax.set_zlim(-1, 1)

# Begin plotting.
wframe = None
tstart = time.time()

# 100 evenly-spaced phases from 0 to ~57 rad (180/pi). The cosine wraps every
# 2*pi, so this loop completes ~9 full cycles -- a smooth ripple animation.
for phi in np.linspace(0, 180.0 / np.pi, 100):
    # Remove the previous wireframe before drawing the new one. Without this
    # step every frame would stack on the canvas and slow down quickly.
    if wframe:
        wframe.remove()

    # Radial cosine: amplitude fades to 0 at the unit-circle boundary because
    # of the (1 - hypot(X, Y)) factor, giving a "drum-skin" look.
    Z = np.cos(2 * np.pi * X + phi) * (1 - np.hypot(X, Y))

    # rstride/cstride=2 means draw every other row/column -> ~25x25 wireframe
    # lines instead of 50x50, which keeps each frame cheap to redraw.
    wframe = ax.plot_wireframe(X, Y, Z, rstride=2, cstride=2)

    # Yield to the GUI loop so the window actually refreshes.
    plt.pause(0.001)

print("Average FPS: %f" % (100 / (time.time() - tstart)))
