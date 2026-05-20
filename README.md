# sloane-coherence-records

> **Six world-record packings in Grassmannian coherence — (d=4, n=64) hlc, (d=3, n=14) dgm, and (d=4, n=48) hlc**
>
> Independent researcher, Madrid · Mac M2 single-thread · Three Game of Sloanes cells.

---

## At a glance

On May 12, 2026, the longstanding world record for the minimum-coherence packing of 64 unit vectors in complex 4-dimensional space (held by Henry Cohn et al.) was beaten **twice in a single day** using a novel optimisation paradigm developed by a self-taught researcher running on a personal Mac M2 laptop, in collaboration with the AI assistant Claude (Anthropic). Each of the first two record runs took approximately 5 minutes of wall time on a single CPU thread throttled to 25%. Four days later, on May 16, 2026, a second optimisation engine produced two further records in the same cell, and a fourth optimisation engine produced a sub-Cohn packing in the adjacent cell (4, 48). On May 17, 2026, the same methodology — adapted to a third Game of Sloanes cell — produced a sub-Mixon packing for cell (3, 14).

| Holder | Cell | Date | μ (coherence) | Worst pair | Gap vs. baseline | Engine |
|:---|:---:|:---|:---|:---:|:---|:---|
| Henry Cohn et al. (Game of Sloanes) | (4, 64) | ~2010–2024 | `0.687160201509307` | — | — (baseline) | hlc |
| **Amichis Luengo — record #1** | (4, 64) | **2026-05-12 (afternoon CEST)** | **`0.687040494471422`** | (31, 38) | **−1.197 × 10⁻⁴** | **Aquiles** |
| **Amichis Luengo — record #2** | (4, 64) | **2026-05-12 (evening CEST)** | **`0.687035170223597`** | (31, 38) | **−1.250 × 10⁻⁴** | **Aquiles** |
| **Amichis Luengo — record #3** | (4, 64) | **2026-05-16 (afternoon CEST)** | **`0.687033937262633`** | (6, 17) | **−1.263 × 10⁻⁴** | **Boagrius** |
| **Amichis Luengo — record #4** | (4, 64) | **2026-05-16 (evening CEST)** | **`0.687033931214091`** | (9, 25) | **−1.263 × 10⁻⁴ (−0.0184%)** | **Boagrius** |
| Henry Cohn (Game of Sloanes catalog) | (4, 48) | — | `0.643427715576853` | — | — (baseline) | hlc |
| **Amichis Luengo — record #6** | (4, 48) | **2026-05-16 CEST** | **`0.643425504750473`** | (1, 42) | **−2.21 × 10⁻⁶ (222 units at 8th decimal)** | **Rasputin** |
| Dustin G. Mixon (Game of Sloanes) | (3, 14) | 2019 | `0.637630521755923` | (2, 3) | — (baseline) | dgm |
| **Amichis Luengo — record #5** | (3, 14) | **2026-05-17 CEST** | **`0.637630514941861`** | basin-floor degeneracy¹ | **−6.81 × 10⁻⁹ (8th decimal)** | **Sanjuanbautista** |

¹ The (3, 14) submission sits at a degenerate basin floor where the worst-pair indices migrate across independent verification kernels while the coherence value itself is reproduced byte-exact. Full structural analysis in [`cell_3x14/Paper_3x14_basin_floor.md`](cell_3x14/Paper_3x14_basin_floor.md).

**Records #5 and #6 are reported and verified in separate folders.** The packing for the Game of Sloanes cell (3, 14) dgm — produced on May 17, 2026, with the **Sanjuanbautista** engine — improves upon the standing Mixon (2019) holder by 6.81 × 10⁻⁹ in absolute coherence value, satisfying the Game of Sloanes 8th-decimal-place acceptance rule by exactly one unit at the 8th decimal in the minimisation direction. The improvement is microscopic in absolute terms and is reported with the explicit caveat that the submission and the Mixon holder appear to share a common critical basin whose floor has been reached at machine-quantum precision. The packing for cell (4, 48) hlc — produced on May 16, 2026, with the **Rasputin** engine — improves upon the standing Cohn (catalog) holder by 2.21 × 10⁻⁶ in absolute coherence value (222 units at the 8th decimal in the minimisation direction), with all five verification kernels reporting a stable worst pair `(1, 42)` and the submission appearing to sit at the local floor of the basin in which it was obtained. **No claim of global optimality is made for either cell**, and both submissions are framed as working hypotheses consistent with the accumulated evidence, not as proofs. All the data, the five-kernel ratification tables, the bounds analyses, and the basin-floor technical notes for these cells are in the dedicated folders [`cell_3x14/`](cell_3x14/) and [`cell_4x48/`](cell_4x48/), each of which has its own README and stands as a self-contained sub-project of this repository. The records for cell (4, 64) (records #1–#4) remain in this repository's root directory, unchanged.

