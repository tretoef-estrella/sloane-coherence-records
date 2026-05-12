# Methodology

> A high-level description of the approach. Sufficient detail for a peer to
> understand the conceptual framework, the engineering choices, and the
> verification discipline; not a turnkey implementation. The full source
> code of the optimisation engine is available under separate arrangement
> for research collaboration or commercial licensing (see [`LICENSE`](LICENSE)
> and the *Contact* section of [`README.md`](README.md)).

---

## 1. Problem formulation

We seek a configuration `V = {v_1, ..., v_N} ⊂ ℂ^d` of `N` unit-norm vectors (`d=4`, `N=64`) that minimises the **coherence**
```
μ(V) = max_{i ≠ j} |⟨v_i, v_j⟩|
```
where `⟨·, ·⟩` is the standard Hermitian inner product on `ℂ^d`. The minimum is taken over the product manifold `M = (S^{2d-1})^N` of `N` unit spheres in `ℂ^d`. The cell `(d=4, n=64)` is one of the *Tier S* (most-studied, most-stubborn) entries in the *Game of Sloanes* reference; the previous best (Cohn et al.) had stood for over a decade.

The coherence is non-smooth (a max over `O(N²)` smooth quantities) and the manifold is non-convex (a Cartesian product of spheres). Both features have historically made this problem hard for off-the-shelf optimisers.

---

## 2. The water paradigm (high-level)

Most prior algorithms for this problem fall into two families:

1. **First-order methods on the original (non-smooth) objective** — alternating projection, BCASC (Zörlein & Bossert 2014), various forms of stochastic descent. These zigzag at the kinks of the max function and tend to get pinned at saddle points.
2. **Manifold optimisation on smoothed surrogates** — ManOpt, gradient methods on log-sum-exp approximations (Cuevas-Beltrán et al., Jasper-Mixon-King 2019). These converge well within a basin but rely heavily on the starting point.

The approach taken here, internally referred to as the *water paradigm*, combines four ingredients in a way that — to our knowledge — does not appear in the published literature on this specific cell:

1. **A smoothed-max objective** `L_β(V) = (1/β) log Σ_{i<j} exp(β · |⟨v_i, v_j⟩|²)` with `β` scheduled logarithmically from a small value (gentle, navigates the landscape) to a very large value (sharp, lands exactly on the true coherence). This is well-known machinery.
2. **A Riemannian gradient flow with momentum** on the product-of-spheres manifold, with explicit tangent projection and retraction at each step. The momentum term is critical — it carries the iterate through shallow ridges that pure gradient descent would stall on.
3. **A structure-aware warmstart strategy**, where the initial configuration is not random and not the previous record, but is selected from a family of *satellite basins* discovered by a separate sandbox-exploration step. This is the most important ingredient and the principal source of leverage over prior work.
4. **A disciplined refutation protocol** that automatically terminates a run if no improvement is observed within a window proportional to the total budget. This prevents wasted compute on runs that have already converged or that fell into a shallow basin.

The interaction between these four ingredients is non-trivial. A naive combination of the first three (smoothed-max + Riemannian gradient + random or Cohn-based warmstart) does not beat the record. The fourth — refutation discipline — was learned the hard way over several earlier attempts on smaller test cells.

---

## 3. Sandbox exploration (what produces the warmstarts)

Before any Mac compute is spent on a long optimisation run, an inexpensive Python sandbox is used to map the *structure* of the landscape around a reference packing (the previous record, the Cohn baseline, or a recently obtained record). This step is purely exploratory; it does no Riemannian optimisation. It produces a small ranked list of *candidate basins* — locations in the manifold that are clearly distinct from the reference (by a Gram-invariant signature distance) and that show promising local behaviour under a fast coarse descent.

The candidate basins serve as the **warmstart** for the full Riemannian gradient-flow run on the Mac. Different candidates lead to different local minima of the smoothed-max objective. Some are deeper than others. The two records reported here came from two structurally distinct candidates.

What makes this protocol work where prior approaches stalled is the *structural distinctness* criterion: each candidate is required to differ from the reference packing by a non-trivial Gram-invariant distance (`> 0.005` in normalised L²), which filters out candidates that would collapse back into the same basin under any local descent. Without this filter, the warmstart family is dominated by trivial perturbations of the reference, and the resulting "exploration" is just noise.

---

## 4. Verification discipline

A coherence record is only useful if it is reproducible by an independent observer. The verification pipeline used here is built around the principle **"if five independent code paths agree, the bug is unlikely to be common"**:

