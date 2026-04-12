# NumPy Labs (`labs/numpy/`)

One minimal script per operation (from the repo root: `python3 labs/numpy/<topic>/<file>.py`). Scripts that import **`settings`** (e.g. `struct_npy.py`, `split_npy.py`) need **`PYTHONPATH=.`** or **`pip install -e .`** so paths under **`data/gen/`** resolve.

**Related lab areas:** [pandas](../pandas/README.md), [files](../files/README.md) (stdlib text/CSV I/O), [stats](../stats/README.md) (**`statistics`** module), [ml](../ml/README.md), etc.

| File | Role | Description |
| --- | --- | --- |
| `arithmetic/` | Subfolder | Element-wise `+`, `-`, `*`, `/`, `**`, `%`, `sqrt`, `exp`, `sin`, `log`; topic scripts `inplace_uf`, `bool_mask`, `bcast`; drills such as `negate_between_3_8`, `expr_inplace_ab`, `integer_part_four_ways`, … |
| `aggregation/` | Subfolder | `sum`, `mean`, `median`, `std`, `var`, `min`, `max`, `argmin`, `argmax`, `percentile`; topic script `axis_agg`; drills such as `random_min_max`, `random_mean_30`, … |
| `shape/` | Subfolder | `reshape`, `transpose`, `flatten`, `concatenate`, `split`, `ravel`, `expand_dims`, `squeeze`, `vstack`, `hstack`; topic scripts `idx_flat`, `ravel_t`, `vhstack`, `view_copy`, `struct_npy`, `split_npy`; drills such as `rgba_dtype`, `print_all_values`, … |
| `linalg/` | Subfolder | `dot`, `det`, `eye`, `inv`, `matrix_rank`, `eigvals`, `solve`, `norm`, `trace`, `outer`; topic script `elem_matmul`; drills such as `identity_3`, `matmul_5x3_3x2`, `cauchy_matrix`, … |
| `datetime/` | Subfolder | `datetime64` / `timedelta64`: `yesterday_today_tomorrow`, `july_2016` |

Legacy entry: `basic_numpy.py` (tiny array + mean).

---

## Learning path

Short **topic scripts** mirror a classic NumPy tour: run them in order if you want a linear path. The **100-style drills** table below is separate bite-sized practice.

**Assumptions:** Python 3.10+ and NumPy installed.

### Concept map

| File | Role | Description |
| --- | --- | --- |
| Arithmetic | Concept | Element-wise `+`, `-`, `*`, `/`, `**`; matrix product `@` / `dot` (not `*`) |
| Updates | Concept | In-place `+=`, `-=`; no C-style `++` / `--` |
| ufuncs | Concept | `np.sin`, `np.sqrt`, … on whole arrays |
| Aggregation | Concept | `sum`, `min`, `max`, … and `axis=` |
| Indexing | Concept | Slicing, fancy indexing, `flat` |
| Boolean masks | Concept | Comparisons, `a[mask]`, `a[cond] = …` |
| Shape | Concept | `reshape`, `ravel`, `T`, stack / split |
| Views vs copies | Concept | Slices often share memory; `.copy()` when you need isolation |
| Broadcasting | Concept | How different shapes combine (e.g. scalar + array) |
| Structured arrays | Concept | `dtype` with named fields |
| I/O | Concept | `.npy` / `.npz`; `loadtxt` / `genfromtxt` for text |

### Topic scripts (short names)

