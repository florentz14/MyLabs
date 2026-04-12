# ------------------------------------------------------------ #
# File: bootstrap_ci_mean.py
# Date: 2026-04-02
# Author: Florentino
# Description: Bootstrap 95% CI for the mean.
# ------------------------------------------------------------ #

from __future__ import annotations

import numpy as np


def main() -> None:
    rng = np.random.default_rng(18)
    x = rng.standard_normal(80)
    n_boot = 10_000
    idx = rng.integers(0, len(x), size=(n_boot, len(x)))
    means = x[idx].mean(axis=1)
    lo, hi = np.percentile(means, [2.5, 97.5])
    print(lo, hi, x.mean())


if __name__ == "__main__":
    main()