- **D190-style four-step verification.** Each Mac run terminates by (1) recomputing the coherence from a *cold rebuild* of the packing inside the engine; (2) serialising the packing to the standard *Game of Sloanes* file format; (3) reloading the serialised file and recomputing again; (4) running an independent Python verifier with its own kernel.
- **Triple-kernel sandbox cross-check.** Beyond the engine's own three internal checks, three additional kernels are run in the Python sandbox: (a) NumPy BLAS `conj().T @ V` matrix multiplication; (b) a pure-Python double loop computing each inner product manually, with no NumPy involvement; (c) `np.vdot(V[i], V[j])` per pair using LAPACK. All three are written from scratch and use different code paths.
- **Worst-pair byte-exact cross-validation.** The indices `(i, j)` of the worst pair are required to agree across all five code paths. This is a non-trivial check: a bug that produced the right numerical coherence value by mistake would almost certainly identify a different worst pair.

The full output of the four-step verification on both records is included in [`RECORDS.md`](RECORDS.md). The Python verifier (`verification/verify_sloane_independent.py`) is included in this repository and can be run on any machine with Python 3 and NumPy.

---

## 5. Engineering notes

The engine is written in C++17, compiles with `g++ -O3 -march=native -std=c++17 -funroll-loops`, and runs on a single thread of an Apple M2 chip at 25% CPU throttle (via `taskpolicy -c utility`). The runtime for a full 10-million-step run is approximately 5.5 hours. Each step is dominated by the recomputation of the Gram matrix and the smoothed-max gradient — `O(N² · d)` for the inner products plus `O(N²)` for the softmax weights — implemented with a flat-array `cdouble {double re; double im;}` POD type for cache friendliness. The memory footprint is trivial (kilobytes).

The engine accepts CLI arguments for `MAX_STEPS`, `--warmstart=<file.txt>`, `--seed=<int>`, and beta-schedule and learning-rate parameters. Output is in the standard *Game of Sloanes* format: `2·d·N` floating-point values (real parts of all coordinates first, then imaginary parts), one per line.

The full source is not included in this repository. A peer with experience in Riemannian manifold optimisation could reimplement the framework described above in approximately 300–500 lines of C++ or Python; the difficulty is not in the implementation but in the calibration (beta schedule, momentum coefficient, learning-rate adaptation, kill-window) and in the sandbox-exploration protocol that produces the warmstart family.

---

## 6. Why is this not in the published literature?

Three reasons, conjectured:

1. **The smoothed-max + Riemannian-gradient + momentum combination is straightforward, but the *aggressive* beta schedule (going from `β ≈ 50` up to `β ≈ 10⁸`) was, in our experience, the part most researchers shy away from.** A large terminal `β` makes the objective extremely sharp near a saturated worst pair, and naive implementations encounter numerical issues that look like "the algorithm doesn't work" but are actually just one or two implementation details (renormalisation discipline, softmax stability) that need to be handled correctly.
2. **The sandbox exploration protocol that produces the warmstart family is, frankly, not the kind of step a typical research paper documents.** It is closer to engineering folklore than to publishable algorithm design. But it is what made the difference.
3. **The cell `(4, 64)` is not the cell most researchers focus on.** The community attention has been on smaller cells (`(3, 9)`, `(3, 13)`) where structural questions remain open, and on the large equiangular-tight-frame cells. `(4, 64)` was sitting there with a record that just had not been seriously attacked in a long time.

The methodology generalises to other cells — at least, we have reason to believe so from the development history — but each cell has its own structural features that affect the warmstart family. Future work will report on `(d, n)` pairs beyond `(4, 64)`.

---

## 7. What the paper covers

The technical paper [`paper/PAPER_SLOANE_v15.md`](paper/PAPER_SLOANE_v15.md) contains:

- The detailed history of both records, with byte-exact step-by-step Mac logs.
- Six post-record sandbox exploration probes (termite, rat, bat-echo, mercury, vanilla-Adam, and a hub-vertex variant), all of which **refuted** the hypothesis that a third record was accessible by local refinement of the second-record basin.
- Five structural findings (catalogued as "F-Sloane-NEW v15 #1–#3" plus inherited findings from earlier project iterations) about the topology of the basin landscape around the records.
- Five disciplinary doctrines (catalogued as "D-Sloane-NEW v15 #1–#3") on sandbox-first verification, multi-kernel ratification, and refutation criteria.

The paper is written in an unusual mixed-language style (Spanish prose with technical English) for historical reasons of the project; a translated, formally-typeset version is in preparation for submission to a peer-reviewed journal.

---

## Contact for collaboration

The author welcomes correspondence from researchers in frame theory, Grassmannian optimisation, compressed sensing, and quantum information theory — particularly those interested in collaborating on extensions to other cells `(d, n)` or in applying the methodology to related problems (equiangular lines, mutually unbiased bases, SIC-POVMs, kissing numbers).

For licensing of the engine source code for academic or commercial use, please open a GitHub issue or contact the author directly via the email on this GitHub profile.
