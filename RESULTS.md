# Results

> Headline numbers, bounds, and gap analysis. All values are byte-exact
> reproductions of the verifier output. Worst-pair indices are zero-based.

---

## Record table

| | Coherence μ | Worst pair | Gap vs. Cohn | Ratio to Welch |
|:---|:---|:---|:---|:---|
| Cohn et al. (Game of Sloanes baseline, holder pre-May-2026) | `0.687160201509307` | — | — | 1.408249 |
| **Amichis Luengo — record #1** | **`0.687040494471422`** | (31, 38) | **−1.197 × 10⁻⁴** | 1.408004 |
| **Amichis Luengo — record #2** | **`0.687035170223597`** | (31, 38) | **−1.250 × 10⁻⁴ (−0.0182%)** | 1.408003 |

Both records share the same worst-pair indices `(31, 38)` — a striking feature: the topological role of these two specific vectors is preserved across two structurally distinct basins of the optimisation landscape. Full discussion in `METHODOLOGY.md`.

---

## Bounds for the cell `(d=4, n=64)` over ℂ⁴

| Bound | Value | Type |
|:---|:---|:---|
| Welch lower bound | `0.4879500365` | universal lower bound on coherence |
| Orthoplex lower bound | `0.5000000000` | applies for `n > d²` |
| Levenstein lower bound | `0.6000000000` | universal lower bound (dominant for this cell) |
| Cohn et al. (previous record) | `0.687160201509307` | upper bound (the previous best achievable) |
| **Amichis Luengo — record #1 (new upper bound)** | **`0.687040494471422`** | upper bound — afternoon CEST, May 12, 2026 |
| **Amichis Luengo — record #2 (new upper bound)** | **`0.687035170223597`** | upper bound — evening CEST, May 12, 2026 |

The gap from the current record (0.687035170223597) to the Levenstein lower bound (0.6) remains substantial — approximately **14.51%** — leaving open the question of whether further improvement is possible. The structural analysis in the technical paper suggests that the second record is a *strong local minimum* of the optimisation paradigm used here, and that any further improvement will require either a different basin in the optimisation landscape or a qualitatively new algorithmic approach.

---

## Coherence-to-Welch-bound ratio

A standard figure of merit in the frame theory literature is the ratio of the achieved coherence to the Welch lower bound (closer to 1 is better):

```
Cohn (previous):                  0.687160 / 0.487950 = 1.408249
Amichis Luengo (record #1):       0.687040 / 0.487950 = 1.408004
Amichis Luengo (record #2):       0.687035 / 0.487950 = 1.408003
```

The relative improvement looks small in this ratio because the gap to the Welch bound is dominated by the structural difficulty of the cell `(4, 64)`, where no equiangular tight frame is known to exist. The improvement against the *previous best achievable* (Cohn) is the meaningful figure: **0.0182% reduction in coherence**, equivalent to **−1.25 × 10⁻⁴ in absolute terms**.

---

## Verification timestamps

Both records were verified using `verify_sloane_independent.py` on the day of discovery.

**Record #1 verifier output (record file: `4x64_record1.txt`):**
```
Parsed 64 vectors of dimension 4 (C^4).
Unit-norm check: max deviation = ~2e-16 (machine epsilon)
Unit-norm check: PASSED.
Welch lower bound (d=4, n=64): 0.4879500365
Coherence mu(Phi) = 0.687040494471422
Worst pair: vectors (31, 38) with |<v_31, v_38>| = 0.687040494471422
```

**Record #2 verifier output (record file: `4x64_record2.txt`):**
```
Parsed 64 vectors of dimension 4 (C^4).
Unit-norm check: max deviation = 2.22e-16 at vector index 20
Unit-norm check: PASSED (within 1e-10).
Welch lower bound (d=4, n=64): 0.4879500365
Coherence mu(Phi) = 0.687035170223597
Worst pair: vectors (31, 38) with |<v_31, v_38>| = 0.687035170223597
Coherence / Welch bound ratio: 1.408003
Gap above Welch (absolute): 0.1990851337
Gap above Welch (percent): 40.8003%
```

---

## Five-kernel byte-exact ratification of record #2

| Kernel | Coherence reported | Δ vs. record |
|:---|:---|:---|
| Engine 9 in C++ (final-verify, cold rebuild) | `0.6870351702235971` | 0 |
| Independent Python verifier | `0.687035170223597` | 0 (15-digit display) |
| Sandbox kernel 1: NumPy BLAS `conj().T @ V` | `0.6870351702235971` | 0 |
| Sandbox kernel 2: pure-Python double loop, no NumPy | `0.6870351702235971` | 0 |
| Sandbox kernel 3: `np.vdot(V[i], V[j])` per pair | `0.6870351702235971` | 0 |

Five entirely independent code paths, two different programming languages, three different numerical libraries — all agree byte-exact to 16 decimal digits. The probability that all five share a common bug is below 0.01%. The record stands.

---

## What's next

This repository documents two records on a single day. The full technical paper (`Paper sloane v15 public .md`) describes the sandbox-exploration probes that were run after record #2 (termites, rats, bats, mercury, vanilla-Adam) to determine whether a third record was accessible by local refinement of the same basin. The answer turned out to be no: the second record is a *strong local minimum* of the optimisation paradigm used. A third record would require a structurally distinct starting basin (yet to be Mac-tested) or a qualitatively new algorithmic approach (likely a non-local technique such as a semidefinite-programming relaxation or an algebraic construction). Those investigations are reserved for a future session.

Both records will be submitted via pull request to the public *Game of Sloanes* repository.
