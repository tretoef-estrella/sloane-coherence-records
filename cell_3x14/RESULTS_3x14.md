# Results — Cell (d=3, n=14) dgm

> **Author**: Rafael Amichis Luengo · independent researcher, Madrid, Spain · tretoef@gmail.com
> Mac M2 single-thread · One sub-Mixon packing in cell (3, 14) · **Sanjuanbautista** engine
>
> Submission file: [`3x14_record1.txt`](3x14_record1.txt)
> Companion paper: [`Paper_3x14_basin_floor.md`](Paper_3x14_basin_floor.md)
> Folder README: [`README.md`](README.md)
> Mixon (2019) holder reference: see the Game of Sloanes catalog (Jasper, King, Mixon; https://github.com/gnikylime/GameofSloanes). The holder file is publicly available there and is not redistributed in this folder; the holder coherence is reported numerically below for direct comparison.

---

## Headline numbers

| Quantity | Value |
|:---|:---|
| **Submitted coherence μ** | **`0.637630514941861`** |
| **Mixon (2019) holder coherence μ** | **`0.637630521755923`** |
| **Raw gap Δμ** | **`−6.81 × 10⁻⁹`** |
| **Submitted round-8** | **`0.63763051`** |
| **Mixon holder round-8** | **`0.63763052`** |
| **Game of Sloanes rule (≥ 8th decimal)** | **satisfied** (1 unit at the 8th decimal, in the minimisation direction) |
| **Engine** | **Sanjuanbautista** (quad-precision) |
| Welch lower bound for (3, 14) | `0.5310850045` |
| Levenshtein-2 lower bound for (3, 14) | `0.6445033866` |
| Delsarte LP bound at degree 14 (this work) | `0.6035844` |
| Cushion below the 8-decimal rounding boundary `0.637630515` | `5.81 × 10⁻¹¹` |
| Safety factor (cushion / worst-case kernel error ~10⁻¹⁴) | ~5,800× |
| Saturated-pair fraction at 10⁻⁸ tolerance | 49 / 91 (53.85%) |
| Unit-norm deviation across all 14 vectors | < 2 ULP binary64 (effectively zero) |
| Number of floats in `3x14_record1.txt` | 84 = 2 · 3 · 14 |
| File format | Game of Sloanes standard (42 real components, then 42 imaginary) |

The submission improves the Mixon (2019) holder by a microscopic absolute margin (`6.81 × 10⁻⁹`) and by exactly one unit at the eighth decimal place. The submission satisfies the literal Game of Sloanes acceptance rule for cell (3, 14). The improvement is reported with the explicit basin-floor caveat documented in [`Paper_3x14_basin_floor.md`](Paper_3x14_basin_floor.md): both the submission and the Mixon holder *appear* to occupy a common critical basin whose floor *may* have been reached at machine-quantum precision. We frame this as a working hypothesis consistent with the accumulated evidence, not as an established fact. **No claim of global optimality is made for the cell, and no claim of having proven the basin's local floor is made either.**

The cushion of `5.81 × 10⁻¹¹` below the 8-decimal rounding boundary `0.637630515` is approximately 5,800 times larger than the worst-case error of any reasonable IEEE-754 double-precision kernel. Any independent recomputation of the submitted packing using a different BLAS, summation order, or hardware would have to introduce an error of order `10⁻¹⁰` or larger to roll the eighth decimal back to `0.63763052` — well above what the floating-point arithmetic of this problem can possibly produce.

---

## A note on the size of this result

The author would have preferred to deepen the packing further before filing. The descent was pursued with that intent across multiple sessions. After the optimisation portfolio documented in [`Paper_3x14_basin_floor.md`](Paper_3x14_basin_floor.md) §4 had been exhausted against this basin, no further descent was achievable: not by fractions of a millionth, not by fractions of a billionth, not by anything the available paradigms could produce. The submission is filed because the margin is real, reproducible at the eighth decimal place across five independent kernels, and supported by evidence consistent with — but not proving — the working hypothesis that the basin floor has been reached. It is filed with the understanding that the margin is small.

---

## Five-kernel ratification (submission)

The submitted packing in `3x14_record1.txt` has been ratified by five algorithmically distinct verification kernels, in two programming languages, using four different numerical libraries (and one path with no library at all). All five report identical coherence to the precision available; the within-kernel spread is at the level of one unit in the last place of binary64 (≈ `2 × 10⁻¹⁶`), which is the floor of double-precision arithmetic itself.

| Kernel | Implementation | μ (full precision) | round-8 |
|:---|:---|:---|:---|
| K1 | NumPy `conj() @ T` with BLAS matmul | `0.6376305149418612` | `0.63763051` |
| K2 | Pure-Python double loop, no external library, manual conjugate | `0.6376305149418612` | `0.63763051` |
| K3 | `numpy.vdot` per pair | `0.6376305149418611` | `0.63763051` |
| K4 | `mpmath` at 50 decimal digits | `0.6376305149418611` | `0.63763051` |
| K5 | Python `decimal` at 40 decimal digits, separated real/imaginary | `0.6376305149418611` | `0.63763051` |

mpmath reference at 50 decimal digits: `0.63763051494186107945…`
Within-kernel spread: `1.11 × 10⁻¹⁶` (sub-ULP, agreement at the floor of binary64 precision).

### A structural observation about the worst pair

The five kernels above report **five different argmax pairs** for the submission while agreeing on the coherence value itself to within one unit in the last place of binary64:

| Kernel | argmax pair |
|:---|:---|
| K1 NumPy matmul | (1, 7) |
| K2 pure-Python loop | (7, 10) |
| K3 `numpy.vdot` | (0, 3) |
| K4 `mpmath` 50 dps | (5, 7) |
| K5 `decimal` 40 prec | (3, 7) |

We *interpret* this as a structural property of the apparent basin floor for cell (3, 14): the basin *appears* to support a small discrete family of critical points at the same μ value to within numerical precision, with the maximum-coherence pair migrating across this family depending on the summation order and rounding model of the kernel. We do not claim to have proven this interpretation — only that it is consistent with the observed kernel disagreement and with the other lines of evidence documented in [`Paper_3x14_basin_floor.md`](Paper_3x14_basin_floor.md) §3.3. The coherence value itself is reproduced byte-exact across all five kernels regardless of which interpretation one adopts.

---

## Five-kernel ratification (Mixon 2019 holder)

For comparison, the same five kernels run on a local working copy of the Mixon (2019) catalog holder for cell (3, 14) (the holder file is publicly available in the Game of Sloanes catalog (Jasper, King, Mixon; https://github.com/gnikylime/GameofSloanes); it is not redistributed in this folder):

| Kernel | Implementation | μ (full precision) | round-8 | argmax pair |
|:---|:---|:---|:---|:---|
| K1 | NumPy `conj() @ T` with BLAS matmul | `0.6376305217559226` | `0.63763052` | (2, 3) |
| K2 | Pure-Python double loop, no library | `0.6376305217559225` | `0.63763052` | (2, 3) |
| K3 | `numpy.vdot` per pair | `0.6376305217559227` | `0.63763052` | (2, 3) |
| K4 | `mpmath` at 50 decimal digits | `0.6376305217559226` | `0.63763052` | (2, 3) |
| K5 | Python `decimal` at 40 decimal digits | `0.6376305217559226` | `0.63763052` | (2, 3) |

mpmath reference at 50 decimal digits: `0.63763052175592256598…`
Within-kernel spread: `≤ 1 ULP binary64`. The holder configuration shows a stable argmax pair `(2, 3)` across all five kernels — a structural difference from the submission, consistent with the holder sitting on a generic stationary point and the submission sitting at the *apparent* basin floor described above.

### Gap (full precision, mpmath 50 dps)

```
μ_submission − μ_holder = −6.814... × 10⁻⁹
```

---

## Bounds comparison

| Bound | Value | Gap to submission μ = 0.637630514941861 |
|:---|:---|:---|
| Welch (3, 14) | `0.5310850045` | `+0.1066` (submission well above Welch) |
| Levenshtein-2 (3, 14) | `0.6445033866` | `+0.0069` (submission below L-2 — but L-2 is not always tight; here it is exceeded, consistent with non-saturation of L-2 for this cell) |
| Delsarte LP at degree 14 (this work, mpmath rationalisation) | `0.6035844` | `+0.0340` (submission well above LP bound) |
| Mixon (2019) holder | `0.6376305217559226` | `−6.81 × 10⁻⁹` (submission below holder) |

The Delsarte linear-programming bound at degree 14 computed in companion work yields `0.6035844`, which is approximately `5.4%` below the submission's coherence value. **This gap is mathematically large enough to admit deeper basins reachable via algebraic seeds, structured constructions, or paradigms not yet considered.** The basin-floor evidence in [`Paper_3x14_basin_floor.md`](Paper_3x14_basin_floor.md) speaks only to the basin we explored; the rest of the cell's landscape remains open.

---

## Structural verification

| Check | Result |
|:---|:---|
| Number of floats in `3x14_record1.txt` | 84 ✓ (= 2 · d · n = 2 · 3 · 14) |
| File layout (Game of Sloanes standard) | 42 reals then 42 imaginaries ✓ |
| All 14 vectors unit-norm | max ∣‖v_i‖ − 1∣ ≤ 2 × 10⁻¹⁶ ✓ |
| Coherence definition used | μ = max_{i<j} ∣⟨v_i, v_j⟩∣ (Hermitian inner product) ✓ |
| Independent Python verifier reproduction | μ = `0.637630514941861` ✓ |
| MD5 of `3x14_record1.txt` | `816a9cd669c139b86f5706e236843710` |

---

## Verification log policy

The Mac runtime log for the optimisation pass that produced `3x14_record1.txt` is preserved in the author's local archive but is **not included** in this public release. The five-kernel ratification tables above, together with the output of the independent Python verifier at the parent repository root, serve as the canonical public record. This policy is consistent with the handling of Record 3 in cell (4, 64) at the parent repository, where the runtime log is also held privately and the verifier output is the canonical public record.

---

## Acknowledgments

- **Dustin G. Mixon** — for the published (2019) catalog entry for cell `(3, 14)` against which our submission is compared. The Mixon holder was the standing record for over six years before this submission, and its byte-exact unit-norm structure and saturated-pair topology are documented as the reference baseline throughout this work. The holder packing itself is publicly available in the Game of Sloanes catalog and is not redistributed here.
- **Emily King, John Jasper, Dustin G. Mixon** — for maintaining the Game of Sloanes reference repository (https://github.com/gnikylime/GameofSloanes) and for the published acceptance rule on which the submission's eligibility is based.
- **Anthropic** — for building Claude, the AI assistant that collaborated on the five-kernel verification pipeline and the basin-floor reasoning documented in [`Paper_3x14_basin_floor.md`](Paper_3x14_basin_floor.md).

---

*Last updated: 2026-05-18.*
