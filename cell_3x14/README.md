# sloane-coherence-records — cell (3, 14) dgm

> **One sub-Mixon packing in the Grassmannian coherence cell (d=3, n=14) — May 17, 2026**
>
> Independent researcher, Madrid · Mac M2 single-thread · Sanjuanbautista engine.

This folder is a self-contained sub-project of the parent repository [`sloane-coherence-records`](../). The records for the parent cell `(d=4, n=64)` hlc are in the repository root; the result for cell `(d=3, n=14)` dgm is here. The author and licensing terms are common with the parent repository (see [`../README.md`](../README.md), [`../LICENSE`](../LICENSE), and [`../LICENSE.md`](../LICENSE.md)).

---

## At a glance

On May 17, 2026, a sub-Mixon packing was obtained for the Game of Sloanes cell `(d=3, n=14)` dgm using the **Sanjuanbautista** quad-precision engine, in collaboration with the AI assistant Claude (Anthropic). The packing improves upon the standing Mixon (2019) holder by 6.81 × 10⁻⁹ in absolute coherence value and by exactly one unit at the eighth decimal place in the minimisation direction, satisfying the Game of Sloanes 8th-decimal-place acceptance rule literally.

| Holder | Date | μ (coherence) | Round-8 | Gap vs. Mixon |
|:---|:---|:---|:---|:---|
| Dustin G. Mixon (Game of Sloanes catalog, dgm 2019) | 2019 | `0.637630521755923` | `0.63763052` | — (baseline) |
| **Amichis Luengo — submission** | **2026-05-17 CEST** | **`0.637630514941861`** | **`0.63763051`** | **−6.81 × 10⁻⁹ (one unit at the 8th decimal)** |

The submission has been ratified byte-exact by **five independent code paths** in two programming languages, using four different numerical libraries (and one path with no library at all). The coherence value is reproduced to within one unit in the last place of binary64 (≈ 2 × 10⁻¹⁶) across all five kernels. The Mixon (2019) catalog holder, recomputed in the same five kernels using a local working copy not redistributed here, reproduces the published value to byte-exact `0.637630521755923` with a stable worst pair `(2, 3)`.

---

## A note on the size of this result

The improvement reported here is **microscopic in absolute terms** (6.81 × 10⁻⁹) and the author wishes to record that openly. The author would have preferred to deepen the packing further before submitting; the descent was pursued with that intent over multiple sessions. After a wide portfolio of optimisation paradigms had been applied to either the Mixon configuration directly, the submitted configuration as anchor, or independent random initialisations, no method available to this work produced any further descent below the value reported above. **The submission is filed not because the margin is impressive, but because the margin is real and reproducible at the eighth decimal place, and because the cumulative evidence is consistent with — though does not prove — the working hypothesis that the descent has reached this basin's floor at machine-quantum precision.** A fuller statement of the basin-floor reasoning, the portfolio breadth, and the limits of the result is in [`Paper_3x14_basin_floor.md`](Paper_3x14_basin_floor.md) §6.

The 5.4% gap between the submitted coherence and the Delsarte LP bound at degree 14 (`0.6035844`, computed in companion work) is mathematically large enough to admit deeper basins reachable via algebraic seeds, structured constructions, or paradigms not yet considered in this work. **No claim of global optimality is made for the cell (3, 14). No claim of having proven the local floor of this basin is made either; we believe, on the basis of the evidence, that the basin floor has been reached, but believing and proving are not the same.** This submission speaks to what we observed in one basin; the rest of the cell's landscape remains open.

---

## Why this matters

