# ------------------------------------------------------------ #
# File: sine_wave_simple.py
# Date: 2026-04-26
# Author: Florentino Baez
# Professor: Mauricio Quiroga
# Description: Plot a 1 Hz sine wave (voltage vs time) and save the figure to PNG.
# Explanation: Minimal end-to-end matplotlib example: build the data with NumPy, draw with ax.plot, label everything with ax.set(...), turn on the grid, and persist the figure with fig.savefig before showing it.
# ------------------------------------------------------------ #

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

# Data for plotting: 200 samples covering 2 seconds at 100 Hz, then a 1 Hz
# sine shifted up by 1 so it stays in [0, 2] (i.e. positive "voltage").
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)

fig, ax = plt.subplots()
ax.plot(t, s)

# Bundle xlabel + ylabel + title in one call.
ax.set(
    xlabel="time (s)",
    ylabel="voltage (mV)",
    title="About as simple as it gets, folks",
)

ax.grid()

# Save next to the script in `generated/` so the workspace root stays clean.
OUTPUT_DIR = Path(__file__).parent / "generated"
OUTPUT_DIR.mkdir(exist_ok=True)
output_path = OUTPUT_DIR / "sine_wave.png"
fig.savefig(output_path)
print(f"Figure saved to: {output_path}")

plt.show()
