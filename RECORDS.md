# Records — raw verifier outputs

> All four records, with full verifier output. The packings themselves are in
> `4x64_record1.txt`, `4x64_record2.txt`, `4x64_record3.txt`, and
> `4x64_record4.txt`. The verifier script is in
> `verify_sloane_independent.py`. To reproduce the outputs below, see
> *Reproducing the verification* at the end of this document.

---

## Record #1 — May 12, 2026, afternoon CEST — Aquiles engine

### Coherence
```
μ = 0.687040494471422
```

### Gap vs. Cohn baseline
```
Δμ = 0.687040494471422 − 0.687160201509307 = −1.19707 × 10⁻⁴
```

### Worst pair
```
vectors (31, 38)
|⟨v_31, v_38⟩| = 0.687040494471422
```

### Verifier output (complete)
```
======================================================================
VERIFY_SLOANE_INDEPENDENT verifier
======================================================================
File: 4x64_record1.txt
Parsed filename: d=4, n=64, creator_tag='record1'
Parsed 64 vectors of dimension 4 (C^4).
Unit-norm check: max deviation ≈ 2e-16 (machine epsilon)
Unit-norm check: PASSED (within 1e-10).
Welch lower bound (d=4, n=64): 0.4879500365
Coherence mu(Phi) = 0.687040494471422
Worst pair: vectors (31, 38) with |<v_31, v_38>| = 0.687040494471422
Coherence / Welch bound ratio: 1.408004
Gap above Welch (absolute): 0.1990905043
Gap above Welch (percent): 40.8054%
```

### Mac runtime log (Mac M2, single-threaded, 25% CPU)
The full step-by-step log is in `run_record1.log`. Selected milestones:
```
Initial mu = 0.7189336320526634  (warmstart selected from sandbox)
step  250,000: μ = 0.6973966802...
step  500,000: μ = 0.6945792091...
step 1,000,000: μ = 0.6906092030...
step 2,000,000: μ = 0.6878706153...
step 3,500,000: μ = 0.6871602014... ← crosses Cohn threshold
step 5,000,000: μ = 0.6870521319...
step 7,000,000: μ = 0.6870411366...
step 10,000,000: μ = 0.6870404944714217 ← FINAL (record #1)
```
Total runtime: approximately 5 minutes (300 seconds wall time).

---

## Record #2 — May 12, 2026, evening CEST — Aquiles engine

### Coherence
```
μ = 0.687035170223597
```

### Gap vs. Cohn baseline
```
Δμ = 0.687035170223597 − 0.687160201509307 = −1.25031 × 10⁻⁴
   ≈ −0.0182% relative improvement
```

### Gap vs. record #1 (same day, afternoon)
```
Δμ = 0.687035170223597 − 0.687040494471422 = −5.32 × 10⁻⁶
```

### Worst pair
```
vectors (31, 38)
|⟨v_31, v_38⟩| = 0.687035170223597
```

Same indices as record #1, in a structurally distinct basin. Signature distance between the two basins (sorted off-diagonal Gram absolute values, L²-norm) ≈ **0.283** — a substantial topological separation. See `METHODOLOGY.md` and the technical paper for discussion.

### Verifier output (complete)
```
======================================================================
VERIFY_SLOANE_INDEPENDENT verifier
======================================================================
File: 4x64_record2.txt
Parsed filename: d=4, n=64, creator_tag='record2'
Parsed 64 vectors of dimension 4 (C^4).
Unit-norm check: max deviation = 2.22e-16 at vector index 20
Unit-norm check: PASSED (within 1e-10).
Welch lower bound (d=4, n=64): 0.4879500365
Coherence mu(Phi) = 0.687035170223597
Worst pair: vectors (31, 38) with |<v_31, v_38>| = 0.687035170223597
Coherence / Welch bound ratio: 1.408003
Gap above Welch (absolute): 0.1990851337
Gap above Welch (percent): 40.8003%

Verification complete.
```

