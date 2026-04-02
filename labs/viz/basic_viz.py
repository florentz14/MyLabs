# ------------------------------------------------------------ #
# File: basic_viz.py
# Date: 2026-04-01
# Author: Florentino
# Description: Minimal line chart saved to disk (no GUI / Agg backend).
# ------------------------------------------------------------ #

from __future__ import annotations

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from settings import GEN_PATH


def main() -> None:
    out = GEN_PATH / "basic_viz.png"
    x = [1, 2, 3, 4]
    y = [1, 4, 2, 5]

    fig, ax = plt.subplots(figsize=(5, 3))
    ax.plot(x, y, marker="o")
    ax.set_title("Basic line plot")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    fig.tight_layout()
    fig.savefig(out, dpi=120)
    plt.close(fig)

    print(f"Saved {out}")


if __name__ == "__main__":
    main()
