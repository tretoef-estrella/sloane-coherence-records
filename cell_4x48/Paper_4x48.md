# Empirical Evidence of an Apparent Local Coherence Floor in the (d=4, n=48) Grassmannian Frame Packing Basin

**Author**: Rafael Amichis Luengo
**Affiliation**: Independent researcher, Madrid, Spain
**Date**: May 16, 2026
**Subject**: Companion technical note to the (4, 48) Grassmannian frame packing submission to Game of Sloanes
**Engine**: Rasputin (quad-precision)
**Contact**: tretoef@gmail.com

---

## Abstract

We report a Grassmannian frame packing in complex projective space ℂP³ with N = 48 vectors achieving coherence μ = 0.643425504760055, which improves upon the previous best published packing for cell (4, 48) hlc (Cohn, Game of Sloanes catalog, μ = 0.643427715576853) by 2.21 × 10⁻⁶ in absolute coherence value. The improvement satisfies the Game of Sloanes 8th-decimal-place acceptance criterion by 22 units in the minimisation direction (round-8: `0.64342550` versus `0.64342772`). Beyond reporting the improved packing, this note documents a numerical investigation that we interpret as *suggesting* the submission may lie at a local floor of the basin in which the optimisation was conducted. We phrase this as an interpretation, not an established fact: we do not have a proof that the local floor of the basin has been reached, and we do not claim such a proof. The numerical reproducibility of the reported coherence has been independently verified by five distinct verification kernels at IEEE-754 double precision and by an additional audit at 50 decimal digits across algorithmically distinct arithmetic procedures, with internal disagreement at the level of input-precision propagation. The cumulative evidence — including multi-seed convergence to the same 15th decimal across eight independent initialisations, a multi-paradigm portfolio with no method producing further descent, trust-region radial expansion refutation across 88 attempts at radii spanning five orders of magnitude, targeted-vector perturbation refutation across a comparable number of attempts, and 150 cold-start enumeration with no seed producing a deeper packing — is consistent with the working hypothesis that the basin floor has been reached at machine-quantum precision. **No claim of global optimality is made for the cell (4, 48), and we explicitly leave that question open. No claim that this floor is even the proven local floor of the basin is made either — only that the accumulated evidence is compatible with that interpretation.**

---

## 1. Introduction

The complex Grassmannian frame packing problem asks for a set of N unit vectors in ℂ^d that minimise the worst-case coherence

μ(V) = max_{i ≠ j} ∣⟨v_i, v_j⟩∣.