All six packings have been independently verified, each ratified byte-exact by **five independent code paths** in two programming languages, using four different numerical libraries (and one path with no library at all). Each kernel reports identical coherence to machine precision. Records #1 and #2 share worst pair `(31, 38)` — the basin discovered on May 12. Records #3 and #4 have worst pairs `(6, 17)` and `(9, 25)` respectively, indicating that the cascade from Record 2 to Record 3 to Record 4 traversed structurally distinct basins, not a refinement of the same basin.

---

## Why this matters

Grassmannian frame packings in the cells `(d=4, n=64)`, `(d=4, n=48)`, and `(d=3, n=14)` are not just mathematical curiosities. They are used in:

- **CDMA wireless codes** — minimum-coherence sequences minimise multi-user interference.
- **MIMO precoding** — unitary matrices for multi-antenna systems (Wi-Fi 6E/7 and 5G NR with 4 antennas).
- **Compressed sensing** — measurement matrices whose recovery guarantees depend directly on coherence (Donoho-Elad-Bruckstein).
- **Quantum state tomography** — frames analogous to SIC-POVMs.

A 0.0184% cumulative improvement in coherence for `(4, 64)` translates into a measurable improvement in recovery probability bounds for compressed sensing of 4-sparse signals measured by 64 sensors, and into a new benchmark for packing-based codes in MIMO and CDMA contexts. The previous record for that cell had stood for over 14 years. The (4, 48) improvement (`2.21 × 10⁻⁶` absolute) is large enough to be application-relevant for compressed sensing in that cell, where the coherence appears squared in the dominant terms of recovery bounds. The (3, 14) improvement is mathematically smaller and is offered primarily as a basin-floor benchmark and as a verifiable instance of the Game of Sloanes 8th-decimal acceptance rule being satisfied at machine-quantum precision.

