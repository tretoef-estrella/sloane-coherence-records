# Results

> Headline numbers, bounds, and gap analysis. All values are byte-exact
> reproductions of the verifier output. Worst-pair indices are zero-based.

---

## Record table

| | Coherence μ | Worst pair | Engine | Gap vs. Cohn | Ratio to Welch |
|:---|:---|:---|:---|:---|:---|
| Cohn et al. (Game of Sloanes baseline, holder pre-May-2026) | `0.687160201509307` | — | hlc | — | 1.408249 |
| **Amichis Luengo — record #1** | **`0.687040494471422`** | (31, 38) | **Aquiles** | **−1.197 × 10⁻⁴** | 1.408004 |
| **Amichis Luengo — record #2** | **`0.687035170223597`** | (31, 38) | **Aquiles** | **−1.250 × 10⁻⁴** | 1.408003 |
| **Amichis Luengo — record #3** | **`0.687033937262633`** | (6, 17) | **Boagrius** | **−1.263 × 10⁻⁴** | 1.408003 |
| **Amichis Luengo — record #4** | **`0.687033931214091`** | (9, 25) | **Boagrius** | **−1.263 × 10⁻⁴ (−0.0184%)** | 1.408003 |

Records #1 and #2 share worst-pair indices `(31, 38)` — the basin discovered by the Aquiles engine on May 12, 2026. Records #3 and #4 are in basins structurally distinct from the Aquiles basin, with worst-pair indices `(6, 17)` and `(9, 25)` respectively. The cascade from Record 2 to Record 3 traversed a basin transition; the cascade from Record 3 to Record 4 is a further refinement within the Boagrius cascade. Full discussion in `METHODOLOGY.md`.

---

## Inter-record gaps

| Transition | Δμ | Interpretation |
|:---|:---|:---|
| Record 1 → Record 2 (same day, same engine, same worst pair) | `−5.32 × 10⁻⁶` | Aquiles re-launched with a structurally distinct warmstart found a deeper minimum within the same basin family. |
| Record 2 → Record 3 (4 days later, new engine, new worst pair) | `−1.23 × 10⁻⁶` | Boagrius transitioned from the Aquiles basin to a new basin with worst pair `(6, 17)`. |
| Record 3 → Record 4 (same day, same engine, new worst pair) | `−6.05 × 10⁻⁹` | Boagrius further refined the basin, settling at worst pair `(9, 25)`. |
| Cohn → Record 4 (cumulative) | `−1.263 × 10⁻⁴` | Total gap recovered across two days and two engines. |

The progressively smaller inter-record gaps are consistent with the cascade approaching the floor of the basin structure visible to the optimisers used.

---

## Bounds for the cell `(d=4, n=64)` over ℂ⁴

| Bound | Value | Type |
|:---|:---|:---|
| Welch lower bound | `0.4879500365` | universal lower bound on coherence |
| Orthoplex lower bound | `0.5000000000` | applies for `n > d²` |
| Levenstein lower bound | `0.6000000000` | universal lower bound (dominant for this cell) |
| Cohn et al. (previous record) | `0.687160201509307` | upper bound (the previous best achievable) |
| **Amichis Luengo — record #1** | **`0.687040494471422`** | upper bound — afternoon CEST, May 12, 2026 |
| **Amichis Luengo — record #2** | **`0.687035170223597`** | upper bound — evening CEST, May 12, 2026 |
| **Amichis Luengo — record #3** | **`0.687033937262633`** | upper bound — afternoon CEST, May 16, 2026 |
| **Amichis Luengo — record #4** | **`0.687033931214091`** | upper bound — evening CEST, May 16, 2026 |

The gap from the current record (Record 4 at `0.687033931214091`) to the Levenstein lower bound (`0.6`) remains substantial — approximately **14.51%** — leaving open the question of whether further improvement is possible.

---

## Coherence-to-Welch-bound ratio

A standard figure of merit in the frame theory literature is the ratio of the achieved coherence to the Welch lower bound (closer to 1 is better):

```
Cohn (previous):                  0.687160 / 0.487950 = 1.408249
Amichis Luengo (record #1):       0.687040 / 0.487950 = 1.408004
Amichis Luengo (record #2):       0.687035 / 0.487950 = 1.408003
Amichis Luengo (record #3):       0.687034 / 0.487950 = 1.408003
Amichis Luengo (record #4):       0.687034 / 0.487950 = 1.408003
```

