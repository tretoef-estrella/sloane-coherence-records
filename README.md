# sloane-coherence-records

> **Four world records in Grassmannian coherence packings (d=4, n=64) hlc — May 12–16, 2026**
>
> Independent researcher, Madrid · Mac M2 single-thread · One cell · Four sub-Cohn packings.

---

## At a glance

Between May 12 and May 16, 2026, the longstanding world record for the minimum-coherence packing of 64 unit vectors in complex 4-dimensional space (held by Henry Cohn et al.) was beaten **four times in succession** using two optimisation engines developed by a self-taught researcher running on a personal Mac M2 laptop, in collaboration with the AI assistant Claude (Anthropic). The first record was obtained in the afternoon of May 12; the fourth in the evening of May 16. Each record was filed as a successor to the previous one in a cascade of sub-Cohn packings.

| Holder | Date | μ (coherence) | Worst pair | Gap vs. Cohn | Engine |
|:---|:---|:---|:---|:---|:---|
| Henry Cohn et al. (Game of Sloanes) | ~2010–2024 | `0.687160201509307` | — | — (baseline) | hlc |
| **Amichis Luengo — record #1** | **2026-05-12 (afternoon CEST)** | **`0.687040494471422`** | (31, 38) | **−1.197 × 10⁻⁴** | **Aquiles** |
| **Amichis Luengo — record #2** | **2026-05-12 (evening CEST)** | **`0.687035170223597`** | (31, 38) | **−1.250 × 10⁻⁴** | **Aquiles** |
| **Amichis Luengo — record #3** | **2026-05-16 (afternoon CEST)** | **`0.687033937262633`** | (6, 17) | **−1.263 × 10⁻⁴** | **Boagrius** |
| **Amichis Luengo — record #4** | **2026-05-16 (evening CEST)** | **`0.687033931214091`** | (9, 25) | **−1.263 × 10⁻⁴ (−0.0184%)** | **Boagrius** |

All four packings have been independently verified, each ratified byte-exact by **five independent code paths** in two programming languages, using four different numerical libraries (and one path with no library at all). Each kernel reports identical coherence to the precision available, and the worst-pair indices agree across all five paths in every case. Record #2 was additionally reproduced byte-exact by Professor **Henry Cohn (MIT)** in his own code on May 12, 2026 (43 minutes after notification by the author).

Records #1 and #2 share worst pair `(31, 38)` — the basin discovered on May 12. Records #3 and #4 have worst pairs `(6, 17)` and `(9, 25)` respectively, indicating that the cascade from Record 2 to Record 3 to Record 4 traversed structurally distinct basins, not a refinement of the same basin.

---

## Why this matters

Grassmannian frame packings in the cell `(d=4, n=64)` are not just a mathematical curiosity. They are used in:

- **CDMA wireless codes** — minimum-coherence sequences minimise multi-user interference.
- **MIMO precoding** — unitary matrices for multi-antenna systems (Wi-Fi 6E/7 and 5G NR with 4 antennas).
- **Compressed sensing** — measurement matrices whose recovery guarantees depend directly on coherence (Donoho-Elad-Bruckstein).
- **Quantum state tomography** — frames analogous to SIC-POVMs.

A 0.0184% cumulative improvement in coherence translates into a measurable improvement in recovery probability bounds for compressed sensing of 4-sparse signals measured by 64 sensors, and into a new benchmark for packing-based codes in MIMO and CDMA contexts. The previous record had stood for over 14 years.

---

## The story, in two paragraphs

Cohn et al. had held the record for `(4, 64)` hlc for over a decade. The standard approach to this problem (alternating projections, BCASC, ManOpt, gradient-based refinement) had been thoroughly explored by the experts. **A first optimisation paradigm — internally codenamed the *water paradigm* — combined Riemannian gradient flow over a smoothed-max coherence loss with a structure-aware warmstart strategy.** From a Mac M2 with no special hardware, **each of the first two record runs took approximately 5 minutes of wall time** once the warmstart was supplied. Both Records 1 and 2 were produced on May 12, 2026, by the engine internally named *Aquiles*, in two distinct basins of the optimisation landscape sharing the same worst-pair indices.

