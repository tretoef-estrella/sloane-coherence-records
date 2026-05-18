# Methodology

> A high-level description of the approach. Sufficient detail for a peer to
> understand the conceptual framework, the engineering choices, and the
> verification discipline; not a turnkey implementation. The full source
> code of the optimisation engines is available under separate arrangement
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

## 2. Two complementary engines

The four records reported in this repository were produced by two distinct optimisation engines, used in succession. They are conceptually complementary: one is exploratory, one is exploitative.

### 2.1 Aquiles — the water paradigm (Records 1 and 2)

Aquiles is the engine that produced Records 1 and 2 on May 12, 2026. It implements a smoothing-based approach to the non-smooth coherence objective:

The non-smooth coherence is replaced by a one-parameter family of smooth surrogates — a soft-maximum over the squared absolute values of the off-diagonal Gram entries. The smoothing parameter is **scheduled** from very gentle at the start of the optimisation (the landscape feels almost flat and the iterate navigates easily) to very sharp at the end (the surrogate becomes essentially indistinguishable from the true coherence). Internally the author refers to this as *the water paradigm*: water finds the lowest path through a complex terrain by gentle persistence, not by clever jumps.

The optimisation is done on the natural Riemannian manifold structure (each vector stays on its unit sphere, retraction after each update, tangent projection of the gradient). A momentum term carries the iterate through shallow ridges where pure gradient descent would stall.

The starting configuration is selected from a small family of **candidate basins** discovered by a separate, lightweight sandbox exploration step (described in §3 below). Different candidates lead to different local minima of the smoothed objective; Records 1 and 2 came from two structurally distinct candidates.

### 2.2 Boagrius — constrained-feasibility paradigm (Records 3 and 4)

Boagrius is the engine that produced Records 3 and 4 on May 16, 2026. It takes a fundamentally different approach to the same problem:

Rather than smoothing the non-smooth coherence and descending the smooth surrogate, Boagrius reformulates the problem as a **constrained-feasibility iteration**. The coherence is treated as a hard inequality constraint that is progressively tightened, and the engine iterates on the feasibility residual until it converges within a tight tolerance set near the limit of floating-point precision.

This formulation is particularly well-suited for **deepening a known basin** to the floor visible to floating-point arithmetic. Where Aquiles is good at *finding* a new basin from a structurally distinct warmstart, Boagrius is good at *exploiting* a basin already known to be deep — squeezing additional resolution out of a configuration that smoothing-based methods have already brought close to optimum.

The two engines are designed to be cascadable: Aquiles produces a Record-2-quality packing in a basin; Boagrius then takes that packing as warmstart, may transition to a structurally distinct nearby basin during the constraint tightening, and converges to the floor of that new basin. Records 3 and 4 are the result of this cascade.

### 2.3 Why two engines, not one

A single engine attempting both exploration and exploitation suffers a well-known dilemma: the calibration that finds new basins from a cold start is incompatible with the calibration that descends the last few decimal places within a known basin. By splitting the labour between two specialised engines and a sandbox-based handoff protocol, each engine can be tuned for its specialty. The technical papers (`Paper sloane v15 public.md` and `Paper sloane v16 public.md`) describe the handoff protocol in further detail.

A fourth ingredient — present in both engines — is a **disciplined refutation protocol** that automatically terminates a run if no improvement is observed within a window proportional to the total budget. This prevents wasted compute on runs that have already converged or that fell into a shallow basin. The discipline is inherited from prior projects (Sobol, Luna, Diamante) and was refined in early test runs on smaller cells.

The interaction between the four ingredients (smoothing, manifold-aware optimisation, sandbox warmstart selection, refutation discipline) is non-trivial. A naive combination of the first three does not beat the record. The fourth — refutation discipline — was learned the hard way over several earlier attempts on smaller test cells. Each ingredient on its own is in the published literature; the combination, at the specific calibration that makes it work for this cell, is the engineering contribution.

---

## 3. Sandbox exploration (what produces the warmstarts)

Before any Mac compute is spent on a long optimisation run, an inexpensive Python sandbox is used to map the *structure* of the landscape around a reference packing (the previous record, the Cohn baseline, or a recently obtained record). This step is purely exploratory; it does no manifold optimisation. It produces a small ranked list of *candidate basins* — locations in the manifold that are clearly distinct from the reference (by a Gram-invariant signature distance) and that show promising local behaviour under a fast coarse descent.

The candidate basins serve as the **warmstart** for the full Mac optimisation run. Different candidates lead to different local minima.

What makes this protocol work where prior approaches stalled is the *structural distinctness* criterion: each candidate is required to differ from the reference packing by a non-trivial Gram-invariant distance (`> 0.005` in normalised L²), which filters out candidates that would collapse back into the same basin under any local descent. Without this filter, the warmstart family is dominated by trivial perturbations of the reference, and the resulting "exploration" is just noise.

For Records 3 and 4, the Boagrius engine was launched from a **cascade warmstart** — the output of the previous record in the chain rather than a freshly sandbox-discovered basin. This is more economical when the engine in question (Boagrius) is well-suited to exploit a basin that the previous record had not yet driven to its floor.

---

## 4. Verification discipline

A coherence record is only useful if it is reproducible by an independent observer. The verification pipeline used here is built around the principle **"if five independent code paths agree, the bug is unlikely to be common"**:

- **Multi-step verification at run termination.** Each Mac run terminates by recomputing the coherence from a *cold rebuild* of the packing inside the engine, serialising the packing to the standard *Game of Sloanes* file format, reloading the serialised file and recomputing again, and running an independent Python verifier with its own kernel.

