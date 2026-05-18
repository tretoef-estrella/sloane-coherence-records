# Empirical Evidence of an Apparent Local Coherence Floor in the (d=3, n=14) Grassmannian Frame Packing Basin

**Author**: Rafael Amichis Luengo
**Affiliation**: Independent researcher, Madrid, Spain
**Date**: May 17, 2026
**Subject**: Companion technical note to the (3, 14) Grassmannian frame packing submission to Game of Sloanes
**Engine**: Sanjuanbautista (quad-precision)
**Contact**: tretoef@gmail.com

---

## Abstract

We report a Grassmannian frame packing in complex projective space ℂP² with N = 14 vectors achieving coherence μ = 0.637630514941861, which improves upon the previous best published packing (Mixon, 2019, μ = 0.637630521755923) by 6.81 × 10⁻⁹ in absolute coherence value. The improvement satisfies the Game of Sloanes 8th-decimal-place acceptance criterion by exactly one unit at the 8th decimal in the minimisation direction. Beyond reporting the improved packing, this note documents a numerical investigation that we interpret as *suggesting* both the new packing and the prior holder may lie within a single critical basin whose local floor *appears to be at or near the value of the new packing*. We are careful to phrase this as an interpretation, not a proof: we do not have a proof that the local floor of the basin has been reached, and we do not claim such a proof. The numerical reproducibility of the reported coherence has been independently verified by five distinct verification kernels at IEEE-754 double precision and by an additional audit at 100 decimal digits across five algorithmically distinct arithmetic procedures, with internal disagreement at the level of input-precision propagation. The cumulative evidence is consistent with — but does not prove — the working hypothesis that this basin's coherence floor has been reached at machine-quantum precision. **The improvement is microscopic in absolute terms and the author would have preferred to deepen the packing further before filing; after the available portfolio of paradigm families had been exhausted against this basin, no further descent was achievable.** **No claim of global optimality is made for the cell (3, 14), and we explicitly leave that question open. No claim that this floor is even the proven local floor of the basin is made either — only that the accumulated evidence is compatible with that interpretation.**

---

## 1. Introduction

The complex Grassmannian frame packing problem asks for a set of N unit vectors in ℂ^d that minimise the worst-case coherence

μ(V) = max_{i ≠ j} ∣⟨v_i, v_j⟩∣.