Four days later, on May 16, 2026, a second optimisation engine — internally named *Boagrius* — was applied to the cell. Boagrius uses a different paradigm: rather than smoothed-max with momentum, it applies a constrained-optimisation framework with a feasibility-driven stopping discipline. Starting from a Record-2 warmstart (and then cascading), Boagrius produced Record 3 in the afternoon and Record 4 in the evening, both in basins structurally distinct from the Aquiles basin (different worst-pair indices). Record 4 — the deepest known packing for the cell as of this writing — required approximately 9 minutes of wall time on the same Mac M2 single-thread.

> **Note on runtime.** Earlier versions of the documentation for Records 1 and 2 stated, in error, that each run took "approximately 5.5 hours". That figure was a memory-based estimate from the drafting AI assistant, not a number read from the actual Mac log. The correct figures (Records 1 and 2: 5 min wall time each; Record 4: 568 s ≈ 9 min 28 s wall time, all byte-exact reproducible) are documented in [`ERRATA.md`](ERRATA.md). The records themselves were never affected.

---

## What the engines actually are

**Aquiles** is the codename for the C++ engine that produced Records 1 and 2. It is single-threaded, allocates a few kilobytes of memory, compiles with `g++ -O3 -march=native -std=c++17 -funroll-loops`, and produces a world-record packing in under six minutes when given a structurally appropriate warmstart. It is hand-tuned for the geometry of complex Grassmannian coherence packings, with flat-array POD complex doubles, incremental Gram updates, smoothed-max loss with an aggressive logarithmic temperature schedule, Riemannian retraction after each gradient step, heavy-ball momentum, and a refutation-criterion-driven kill.

**Boagrius** is the codename for the second C++ engine, which produced Records 3 and 4. It uses a different conceptual framework: instead of a smoothed-max landscape, Boagrius operates on a constrained-feasibility formulation where the coherence is treated as a hard constraint and the engine iterates on the constraint residual until convergence within a quad-precision feasibility tolerance. The two engines are complementary: Aquiles is exploratory (good at finding new basins from random or sandbox warmstarts), Boagrius is exploitative (good at deepening a known basin to the limit of floating-point precision).

The leverage in this project does not live in either engine alone. It lives in **the combination of fast disciplined engines and a sandbox protocol that discovers the right places on the manifold to launch them from**. A higher-level description is in [`METHODOLOGY.md`](METHODOLOGY.md). The full source code of both engines is held under separate licensing arrangement (see *Licensing and engine availability* below).

---

## What's in this repository

- **[`PROOF.md`](PROOF.md)** — Smoking-gun one-pager. Everything needed to be convinced (or to disprove) in a single read.
- **[`RESULTS.md`](RESULTS.md)** — Headline numbers, bounds comparison, gap analysis.
- **[`RECORDS.md`](RECORDS.md)** — Raw verifier outputs for all four packings.
- **[`METHODOLOGY.md`](METHODOLOGY.md)** — High-level description of both engines (full source code reserved; see *Licensing and engine availability* below).
- **[`GUIDE FOR EVERYONE.md`](GUIDE%20FOR%20EVERYONE.md)** — For non-mathematicians: what a Grassmannian packing is and why people care.
- **[`CITATION.md`](CITATION.md)** and **[`CITATION.cff`](CITATION.cff)** — How to cite this work.
- **[`LICENSE`](LICENSE)** and **[`LICENSE.md`](LICENSE.md)** — Open content (MIT) and engine licensing terms.
- **[`ERRATA.md`](ERRATA.md)** — Permanent record of any correction made to the documentation after publication, including the full Mac runtime log for record #2.
- **[`Paper sloane v15 public .md`](Paper%20sloane%20v15%20public%20.md)** — Original technical paper covering Records 1 and 2, exploration history, and the structural findings about the basin landscape on May 12.
- **[`Paper sloane v16 public.md`](Paper%20sloane%20v16%20public.md)** — Updated technical paper extending the v15 coverage to Records 3 and 4 (Boagrius engine, May 16 sessions). Maintained alongside v15; v15 is preserved as a snapshot of the May 12 state.
- **[`4x64_record1.txt`](4x64_record1.txt)**, **[`4x64_record2.txt`](4x64_record2.txt)**, **[`4x64_record3.txt`](4x64_record3.txt)**, and **[`4x64_record4.txt`](4x64_record4.txt)** — All four packings, in standard Game of Sloanes file format (2·d·n floating-point values: 4·64 real parts followed by 4·64 imaginary parts).
- **[`run_record1.log`](run_record1.log)**, **[`run_record2.log`](run_record2.log)**, and **[`run_record4.log`](run_record4.log)** — Mac runtime logs. The log for Record 3 is preserved in the author's local archive but is not included here; the verifier output in `RECORDS.md` serves as the canonical record for it.
- **[`verify_sloane_independent.py`](verify_sloane_independent.py)** — Independent Python verifier with its own clean-room kernel. Reproduces all four coherence values to machine precision.
- **[`WITNESS.md`](WITNESS.md)** — A note from Claude (Anthropic) describing its role in the collaboration.