| File | Role | Description |
| --- | --- | --- |
| `elem_matmul.py` | Topic script | `linalg/` — Vectors: `+`, `-`, `**`; matrices: `*` (element-wise) vs `@` (matmul) |
| `inplace_uf.py` | Topic script | `arithmetic/` — `+=` / `-=`; `np.sin`, `np.sqrt` |
| `axis_agg.py` | Topic script | `aggregation/` — Whole-array `sum` / `max` vs `sum(axis=0)` |
| `idx_flat.py` | Topic script | `shape/` — Slices, slice assignment, `for row in arr`, `arr.flat` |
| `bool_mask.py` | Topic script | `arithmetic/` — Boolean mask, filter, assign through mask |
| `ravel_t.py` | Topic script | `shape/` — `reshape`, `ravel`, `.T` |
| `vhstack.py` | Topic script | `shape/` — `np.vstack`, `np.hstack` |
| `view_copy.py` | Topic script | `shape/` — View mutates base; `.copy()` does not |
| `bcast.py` | Topic script | `arithmetic/` — `vector + scalar`, `matrix + row` |
| `struct_npy.py` | Topic script | `shape/` — Structured array fields; `np.save` / `load` → `data/gen/struct_npy_rand.npy` |
| `split_npy.py` | Topic script | `shape/` — `hsplit` / `vsplit`; `save`/`load`; `genfromtxt` from `StringIO` |

Related drills and one-offs: `linalg/dot.py`, `arithmetic/broadcast_multiply_rgb.py`, `shape/rgba_dtype.py`, `arithmetic/negate_between_3_8.py`, CSV-oriented work under `labs/files/`.

### Technical notes

- **Broadcasting:** trailing dimensions must match or be `1`.
- **`.npy` / `.npz`:** good for NumPy-native round-trips; compact and fast vs plain text.
- **Structured arrays:** handy for mixed dtypes inside NumPy; for large tables, pandas is often simpler.

```bash
# Topic path (from repo root)
PYTHONPATH=. python3 labs/numpy/linalg/elem_matmul.py
PYTHONPATH=. python3 labs/numpy/shape/struct_npy.py
PYTHONPATH=. python3 labs/numpy/shape/split_npy.py
python3 labs/numpy/arithmetic/inplace_uf.py
python3 labs/numpy/aggregation/axis_agg.py
```

---

## NumPy 100–style drills (items 6–15, 18–25, 33–53, 55–100)

Short exercises live **next to the topic** they illustrate (not in a separate `exercises/` folder).

