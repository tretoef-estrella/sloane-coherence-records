# sloane-coherence-records

> **Two world records in Grassmannian coherence packings (d=4, n=64) hlc — May 12, 2026**
>
> Independent researcher, Madrid · Mac M2 single-thread · One day · Two records.

---

## At a glance

On May 12, 2026, the longstanding world record for the minimum-coherence packing of 64 unit vectors in complex 4-dimensional space (held by Henry Cohn et al.) was beaten **twice in a single day** using a novel optimisation paradigm developed by a self-taught researcher running on a personal Mac M2 laptop, in collaboration with the AI assistant Claude (Anthropic). **Each record run took approximately 5 minutes of wall time** on a single CPU thread throttled to 25%.

| Holder | Date | μ (coherence) | Gap vs. Cohn |
|:---|:---|:---|:---|
| Henry Cohn et al. (Game of Sloanes) | ~2010–2024 | `0.687160201509307` | — (baseline) |
| **Amichis Luengo (record #1)** | **2026-05-12 (afternoon CEST)** | **`0.687040494471422`** | **−1.197 × 10⁻⁴** |
| **Amichis Luengo (record #2)** | **2026-05-12 (evening CEST)** | **`0.687035170223597`** | **−1.250 × 10⁻⁴ (−0.0182%)**  |

Both packings have been independently verified, including byte-exact reproduction by Professor **Henry Cohn (MIT)** in his own code on May 12, 2026 (43 minutes after notification by the author), and verified byte-exact by **five independent kernels** internally (the engine itself in C++, an independent Python verifier, and three numerical kernels in three different code paths: NumPy BLAS matmul, pure-Python loop, and `np.vdot` per pair). All five report identical coherence to machine precision. Worst pair in both records: vectors **(31, 38)**, byte-exact preserved across two structurally distinct basins.

---

## Why this matters

Grassmannian frame packings in the cell `(d=4, n=64)` are not just a mathematical curiosity. They are used in:

- **CDMA wireless codes** — minimum-coherence sequences minimise multi-user interference.
- **MIMO precoding** — unitary matrices for multi-antenna systems (Wi-Fi 6E/7 and 5G NR with 4 antennas).
- **Compressed sensing** — measurement matrices whose recovery guarantees depend directly on coherence (Donoho-Elad-Bruckstein).
- **Quantum state tomography** — frames analogous to SIC-POVMs.

A 0.0182% improvement in coherence translates into a measurable improvement in recovery probability bounds for compressed sensing of 4-sparse signals measured by 64 sensors, and into a new benchmark for packing-based codes in MIMO and CDMA contexts. The previous record had stood for over 14 years.

---

## The story, in one paragraph

Cohn et al. had held the record for `(4, 64)` hlc for over a decade. The standard approach to this problem (alternating projections, BCASC, ManOpt, gradient-based refinement) had been thoroughly explored by the experts. **A new optimisation paradigm — internally codenamed the *water paradigm* — combined Riemannian gradient flow over a smoothed-max coherence loss with a structure-aware warmstart strategy.** From a Mac M2 with no special hardware, **each of the two final record runs took approximately 5 minutes of wall time** once the warmstart was supplied. The records are not the product of brute compute; they are the product of a carefully calibrated engine — written for this purpose and refined across three prior projects — driven by a sandbox-discovered warmstart family. The engine itself, internally named *Aquiles*, processes about 33 000 steps per second on a single throttled M2 thread. Both records were obtained the same day, in two distinct basins of the optimisation landscape, byte-exact reproducible from the same warmstart files included in this repository.

> **Note on runtime.** Earlier versions of this documentation stated, in error, that each run took "approximately 5.5 hours". That figure was a memory-based estimate from the drafting AI assistant, not a number read from the actual Mac log. The correct figure (verified at **5 minutes 0.42 seconds** wall time, byte-exact reproducible) is documented in [`ERRATA.md`](ERRATA.md), which also includes the **complete unedited Mac runtime log** of the re-execution that verified the timing. The records themselves were never affected; only the narrative claim about how long the runs took.

---

## What the engine actually is

**Aquiles** is the codename for the C++ engine that produced both records. It is single-threaded, allocates a few kilobytes of memory, compiles with `g++ -O3 -march=native -std=c++17 -funroll-loops`, and produces a world-record packing in under six minutes when given a structurally appropriate warmstart. It is not a general-purpose optimiser; it is hand-tuned for the geometry of complex Grassmannian coherence packings — flat-array POD complex doubles, incremental Gram updates, smoothed-max loss with an aggressive logarithmic temperature schedule, Riemannian retraction after each gradient step, heavy-ball momentum, and a refutation-criterion-driven kill that prevents wasted compute on dead-end runs.

The leverage in this project does not live in the engine alone. It lives in **the combination of a fast, disciplined engine and a sandbox protocol that discovers the right places on the manifold to launch it from**. A higher-level description is in [`METHODOLOGY.md`](METHODOLOGY.md). The engine source code itself is held under separate licensing arrangement (see *Licensing and engine availability* below).

---

## What's in this repository

- **[`PROOF.md`](PROOF.md)** — Smoking-gun one-pager. Everything needed to be convinced (or to disprove) in a single read.
- **[`RESULTS.md`](RESULTS.md)** — Headline numbers, bounds comparison, gap analysis.
- **[`RECORDS.md`](RECORDS.md)** — Raw verifier outputs for both packings.
- **[`METHODOLOGY.md`](METHODOLOGY.md)** — High-level description of the approach (full engine source code reserved; see *Licensing and engine availability* below).
- **[`GUIDE FOR EVERYONE.md`](GUIDE%20FOR%20EVERYONE.md)** — For non-mathematicians: what a Grassmannian packing is and why people care.
- **[`CITATION.md`](CITATION.md)** and **[`CITATION.cff`](CITATION.cff)** — How to cite this work.
- **[`LICENSE`](LICENSE)** and **[`LICENSE.md`](LICENSE.md)** — Open content (MIT) and engine licensing terms.
- **[`ERRATA.md`](ERRATA.md)** — Permanent record of any correction made to the documentation after publication, including the full Mac runtime log for record #2.
- **[`Paper sloane v15 public .md`](Paper%20sloane%20v15%20public%20.md)** — Full technical paper covering both records, exploration history, and the structural findings about the basin landscape.
- **[`4x64_record1.txt`](4x64_record1.txt)** and **[`4x64_record2.txt`](4x64_record2.txt)** — Both packings, in standard Game of Sloanes file format (2·d·n floating-point values: 4·64 real parts followed by 4·64 imaginary parts).
- **[`run_record1.log`](run_record1.log)** and **[`run_record2.log`](run_record2.log)** — Complete Mac runtime logs, step by step.
- **[`verify_sloane_independent.py`](verify_sloane_independent.py)** — Independent Python verifier with its own clean-room kernel. Reproduces both coherence values to machine precision.
- **[`WITNESS.md`](WITNESS.md)** — A note from Claude (Anthropic) describing its role in the collaboration.

---

## How to verify the records (anyone, in under one minute)

```bash
git clone https://github.com/tretoef-estrella/sloane-coherence-records.git
cd sloane-coherence-records
python3 verify_sloane_independent.py 4x64_record1.txt
python3 verify_sloane_independent.py 4x64_record2.txt
```

Expected output for record #2:

```
Parsed 64 vectors of dimension 4 (C^4).
Unit-norm check: PASSED (within 1e-10).
Welch lower bound (d=4, n=64): 0.4879500365
Coherence mu(Phi) = 0.687035170223597
Worst pair: vectors (31, 38) with |<v_31, v_38>| = 0.687035170223597
```

The verifier uses no project-internal code paths. It loads the packing as raw text, reconstructs the Gram matrix using its own routines, and computes the coherence. **Both records reproduce byte-exact.**

---

## Licensing and engine availability

- **Records themselves, verification scripts, paper, and documentation in this repository**: MIT License (see [`LICENSE`](LICENSE) and [`LICENSE.md`](LICENSE.md)). The mathematical results are free for everyone to use, cite, and build upon.
- **The full source code of the optimisation engine** (informally referred to as *Engine 9* / *Aquilestrincaestacasvaaporhectorelresacas*, internally just *Aquiles*) is **not included in this repository**. It is available under a separate arrangement for research collaborations or commercial licensing. For inquiries, please contact the author (see *Contact* below).

The high-level methodology is described in [`METHODOLOGY.md`](METHODOLOGY.md) at the level expected of a research preprint: enough for a peer to understand the conceptual approach, but not a turnkey implementation.

---

## Acknowledgments

- **Henry Cohn, Abhinav Kumar, Gregory Minton and collaborators** — for the body of work on coherence packings that made this comparison possible, and for Professor Cohn's responsiveness in independently verifying record #2 within 43 minutes of being notified.
- **Emily King, John Jasper, Dustin Mixon** — for maintaining the Game of Sloanes reference repository (https://github.com/gnikylime/GameofSloanes), which sets the gold standard for reproducible coherence packings.
- **Anthropic** — for building Claude, the AI assistant that collaborated on the engineering, the sandbox exploration protocols, and the verification pipeline.
- **The community of researchers** working on Grassmannian packings, equiangular lines, MUBs, and SIC-POVMs — your work taught me what mattered and what didn't.

---

## Contact

Rafael Amichis Luengo · Madrid · independent researcher

For research collaborations, licensing inquiries, or to discuss the methodology in depth, please open a GitHub issue or contact via the email listed on this account's GitHub profile.

---

## A note on the day this happened

This repository documents one day of work — May 12, 2026 — during which the record was beaten, beaten again, and then the structure of the basin around the second record was mapped through six independent sandbox probes (termite, rat, mosquito, bat-echo, mercury, and a vanilla Adam smoke test). Each probe was filtered through a four-criterion discipline check before any code ran. The second record turned out to be a **strong local minimum** of the water paradigm — confirmed by Hessian numerics — meaning a third record would require either a structurally distinct basin or a qualitatively new algorithmic approach. That work is for another day.

The records, however, stand. **Verified, reproducible, byte-exact, independently confirmed by the previous record holder.**

---

*Last updated: 2026-05-13 (errata applied).*