For the cell (d = 3, N = 14), the Game of Sloanes catalog (Jasper, King, Mixon; https://github.com/gnikylime/GameofSloanes) lists a packing due to Mixon (2019) with μ = 0.637630521755923. The relevant bounds for this cell are: Welch 0.5310850045, Levenshtein-2 0.6445033866, and a Delsarte-style linear-programming bound at degree 14 (computed in companion work) yielding μ ≥ 0.6035844. The Mixon packing does not saturate any of these bounds, leaving room — at the level of the published bounds — for the existence of deeper packings.

This note documents:

1. A new packing achieving μ = 0.637630514941861, reducing the previously published value by 6.81 × 10⁻⁹ (Section 2).
2. Several lines of evidence consistent with the hypothesis that the new packing and the prior holder occupy a common critical basin (Section 3).
3. The breadth of the optimisation portfolio applied within this basin, described at the level of paradigm families (Section 4).
4. Numerical reproducibility evidence at 100-decimal-digit precision across five independent arithmetic algorithms (Section 5).
5. A cautious empirical statement about the basin's *apparent* local floor (Section 6).

We do not claim global optimality. The exploration is local to one basin of the (3, 14) coherence landscape. The Delsarte lower bound 0.6035844 leaves a gap of approximately 5.4% to our value, which is mathematically large enough to admit deeper basins reachable via algebraic seeds or paradigms not yet considered. **We also do not claim a proof of the basin's local floor.** The reasoning of Sections 3 and 6 is interpretive, anchored in convergent evidence across multiple independent paradigm families and verification kernels, but it is not a mathematical proof. In context, the improvement reported here is small. The decision to submit reflects the convergence of independent evidence consistent with a basin-floor interpretation, rather than confidence that the improvement is methodologically significant in isolation.

---

## 2. The new packing

The packing is provided in the file `3x14_record1.txt` (located alongside this note) in the Game of Sloanes layout: 84 real numbers, comprising 42 real components followed by 42 imaginary components for 14 complex 3-vectors. The coherence has been independently verified using five distinct numerical kernels at IEEE-754 binary64 and via an extended audit at 100 decimal digits across five algorithmically distinct arithmetic procedures, with internal disagreement at the level of input-precision propagation (~10⁻¹⁷).

The packing was produced by the **Sanjuanbautista** engine — a single-threaded C++ engine operating in quad-precision (128-bit) arithmetic throughout its inner loop, on a Mac M2 under 25% CPU throttling. The distinctive feature of Sanjuanbautista relative to the parent repository's IEEE-754 double-precision engines is that quad-precision arithmetic allows the engine to resolve descent below the threshold at which conventional double-precision engines saturate. For a cell whose holder configuration appears to sit near a degenerate basin floor — as the Mixon (2019) holder for (3, 14) appears to, on the evidence summarised in Section 3 — quad-precision is the difference between stalling at the saturation threshold and being able to push further.

| Quantity | Value |
|:---|:---|
| μ (proposed packing) | 0.637630514941861 |
| μ (prior holder, Mixon 2019) | 0.637630521755923 |
| Δμ (proposed − holder) | −6.81 × 10⁻⁹ |
| Eight-decimal rounded value (proposed) | 0.63763051 |
| Eight-decimal rounded value (holder) | 0.63763052 |
| Unit-norm deviation across all 14 vectors | < 2 ULP binary64 |
| Saturated-pair fraction (within 10⁻⁸ of μ) | 49 / 91 (53.85%) |
| Cushion below the 8-decimal-rounding boundary 0.637630515 | 5.81 × 10⁻¹¹ |

The saturated-pair fraction is identical to that of the Mixon holder under the same verification kernel and tolerance, which is the first structural indication that both packings *may* occupy the same critical basin.

---

## 3. Lines of evidence consistent with a common-basin interpretation

Four independent lines of evidence are consistent with the interpretation that the proposed packing and the Mixon holder lie within a single critical basin, rather than being independent local minima. We present these as evidence supporting a hypothesis, not as a proof.

### 3.1 Continuous descent trajectory

A monotone descent trajectory connects the two packings. Beginning from the Mixon configuration, a sequence of refinement passes accumulated the 6.81 × 10⁻⁹ descent continuously. No discontinuity, no basin-crossing event, and no abrupt coherence jump was observed at any step. This is consistent with — though does not by itself prove — the two packings lying within a single basin.

### 3.2 Identical saturated-pair topology

Both configurations exhibit a 49/91 saturated-pair fraction at the 10⁻⁸ tolerance level, with the saturated pairs forming a graph of comparable degree sequence and equivalent vertex-multiplicity pattern. This shared combinatorial fingerprint, combined with the continuous descent trajectory of §3.1, is consistent with the new packing being a refinement of the Mixon packing within the same basin rather than a structurally distinct optimum.

### 3.3 Multiple refined critical points at the apparent basin floor

Several distinct numerical methods, drawing on disjoint paradigm families, all converge to the same coherence value to within one unit in the last place of binary64 (≈ 2 × 10⁻¹⁶). The converged solutions report the maximum coherence at **different argmax pairs** despite agreeing on the coherence value itself. We interpret this as evidence that the apparent basin floor supports a small discrete family of critical points related by reorganisation of which pairs occupy the active set, all at the same μ value within numerical precision. This is itself an interpretive structural observation about the apparent basin floor — a degeneracy that would not be expected at a generic stationary point. **The interpretation is consistent with the observations but is not proven.**

The same degeneracy is visible in the five-kernel ratification of the single submitted packing reported in `RESULTS_3x14.md`: the five kernels report five different argmax pairs while agreeing on the μ value to within 10⁻¹⁶. This is consistent with the apparent basin floor sitting on a degenerate critical structure where multiple pairs are simultaneously active.

### 3.4 Basin convergence from random initial conditions

Independent random initialisations spanning disjoint pseudo-random number generator seed ranges were performed. A small subset of these starts converged to the apparent basin floor reported in Section 2 (within one ULP binary64), without any warm-start guidance. No initialisation produced a coherence below the value reported. We interpret this as evidence that the basin is not only the floor of a warm-start refinement trajectory, but also an attractor of unguided random initialisation in this cell. As above, this is interpretive, not proven.

---

## 4. Optimisation portfolio within the basin

A wide portfolio of optimisation paradigm families was applied to either (i) the Mixon configuration directly, (ii) the proposed packing as anchor, or (iii) intermediate states of the descent trajectory of §3.1, plus (iv) independent random initialisations. A small subset of paradigms reached the apparent basin floor reported in Section 2; the remainder produced no measurable descent below it.

The paradigm families covered include:

- **First-order methods on smooth surrogates of the coherence functional**, including smooth-max and p-frame potential surrogates with homotopy schedules.
- **Second-order and constrained methods in extended precision**, responsible for the sub-ULP converged solutions of §3.3.
- **Sampling and stochastic methods**, including parallel tempering, simulated annealing, and quasi-Monte Carlo tangent perturbations.
- **Constraint-set manipulation**, including sequential active-set reorganisation and bisection on the target coherence value.
- **Geometric and topological perturbations**, including random vector kicks, local rotations in randomly chosen coordinate planes, geodesic bracketing, and thermal-quench protocols.
- **Algebraic and number-theoretic seed methods**, including cyclotomic seed sweeps with Galois orbit completion and probing of low-degree algebraic numbers near the apparent basin floor value.
- **Convex relaxation and lifting**, including semidefinite programming relaxation as cross-validation.
- **Ambient-metric deformation** within a one-parameter family of Hermitian metrics.
- **Trust-region radial expansion** in the saturated-constraint normal cone.
- **Targeted-vector perturbation** at hub vectors of the saturated-pair graph.
- **Large-scale random-initialisation enumeration** across disjoint seed ranges.

Hyperparameter schedules, step-size tuning, warmstart chain ordering, the specific sequence of refinement moves, and the per-paradigm convergence diagnostics are deliberately not reproduced here. The high-level description is at the level expected of a research preprint: enough for a peer to understand the paradigm coverage, not a turnkey reproduction of every method.

**The relevant empirical fact is that, across this portfolio, no paradigm produced descent below μ = 0.637630514941861 in this basin.** The descent was pursued with intent over multiple sessions. After the portfolio was exhausted, the value reported in this note was the deepest the available paradigms could reach. We interpret this as evidence consistent with the basin-floor hypothesis, while noting that the absence of descent under our specific portfolio does not constitute a proof that no other paradigm could descend further.

---

## 5. Numerical reproducibility at 100 decimal digits

The reported coherence has been independently audited at 100 decimal digits across five algorithmically distinct arithmetic procedures:

1. Naive complex multiplication in arbitrary precision.
2. Separated real/imaginary parts with explicit cross-products.
3. Squared-magnitude-first formulation (computing ∣⟨v_i, v_j⟩∣² and taking the square root at the end).
4. Pairwise summation tree for the inner-product accumulation.
5. Base-10 `Decimal` arithmetic at 40+ decimal digits.

All five report the same coherence value to within the level of input-precision propagation (≈ 10⁻¹⁷). The mpmath reference at 50 decimal digits is:

```
μ_submission = 0.63763051494186107945…
μ_holder     = 0.63763052175592256598…
```

This level of cross-algorithm agreement is the floor of what can be observed in this problem: the coherence is fully reproducible at machine-quantum precision.

The cumulative count of independent verifications spans this work and a separate peer-review session: ten distinct verification kernels concurring byte-exact on round-8 = 0.63763051 for the submission and round-8 = 0.63763052 for the holder.

---

## 6. Apparent basin floor and limits of the result

The combination of:

- a continuous monotone descent trajectory connecting the Mixon holder to the submission (§3.1),
- identical saturated-pair topology in both configurations (§3.2),
- multiple refined critical points at the same μ value to within one ULP binary64 (§3.3),
- a subset of unguided random initialisations converging to the same μ value with no warm-start guidance (§3.4), and
- portfolio breadth covering eleven paradigm families (§4) with no method producing any descent below the reported value,

is consistent with — though does not prove — the interpretation that a local coherence floor has been reached at machine-quantum precision in this basin. **We frame this as a working hypothesis supported by accumulated evidence, not as an established theorem.** The submission is offered with this caveat explicitly recorded.

**We do not claim that this floor is the global minimum for the cell (3, 14).** The 5.4% gap to the Delsarte LP bound 0.6035844 is mathematically large enough to admit the existence of deeper basins reachable via algebraic seeds, structured constructions, or paradigms not yet considered in this work.

**We do not claim that this floor is even the proven local floor of the basin we explored.** All five lines of evidence above are interpretive. A future result that descended below μ = 0.637630514941861 in this basin would not contradict any *fact* asserted in this note; it would refine the interpretation we have offered. We have made every effort to phrase the basin-floor claim as a hypothesis consistent with the evidence we have, not as a proof.

The author records openly that, in the absolute scale of the cell's coherence landscape, the improvement reported here (6.81 × 10⁻⁹) is small. The descent was pursued further than the filing margin; after the available portfolio had been exhausted, no further descent was achievable. The submission is filed because the margin is real, reproducible at the eighth decimal place across five independent verification kernels, and consistent with the basin-floor hypothesis. **The submission is filed not because the margin is impressive, but because the margin is real.**

---

## 7. Acknowledgments

- **Dustin G. Mixon** — for the published (2019) catalog entry for cell `(3, 14)` against which this submission is compared. The Mixon holder has been the standing record for over six years before this submission, and its structural properties were the reference baseline throughout this work. The holder packing itself remains publicly available in the Game of Sloanes catalog and is not redistributed in this folder.
- **Emily King, John Jasper, Dustin G. Mixon** — for maintaining the Game of Sloanes reference repository and for the published acceptance rule on which the submission's eligibility is based.
- **Henry Cohn, Abhinav Kumar, Gregory Minton** — for the body of work on coherence packings, and (separately) for Professor Cohn's independent verification of an unrelated submission for cell (4, 64) in the parent repository's history.
- **Anthropic** — for building Claude, the AI assistant that collaborated on the structural analysis, the five-kernel verification pipeline, the 100-decimal-digit audit, and the basin-floor reasoning documented above.
- **Welch, Levenstein, Delsarte, Goethals, Seidel, Calderbank, Casazza, Fickus, Tremain, Sloane, Conway, Jasper, King, Mixon** — for the foundational results on coherence bounds, Grassmannian packings, equiangular tight frames, and the surrounding literature on which this submission is built.

---

## 8. References

- Conway, J. H., Hardin, R. H., Sloane, N. J. A. "Packing lines, planes, etc.: packings in Grassmannian spaces." *Experimental Mathematics*, 5(2):139-159, 1996.
- Delsarte, P., Goethals, J. M., Seidel, J. J. "Bounds for systems of lines, and Jacobi polynomials." *Philips Research Reports*, 30:91-105, 1975.
- Fickus, M., Mixon, D. G. "Tables of the existence of equiangular tight frames." arXiv:1504.00253, 2016.
- Jasper, J., King, E. J., Mixon, D. G. "Game of Sloanes: Best known packings in complex projective space." *Wavelets and Sparsity XVIII*, SPIE Proceedings 11138, 416-425, 2019. arXiv:1907.07848. Game of Sloanes catalog repository: https://github.com/gnikylime/GameofSloanes.
- Levenstein, V. I. "Bounds on the maximal cardinality of a code with bounded modulus of the inner product." *Soviet Math. Dokl.*, 25:526-531, 1982.
- Mixon, D. G. (2019). Catalog entry for cell (3, 14) in the Game of Sloanes catalog (Jasper, King, Mixon). The packing file is publicly available at the Game of Sloanes repository listed above.
- Welch, L. R. "Lower bounds on the maximum cross correlation of signals." *IEEE Trans. Inf. Theory*, 20(3):397-399, 1974.

---

*Last updated: 2026-05-18.*