| File | Role | Description |
| --- | --- | --- |
| `zeros_fifth_one.py` | Drill | `shape/` — **6.** Length-10 zeros, index 4 → 1 |
| `arange_10_49.py` | Drill | `shape/` — **7.** `np.arange(10, 50)` |
| `reverse_vector.py` | Drill | `shape/` — **8.** Reverse 1-D with `[::-1]` |
| `reshape_3x3_0_8.py` | Drill | `shape/` — **9.** 3×3 matrix 0…8 |
| `nonzero_indices.py` | Drill | `shape/` — **10.** `np.nonzero` on a small vector |
| `identity_3.py` | Drill | `linalg/` — **11.** 3×3 identity (`np.eye`) |
| `random_3cube.py` | Drill | `shape/` — **12.** Random 3×3×3 |
| `random_min_max.py` | Drill | `aggregation/` — **13.** 10×10 random, `min` / `max` |
| `random_mean_30.py` | Drill | `aggregation/` — **14.** Length-30 random, `mean` |
| `border_ones.py` | Drill | `shape/` — **15.** Ones on border, zeros inside |
| `subdiag_1_to_4.py` | Drill | `shape/` — **18.** 5×5, values 1…4 on first sub-diagonal |
| `checkerboard_8.py` | Drill | `shape/` — **19.** 8×8 checkerboard `(i+j)%2` |
| `unravel_100th.py` | Drill | `shape/` — **20.** `(x,y,z)` of 100th element in `(6,7,8)` (C order, index 99) |
| `checkerboard_tile_8.py` | Drill | `shape/` — **21.** 8×8 checkerboard with `np.tile` |
| `normalize_random_5x5.py` | Drill | `aggregation/` — **22.** Min–max normalize random 5×5 |
| `rgba_dtype.py` | Drill | `shape/` — **23.** RGBA as four `uint8` fields |
| `matmul_5x3_3x2.py` | Drill | `linalg/` — **24.** Matrix product 5×3 @ 3×2 |
| `negate_between_3_8.py` | Drill | `arithmetic/` — **25.** In-place negate for `3 < x < 8` |
| `yesterday_today_tomorrow.py` | Drill | `datetime/` — **33.** `datetime64` + 1 day |
| `july_2016.py` | Drill | `datetime/` — **34.** All days in July 2016 |
| `expr_inplace_ab.py` | Drill | `arithmetic/` — **35.** `((A+B)*(-A/2))` with `out=` |
| `integer_part_four_ways.py` | Drill | `arithmetic/` — **36.** Integer part: `floor`, `trunc`, `astype`, `modf` |
| `matrix_rows_0_to_4.py` | Drill | `shape/` — **37.** 5×5 rows `0…4` (`broadcast_to`) |
| `fromiter_generator.py` | Drill | `shape/` — **38.** `np.fromiter` + generator |
| `linspace_open_0_1.py` | Drill | `shape/` — **39.** 10 values strictly between 0 and 1 |
| `sort_random_vector.py` | Drill | `shape/` — **40.** Sort random length-10 vector |
| `add_reduce_sum.py` | Drill | `aggregation/` — **41.** `np.add.reduce` vs `sum` |
| `arrays_equal.py` | Drill | `shape/` — **42.** `array_equal` / `allclose` |
| `readonly_flags.py` | Drill | `shape/` — **43.** `flags.writeable = False` |
| `cartesian_to_polar.py` | Drill | `shape/` — **44.** `hypot`, `arctan2` |
| `replace_max_zero.py` | Drill | `shape/` — **45.** Replace max by 0 |
| `structured_grid_xy.py` | Drill | `shape/` — **46.** Structured `(x,y)` on `[0,1]²` grid |
| `cauchy_matrix.py` | Drill | `linalg/` — **47.** `1/(x_i - y_j)` |
| `iinfo_finfo_print.py` | Drill | `shape/` — **48.** `np.iinfo` / `np.finfo` |
| `print_all_values.py` | Drill | `shape/` — **49.** `set_printoptions(threshold=…)` |
| `closest_to_scalar.py` | Drill | `aggregation/` — **50.** Nearest value via `argmin` on `\|v-z\|` |
| `structured_xy_rgb.py` | Drill | `shape/` — **51.** Structured position + RGB |
| `pairwise_distances.py` | Drill | `shape/` — **52.** Consecutive distances on `(100,2)` |
| `float32_to_int32_inplace.py` | Drill | `shape/` — **53.** `astype` / `copyto` to int32 |

### Items 55–100

