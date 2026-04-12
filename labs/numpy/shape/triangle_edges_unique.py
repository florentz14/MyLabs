# ------------------------------------------------------------ #
# File: triangle_edges_unique.py
# Date: 2026-04-02
# Author: Florentino
# Description: Unique undirected edges from triangle vertex triplets.
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    rng = np.random.default_rng(7)
    triplets = rng.integers(0, 8, size=(10, 3))
    e = []
    for t in triplets:
        a, b, c = t
        e.extend(((min(a, b), max(a, b)), (min(b, c), max(b, c)), (min(c, a), max(c, a))))
    edges = np.array(e)
    uniq = np.unique(edges, axis=0)
    print(uniq.shape)


if __name__ == "__main__":
    main()
