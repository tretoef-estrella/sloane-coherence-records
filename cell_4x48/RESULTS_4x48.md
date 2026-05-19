# Results — Cell (d=4, n=48) hlc

> **Author**: Rafael Amichis Luengo · independent researcher, Madrid, Spain · tretoef@gmail.com
> Mac M2 single-thread · One sub-Cohn packing in cell (4, 48) · **Rasputin** engine
>
> Submission file: [`4x48_record1.txt`](4x48_record1.txt)
> Companion paper: [`Paper_4x48.md`](Paper_4x48.md)
> Folder README: [`README.md`](README.md)
> Cohn (catalog) holder reference: see the Game of Sloanes catalog (Jasper, King, Mixon; https://github.com/gnikylime/GameofSloanes). The holder file is publicly available there and is not redistributed in this folder; the holder coherence is reported numerically below for direct comparison.

---

## Headline numbers

| Quantity | Value |
|:---|:---|
| **Submitted coherence μ** | **`0.643425504750473`** |
| **Cohn (catalog) holder coherence μ** | **`0.643427715576853`** |
| **Raw gap Δμ** | **`−2.21 × 10⁻⁶`** |
| **Submitted round-8** | **`0.64342550`** |
| **Cohn holder round-8** | **`0.64342772`** |
| **Game of Sloanes rule (≥ 8th decimal)** | **satisfied** (222 units at the 8th decimal, in the minimisation direction) |
| **Engine** | **Rasputin** (quad-precision) |
| **Worst pair (stable across 5 kernels)** | **(1, 42)** |
| Welch lower bound for (4, 48) | `0.4837794468` |
| Levenshtein-2 lower bound for (4, 48) | `0.5877538100` |
| Cushion to 8-decimal upper boundary `0.643425505` | `2.4953 × 10⁻¹⁰` |
| Cushion to 8-decimal lower boundary `0.643425495` | `9.7505 × 10⁻⁹` |
| Saturated-pair fraction at 10⁻⁸ tolerance | 274 / 1128 (24.29%) |
| Unit-norm deviation across all 48 vectors | `2.21 × 10⁻¹¹` (well within unit-norm tolerance) |
| Number of floats in `4x48_record1.txt` | 384 = 2 · 4 · 48 |
| File format | Game of Sloanes standard (192 real components, then 192 imaginary) |

The submission improves the Cohn (catalog) holder by an absolute margin of `2.21 × 10⁻⁶` and by 222 units at the eighth decimal place (round-8 `0.64342550` versus `0.64342772`). The submission satisfies the Game of Sloanes acceptance rule for cell (4, 48) by a comfortable margin. The improvement is reported with the explicit basin-floor caveat documented in [`Paper_4x48.md`](Paper_4x48.md): the submission appears to occupy a critical basin whose floor may have been reached at machine-quantum precision. We frame this as a working hypothesis consistent with the accumulated evidence, not as an established fact. **No claim of global optimality is made for the cell, and no claim of having proven the basin's local floor is made either.**

The submitted μ sits inside the round-8 band `[0.643425495, 0.643425505]` with cushion `9.7505 × 10⁻⁹` to the lower band edge and cushion `2.4953 × 10⁻¹⁰` to the upper band edge. Any independent recomputation of the submitted packing using a different BLAS, summation order, or hardware would have to introduce an error of order `10⁻¹⁰` or larger near the upper band edge to roll the eighth decimal — well above what the floating-point arithmetic of this problem can possibly produce (five-kernel ratification reports zero ULP spread in binary64).

---

## A note on the size and limits of the result

The improvement reported here is comfortably above the Game of Sloanes acceptance threshold and is delivered on a Cohn-held cell with a number of years' standing. The author records openly that the descent was pursued further than the filing margin would have required; the optimisation portfolio documented in [`Paper_4x48.md`](Paper_4x48.md) §4 was exhausted against the basin before this value was settled, and no method available to this work produced any further descent below the value reported above. The submission is filed because the margin is real, reproducible at the eighth decimal place across five independent kernels, and supported by structural evidence that the basin floor has been reached — under the working hypothesis framed throughout this folder, which we do not claim to have proven.

---

## Five-kernel ratification (submission)

The submitted packing in `4x48_record1.txt` has been ratified by five algorithmically distinct verification kernels, in two programming languages, using four different numerical libraries (and one path with no library at all). All five report identical coherence to the precision available; the spread across binary64 kernels is `0` ULP (byte-exact agreement at the floor of double precision).

| Kernel | Implementation | μ (full precision) | round-8 | worst pair |
|:---|:---|:---|:---|:---:|
| K1 | NumPy `conj() @ T` with BLAS matmul | `0.6434255047504730` | `0.64342550` | (1, 42) |
| K2 | Pure-Python double loop, no external library, manual conjugate | `0.6434255047504730` | `0.64342550` | (1, 42) |
| K3 | `numpy.vdot` per pair | `0.6434255047504730` | `0.64342550` | (1, 42) |
| K4 | `mpmath` at 50 decimal digits | `0.6434255047504729` | `0.64342550` | (1, 42) |
| K5 | Python `decimal` at 40 decimal digits, separated real/imaginary | `0.6434255047504729` | `0.64342550` | (1, 42) |

mpmath reference at 50 decimal digits: `0.64342550475047294487215211018782112107460104494113…`
Within-kernel spread (binary64 kernels K1, K2, K3): `0` ULP (byte-exact agreement at the floor of binary64 precision). Arbitrary-precision kernels K4 (mpmath) and K5 (decimal) agree with the binary64 kernels through the 16th significant digit.

### A structural observation about the worst pair

All five kernels report the **same** worst pair `(1, 42)` for the submission. This is in contrast to the (3, 14) submission in our companion folder, where the five kernels report five different argmax pairs at the same μ value to within one unit in the last place of binary64 — a structural difference that we interpret (in [`Paper_4x48.md`](Paper_4x48.md) §3) as evidence that the basin floor for cell (4, 48) supports a non-degenerate critical structure with a single unambiguous maximum-coherence pair, rather than the degenerate family of equivalent critical points observed at the apparent basin floor of cell (3, 14).

This is an interpretation consistent with the kernel observations, not a proven structural claim.

---

## Five-kernel ratification (Cohn catalog holder)

For comparison, the same five kernels run on a local working copy of the Cohn (catalog) holder for cell (4, 48) (the holder file is publicly available in the Game of Sloanes catalog (Jasper, King, Mixon; https://github.com/gnikylime/GameofSloanes); it is not redistributed in this folder):

| Kernel | Implementation | μ (full precision) | round-8 | argmax pair |
|:---|:---|:---|:---|:---|
| K1 | NumPy `conj() @ T` with BLAS matmul | `0.6434277155768530` | `0.64342772` | stable |
| K2 | Pure-Python double loop, no library | `0.6434277155768529` | `0.64342772` | stable |
| K3 | `numpy.vdot` per pair | `0.6434277155768531` | `0.64342772` | stable |
| K4 | `mpmath` at 50 decimal digits | `0.6434277155768530` | `0.64342772` | stable |
| K5 | Python `decimal` at 40 decimal digits | `0.6434277155768530` | `0.64342772` | stable |

mpmath reference at 50 decimal digits: `0.643427715576853032…`
Within-kernel spread: `≤ 2 ULP binary64`.

### Gap (full precision, mpmath 50 dps)

```
μ_submission − μ_holder = −2.211 × 10⁻⁶
```

---

## Bounds comparison

| Bound | Value | Gap to submission μ = 0.643425504750473 |
|:---|:---|:---|
| Welch (4, 48) | `0.4837794468` | `+0.1596` (submission well above Welch) |
| Levenshtein-2 (4, 48) | `0.5877538100` | `+0.0557` (submission well above Levenshtein-2) |
| Cohn (catalog) holder | `0.6434277155768530` | `−2.21 × 10⁻⁶` (submission below holder) |

The Levenshtein-2 bound at `0.5877538100` is approximately 8.65% below the submission's coherence value. **This gap is mathematically large enough to admit deeper basins reachable via algebraic seeds, structured constructions, or paradigms not yet considered.** The basin-floor evidence in [`Paper_4x48.md`](Paper_4x48.md) speaks only to the basin we explored; the rest of the cell's landscape remains open.

---

## Structural verification

| Check | Result |
|:---|:---|
| Number of floats in `4x48_record1.txt` | 384 ✓ (= 2 · d · n = 2 · 4 · 48) |
| File layout (Game of Sloanes standard) | 192 reals then 192 imaginaries ✓ |
| All 48 vectors unit-norm | max ∣‖v_i‖ − 1∣ ≤ `2.21 × 10⁻¹¹` ✓ (well within unit-norm tolerance for IEEE-754 reproducibility) |
| Coherence definition used | μ = max_{i<j} ∣⟨v_i, v_j⟩∣ (Hermitian inner product) ✓ |
| Independent Python verifier reproduction | μ = `0.643425504750473` ✓ |
| Worst pair (stable across 5 kernels) | (1, 42) ✓ |
| Saturated-pair fraction at 10⁻⁸ tolerance | 274 / 1128 = 24.29% ✓ |

---

## Verification log policy

The Mac runtime log for the optimisation pass that produced `4x48_record1.txt` is preserved in the author's local archive but is **not included** in this public release. The five-kernel ratification tables above, together with the output of the independent Python verifier at the parent repository root, serve as the canonical public record. This policy is consistent with the handling of Record 3 in cell (4, 64) and of the (3, 14) submission at the parent repository, where the runtime logs are also held privately and the verifier output is the canonical public record.

---

## Acknowledgments

- **Henry Cohn** — for the published catalog entry for cell `(4, 48)` in the Game of Sloanes catalog against which our submission is compared. The Cohn holder has been the standing record for this cell for a number of years, and its byte-exact unit-norm structure and saturated-pair topology are documented as the reference baseline throughout this work. The holder packing itself is publicly available in the Game of Sloanes catalog and is not redistributed here.
- **Emily King, John Jasper, Dustin G. Mixon** — for maintaining the Game of Sloanes reference repository (https://github.com/gnikylime/GameofSloanes) and for the published acceptance rule on which the submission's eligibility is based.
- **Anthropic** — for building Claude, the AI assistant that collaborated on the five-kernel verification pipeline and the basin-floor reasoning documented in [`Paper_4x48.md`](Paper_4x48.md).

---

*Last updated: 2026-05-19 (revised).*