---

## How to verify the records (anyone, in under one minute)

```bash
git clone https://github.com/tretoef-estrella/sloane-coherence-records.git
cd sloane-coherence-records
python3 verify_sloane_independent.py 4x64_record1.txt
python3 verify_sloane_independent.py 4x64_record2.txt
python3 verify_sloane_independent.py 4x64_record3.txt
python3 verify_sloane_independent.py 4x64_record4.txt
```

Expected output for record #4 (the deepest):

```
Parsed 64 vectors of dimension 4 (C^4).
Unit-norm check: PASSED (within 1e-10).
Welch lower bound (d=4, n=64): 0.4879500365
Coherence mu(Phi) = 0.687033931214091
Worst pair: vectors (9, 25) with |<v_9, v_25>| = 0.687033931214091
```

The verifier uses no project-internal code paths. It loads the packing as raw text, reconstructs the Gram matrix using its own routines, and computes the coherence. **All four records reproduce byte-exact.**

---

## Licensing and engine availability

- **Records themselves, verification scripts, paper, and documentation in this repository**: MIT License (see [`LICENSE`](LICENSE) and [`LICENSE.md`](LICENSE.md)). The mathematical results are free for everyone to use, cite, and build upon.
- **The full source code of the two optimisation engines** (*Aquiles* and *Boagrius*) is **not included in this repository**. It is available under a separate arrangement for research collaborations or commercial licensing. For inquiries, please contact the author (see *Contact* below).

The high-level methodology is described in [`METHODOLOGY.md`](METHODOLOGY.md) at the level expected of a research preprint: enough for a peer to understand the conceptual approach, but not a turnkey implementation.

---

## Acknowledgments

- **Henry Cohn, Abhinav Kumar, Gregory Minton and collaborators** — for the body of work on coherence packings that made this comparison possible, and for Professor Cohn's responsiveness in independently verifying record #2 within 43 minutes of being notified.
- **Emily King, John Jasper, Dustin Mixon** — for maintaining the Game of Sloanes reference repository (https://github.com/gnikylime/GameofSloanes), which sets the gold standard for reproducible coherence packings.
- **Anthropic** — for building Claude, the AI assistant that collaborated on the engineering, the sandbox exploration protocols, and the verification pipeline.
- **The community of researchers** working on Grassmannian packings, equiangular lines, MUBs, and SIC-POVMs — your work taught me what mattered and what didn't.

---

## Contact

Rafael Amichis Luengo · Madrid · independent researcher. email: tretoef@gmail.com

For research collaborations, licensing inquiries, or to discuss the methodology in depth, please open a GitHub issue or contact via the email listed on this account's GitHub profile.

---

## A note on the days these results happened

This repository documents two days of work — May 12, 2026, and May 16, 2026 — during which four sub-Cohn packings were obtained for the cell `(4, 64)` hlc, beating a 14-year-old record. The first two records (May 12) came from the Aquiles engine in two distinct basins sharing the same worst-pair indices. The third and fourth records (May 16) came from the Boagrius engine in basins structurally distinct from the Aquiles basin. The cumulative gap from Record 4 down to the Cohn baseline is approximately `−1.26 × 10⁻⁴` in absolute terms (`−0.0184%` relative). Each record was filtered through the same verification discipline: byte-exact ratification by five independent code paths, agreement on worst-pair indices, and (for Record 2) independent reproduction by the previous record holder.

The records stand. **Verified, reproducible, byte-exact, four sub-Cohn packings in a single cell over two days.**

---

*Last updated: 2026-05-18 (Records 3 and 4 added; structure of the four-record cascade documented).*