| File | Role | Description |
| --- | --- | --- |
| `ndenumerate.py` | Drill | `shape/` — **55.** Walk N-D index + value pairs with `np.ndenumerate` |
| `gaussian_2d.py` | Drill | `shape/` — **56.** Build or sample a 2-D Gaussian bump / grid |
| `random_p_elements_2d.py` | Drill | `shape/` — **57.** Choose `p` distinct cells from a 2-D array |
| `row_subtract_mean.py` | Drill | `aggregation/` — **58.** Center each row by subtracting its mean |
| `sort_by_column.py` | Drill | `shape/` — **59.** Sort matrix rows using a chosen column as key |
| `has_null_columns.py` | Drill | `shape/` — **60.** Find columns that are all NaN (or “null”) |
| `nearest_value.py` | Drill | `aggregation/` — **61.** Nearest entry in an array to each query value |
| `nditer_sum_broadcast.py` | Drill | `shape/` — **62.** `np.nditer` with reduction and broadcasting |
| `named_ndarray.py` | Drill | `shape/` — **63.** Subclass `ndarray` with an extra name field |
| `add_at_repeated_indices.py` | Drill | `arithmetic/` — **64.** Accumulate with `np.add.at` at repeated indices |
| `accumulate_weights_by_index.py` | Drill | `aggregation/` — **65.** Sum weights bucketed by integer labels |
| `unique_rgb_colors.py` | Drill | `shape/` — **66.** Count distinct RGB tuples in an image-like array |
| `sum_axes_last_two.py` | Drill | `aggregation/` — **67.** Sum over the last two axes of an N-D array |
| `mean_by_subset_index.py` | Drill | `aggregation/` — **68.** Grouped mean using an index / label array |
| `dot_product_diagonal.py` | Drill | `linalg/` — **69.** Diagonal of `A @ B` via `einsum` (avoid full matmul) |
| `interleave_three_zeros.py` | Drill | `shape/` — **70.** Insert runs of zeros between blocks of data |
| `broadcast_multiply_rgb.py` | Drill | `arithmetic/` — **71.** Scale RGB planes with a broadcast 1×1×3 vector |
| `swap_rows.py` | Drill | `shape/` — **72.** Exchange two rows of a 2-D array in place |
| `triangle_edges_unique.py` | Drill | `shape/` — **73.** Unique undirected edges from integer triples |
| `inverse_bincount.py` | Drill | `shape/` — **74.** Rebuild a 1-D array from bin counts (inverse of `bincount`) |
| `sliding_mean.py` | Drill | `aggregation/` — **75.** Moving average with a 1-D sliding window |
| `sliding_window_matrix.py` | Drill | `shape/` — **76.** Slide a window over a 2-D array (stacked patches) |
| `inplace_negate_sign.py` | Drill | `arithmetic/` — **77.** Flip signs using `np.sign` / multiply by −1 in place |
| `point_to_line_distance.py` | Drill | `shape/` — **78.** Distance from points to a single line (geometry) |
| `points_to_lines_distance.py` | Drill | `shape/` — **79.** Distances from point set to several lines |
| `extract_centered_patch.py` | Drill | `shape/` — **80.** Crop a fixed-size window around a center index |
| `rolling_windows_1d.py` | Drill | `shape/` — **81.** 1-D signal → matrix of overlapping windows |
| `rank_low_vs_full.py` | Drill | `linalg/` — **82.** Compare rank of a product vs full matrix (see `matrix_rank.py`) |
| `mode_most_frequent.py` | Drill | `aggregation/` — **83.** Most frequent value in an array |
| `sliding_window_3x3.py` | Drill | `shape/` — **84.** 3×3 neighborhood operation on a grid |
| `symmetric_ndarray_subclass.py` | Drill | `shape/` — **85.** Enforce symmetry in a custom `ndarray` subclass |
| `batched_matvec_sum.py` | Drill | `linalg/` — **86.** Stack of matrix–vector products then sum |
| `block_sum_4x4.py` | Drill | `aggregation/` — **87.** Sum non-overlapping 4×4 tiles in a grid |
| `game_of_life.py` | Drill | `shape/` — **88.** One (or more) steps of Conway’s Game of Life |
| `n_largest.py` | Drill | `aggregation/` — **89.** Find the `n` largest elements (indices or values) |
| `cartesian_product_many.py` | Drill | `shape/` — **90.** Cartesian product of several 1-D coordinate arrays |
| `record_from_arrays.py` | Drill | `shape/` — **91.** Build structured / record array from column vectors |
| `cube_three_ways.py` | Drill | `arithmetic/` — **92.** Same 3-D cube built with three different NumPy idioms |
| `rows_containing_multiset.py` | Drill | `shape/` — **93.** Rows whose multiset of entries matches a target |
| `rows_not_all_equal.py` | Drill | `shape/` — **94.** Mask rows where values are not all the same |
| `int_to_binary_matrix.py` | Drill | `shape/` — **95.** Encode integers as rows of binary bits |
| `unique_rows_2d.py` | Drill | `shape/` — **96.** Unique rows of a 2-D array (order-preserving or sorted) |
| `einsum_inner_outer.py` | Drill | `shape/` — **97.** Inner and outer products via `np.einsum` |
| `equidistant_path_samples.py` | Drill | `shape/` — **98.** Evenly spaced samples along a piecewise-linear path |
| `multinomial_rows_select.py` | Drill | `shape/` — **99.** Multinomial draws then pick columns per row |
| `bootstrap_ci_mean.py` | Drill | `aggregation/` — **100.** Bootstrap confidence interval for the mean |

Example:

```bash
python3 labs/numpy/shape/zeros_fifth_one.py
python3 labs/numpy/aggregation/random_mean_30.py
python3 labs/numpy/datetime/july_2016.py
```