Readers interested in exploring the *structural geography* of any Grassmannian packing — not just the ones documented here — may find useful the companion browser-based diagnostic tool [**KADE Packing Diagnostic**](https://tretoef-estrella.github.io/KADE/), which computes a five-kernel coherence verification, Welch slack, saturated graph density, cliff D₁, worst d-tuple morphology, frame tightness, Bargmann phases, and a live side-by-side comparison against the current Game of Sloanes holder for the same cell. Drop a packing in, look at the fingerprint. Runs entirely in the browser. Useful for pre-submission sanity checks (with the float64 disclaimer noted in that tool's own *About* tab).

---

## The story, in three paragraphs

Cohn et al. had held the record for `(4, 64)` hlc for over a decade. The standard approach to this problem (alternating projections, BCASC, ManOpt, gradient-based refinement) had been thoroughly explored by the experts. **A first optimisation paradigm — internally codenamed the *water paradigm* — combined Riemannian gradient flow over a smoothed-max coherence loss with a structure-aware warmstart strategy.** From a Mac M2 with no special hardware, **each of the first two record runs took approximately 5 minutes of wall time** once the warmstart was supplied. Both Records 1 and 2 were produced on May 12, 2026, by the engine internally named *Aquiles*, in two distinct basins of the optimisation landscape sharing the same worst-pair indices.

Four days later, on May 16, 2026, a second optimisation engine — internally named *Boagrius* — was applied to the cell. Boagrius uses a different paradigm: rather than smoothed-max with momentum, it applies a constrained-optimisation framework with a feasibility-driven stopping discipline. Starting from a Record-2 warmstart (and then cascading), Boagrius produced Record 3 in the afternoon and Record 4 in the evening, both in basins structurally distinct from the Aquiles basin (different worst-pair indices). Record 4 — the deepest known packing for the cell as of this writing — required approximately 9 minutes of wall time on the same Mac M2 single-thread. On the same Saturday afternoon, a fourth optimisation engine — internally named *Rasputin* — was applied to the adjacent Cohn-held cell (4, 48). Rasputin produced a sub-Cohn packing improving the catalog holder by 222 units at the eighth decimal place, with a stable worst pair `(1, 42)` across all verification kernels and a multi-paradigm portfolio confirming that the submission sits at the local floor of the basin in which it was obtained.

The day after, on May 17, 2026, the same methodology — adapted to cell (3, 14) and applied via a third quad-precision engine internally named *Sanjuanbautista* — produced a sub-Mixon packing at the apparent degenerate basin floor of that cell. The improvement for (3, 14) is microscopic by absolute measure (6.81 × 10⁻⁹) but satisfies the Game of Sloanes acceptance rule literally; the basin-floor evidence is documented as a working hypothesis in the dedicated folder, not as a proven theorem.

> **Note on runtime.** Earlier versions of the documentation for Records 1 and 2 stated, in error, that each run took "approximately 5.5 hours". That figure was a memory-based estimate from the drafting AI assistant, not a number read from the actual Mac log. The correct figures (Records 1 and 2: 5 min wall time each; Record 4: 568 s ≈ 9 min 28 s wall time, all byte-exact reproducible) are documented in [`ERRATA.md`](ERRATA.md). The records themselves were never affected.

---

## What the engines actually are

**Aquiles** is the codename for the C++ engine that produced Records 1 and 2. It is single-threaded, allocates a few kilobytes of memory, compiles with `g++ -O3 -march=native -std=c++17 -funroll-loops`, and produces a world-record packing in under six minutes when given a structurally appropriate warmstart. It is hand-tuned for the geometry of complex Grassmannian coherence packings, with flat-array POD complex doubles, incremental Gram updates, smoothed-max loss with an aggressive logarithmic temperature schedule, Riemannian retraction after each gradient step, heavy-ball momentum, and a refutation-criterion-driven kill.

**Boagrius** is the codename for the second C++ engine, which produced Records 3 and 4. It uses a different conceptual framework: instead of a smoothed-max landscape, Boagrius operates on a constrained-feasibility formulation where the coherence is treated as a hard constraint and the engine iterates on the constraint residual until convergence within a quad-precision feasibility tolerance. The two engines are complementary: Aquiles is exploratory (good at finding new basins from random or sandbox warmstarts), Boagrius is exploitative (good at deepening a known basin to the limit of floating-point precision).

**Sanjuanbautista** is the codename for the third C++ engine, which produced the (3, 14) record reported in [`cell_3x14/`](cell_3x14/). The distinctive public feature of Sanjuanbautista relative to the parent repository's engines is that it operates in **quad-precision (128-bit) arithmetic throughout the inner loop**, rather than in IEEE-754 double-precision or in double-double. This makes the engine slower than Aquiles or Boagrius per iteration, but it allows the engine to resolve descent below the threshold at which conventional double-precision engines saturate. In cells where the holder configuration sits near a degenerate basin floor — as the Mixon (2019) holder for (3, 14) appears to — quad-precision is the difference between stalling at the saturation threshold and being able to push to the basin floor itself.

**Rasputin** is the codename for the fourth C++ engine, which produced the (4, 48) record reported in [`cell_4x48/`](cell_4x48/). Like Sanjuanbautista, Rasputin operates in **quad-precision (128-bit) arithmetic throughout its inner loop**. The distinction between Rasputin and Sanjuanbautista is operational rather than methodological: Rasputin is hardened for cells where the holder configuration is structurally tight in the sense of admitting many simultaneously near-saturated pairs (24.29% saturated pairs at the 10⁻⁸ tolerance level in the case of (4, 48)), and a non-trivial descent is feasible in absolute coherence terms rather than only at the eighth-decimal rounding boundary. The four engines are complementary: Aquiles explores new basins from random or sandbox warmstarts in double-precision cells; Boagrius deepens a known basin to the limit of double-precision; Sanjuanbautista is the quad-precision endgame for cells where the basin floor appears degenerate; Rasputin is the quad-precision attack engine for cells where the holder is structurally tight and a non-trivial descent is feasible.

The leverage in this project does not live in any one engine. It lives in **the combination of fast disciplined engines and a sandbox protocol that discovers the right places on the manifold to launch them from**. A higher-level description is in [`METHODOLOGY.md`](METHODOLOGY.md). The full source code of all four engines is held under separate licensing arrangement (see *Licensing and engine availability* below).

---

## What's in this repository

### Cell (4, 64) hlc — root directory

- **[`PROOF.md`](PROOF.md)** — Smoking-gun one-pager. Everything needed to be convinced (or to disprove) in a single read.
- **[`RESULTS.md`](RESULTS.md)** — Headline numbers, bounds comparison, gap analysis.
- **[`RECORDS.md`](RECORDS.md)** — Raw verifier outputs for all four packings.
- **[`METHODOLOGY.md`](METHODOLOGY.md)** — High-level description of the engines (full source code reserved; see *Licensing and engine availability* below).
- **[`GUIDE FOR EVERYONE.md`](GUIDE%20FOR%20EVERYONE.md)** — For non-mathematicians: what a Grassmannian packing is and why people care.
- **[`CITATION.md`](CITATION.md)** and **[`CITATION.cff`](CITATION.cff)** — How to cite this work.
- **[`LICENSE`](LICENSE)** and **[`LICENSE.md`](LICENSE.md)** — Open content (MIT) and engine licensing terms.
- **[`ERRATA.md`](ERRATA.md)** — Permanent record of any correction made to the documentation after publication.
- **[`Paper sloane v15 public .md`](Paper%20sloane%20v15%20public%20.md)** — Original technical paper covering Records 1 and 2.
- **[`Paper sloane v16 public.md`](Paper%20sloane%20v16%20public.md)** — Updated technical paper extending the v15 coverage to Records 3 and 4 (Boagrius engine, May 16 sessions).
- **[`4x64_record1.txt`](4x64_record1.txt)**, **[`4x64_record2.txt`](4x64_record2.txt)**, **[`4x64_record3.txt`](4x64_record3.txt)**, and **[`4x64_record4.txt`](4x64_record4.txt)** — All four packings, in standard Game of Sloanes file format (2·d·n floating-point values: 4·64 real parts followed by 4·64 imaginary parts).
- **[`run_record1.log`](run_record1.log)**, **[`run_record2.log`](run_record2.log)**, and **[`run_record4.log`](run_record4.log)** — Mac runtime logs.
- **[`WITNESS.md`](WITNESS.md)** — A note from Claude (Anthropic) describing its role in the collaboration.

### Cell (3, 14) dgm — [`cell_3x14/`](cell_3x14/)

The (3, 14) record (Record #5 in the table above) lives in a dedicated sub-folder with its own README, results document, basin-floor technical note, and packing file. See [`cell_3x14/README.md`](cell_3x14/README.md) for the full presentation of that result.

### Cell (4, 48) hlc — [`cell_4x48/`](cell_4x48/)

The (4, 48) record (Record #6 in the table above) lives in a dedicated sub-folder with its own README, results document, basin-floor technical note, and packing file. See [`cell_4x48/README.md`](cell_4x48/README.md) for the full presentation of that result.

### Shared

- **[`verify_sloane_independent.py`](verify_sloane_independent.py)** — Independent Python verifier with its own clean-room kernel. Reproduces all six coherence values (four in cell (4, 64), one in cell (3, 14), one in cell (4, 48)) to machine precision.

---

## How to verify the records (anyone, in under one minute)

```bash
git clone https://github.com/tretoef-estrella/sloane-coherence-records.git
cd sloane-coherence-records
python3 verify_sloane_independent.py 4x64_record1.txt
python3 verify_sloane_independent.py 4x64_record2.txt
python3 verify_sloane_independent.py 4x64_record3.txt
python3 verify_sloane_independent.py 4x64_record4.txt
python3 verify_sloane_independent.py cell_3x14/3x14_record1.txt
python3 verify_sloane_independent.py cell_4x48/4x48_record1.txt
```

Expected output for record #4 in cell (4, 64) (the deepest packing for that cell):

```
Parsed 64 vectors of dimension 4 (C^4).
Unit-norm check: PASSED (within 1e-10).
Welch lower bound (d=4, n=64): 0.4879500365
Coherence mu(Phi) = 0.687033931214091
Worst pair: vectors (9, 25) with |<v_9, v_25>| = 0.687033931214091
```

Expected output for the (3, 14) packing (record #5):

```
Parsed 14 vectors of dimension 3 (C^3).
Unit-norm check: PASSED (within 1e-10).
Welch lower bound (d=3, n=14): 0.5310850045
Coherence mu(Phi) = 0.637630514941861
```

Expected output for the (4, 48) packing (record #6):

```
Parsed 48 vectors of dimension 4 (C^4).
Unit-norm check: PASSED (within 1e-10).
Welch lower bound (d=4, n=48): 0.4837794468
Coherence mu(Phi) = 0.643425504750473
Worst pair: vectors (1, 42) with |<v_1, v_42>| = 0.643425504750473
```

The verifier uses no project-internal code paths. It loads the packing as raw text, reconstructs the Gram matrix using its own routines, and computes the coherence. **All six packings reproduce byte-exact.**

A second, browser-based way to verify: open the [**KADE Packing Diagnostic**](https://tretoef-estrella.github.io/KADE/), drag any of the `.txt` files into it, and read the full structural fingerprint (μ across five independent float64 kernels, Welch slack, saturated graph, cliff, worst d-tuple morphology, Bargmann phases, lower-bound validity, and a side-by-side comparison against the current Game of Sloanes holder). Useful when the verifier output above leaves you wondering what *else* is going on in the packing beyond the worst-pair coherence value. KADE runs entirely client-side, no data leaves the browser.

(Note for the (3, 14) packing: as documented in [`cell_3x14/RESULTS_3x14.md`](cell_3x14/RESULTS_3x14.md) and [`cell_3x14/Paper_3x14_basin_floor.md`](cell_3x14/Paper_3x14_basin_floor.md), the worst-pair indices vary across independent verification kernels because the basin floor for this cell supports a small discrete family of critical points at the same μ value to within one unit in the last place of binary64. The coherence value itself is reproduced byte-exact across kernels; the argmax pair is a structural property of the basin floor, not a kernel error. For the (4, 48) packing, by contrast, the worst pair `(1, 42)` is stable across all five verification kernels — a structural difference from cell (3, 14) discussed in [`cell_4x48/Paper_4x48.md`](cell_4x48/Paper_4x48.md) §3.)

---

## Licensing and engine availability

- **Records themselves, verification scripts, papers, and documentation in this repository**: MIT License (see [`LICENSE`](LICENSE) and [`LICENSE.md`](LICENSE.md)). The mathematical results are free for everyone to use, cite, and build upon.
- **The full source code of the four optimisation engines** (*Aquiles*, *Boagrius*, *Sanjuanbautista*, and *Rasputin*) is **not included in this repository**. It is available under a separate arrangement for research collaborations or commercial licensing. For inquiries, please contact the author (see *Contact* below).

The high-level methodology is described in [`METHODOLOGY.md`](METHODOLOGY.md) at the level expected of a research preprint: enough for a peer to understand the conceptual approach, but not a turnkey implementation.

---

## Acknowledgments

- **Henry Cohn, Abhinav Kumar, Gregory Minton and collaborators** — for the body of work on coherence packings that made this comparison possible, and for the published Cohn catalog entry for cell `(4, 48)` against which our packing in [`cell_4x48/`](cell_4x48/) is compared.
- **Emily King, John Jasper, Dustin G. Mixon** — for maintaining the Game of Sloanes reference repository (https://github.com/gnikylime/GameofSloanes), which sets the gold standard for reproducible coherence packings, and for the published Mixon (2019) catalog entry for cell `(3, 14)` against which our packing in [`cell_3x14/`](cell_3x14/) is compared.
- **Anthropic** — for building Claude, the AI assistant that collaborated on the engineering, the sandbox exploration protocols, and the verification pipeline.
- **The community of researchers** working on Grassmannian packings, equiangular lines, MUBs, and SIC-POVMs — your work taught me what mattered and what didn't.

---

## Contact

Rafael Amichis Luengo · Madrid · independent researcher. email: tretoef@gmail.com

For research collaborations, licensing inquiries, or to discuss the methodology in depth, please open a GitHub issue or contact via the email listed on this account's GitHub profile.

---

## A note on the days these results happened

This repository documents three days of work — May 12, 2026, May 16, 2026, and May 17, 2026 — during which six sub-catalog packings were obtained across three Game of Sloanes cells. The first two records (May 12) came from the Aquiles engine in two distinct basins of cell (4, 64) sharing the same worst-pair indices. The third and fourth records (May 16) came from the Boagrius engine in basins of cell (4, 64) structurally distinct from the Aquiles basin. The sixth record (May 16, the same Saturday) came from the Rasputin engine in cell (4, 48), improving the Cohn catalog holder by 222 units at the eighth decimal place. The fifth record (May 17) came from the Sanjuanbautista engine in cell (3, 14) and is reported with explicit basin-floor caveats. Each packing was filtered through the same verification discipline: byte-exact ratification by five independent code paths and agreement on the coherence value across all kernels.

The records stand. **Verified, reproducible, byte-exact, four sub-Cohn packings in cell (4, 64), one sub-Cohn packing in cell (4, 48), and one sub-Mixon packing in cell (3, 14).**

---

*Last updated: 2026-05-20.*