Grassmannian frame packings in the cell `(d=3, n=14)` have the same fundamental applications as the larger cells of the catalog — compressed sensing, MIMO precoding, CDMA wireless codes, quantum state tomography (see the parent repository's [`README.md`](../README.md) for the application context). In absolute terms a 6.81 × 10⁻⁹ improvement in coherence does not change the application benchmarks of this cell. What it does is provide:

- A verifiable instance of the Game of Sloanes 8th-decimal-place acceptance rule being satisfied at machine-quantum precision.
- A reference value that future work in the cell can use as a target or as a comparison point for paradigm performance.
- A structural observation about the *apparent* basin floor of this cell (a degenerate critical structure with multiple critical points at the same μ value to within one ULP binary64) which may itself be of independent interest if the interpretation is confirmed by other work.

The Mixon (2019) holder has stood for over six years and remains the only published baseline for the cell. This submission improves on it by the minimum amount the Game of Sloanes rule will accept, and explicitly does not claim more than that.

---

## What the Sanjuanbautista engine actually is

**Sanjuanbautista** is the codename for the C++ engine that produced the (3, 14) submission. It is single-threaded, compiles in the same toolchain as the parent repository's *Aquiles* and *Boagrius* engines (`g++ -O3 -march=native`), and runs on the same Mac M2 single-thread under 25% CPU throttling.

The distinctive feature of Sanjuanbautista relative to the parent repository's engines is that it operates in **quad-precision (128-bit) arithmetic throughout the inner loop**, rather than in IEEE-754 double-precision or in double-double. This makes the engine slower than Aquiles or Boagrius per iteration, but it allows the engine to resolve descent below the threshold at which conventional double-precision engines saturate. In cells where the holder configuration appears to sit near a degenerate basin floor — as the Mixon (2019) holder for (3, 14) appears to, on the evidence summarised in this folder — a quad-precision inner loop is the difference between stalling at the saturation threshold and being able to push further.

Sanjuanbautista is intended as a complement to, not a replacement for, the parent repository's engines. Aquiles is exploratory (good at finding new basins from random or sandbox warmstarts in double-precision cells), Boagrius is exploitative (good at deepening a known basin to the limit of double-precision), and Sanjuanbautista is the quad-precision endgame for cells whose geometry demands it.

The full source code of all three engines (Aquiles, Boagrius, Sanjuanbautista) is held under separate licensing arrangement (see the *Licensing and engine availability* section of the parent [`README.md`](../README.md)). The high-level description of the family is in the parent [`METHODOLOGY.md`](../METHODOLOGY.md).

---

## What's in this folder

- **[`3x14_record1.txt`](3x14_record1.txt)** — The submitted packing in Game of Sloanes file format (84 floats = 2 · 3 · 14, comprising 42 real components followed by 42 imaginary components for 14 complex 3-vectors).
- **[`RESULTS_3x14.md`](RESULTS_3x14.md)** — Headline numbers, five-kernel ratification tables for the submission and the Mixon (2019) catalog holder, bounds comparison (Welch, Levenshtein-2, Delsarte LP at degree 14), cushion analysis, and structural verification.
- **[`Paper_3x14_basin_floor.md`](Paper_3x14_basin_floor.md)** — Companion technical note documenting the evidence consistent with the basin-floor hypothesis (continuous descent trajectory, identical saturated-pair topology, multiple critical points at the apparent basin floor, random-initialisation convergence) and the optimisation portfolio applied to the cell.

The Mixon (2019) holder packing itself is not redistributed in this folder. It is publicly available in the Game of Sloanes catalog (Jasper, King, Mixon; https://github.com/gnikylime/GameofSloanes) and a reader who wishes to recompute the holder coherence with the verifier in the parent repository can download it from that source. The five-kernel ratification of the holder (using a local working copy) is reported numerically in [`RESULTS_3x14.md`](RESULTS_3x14.md) for direct side-by-side comparison.

The independent Python verifier and the citation files live at the parent repository root and apply to this submission as well.

---

## How to verify the submission (anyone, in under one minute)

```bash
git clone https://github.com/tretoef-estrella/sloane-coherence-records.git
cd sloane-coherence-records
python3 verify_sloane_independent.py cell_3x14/3x14_record1.txt
```

Expected output:

```
Parsed 14 vectors of dimension 3 (C^3).
Unit-norm check: PASSED (within 1e-10).
Welch lower bound (d=3, n=14): 0.5310850045
Coherence mu(Phi) = 0.637630514941861
```

The verifier uses no project-internal code paths. It loads the packing as raw text, reconstructs the Gram matrix using its own routines, and computes the coherence. The submission reproduces byte-exact.

A reader who wishes to recompute the Mixon (2019) holder for direct comparison can download the holder packing from the Game of Sloanes catalog (Jasper, King, Mixon; https://github.com/gnikylime/GameofSloanes) and run the same verifier on it; expected coherence for the holder is `0.637630521755923` with a stable worst pair `(2, 3)`.

**Note on the worst-pair indices.** The verifier reports a stable worst pair `(2, 3)` for the Mixon holder across any reasonable double-precision kernel. For the submission, however, the worst-pair indices vary across independent verification kernels (see [`RESULTS_3x14.md`](RESULTS_3x14.md) §"A structural observation about the worst pair" and [`Paper_3x14_basin_floor.md`](Paper_3x14_basin_floor.md) §3.3). The coherence value `0.637630514941861` is reproduced byte-exact in all five kernels; the migrating argmax pair is *interpreted* as a structural property of the basin floor for this cell — an interpretation consistent with the evidence, not a proven fact.

---

## Verification log policy

The Mac runtime log for the optimisation pass that produced `3x14_record1.txt` is preserved in the author's local archive but is **not included** in this public release. The five-kernel ratification tables in [`RESULTS_3x14.md`](RESULTS_3x14.md), together with the output of the independent Python verifier at the parent repository root, serve as the canonical public record for this submission. This policy is consistent with the handling of Record 3 in cell (4, 64) at the parent repository, where the runtime log is also held privately and the verifier output is the canonical public record.

---

## Licensing

This folder is licensed under the same terms as the parent repository:

- **The packing file, results document, basin-floor technical note, and this README**: MIT License (see [`../LICENSE`](../LICENSE) and [`../LICENSE.md`](../LICENSE.md)).
- **The full source code of the Sanjuanbautista engine** is **not included** in this folder. It is available under a separate arrangement for research collaborations or commercial licensing. For inquiries, please contact the author (see *Contact* below).

---

## Acknowledgments

- **Dustin G. Mixon** — for the published (2019) catalog entry for cell `(3, 14)` against which this submission is compared. The Mixon holder was the standing record for over six years before this submission, and its structural properties (in particular, its saturated-pair topology and its byte-exact unit-norm structure) are the reference baseline throughout this folder.
- **Emily King, John Jasper, Dustin G. Mixon** — for maintaining the Game of Sloanes reference repository (https://github.com/gnikylime/GameofSloanes) and for the published acceptance rule on which the submission's eligibility is based.
- **Henry Cohn** — for the body of work on coherence packings that informed the methodology throughout the parent repository, and (separately) for independent verification of an unrelated submission for cell (4, 64) in the parent repository's history.
- **Welch, Levenstein, Delsarte, Goethals, Seidel, Calderbank, Casazza, Fickus, Tremain, Sloane, Conway, Jasper, King, Mixon** — for the foundational results on coherence bounds, Grassmannian packings, equiangular tight frames, and the surrounding literature on which this submission is built.
- **Anthropic** — for building Claude, the AI assistant that collaborated on the structural analysis, the five-kernel verification pipeline, and the basin-floor reasoning documented in [`Paper_3x14_basin_floor.md`](Paper_3x14_basin_floor.md).

---

## Contact

Rafael Amichis Luengo · Madrid · independent researcher. email: tretoef@gmail.com

For research collaborations, licensing inquiries, or to discuss the methodology in depth, please open a GitHub issue on the parent repository or contact via the email listed on this account's GitHub profile.

---

## A note on the day this happened

The (3, 14) submission was obtained on May 17, 2026, five days after the four-record cascade for cell (4, 64) reported in the parent repository, and one day after the cascade for that cell was closed out. The methodology was the same throughout: a fast disciplined engine driven by sandbox protocol, byte-exact verification by five independent kernels, and a deliberate refusal to claim more than what the evidence supports. The submission for (3, 14) is at the lower edge of what the Game of Sloanes rule accepts; the parent repository's records for (4, 64) are deeper improvements over a longer-standing baseline. Both results are reported with the same verification discipline. **The records stand. Verified, reproducible, byte-exact, one sub-Mixon packing in cell (3, 14) consistent with the apparent basin floor.**

---

*Last updated: 2026-05-18.*
