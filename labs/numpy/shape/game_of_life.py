# ------------------------------------------------------------ #
# File: game_of_life.py
# Date: 2026-04-02
# Author: Florentino
# Description: One step of Conway's Game of Life (8-neighbor sum via roll).
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def step(z: np.ndarray) -> np.ndarray:
    n = np.zeros_like(z, dtype=np.int32)
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            if dx == 0 and dy == 0:
                continue
            n += np.roll(np.roll(z, dx, axis=0), dy, axis=1)
    return ((n == 3) | (z.astype(bool) & (n == 2))).astype(np.uint8)


def main() -> None:
    rng = np.random.default_rng(12)
    z = rng.integers(0, 2, size=(8, 8), dtype=np.uint8)
    print("before\n", z)
    print("after\n", step(z))


if __name__ == "__main__":
    main()