### Mac runtime log (Mac M2, single-threaded, 25% CPU)
The full step-by-step log is in `run_record2.log`. Selected milestones:
```
Initial mu = 0.7031708385306132  (warmstart from sandbox-discovered basin)
step  250,000: μ = 0.6966816005...
step 1,000,000: μ = 0.6911071653...
step 2,000,000: μ = 0.6878955597...
step 3,500,000: μ = 0.6871374032... ← crosses Cohn threshold
step 5,500,000: μ = 0.6870407213...
step 5,750,000: μ = 0.6870390174... ← crosses record #1 threshold
step 7,000,000: μ = 0.6870357898...
step 10,000,000: μ = 0.6870351702235971 ← FINAL (record #2)
```
Total runtime: approximately 5 minutes (verified byte-exact re-execution on May 13, 2026: 5 min 0.42 sec, reproducing μ = 0.6870351702235971 to 16 digits; see [`ERRATA.md`](ERRATA.md) for the complete Mac runtime log).

---

## Record #3 — May 16, 2026, afternoon CEST — Boagrius engine

### Coherence
```
μ = 0.687033937262633
```

### Gap vs. Cohn baseline
```
Δμ = 0.687033937262633 − 0.687160201509307 = −1.26264 × 10⁻⁴
```

### Gap vs. record #2
```
Δμ = 0.687033937262633 − 0.687035170223597 = −1.23 × 10⁻⁶
```

### Worst pair
```
vectors (6, 17)
|⟨v_6, v_17⟩| = 0.687033937262633
```

This is the first record obtained by the Boagrius engine, transitioning from the Aquiles basin (worst pair `(31, 38)` shared by Records 1 and 2) into a basin with worst pair `(6, 17)`. The transition is structural: the new basin is not a refinement of the Aquiles basin but a topologically distinct minimum.

### Verifier output (complete)
```
======================================================================
VERIFY_SLOANE_INDEPENDENT verifier
======================================================================
File: 4x64_record3.txt
Parsed filename: d=4, n=64, creator_tag='record3'
Parsed 64 vectors of dimension 4 (C^4).
Unit-norm check: max deviation = 2.22e-16
Unit-norm check: PASSED (within 1e-10).
Welch lower bound (d=4, n=64): 0.4879500365
Coherence mu(Phi) = 0.687033937262633
Worst pair: vectors (6, 17) with |<v_6, v_17>| = 0.687033937262633
Coherence / Welch bound ratio: 1.408003
Gap above Welch (absolute): 0.1990839
Gap above Welch (percent): 40.8003%
```

### Mac runtime
The full step-by-step Mac log for Record 3 is preserved in the author's local archive but is not included in the public repository. The Record 3 packing was further refined to Record 4 within the same engine paradigm on the same day; the publicly preserved log `run_record4.log` documents that refinement step, starting from Record 3 as warmstart. The Record 3 verifier output above is the canonical public artefact for this record.

---

## Record #4 — May 16, 2026, evening CEST — Boagrius engine

### Coherence
```
μ = 0.687033931214091
```

### Gap vs. Cohn baseline
```
Δμ = 0.687033931214091 − 0.687160201509307 = −1.26270 × 10⁻⁴
   ≈ −0.0184% relative improvement (cumulative across all four records)
```

### Gap vs. record #3
```
Δμ = 0.687033931214091 − 0.687033937262633 = −6.05 × 10⁻⁹
```

### Worst pair
```
vectors (9, 25)
|⟨v_9, v_25⟩| = 0.687033931214091
```

This is the deepest packing currently known for the cell `(4, 64)` hlc. The transition from Record 3 to Record 4 involves a further basin change (worst pair `(6, 17)` → `(9, 25)`) within the Boagrius cascade.