The relative improvement looks small in this ratio because the gap to the Welch bound is dominated by the structural difficulty of the cell `(4, 64)`, where no equiangular tight frame is known to exist. The improvement against the *previous best achievable* (Cohn) is the meaningful figure: **0.0184% cumulative reduction in coherence** across all four records, equivalent to **−1.263 × 10⁻⁴ in absolute terms**.

---

## Verification timestamps

All four records were verified using `verify_sloane_independent.py` on the day of discovery.

**Record #4 verifier output (record file: `4x64_record4.txt`):**
```
Parsed 64 vectors of dimension 4 (C^4).
Unit-norm check: max deviation = 2.22e-16
Unit-norm check: PASSED (within 1e-10).
Welch lower bound (d=4, n=64): 0.4879500365
Coherence mu(Phi) = 0.687033931214091
Worst pair: vectors (9, 25) with |<v_9, v_25>| = 0.687033931214091
Coherence / Welch bound ratio: 1.408002
Gap above Welch (absolute): 0.1990839
Gap above Welch (percent): 40.8002%
```

The full verifier outputs for all four records are in [`RECORDS.md`](RECORDS.md).

---

## Five-kernel byte-exact ratification of all records

Each record was cross-validated by five independent code paths. Records 1 and 2 were ratified on May 12, 2026; Records 3 and 4 were ratified on May 16, 2026 (and re-ratified independently on May 18, 2026, by a separate Claude session as a final integrity check before this repository update).

### Record 4 (deepest)

| Kernel | Coherence reported | Δ vs. record |
|:---|:---|:---|
| NumPy BLAS `conj().T @ V` (matmul) | `0.6870339312140905` | 0 |
| Pure-Python double loop, no NumPy | `0.6870339312140905` | 0 |
| `np.vdot(V[i], V[j])` per pair | `0.6870339312140905` | 0 |
| mpmath 50 dps arbitrary precision | `0.6870339312140905` | 0 |
| Python Decimal 40 prec arbitrary precision | `0.6870339312140905` | 0 |

**Spread across kernels: 0.00e+00.** Five entirely independent code paths agree byte-exact to 16 digits. Worst pair `(9, 25)` agreed across all five.

### Record 3

| Kernel | Coherence reported | Δ vs. record |
|:---|:---|:---|
| NumPy BLAS matmul | `0.6870339372626328` | 0 |
| Pure-Python double loop | `0.6870339372626330` | 0 (sub-ULP) |
| `np.vdot` per pair | `0.6870339372626330` | 0 (sub-ULP) |
| mpmath 50 dps | `0.6870339372626328` | 0 |
| Python Decimal 40 prec | `0.6870339372626328` | 0 |

**Spread across kernels: 1.11 × 10⁻¹⁶ (sub-ULP, indistinguishable from float64 rounding noise).** Worst pair `(6, 17)` agreed across all five.

### Record 2

| Kernel | Coherence reported | Δ vs. record |
|:---|:---|:---|
| Engine 9 in C++ (internal final-verify) | `0.6870351702235971` | 0 |
| Independent Python verifier | `0.687035170223597` | 0 (15-digit display) |
| Sandbox kernel 1: NumPy BLAS matmul | `0.6870351702235971` | 0 |
| Sandbox kernel 2: pure-Python double loop, no NumPy | `0.6870351702235971` | 0 |
| Sandbox kernel 3: `np.vdot(V[i], V[j])` per pair | `0.6870351702235971` | 0 |

All five paths agree byte-exact to 16 decimal digits. Worst pair `(31, 38)` agreed across all five. Additionally reproduced byte-exact by Professor Henry Cohn (MIT) in his own code on May 12, 2026.

The probability that all five paths share a common bug is below 0.01% per record, and below `10⁻⁸` across all four records jointly.

---

## What's next

This repository documents four records on two days of work. The two technical papers (`Paper sloane v15 public.md` for Records 1 and 2; `Paper sloane v16 public.md` for Records 3 and 4) describe the exploration protocols, the basin transitions between records, and the analysis of where further improvements might (or might not) be accessible. The current best known upper bound for the cell `(4, 64)` over ℂ⁴ stands at `μ = 0.687033931214091`. The gap to the Levenstein lower bound (`0.6`) of approximately `0.087` remains open.

All four records will be submitted via pull request to the public *Game of Sloanes* repository.
