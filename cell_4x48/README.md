# sloane-coherence-records — cell (4, 48) hlc

> **One sub-Cohn packing in the Grassmannian coherence cell (d=4, n=48) — May 16, 2026 (revised May 19, 2026)**
>
> Independent researcher, Madrid · Mac M2 single-thread · Rasputin engine.

This folder is a self-contained sub-project of the parent repository [`sloane-coherence-records`](../). The records for the parent cell `(d=4, n=64)` hlc are in the repository root; the result for cell `(d=3, n=14)` dgm is in [`cell_3x14/`](../cell_3x14/); the result for cell `(d=4, n=48)` hlc is here. The author and licensing terms are common with the parent repository (see [`../README.md`](../README.md), [`../LICENSE`](../LICENSE), and [`../LICENSE.md`](../LICENSE.md)).

---

## At a glance

On May 16, 2026, a sub-Cohn packing was obtained for the Game of Sloanes cell `(d=4, n=48)` hlc using the **Rasputin** quad-precision engine, in collaboration with the AI assistant Claude (Anthropic). The packing improves upon the standing Cohn catalog holder by 2.21 × 10⁻⁶ in absolute coherence value and by 222 units at the eighth decimal place in the minimisation direction (round-8: `0.64342550` versus holder round-8 `0.64342772`), satisfying the Game of Sloanes 8th-decimal-place acceptance rule by a comfortable margin.

| Holder | Date | μ (coherence) | Round-8 | Worst pair | Gap vs. Cohn |
|:---|:---|:---|:---|:---:|:---|
| Henry Cohn (Game of Sloanes catalog, hlc) | ~2010–2024 | `0.643427715576853` | `0.64342772` | — | — (baseline) |
| **Amichis Luengo — submission** | **2026-05-16 CEST** | **`0.643425504750473`** | **`0.64342550`** | **(1, 42)** | **−2.21 × 10⁻⁶ (222 units at the 8th decimal)** |

The submission has been ratified byte-exact by **five independent code paths** in two programming languages, using four different numerical libraries (and one path with no library at all). The coherence value is reproduced with zero ULP spread across binary64 kernels, and all five kernels report the **same** worst pair `(1, 42)` — a structural property of this basin that contrasts with the worst-pair migration observed in cell (3, 14) and is documented further in [`Paper_4x48.md`](Paper_4x48.md).

---

## A note on the result and its limits

The improvement reported here is substantively larger than the (3, 14) submission in our companion folder (a gap of `2.21 × 10⁻⁶` at the 8th decimal here versus `6.81 × 10⁻⁹` there), and it is delivered on a Cohn-held cell whose holder has stood for a number of years. The author wishes to record openly, however, that the improvement was obtained on the first day of attacking this cell and is the deepest the available portfolio of optimisation paradigms could reach. The author would have preferred to deepen the packing further before filing; after roughly twenty distinct attack paradigms had been applied to either the Cohn configuration directly, the submitted configuration as anchor, or independent random initialisations, no method produced any further descent below the value reported above.

**The submission is filed because the margin is real, reproducible at the eighth decimal place across five independent verification kernels, and consistent with — though not a proof of — the working hypothesis that the descent has reached this basin's floor at machine-quantum precision. No claim of global optimality is made for the cell. No claim of having proven the local floor of the basin is made either; we believe, on the basis of the accumulated evidence, that the basin floor has been reached, but believing and proving are not the same.**

A fuller statement of the basin-floor reasoning, the portfolio breadth, and the limits of the result is in [`Paper_4x48.md`](Paper_4x48.md) §6.

---

## Why this matters

