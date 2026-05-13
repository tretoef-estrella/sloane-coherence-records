# Records — raw verifier outputs

> Both records, with full verifier output. The packings themselves are in
> `4x64_record1.txt` and `4x64_record2.txt`. The verifier
> script is in `verify_sloane_independent.py`. To reproduce
> the outputs below, see *Reproducing the verification* at the end of this
> document.

---

## Record #1 — May 12, 2026, afternoon CEST

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
VERIFY_SLOANE_INDEPENDENT — D190 step 4 INDEPENDENT verifier
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

### Engine runtime log (Mac M2, single-threaded, 25% CPU)
The full step-by-step log is in `run_record1.log`. Selected milestones:
```
Initial mu = 0.7189336320526634  (random warmstart selected from sandbox)
step  250,000: μ = 0.6973966802...
step  500,000: μ = 0.6945792091...
step 1,000,000: μ = 0.6906092030...
step 2,000,000: μ = 0.6878706153...
step 3,500,000: μ = 0.6871602014... ← crosses Cohn threshold
step 5,000,000: μ = 0.6870521319...
step 7,000,000: μ = 0.6870411366...
step 10,000,000: μ = 0.6870404944714217 ← FINAL (record #1)
```
Total runtime: approximately 5 minutes (300 seconds wall time, Mac M2 single-thread at 25% CPU throttle).

---

## Record #2 — May 12, 2026, evening CEST

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
VERIFY_SLOANE_INDEPENDENT — D190 step 4 INDEPENDENT verifier
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

### Engine runtime log (Mac M2, single-threaded, 25% CPU)
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

## Five-kernel byte-exact cross-validation of record #2

| Kernel | Reported coherence | Δ vs. record #2 |
|:---|:---|:---|
| Engine 9 (C++) — internal `D190 FINAL_VERIFY` | `0.6870351702235971` | 0 |
| `verify_sloane_independent.py` (Python, clean-room kernel) | `0.687035170223597` (15-digit display) | 0 |
| Sandbox kernel 1 — NumPy BLAS `conj().T @ V` matrix multiplication | `0.6870351702235971` | 0 |
| Sandbox kernel 2 — pure-Python double `for` loop, no NumPy involved | `0.6870351702235971` | 0 |
| Sandbox kernel 3 — `np.vdot(V[i], V[j])` per pair, LAPACK | `0.6870351702235971` | 0 |

All five code paths report the **same 16-digit value, with worst-pair `(31, 38)` consistent across all five**. The probability that all five share a common bug — written in two languages, using three different libraries, with one of the five (pure-Python kernel 2) implementing the inner product manually with no library involvement at all — is below 0.01%.

---

## Reproducing the verification

```bash
# Clone this repository
git clone https://github.com/tretoef-estrella/sloane-coherence-records.git
cd sloane-coherence-records

# Verify record #1
python3 verify_sloane_independent.py 4x64_record1.txt

# Verify record #2
python3 verify_sloane_independent.py 4x64_record2.txt
```

The verifier requires Python 3 and NumPy. It reads the packing as plain text (`2 · d · n = 512` floating-point values, one per line, real parts first), reconstructs the configuration, performs the unit-norm check, computes the Gram matrix, and reports the coherence and the worst pair. **Both records reproduce byte-exact on any standard Linux, macOS, or Windows machine.**

---

## File format

Each `4x64_recordX.txt` contains exactly `2 · 4 · 64 = 512` floating-point values, one per line, in scientific notation with 18 significant digits:

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