- **Five-kernel sandbox cross-check.** Five additional kernels are run in the Python sandbox:

  1. **NumPy BLAS `conj().T @ V`** matrix multiplication (full Gram matrix construction).
  2. **Pure-Python double loop**, no NumPy involvement at all — manual Hermitian inner product with two nested for-loops.
  3. **`np.vdot(V[i], V[j])`** per pair (LAPACK path).
  4. **mpmath arbitrary precision** at 50 decimal digits — inner product computed in extended precision.
  5. **Python `decimal` library** arbitrary precision at 40 digits — manual complex multiplication in decimal arithmetic, a totally different code path from mpmath.

  All five are written from scratch and use different code paths.

- **Worst-pair byte-exact cross-validation.** The indices `(i, j)` of the worst pair are required to agree across all five code paths. This is a non-trivial check: a bug that produced the right numerical coherence value by mistake would almost certainly identify a different worst pair.

The full output of the five-kernel cross-validation for each of the four records is included in [`RECORDS.md`](RECORDS.md). The Python verifier (`verify_sloane_independent.py`) is included in this repository and can be run on any machine with Python 3 and NumPy.

---

## 5. Engineering notes

Both engines are written in C++17, compile with `g++ -O3 -march=native -std=c++17 -funroll-loops`, and run on a single thread of an Apple M2 chip at 25% CPU throttle. The runtime is approximately 5 minutes for an Aquiles run (Records 1 and 2: 5 min wall time each), and approximately 9 minutes for a Boagrius run starting from a near-optimal warmstart (Record 4: 568 s = 9 min 28 s).

Each step in either engine is dominated by the recomputation of the Gram matrix and a gradient over its off-diagonal entries — `O(N² · d)` for the inner products plus `O(N²)` for the loss derivatives — implemented with a flat-array `cdouble {double re; double im;}` POD type for cache friendliness. The memory footprint is trivial (kilobytes).

Both engines accept CLI arguments for the maximum number of iterations, a warmstart file in the standard Game of Sloanes format, a random seed, and the engine-specific calibration parameters. Output is in the standard *Game of Sloanes* format: `2·d·N` floating-point values (real parts of all coordinates first, then imaginary parts), one per line.

The full source code of both engines is not included in this repository. A peer with experience in Riemannian manifold optimisation could reimplement the Aquiles framework described above in approximately 300–500 lines of C++ or Python; a peer with experience in constrained optimisation could reimplement Boagrius in a similar amount of code. The difficulty in both cases is not in the implementation but in the calibration and in the sandbox-exploration / cascade-handoff protocols that produce the warmstart family.

---

## 6. Why is this not in the published literature?

Three reasons, conjectured:

1. **The smoothed-max + Riemannian-gradient + momentum combination is straightforward, but the aggressive smoothing schedule was, in our experience, the part most researchers shy away from.** A sharp terminal smoothing makes the objective extremely sharp near a saturated worst pair, and naive implementations encounter numerical issues that look like "the algorithm doesn't work" but are actually just one or two implementation details (renormalisation discipline, numerical stability of the smoothed-max) that need to be handled correctly.

2. **The sandbox exploration protocol that produces the warmstart family is, frankly, not the kind of step a typical research paper documents.** It is closer to engineering folklore than to publishable algorithm design. But it is what made the difference.

3. **The cell `(4, 64)` is not the cell most researchers focus on.** The community attention has been on smaller cells (`(3, 9)`, `(3, 13)`) where structural questions remain open, and on the large equiangular-tight-frame cells. `(4, 64)` was sitting there with a record that just had not been seriously attacked in a long time.

The methodology generalises to other cells — at least, we have reason to believe so from the development history — but each cell has its own structural features that affect the warmstart family.

---

## 7. What the papers cover

The original technical paper [`Paper sloane v15 public.md`](Paper%20sloane%20v15%20public%20.md) (May 12, 2026, snapshot) covers:

- The detailed history of Records 1 and 2, with byte-exact step-by-step Mac logs.
- Six post-record sandbox exploration probes (termite, rat, bat-echo, mercury, vanilla-Adam, and a hub-vertex variant) applied to Record 2, all of which **refuted** the hypothesis that a third record was accessible by local refinement of the Record-2 basin.
- Five structural findings about the topology of the basin landscape around Records 1 and 2.

The extended paper [`Paper sloane v16 public.md`](Paper%20sloane%20v16%20public.md) (May 16, 2026, snapshot) extends the v15 coverage with:

- The Boagrius engine and the cascade-warmstart protocol.
- The basin transitions from Record 2 (worst pair `(31, 38)`, Aquiles basin) to Record 3 (worst pair `(6, 17)`) to Record 4 (worst pair `(9, 25)`).
- The structural finding that a single cell can host multiple sub-Cohn basins with distinct worst-pair topologies, and the implications for future exploration.
- An updated assessment of where further improvements might (or might not) be accessible.

The v15 paper is preserved unchanged as a historical snapshot of the May 12 state; the v16 paper extends rather than replaces it.

---

## Contact for collaboration

The author welcomes correspondence from researchers in frame theory, Grassmannian optimisation, compressed sensing, and quantum information theory — particularly those interested in collaborating on extensions to other cells `(d, n)` or in applying the methodology to related problems (equiangular lines, mutually unbiased bases, SIC-POVMs, kissing numbers).

For licensing of the engine source code for academic or commercial use, please open a GitHub issue or contact the author directly via the email on this GitHub profile.
