# Four world records in Grassmannian coherence packings (d=4, n=64) hlc

**Public methodology paper · May 16, 2026 (extension of v15 to Records 3 and 4)**

---

**Author**: Rafael Amichis Luengo
**Affiliation**: Independent researcher, Madrid, Spain
**Collaborator**: Claude (Anthropic) — AI research assistant
**Repository**: https://github.com/tretoef-estrella/sloane-coherence-records

---

## Editorial note

This is the **v16 public methodology paper**, which extends the original v15 paper to cover Records 3 and 4 of the cell `(d=4, n=64)` hlc. The v15 paper documented the first two records (May 12, 2026) obtained by the Aquiles engine; the v16 paper extends that documentation to include the Boagrius engine and the basin transitions that produced Records 3 and 4 (May 16, 2026).

The v15 paper is preserved in the repository as a historical snapshot of the May 12 state and is not edited. The v16 paper follows the same redaction principle: it documents the conceptual framework, the chronology, the structural findings, and the disciplinary lessons, but it does **not** document the specific algorithmic parameters of either the Aquiles or the Boagrius engines. Those parameters remain reserved for separate licensing arrangements (see the parent repository's `LICENSE.md` and the contact note in `README.md`).

What this paper contains:

- The full chronology of how Records 3 and 4 were obtained, in continuity with the v15 paper for Records 1 and 2.
- The Boagrius engine at the general-description level expected of a research preprint.
- The cascade-warmstart protocol that hands a packing from one engine to the next.
- The structural findings that emerged from the basin transitions across the four records.
- The disciplinary doctrines that survived the second session and the new ones that emerged from it.

What this paper does **not** contain:

- Specific hyperparameters of either engine.
- Detailed sandbox-protocol parameters for the new probes run on May 16.
- Internal codenames for sub-systems beyond the two engine names (Aquiles, Boagrius).
- The mixed-language prose style of the internal version.

---

## 1. Context and prior records

The v15 paper (May 12, 2026) documents Records 1 and 2 in detail. In summary:

- **Record 1**: μ = 0.687040494471422, worst pair (31, 38), Aquiles engine, May 12 afternoon CEST. Gap vs. Cohn: −1.197 × 10⁻⁴.
- **Record 2**: μ = 0.687035170223597, worst pair (31, 38), Aquiles engine, May 12 evening CEST. Gap vs. Cohn: −1.250 × 10⁻⁴ (−0.0182%).

Both records were verified byte-exact by five independent kernels. Record 2 was additionally reproduced byte-exact by Henry Cohn (MIT) in his own code within 43 minutes of notification.

The v15 paper closes with a strong-local-minimum analysis of Record 2: six post-record sandbox probes (termites, rats, bat-echo, mercury, vanilla-Adam, hub-vertex) all refuted the hypothesis that a third record was accessible by local refinement within the Aquiles basin. The conclusion at the time was: any further improvement would require either a structurally distinct basin or a qualitatively new algorithmic paradigm.

Both possibilities were on the table when the Sloane project was reopened four days later.

---

## 2. The Boagrius engine

The Boagrius engine was developed during the four days between May 12 and May 16, 2026. It is not a variant of Aquiles. It is a separate engine, built around a different conceptual framework.

### 2.1 Conceptual framework

Where Aquiles smooths the non-smooth coherence and descends the smooth surrogate with Riemannian gradient flow, Boagrius treats the coherence as a hard inequality constraint that is progressively tightened by a feasibility-driven outer iteration. Each outer iteration solves a tightly-constrained inner problem; the constraint is then tightened slightly and the next outer iteration begins from the previous solution.

The intuition is the following. Smoothing-based methods (Aquiles) are good at navigating a complicated landscape from far away — they trade local precision for global mobility. Constraint-tightening methods (Boagrius) are good at the opposite — they trade global mobility for precision near a solution that is already known to be close. The two are conceptually complementary: Aquiles to find a deep basin, Boagrius to drive it to the floor of floating-point precision.

### 2.2 The cascade-warmstart protocol

Rather than launching Boagrius from a freshly sandbox-discovered basin (the Aquiles protocol), Boagrius takes the current best packing as warmstart and applies its constraint-tightening procedure. During the tightening, the iterate may transition smoothly to a structurally distinct nearby basin if the constraint geometry favours that transition. When the constraint tightens past a critical value, the iterate is committed to its current basin and the engine descends to its floor.

This is a different protocol from the v15 sandbox exploration. The v15 sandbox produces structurally distinct candidate basins by design; Boagrius's cascade-warmstart discovers them as a by-product of the constraint tightening, not as a sandbox decision. In practice, the cascade-warmstart is more economical when the engine is well-calibrated for the cell in question, and the v15 sandbox is more reliable when the engine is being applied to a new cell where the basin structure is not yet mapped.

### 2.3 Verification discipline (unchanged)

Boagrius preserves the verification discipline introduced for Aquiles in v15: five independent code paths, byte-exact agreement, worst-pair cross-validation across all kernels. The pipeline is invariant under engine choice.

---

## 3. Chronology of Records 3 and 4

The times below are CEST (Madrid local time, UTC+2).

### May 16, 2026 (afternoon) — Record 3

The Boagrius engine, launched on the morning of May 16 with the Record 2 packing as warmstart, ran for several short pilot sessions on smaller cells during the morning to calibrate the constraint-tightening schedule. The pilots terminated cleanly. In the afternoon, Boagrius was launched on the cell `(4, 64)` with the Record 2 packing as warmstart.

After approximately 9 minutes of wall time on a Mac M2 (single-thread, 25% CPU throttle), the constraint tightening pushed the iterate through a basin transition. The new basin has worst pair `(6, 17)` — structurally distinct from the Aquiles basin's `(31, 38)`. The engine converged to:

> **μ₃ = 0.687033937262633   (record #3, gap vs. Cohn: −1.263 × 10⁻⁴, gap vs. record 2: −1.23 × 10⁻⁶)**

Five-kernel byte-exact ratification was performed immediately. All five kernels agreed on `(6, 17)` as worst pair; coherence values agreed to within sub-ULP spread (1.11 × 10⁻¹⁶).

### May 16, 2026 (evening) — Record 4

Record 3 was used as the warmstart for a second Boagrius run in the evening of May 16. The engine ran for 568.00 seconds (≈ 9 min 28 s) wall time on the same Mac M2. The constraint tightening from the Record 3 basin produced another basin transition during the early iterations — the first sub-Record-3 improvement appearing at outer iteration 22 — and the engine converged to:

> **μ₄ = 0.687033931214091   (record #4, gap vs. Cohn: −1.263 × 10⁻⁴ (−0.0184%), gap vs. record 3: −6.05 × 10⁻⁹)**

with worst pair `(9, 25)` — again structurally distinct from both the Aquiles basin and the Record 3 basin.

The engine terminated by its internal stopping criterion at outer iteration 2061 (corresponding to the iterate becoming fully constrained within the new basin to within floating-point precision). The five-kernel ratification produced zero spread across the five paths and agreement on `(9, 25)` as worst pair.

### Summary of the four-record cascade

| Record | Engine | Worst pair | μ | Gap vs. Cohn |
|:---|:---|:---|:---|:---|
| 1 | Aquiles | (31, 38) | 0.687040494471422 | −1.197 × 10⁻⁴ |
| 2 | Aquiles | (31, 38) | 0.687035170223597 | −1.250 × 10⁻⁴ |
| 3 | Boagrius | (6, 17) | 0.687033937262633 | −1.263 × 10⁻⁴ |
| 4 | Boagrius | (9, 25) | 0.687033931214091 | −1.263 × 10⁻⁴ (−0.0184%) |

The cell `(4, 64)` thus supports at least three structurally distinct sub-Cohn basins — the Aquiles basin (Records 1 and 2 sharing it) and the two Boagrius basins (Records 3 and 4). This is one of the principal structural findings of the v16 work.

---

## 4. Structural findings (extension of v15)

The v15 paper reported five structural findings about the Aquiles basin landscape. The v16 work extends these with three additional findings concerning the cascade across multiple basins.

### Finding 6 (v16) — At least three sub-Cohn basins exist for this cell

The four records occupy at least three structurally distinct basins (Aquiles `(31, 38)`, Boagrius-3 `(6, 17)`, Boagrius-4 `(9, 25)`). The basin structure of this cell is therefore not unimodal in the sub-Cohn region; it contains multiple distinct minima, all of which are sub-Cohn.

This is a substantive structural observation. The conjecture in the v15 paper that the second record was a strong local minimum was correct *within* the Aquiles basin — but the v16 work demonstrates that the next-deepest minima are in different basins entirely. Local Hessian analysis of any single basin cannot reveal this; it requires either a sandbox-style exploration or a constraint-tightening method that naturally transitions across basins.

### Finding 7 (v16) — The cascade-warmstart protocol discovers new basins

Boagrius applied to a Record-N warmstart does not always stay in the Record-N basin. During the constraint tightening, the iterate can transition to a structurally distinct basin if the tightening geometry favours it. In the May 16 run, this happened twice: once between Records 2 and 3 (Aquiles → Boagrius-3), and once between Records 3 and 4 (Boagrius-3 → Boagrius-4).

This was not anticipated when Boagrius was designed; the original intent of the constraint-tightening framework was to deepen a known basin to its floor, not to navigate across basins. The basin-transition behaviour emerged from the interaction of the constraint tightening with the basin geometry of this cell. It may not generalise to all cells; for cells with a strongly dominant single basin, Boagrius would presumably just deepen that one basin to its floor without transitioning.

### Finding 8 (v16) — The sub-Cohn region is finite-rich but still bounded

The cumulative gap from Record 4 to Cohn is approximately `−1.263 × 10⁻⁴`. This is small in absolute terms but large compared to the inter-record gaps within the cascade (Record 2 → 3: −1.23 × 10⁻⁶; Record 3 → 4: −6.05 × 10⁻⁹). The pattern of progressively smaller gaps suggests that the cascade is approaching a structural floor — either the true global optimum or the floor visible to floating-point computation. The Levenstein lower bound remains at `0.6`, leaving a 14.51% gap that no exploration in this work has approached.

Whether further sub-Cohn basins exist beyond what the cascade has discovered, and whether any of them sit below Record 4, is an open question for future work.

---

## 5. Disciplinary doctrines (extension of v15)

The v15 paper documented three disciplinary doctrines: sandbox-first discipline, multi-kernel byte-exact verification, and refutation-criterion-driven kill. The v16 work confirms all three and adds two more:

### Doctrine 4 (v16) — Cascade-warmstart over fresh-random when an engine is well-calibrated

Once a cell's basin structure is partially mapped, it is more efficient to cascade a known-good packing through a complementary engine than to launch from a fresh sandbox-discovered basin. The v15 sandbox protocol remains the right tool for entering a new cell or for crossing into a region of the manifold where no good packings are known; for refining within a region already known to be sub-Cohn, cascade-warmstart is cheaper and often discovers new basins as a by-product of the tightening.

### Doctrine 5 (v16) — Engine specialisation beats engine generality

A single engine attempting both exploration and exploitation will struggle with the calibration trade-off between the two regimes. Specialising the engines — Aquiles for exploration, Boagrius for exploitation — and handing off via a cascade-warmstart protocol exposed structural features (Records 3 and 4) that neither engine alone would have produced.

This is a design principle, not an algorithmic claim. The author offers it tentatively: it worked for this cell with these two engines. Whether the same pattern (exploration engine → exploitation engine) generalises to other cells is an empirical question that would need to be tested cell by cell.

---

## 6. What remains open

The four records reported here are the best **known** coherence values for the cell `(4, 64)` over ℂ⁴. They are not necessarily the **optimal** values. The Levenstein lower bound is `0.6`, and the current best upper bound is Record 4 at `0.687033931214091` — a gap of approximately 14.51% that the lower-bound theory does not close.

The natural next directions for future work:

1. **Search for a fifth basin.** A v15-style sandbox sweep launched from each of the four records (or from a structurally distant random initialisation) might discover a fifth sub-Cohn basin. The Mac compute budget for this is moderate.

2. **Algebraic constructions in the sub-Cohn region.** Hoggar-type, MUB-type, or cyclotomic projections might land in or near the basins discovered here. If so, the algebraic structure could give an exact (rather than numerical) characterisation of the basins.

3. **Improved lower bounds.** The strong-local-minimum analysis of v15, applied across multiple basins as in v16, might support an improved lower bound below `0.6`. This would be a project of analysis rather than computation.

The author has no immediate plans to pursue these. The current focus is on archiving the four records appropriately (PR to the *Game of Sloanes* repository, formal write-up, notification to the relevant researchers) before considering next steps.

---

## 7. Acknowledgments (unchanged from v15)

- **Henry Cohn, Abhinav Kumar, Gregory Minton** and collaborators — for maintaining the *Game of Sloanes* repository and for the body of work on coherence packings that made this comparison possible, and for Professor Cohn's responsiveness in independently verifying Record 2.
- **Dustin Mixon, John Jasper, Joseph Iverson, Emily King** and others in the equiangular-tight-frame / Grassmannian-packing community — for the literature that taught the author what mattered and what didn't.
- **Anthropic** — for building Claude, the AI assistant that collaborated on the engineering, the sandbox exploration protocols, and the verification pipeline.
- **The Sobol, Luna, and Diamante project communities** — for the prior methodological work that made these rapid Sloane results possible.

---

## 8. Reproducibility (extension of v15)

All four records, the independent Python verifier, the Mac runtime logs for Records 1, 2, and 4, and the two technical papers (v15 and v16) are included in the repository under MIT license. Anyone can:

1. Clone the repository.
2. Run `python3 verify_sloane_independent.py 4x64_record1.txt` and similarly for records 2, 3, 4.

and obtain the byte-exact coherence values reported in this paper, on their own machine, in under one minute.

The optimisation engine source code (both Aquiles and Boagrius) is not included in the public repository for the reasons described in the editorial note. It is available under separate arrangement for research collaboration or commercial licensing — please open a GitHub issue or contact the author directly.

---

*Submitted to the public record: May 16, 2026, Madrid.*
*This paper is part of the repository https://github.com/tretoef-estrella/sloane-coherence-records and is licensed under MIT. It extends the v15 paper, which is preserved unchanged as a snapshot of the May 12 state.*