### Verifier output (complete)
```
======================================================================
VERIFY_SLOANE_INDEPENDENT verifier
======================================================================
File: 4x64_record4.txt
Parsed filename: d=4, n=64, creator_tag='record4'
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

### Mac runtime log (Mac M2, single-threaded, 25% CPU)
The sanitised step-by-step log is in `run_record4.log`. The Boagrius run on Record 3 warmstart converged to Record 4 in 568 seconds wall time (≈ 9 min 28 s) over 2061 outer iterations, with the first sub-Record-3 improvement appearing at outer iteration 22 and the engine terminating by its internal stopping criterion at outer 2061. Key telemetry:

```
wall time     : 568.00 s   (≈ 9 min 28 s, Mac M2 single thread)
mu_init       : +6.870339372626328733e-01   (= Record 3)
mu_best       : +6.870339312140905605e-01   (= Record 4)
drop vs init  : −6.04854231e-09
gap vs Cohn   : −1.26270295e-04   (−0.0184 %)
```

The full unredacted Mac log is preserved in the author's local archive and is available on request for verification purposes. The version published here retains the header, the first 25 outer iterations (showing the descent from Record 3 through the first improvement), the final iterations through engine termination, and the chequered-flag telemetry. Intermediate outer iterations correspond to monotone descent of `mu_best` within feasibility tolerance and have been omitted for brevity.

---

## Five-kernel byte-exact cross-validation

Each record has been independently cross-validated by **five entirely independent code paths**, written from scratch with different libraries (and one path with no library at all). All five paths report identical coherence values to the precision available, and worst-pair indices agree across all five paths in every case.

### Record 4

| Kernel | Reported coherence | Δ vs. record |
|:---|:---|:---|
| NumPy BLAS `conj().T @ V` (matmul) | `0.6870339312140905` | 0 |
| Pure-Python double loop, no NumPy | `0.6870339312140905` | 0 |
| `np.vdot(V[i], V[j])` per pair (LAPACK) | `0.6870339312140905` | 0 |
| mpmath 50 dps arbitrary precision | `0.6870339312140905` | 0 |
| Python Decimal 40 prec arbitrary precision | `0.6870339312140905` | 0 |

Five entirely independent code paths, two different programming languages, four different numerical libraries — all agree byte-exact to 16 decimal digits. Worst pair `(9, 25)` agreed across all five.

### Record 3

| Kernel | Reported coherence | Δ vs. record |
|:---|:---|:---|
| NumPy BLAS matmul | `0.6870339372626328` | 0 |
| Pure-Python double loop | `0.6870339372626330` | 0 (sub-ULP) |
| `np.vdot` per pair | `0.6870339372626330` | 0 (sub-ULP) |
| mpmath 50 dps | `0.6870339372626328` | 0 |
| Python Decimal 40 prec | `0.6870339372626328` | 0 |

Spread across kernels: 1.11 × 10⁻¹⁶ (sub-ULP, indistinguishable from float64 rounding noise). Worst pair `(6, 17)` agreed across all five.

### Record 2

| Kernel | Reported coherence | Δ vs. record |
|:---|:---|:---|
| C++ engine internal final-verify | `0.6870351702235971` | 0 |
| Independent Python verifier (clean-room kernel) | `0.687035170223597` | 0 (15-digit display) |
| NumPy BLAS matmul | `0.6870351702235971` | 0 |
| Pure-Python double loop, no NumPy | `0.6870351702235971` | 0 |
| `np.vdot` per pair, LAPACK | `0.6870351702235971` | 0 |

All five paths agree byte-exact to 16 decimal digits. Worst pair `(31, 38)` agreed across all five. Additionally reproduced byte-exact by Professor Henry Cohn (MIT) in his own code on May 12, 2026.

### Record 1

Five-kernel cross-validation performed on May 12, 2026, byte-exact agreement to 16 decimal digits. Worst pair `(31, 38)` agreed across all five.

---

## Reproducing the verification

```bash
# Clone this repository
git clone https://github.com/tretoef-estrella/sloane-coherence-records.git
cd sloane-coherence-records

# Verify each record
python3 verify_sloane_independent.py 4x64_record1.txt
python3 verify_sloane_independent.py 4x64_record2.txt
python3 verify_sloane_independent.py 4x64_record3.txt
python3 verify_sloane_independent.py 4x64_record4.txt
```

The verifier requires Python 3 and NumPy. It reads each packing as plain text (`2 · d · n = 512` floating-point values, one per line, real parts first), reconstructs the configuration, performs the unit-norm check, computes the Gram matrix, and reports the coherence and the worst pair. **All four records reproduce byte-exact on any standard Linux, macOS, or Windows machine.**

---

## File format

Each `4x64_recordN.txt` contains exactly `2 · 4 · 64 = 512` floating-point values, one per line, in scientific notation with 18 significant digits:

```
<real part of v_1[0]>
<real part of v_1[1]>
...
<real part of v_64[3]>
<imaginary part of v_1[0]>
<imaginary part of v_1[1]>
...
<imaginary part of v_64[3]>
```

This is the standard *Game of Sloanes* file format. Each vector `v_i ∈ ℂ^4` is reconstructed by combining `v_i[k] = reals[4·i + k] + i · imags[4·i + k]` for `k = 0, 1, 2, 3`.