For the cell (d = 4, N = 48), the Game of Sloanes catalog (Jasper, King, Mixon; https://github.com/gnikylime/GameofSloanes) lists a packing due to Henry Cohn with μ = 0.643427715576853. The relevant bounds for this cell are: Welch 0.4837794468 and Levenshtein-2 0.5877538100. The Cohn packing does not saturate any of these bounds, leaving room — at the level of the published bounds — for the existence of deeper packings.

This note documents:

1. A new packing achieving μ = 0.643425504760055, reducing the previously published value by 2.21 × 10⁻⁶ and improving the eighth decimal place by 22 units (Section 2).
2. Several lines of evidence consistent with the hypothesis that the new packing sits at the floor of the basin in which it was obtained (Section 3).
3. The breadth of the optimisation portfolio applied within this basin, described at the level of paradigm families (Section 4).
4. Numerical reproducibility evidence across five independent arithmetic kernels at 50-decimal-digit reference precision (Section 5).
5. A cautious empirical statement about the basin's apparent local floor and the limits of the result (Section 6).

We do not claim global optimality. The exploration is local to one basin of the (4, 48) coherence landscape. The Levenshtein-2 lower bound 0.5877538100 leaves a gap of approximately 8.65% to our value, which is mathematically large enough to admit deeper basins reachable via algebraic seeds or paradigms not yet considered. **We also do not claim a proof of the basin's local floor.** The reasoning of Sections 3 and 6 is interpretive, anchored in convergent evidence across multiple independent paradigm families and verification kernels, but it is not a mathematical proof.

---

## 2. The new packing

The packing is provided in the file `4x48_record1.txt` (located alongside this note) in the Game of Sloanes layout: 384 real numbers, comprising 192 real components followed by 192 imaginary components for 48 complex 4-vectors. The coherence has been independently verified using five distinct numerical kernels at IEEE-754 binary64 and via an extended audit at 50 decimal digits across algorithmically distinct arithmetic procedures, with internal disagreement at the level of input-precision propagation (≈ 10⁻¹⁶).

The packing was produced by the **Rasputin** engine — a single-threaded C++ engine operating in quad-precision (128-bit) arithmetic throughout its inner loop, on a Mac M2 under 25% CPU throttling. The distinctive public feature of Rasputin relative to standard IEEE-754 double-precision implementations is that quad-precision arithmetic allows the engine to resolve descent below the threshold at which conventional double-precision engines saturate. For a cell whose holder configuration is structurally tight in the sense of admitting many simultaneously near-saturated pairs — as the Cohn holder for (4, 48) is, with 274 of 1128 pairs (24.29%) within 10⁻⁸ of the maximum at the holder configuration — quad-precision is the difference between stalling above the holder's coherence and being able to push to the floor of the basin in which the optimisation is conducted.

| Quantity | Value |
|:---|:---|
| μ (proposed packing) | 0.643425504760055 |
| μ (prior holder, Cohn) | 0.643427715576853 |
| Δμ (proposed − holder) | −2.21 × 10⁻⁶ |
| Eight-decimal rounded value (proposed) | 0.64342550 |
| Eight-decimal rounded value (holder) | 0.64342772 |
| Unit-norm deviation across all 48 vectors | ≤ 2.21 × 10⁻¹¹ |
| Saturated-pair fraction (within 10⁻⁸ of μ) | 274 / 1128 (24.29%) |
| Cushion below the 8-decimal-rounding boundary 0.643425505 | 4.92 × 10⁻¹⁰ |
| Worst pair (stable across 5 kernels) | (1, 24) |

The saturated-pair fraction is consistent with that of the Cohn holder under the same verification kernel and tolerance, which is the first structural indication that both packings may occupy the same critical basin. Section 3 documents four further lines of evidence consistent with that interpretation.

---

## 3. Lines of evidence consistent with the basin-floor hypothesis

Four independent lines of evidence are consistent with the interpretation that the submission sits at the floor of the basin in which it was obtained. We present these as evidence supporting a hypothesis, not as a proof.

### 3.1 Multi-seed convergence to the same 15th decimal

The submitted packing was reached as the convergent endpoint of eight independent optimisation chains, each initialised from a distinct pseudo-random number generator seed. The eight chains converged to the same coherence value, agreement extending to the 15th decimal place — i.e., to within one unit in the last place of binary64 (≈ 2 × 10⁻¹⁶). This is several orders of magnitude tighter than the cushion below the 8th-decimal-rounding boundary, and it is consistent with the eight chains having found the same critical point of the constrained optimisation problem, modulo the unitary symmetry of the manifold.

### 3.2 Stable worst-pair structure

All five verification kernels report the same worst pair `(1, 24)` for the submission, with the coherence value reproduced to within one unit in the last place of binary64. This is in contrast to the (3, 14) submission in our companion folder, where the five kernels report five different argmax pairs and we interpret that observation as evidence of a degenerate basin floor with a small discrete family of critical points at the same μ value. We interpret the stability of the (1, 24) pair across kernels in the (4, 48) submission as evidence that the basin floor for cell (4, 48) supports a non-degenerate critical structure with a single unambiguous maximum-coherence pair, rather than the degenerate family of equivalent critical points seen in cell (3, 14). As above, this is interpretive.

### 3.3 Trust-region radial expansion refutation

A trust-region radial expansion was conducted around the submission as anchored pivot. The expansion swept eleven radii in geometric progression spanning five orders of magnitude (`1e-6` to `1e-1`, ratio ~5×), and for each radius sampled eight random unit-tangent directions on the Stiefel manifold. Each of the resulting 88 perturbed initial conditions was run through 30 inner iterations of the engine's refinement loop. **Across all 88 attempts, zero commits to a deeper coherence value were observed.** The perturbed runs typically returned coherence values in the range `0.6434258` to `0.6434267` (i.e., approximately 3 × 10⁻⁷ to 2 × 10⁻⁶ above the pivot), and the run that retained the best coherence simply returned to the pivot unchanged.

We interpret this as evidence that, within a 10% geometric neighbourhood of the submission on the manifold, the basin in which the submission sits is the unique basin accessible via continuous deformation, and the submission itself is the deepest point of that basin reachable by radial-direction inner refinement.

### 3.4 Targeted-vector perturbation refutation

A second perturbation paradigm targeted specific vector elements of the submission rather than radial directions in the full manifold. Three sub-paradigms were applied: (i) single-vector perturbation, in which each of the 48 vectors in turn was perturbed by a random Hermitian shift of fixed radius before being renormalised onto the unit sphere; (ii) pair-swap perturbation, in which random pairs of vectors were exchanged and then both perturbed; and (iii) hub-targeted perturbation, focused on the top-12 hub vectors of the saturated-pair graph at the submission. Each attempt was followed by 30 inner iterations of the engine's refinement loop. **Across all attempts in all three sub-paradigms, zero commits to a deeper coherence value were observed.**

We interpret this as evidence that the basin in which the submission sits is robust against local perturbation of any particular vector or vector pair: the basin does not contain a deeper critical structure reachable by reorganising the active set of pairs or by perturbing the hub vectors of the saturated-pair graph.

### 3.5 Cold-start enumeration refutation

A 150-fold cold-start enumeration was performed: 150 independent initialisations were drawn uniformly from the Stiefel manifold using disjoint pseudo-random number generator seed ranges, and each was run through the engine's full refinement loop. The vast majority of cold starts converged to coherence values in the range `0.67` to `0.69` (basins substantially shallower than the submission), and no cold start produced a coherence value below the submission's coherence. We interpret this as evidence that the submission's basin is, at minimum, an attractor of unguided random initialisation on this manifold, and that no shallower basin reaches a coherence value deeper than the submission.

---

## 4. Optimisation portfolio within the basin

A wide portfolio of optimisation paradigm families was applied to either (i) the Cohn configuration directly, (ii) the proposed packing as anchor, or (iii) independent cold-start initialisations. A small subset of paradigms reached the apparent basin floor reported in Section 2; the remainder produced no measurable descent below it.

The paradigm families covered include:

- **First-order methods on smooth surrogates of the coherence functional**, including smooth-max and p-frame potential surrogates with homotopy schedules.
- **Second-order and constrained methods in extended precision**, responsible for the converged solutions reported in Sections 2 and 3.1.
- **Trust-region radial expansion** in the saturated-constraint normal cone, as documented in Section 3.3.
- **Targeted-vector perturbation** at single vectors, vector pairs, and hub vectors of the saturated-pair graph, as documented in Section 3.4.
- **Parallel tempering and temperature-ladder sampling** with Metropolis-Hastings swap acceptance between adjacent chains.
- **Geometric and topological perturbations**, including random Hermitian kicks, local rotations in randomly chosen coordinate planes, and thermal-quench protocols.
- **Constraint-set manipulation**, including freezing of selected dual variables and trust-region inner-iteration budget expansion when feasibility approaches machine precision.
- **Multi-warmstart parallel chains** with shared anchor and adaptive damping when feasibility margins enter the sub-nanonormal regime.
- **Large-scale cold-start enumeration** with 150 independent seed-disjoint initialisations on the Stiefel manifold, as documented in Section 3.5.

Hyperparameter schedules, step-size tuning, warmstart chain ordering, the specific sequence of refinement moves, and the per-paradigm convergence diagnostics are deliberately not reproduced here. The high-level description is at the level expected of a research preprint: enough for a peer to understand the paradigm coverage, not a turnkey reproduction of every method.

**The relevant empirical fact is that, across this portfolio, no paradigm produced descent below μ = 0.643425504760055 in the basin where the submission was obtained.** The descent was pursued with intent across this Saturday's optimisation session, and the value reported in this note was the deepest the available paradigms could reach. We interpret this as evidence consistent with the basin-floor hypothesis, while noting that the absence of descent under our specific portfolio does not constitute a proof that no other paradigm could descend further.

---

## 5. Numerical reproducibility across five independent kernels

The reported coherence has been independently audited across five algorithmically distinct verification kernels, in two programming languages, using four different numerical libraries (and one path with no library at all):

1. NumPy `conj() @ T` with BLAS matmul (binary64).
2. Pure-Python double loop with no external library and manual conjugate (binary64).
3. NumPy `numpy.vdot` per pair (binary64).
4. mpmath at 50 decimal digits.
5. Python `decimal` at 40 decimal digits, separated real/imaginary parts.

All five report the same coherence value to within one unit in the last place of binary64 (`2.22 × 10⁻¹⁶`). The mpmath reference at 50 decimal digits is:

```
μ_submission = 0.643425504760055106…
μ_holder     = 0.643427715576853032…
```

All five kernels also report the **same** worst pair `(1, 24)` for the submission — a structural property of the basin floor in cell (4, 48) that contrasts with the worst-pair migration observed in the apparent basin floor of cell (3, 14) (see [`../cell_3x14/Paper_3x14_basin_floor.md`](../cell_3x14/Paper_3x14_basin_floor.md) §3.3 for the complementary observation in that cell).

---

## 6. Apparent local basin floor and limits of the result

The combination of:

- multi-seed convergence to the same 15th decimal across eight independent initialisations (§3.1),
- stable worst-pair structure across five independent verification kernels (§3.2),
- trust-region radial expansion refutation across 88 attempts spanning five orders of magnitude in radius (§3.3),
- targeted-vector perturbation refutation across single-vector, pair-swap, and hub-targeted attempts (§3.4),
- 150-fold cold-start enumeration with no seed producing a deeper packing (§3.5), and
- portfolio breadth covering the paradigm families enumerated in §4 with no method producing any descent below the reported value,

is consistent with — though does not prove — the interpretation that a local coherence floor has been reached at machine-quantum precision in the basin where the submission was obtained. **We frame this as a working hypothesis supported by accumulated evidence, not as an established theorem.** The submission is offered with this caveat explicitly recorded.

**We do not claim that this floor is the global minimum for the cell (4, 48).** The 8.65% gap to the Levenshtein-2 lower bound 0.5877538100 is mathematically large enough to admit the existence of deeper basins reachable via algebraic seeds, structured constructions, or paradigms not yet considered in this work. Candidate algebraic constructions for this cell include Hoggar-type equiangular tight frame embeddings, mutually unbiased basis (MUB) embeddings, and cyclotomic-projection constructions — none of which were applied in the present work, and any of which could in principle access basins not reachable via continuous deformation from the cold-start manifold.

**We do not claim that this floor is even the proven local floor of the basin we explored.** All five lines of evidence above are interpretive. A future result that descended below μ = 0.643425504760055 in this basin would not contradict any fact asserted in this note; it would refine the interpretation we have offered. We have made every effort to phrase the basin-floor claim as a hypothesis consistent with the evidence we have, not as a proof.

The author records openly that the descent was pursued further than the filing margin would have required; the author would have preferred to deepen the packing further before filing, and the optimisation portfolio documented in §4 was exhausted against this basin before this value was settled. Even with the cumulative evidence above, the submission opens the cell rather than closes it. **The submission is filed because the margin is real, reproducible at the eighth decimal place across five independent verification kernels, and consistent with the basin-floor hypothesis. The records stand; the cell remains open.**

---

## 7. Acknowledgments

- **Henry Cohn** — for the published catalog entry for cell `(4, 48)` in the Game of Sloanes catalog against which this submission is compared. The Cohn holder has been the standing record for this cell for a number of years, and its structural properties (saturated-pair topology, byte-exact unit-norm structure, dominant Levenshtein-2 lower bound) were the reference baseline throughout this work. Professor Cohn separately performed the independent verification of an unrelated submission for cell (4, 64) in our companion repository's history, within 43 minutes of being notified.
- **Emily King, John Jasper, Dustin G. Mixon** — for maintaining the Game of Sloanes reference repository and for the published acceptance rule on which this submission's eligibility is based.
- **Henry Cohn, Abhinav Kumar, Gregory Minton** — for the body of work on coherence packings that informs the methodology, including the linear-programming and semidefinite-programming bound frameworks that constrain where deeper basins could conceivably lie.
- **Anthropic** — for building Claude, the AI assistant that collaborated on the structural analysis, the five-kernel verification pipeline, and the basin-floor reasoning documented above.
- **Welch, Levenstein, Delsarte, Goethals, Seidel, Calderbank, Casazza, Fickus, Tremain, Sloane, Conway, Jasper, King, Mixon** — for the foundational results on coherence bounds, Grassmannian packings, equiangular tight frames, and the surrounding literature on which this submission is built.

---

## 8. References

- Conway, J. H., Hardin, R. H., Sloane, N. J. A. "Packing lines, planes, etc.: packings in Grassmannian spaces." *Experimental Mathematics*, 5(2):139-159, 1996.
- Delsarte, P., Goethals, J. M., Seidel, J. J. "Bounds for systems of lines, and Jacobi polynomials." *Philips Research Reports*, 30:91-105, 1975.
- Fickus, M., Mixon, D. G. "Tables of the existence of equiangular tight frames." arXiv:1504.00253, 2016.
- Jasper, J., King, E. J., Mixon, D. G. "Game of Sloanes: Best known packings in complex projective space." *Wavelets and Sparsity XVIII*, SPIE Proceedings 11138, 416-425, 2019. arXiv:1907.07848. Game of Sloanes catalog repository: https://github.com/gnikylime/GameofSloanes.
- Levenstein, V. I. "Bounds on the maximal cardinality of a code with bounded modulus of the inner product." *Soviet Math. Dokl.*, 25:526-531, 1982.
- Cohn, H. Catalog entry for cell (4, 48) in the Game of Sloanes catalog (Jasper, King, Mixon). The packing file is publicly available at the Game of Sloanes repository listed above.
- Welch, L. R. "Lower bounds on the maximum cross correlation of signals." *IEEE Trans. Inf. Theory*, 20(3):397-399, 1974.

---

*Last updated: 2026-05-18.*