Grassmannian frame packings in the cell `(d=4, n=48)` have the same fundamental applications as the larger cells of the catalog — compressed sensing, MIMO precoding, CDMA wireless codes, quantum state tomography (see the parent repository's [`README.md`](../README.md) for the application context). In contrast to the (3, 14) submission, which improves the holder by a microscopic absolute margin and is offered primarily as a basin-floor benchmark, the (4, 48) submission improves the holder by `2.21 × 10⁻⁶` in absolute coherence — a margin large enough to be visible in application benchmarks for this cell, particularly for compressed-sensing recovery bounds where the coherence appears squared in the dominant terms.

The Cohn holder for `(4, 48)` has been the standing record for a number of years and remains the only published baseline for the cell. This submission improves on it by 222 units at the eighth decimal place, with all the verification discipline described below.

---

## What the Rasputin engine actually is

**Rasputin** is the codename for the fourth C++ engine in the family used in this repository. It is single-threaded, compiles in the same toolchain as the parent repository's *Aquiles*, *Boagrius*, and *Sanjuanbautista* engines (`g++ -O3 -march=native`), and runs on the same Mac M2 single-thread under 25% CPU throttling.

Like Sanjuanbautista, Rasputin operates in **quad-precision (128-bit) arithmetic throughout its inner loop**, rather than in IEEE-754 double-precision or in double-double. This makes the engine slower than Aquiles or Boagrius per iteration, but it allows the engine to resolve descent below the threshold at which conventional double-precision engines saturate. The distinction between Rasputin and Sanjuanbautista is operational rather than methodological: Rasputin is hardened for cells where the holder configuration is structurally tight in the sense of admitting many simultaneously near-saturated pairs (49% saturated pairs at the 10⁻⁸ tolerance level in the case of (4, 48), versus a different saturated-pair structure in cells where Sanjuanbautista is the natural choice).

The four engines in the family are complementary: Aquiles explores new basins from random or sandbox warmstarts in double-precision cells; Boagrius deepens a known basin to the limit of double-precision; Sanjuanbautista is the quad-precision endgame for cells where the basin floor appears degenerate; and Rasputin is the quad-precision attack engine for cells where the holder is structurally tight and a non-trivial descent is feasible.

The full source code of all four engines (Aquiles, Boagrius, Sanjuanbautista, Rasputin) is held under separate licensing arrangement (see the *Licensing and engine availability* section of the parent [`README.md`](../README.md)). The high-level description of the family is in the parent [`METHODOLOGY.md`](../METHODOLOGY.md).

---

## What's in this folder

- **[`4x48_record1.txt`](4x48_record1.txt)** — The submitted packing in Game of Sloanes file format (384 floats = 2 · 4 · 48, comprising 192 real components followed by 192 imaginary components for 48 complex 4-vectors).
- **[`RESULTS_4x48.md`](RESULTS_4x48.md)** — Headline numbers, five-kernel ratification tables for the submission and the Cohn (catalog) holder, bounds comparison (Welch, Levenshtein-2), cushion analysis, structural verification.
- **[`Paper_4x48.md`](Paper_4x48.md)** — Companion technical note documenting the evidence consistent with the basin-floor hypothesis (multi-seed convergence, trust-region radial expansion refutation, targeted-vector perturbation refutation, large-scale cold-start enumeration) and the optimisation portfolio applied to the cell.

The Cohn (catalog) holder packing itself is not redistributed in this folder. It is publicly available in the Game of Sloanes catalog (Jasper, King, Mixon; https://github.com/gnikylime/GameofSloanes) and a reader who wishes to recompute the holder coherence with the verifier in the parent repository can download it from that source. The five-kernel ratification of the holder (using a local working copy) is reported numerically in [`RESULTS_4x48.md`](RESULTS_4x48.md) for direct side-by-side comparison.

The independent Python verifier and the citation files live at the parent repository root and apply to this submission as well.

---

## How to verify the submission (anyone, in under one minute)

```bash
git clone https://github.com/tretoef-estrella/sloane-coherence-records.git
cd sloane-coherence-records
python3 verify_sloane_independent.py cell_4x48/4x48_record1.txt
```

Expected output:

```
Parsed 48 vectors of dimension 4 (C^4).
Unit-norm check: PASSED (within 1e-10).
Welch lower bound (d=4, n=48): 0.4837794468
Coherence mu(Phi) = 0.643425504750473
Worst pair: vectors (1, 42) with |<v_1, v_42>| = 0.643425504750473
```

The verifier uses no project-internal code paths. It loads the packing as raw text, reconstructs the Gram matrix using its own routines, and computes the coherence. The submission reproduces byte-exact.

A reader who wishes to recompute the Cohn (catalog) holder for direct comparison can download the holder packing from the Game of Sloanes catalog (Jasper, King, Mixon; https://github.com/gnikylime/GameofSloanes) and run the same verifier on it; expected coherence for the holder is `0.643427715576853` with a stable worst pair across kernels.

**Note on the worst pair.** In contrast to the cell (3, 14) submission in our companion folder, where the worst-pair indices vary across independent verification kernels and we interpret that as evidence of a degenerate critical structure at the basin floor, the (4, 48) submission exhibits a **stable** worst pair `(1, 42)` across all five kernels. The basin floor for cell (4, 48), under the working hypothesis stated above, appears to support a single critical structure with an unambiguous maximum-coherence pair rather than a degenerate family of pairs at the same μ value. This is documented further in [`Paper_4x48.md`](Paper_4x48.md) §3.

---

## Verification log policy

The Mac runtime log for the optimisation pass that produced `4x48_record1.txt` is preserved in the author's local archive but is **not included** in this public release. The five-kernel ratification tables in [`RESULTS_4x48.md`](RESULTS_4x48.md), together with the output of the independent Python verifier at the parent repository root, serve as the canonical public record for this submission. This policy is consistent with the handling of Record 3 in cell (4, 64) and of the (3, 14) submission at the parent repository, where the runtime logs are also held privately and the verifier output is the canonical public record.

---

## Licensing

This folder is licensed under the same terms as the parent repository:

- **The packing file, results document, basin-floor technical note, and this README**: MIT License (see [`../LICENSE`](../LICENSE) and [`../LICENSE.md`](../LICENSE.md)).
- **The full source code of the Rasputin engine** is **not included** in this folder. It is available under a separate arrangement for research collaborations or commercial licensing. For inquiries, please contact the author (see *Contact* below).

---

## Acknowledgments

- **Henry Cohn** — for the published catalog entry for cell `(4, 48)` in the Game of Sloanes catalog against which this submission is compared. The Cohn holder has been the standing record for this cell for a number of years, and its structural properties (saturated-pair topology, byte-exact unit-norm structure) are the reference baseline throughout this folder. Professor Cohn separately performed the independent verification of an unrelated submission for cell (4, 64) in the parent repository's history, within 43 minutes of being notified.
- **Emily King, John Jasper, Dustin G. Mixon** — for maintaining the Game of Sloanes reference repository (https://github.com/gnikylime/GameofSloanes), which sets the gold standard for reproducible coherence packings, and for the published acceptance rule on which this submission's eligibility is based.
- **Henry Cohn, Abhinav Kumar, Gregory Minton and collaborators** — for the body of work on coherence packings that informed the methodology throughout the parent repository.
- **Welch, Levenstein, Delsarte, Goethals, Seidel, Calderbank, Casazza, Fickus, Tremain, Sloane, Conway, Jasper, King, Mixon** — for the foundational results on coherence bounds, Grassmannian packings, equiangular tight frames, and the surrounding literature on which this submission is built.
- **Anthropic** — for building Claude, the AI assistant that collaborated on the structural analysis, the five-kernel verification pipeline, and the basin-floor reasoning documented in [`Paper_4x48.md`](Paper_4x48.md).

---

## Contact

Rafael Amichis Luengo · Madrid · independent researcher. email: tretoef@gmail.com

For research collaborations, licensing inquiries, or to discuss the methodology in depth, please open a GitHub issue on the parent repository or contact via the email listed on this account's GitHub profile.

---

## A note on the day this happened

The (4, 48) submission was obtained on May 16, 2026, four days after the four-record cascade for cell (4, 64) reported in the parent repository, on the same Saturday afternoon and evening that the cascade for that cell was being closed out, and one day before the (3, 14) submission in the companion folder. The methodology was the same throughout: a fast disciplined engine driven by sandbox protocol, byte-exact verification by five independent kernels, and a deliberate refusal to claim more than what the evidence supports. The submission for (4, 48) sits comfortably above the Game of Sloanes acceptance threshold and improves on a Cohn-held baseline by a margin large enough to be application-relevant. The cell remains open for deeper packings — we hypothesise the basin floor has been reached at machine-quantum precision, but we do not claim to have proven it.

**The records stand. Verified, reproducible, byte-exact, one sub-Cohn packing in cell (4, 48) consistent with the apparent basin floor.**

---

*Last updated: 2026-05-19 (revised).*
