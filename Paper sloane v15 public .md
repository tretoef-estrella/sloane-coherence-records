# Two world records in Grassmannian coherence packings (d=4, n=64) hlc

**Public methodology paper · May 12, 2026**

---

**Author**: Rafael Amichis Luengo
**Affiliation**: Independent researcher, Madrid, Spain
**Collaborator**: Claude (Anthropic) — AI research assistant
**Repository**: https://github.com/tretoef-estrella/sloane-coherence-records

---

## Editorial note

This is the **public methodology paper** that accompanies the two
coherence records announced in the parent repository. A more detailed
internal version of this document exists, written in mixed Spanish-English
during the development sessions, and contains specific algorithmic
parameters, sandbox protocol details, and internal engine identifiers
that are intentionally **redacted from this public version**.

The redactions are not arbitrary. They protect the engineering know-how
that took real effort to develop, and that the author intends to make
available under separate arrangement for academic collaborations or
commercial licensing (see the parent repository's `LICENSE.md` and the
contact note in `README.md`).

What this public paper contains:

- The full chronology of how the two records were obtained.
- The general methodology, at the level expected of a research preprint.
- The names and general ideas of every exploration probe that was run,
  successful and unsuccessful alike.
- All the **structural findings** about the basin landscape around the
  records — these are scientific results and belong to the community.
- All the **disciplinary doctrines** that were developed during the work,
  because these are general lessons that may be useful to other
  practitioners.

What this public paper does **not** contain:

- Specific hyperparameters of the optimisation engine.
- Detailed sandbox-protocol parameters (number of samples, perturbation
  radii, step counts, etc.) for each probe.
- Internal codenames for the engines and sub-systems used during
  development.
- The mixed-language prose style of the internal version (which is
  unsuitable for an academic audience).

---

## 1. Context and prior work

The author had completed three prior projects in adjacent areas before
attacking the cell `(d=4, n=64)` of the Grassmannian coherence packing
problem:

- **The Sobol project** (closed, public repository) — investigated a
  related optimisation problem with a finite-field structure and developed
  a body of methodology around sandbox-first verification, multi-kernel
  ratification, and refutation-criterion discipline.
- **The Luna project** (closed) — addressed a kissing-number problem in
  dimension 13 and produced a lower bound of K(13) ≥ 1155 by an approach
  that combined structural perturbation with a careful exploration of
  satellite basins.
- **The Diamante project** (closed, public repository) — produced a new
  upper bound on a code-distance parameter in `[22, 6, 13]_4` linear
  coding theory.

Both the Sobol and Diamante repositories are publicly available on the
author's GitHub profile under the same username as this repository.

The cumulative effect of these three prior projects was the development
of a body of practice — sandbox-first discipline, the *four-criterion
check* applied before any code is run, multi-kernel byte-exact
verification, the principle of refutation-criterion-driven kill — that
made it possible to attack the cell `(4, 64)` efficiently. The author
wishes to be explicit about this: **the rapid result is not the product
of personal genius. It is the product of carrying over methodology that
had already been refined across three prior projects on adjacent
problems**. Without the prior projects, the cell `(4, 64)` would have
taken weeks or months instead of days.

The Sloane project itself opened on **10 May 2026** with cell selection
and bounds analysis. **11 May 2026** was spent on pipeline preparation
and validation runs on the smaller cell `(3, 13)`. **Both world records
on the target cell `(4, 64)` were obtained on a single day: 12 May 2026**
— record #1 in the early afternoon, record #2 in the evening. Total
elapsed time from opening the Sloane project to closing the second
world record: **approximately three days**, with **both records
themselves achieved in a single calendar day**.

---

## 2. The problem

We seek a configuration `V = {v_1, ..., v_N} ⊂ ℂ^d` of `N = 64`
unit-norm vectors in complex 4-dimensional space (`d = 4`) that
minimises the **coherence**

```
μ(V) = max_{i ≠ j} |⟨v_i, v_j⟩|
```

where `⟨·, ·⟩` is the standard Hermitian inner product on `ℂ^d`. The
minimum is taken over the product manifold `M = (S^{2d-1})^N` of `N`
unit spheres in `ℂ^d`.

The cell `(d=4, n=64)` is one of the *Tier S* entries in the *Game of
Sloanes* reference repository maintained by Henry Cohn and collaborators.
The previous record (Cohn et al.) was `μ = 0.687160201509307` and had
stood for over a decade. The published lower bound from Levenstein,
which dominates the Welch and Orthoplex bounds for this cell, is
`μ ≥ 0.6` — leaving a substantial gap from the previous record (14.5%
above the lower bound).

The cell is hard for two well-known reasons: the coherence is non-smooth
(a maximum over `O(N²)` smooth quantities) and the manifold is non-convex
(a Cartesian product of spheres). Off-the-shelf optimisers struggle.

---

## 3. The water paradigm (general description)

The approach taken in this work is conceptually simple at the highest
level and was developed iteratively across the three days of work. We
describe it here at a level of detail sufficient for a peer to understand
the conceptual framework. The specific numerical parameters that make it
actually converge to the records are documented in the internal version
of this paper and are not reproduced here.

**Ingredient 1.** The non-smooth coherence is replaced by a one-parameter
family of smooth surrogates — a soft-maximum over the squared absolute
values of the off-diagonal Gram entries. The smoothing parameter is
**scheduled** from very gentle at the start of the optimisation (the
landscape feels almost flat and the iterate navigates easily) to very
sharp at the end (the surrogate becomes essentially indistinguishable
from the true coherence). Internally the author refers to this as
*the water paradigm*: water finds the lowest path through a complex
terrain by gentle persistence, not by clever jumps.

**Ingredient 2.** The optimisation is done on the natural Riemannian
manifold structure (each vector stays on its unit sphere, retraction
after each update, tangent projection of the gradient). A momentum term
is used to carry the iterate through shallow ridges where pure gradient
descent would stall. The combination of *smoothing schedule* and
*Riemannian gradient flow with momentum* is well-known in the manifold
optimisation literature; the precise calibration is what differentiates
a working implementation from a non-working one, and that calibration is
the main proprietary content of the engine.

**Ingredient 3.** The **starting configuration** is not random and is
not the previous record. It is selected from a small family of
*candidate basins* discovered by a separate, lightweight sandbox
exploration step. This sandbox produces a ranked list of structurally
distinct starting points (filtered by a Gram-invariant distance metric
to ensure each candidate is meaningfully different from the others);
the engine is then launched from each candidate. Different candidates
lead to different local minima of the smoothed objective. Some are
deeper than others. The two records reported here came from two
structurally distinct candidates discovered by this sandbox protocol.

**Ingredient 4.** A **refutation-criterion-driven kill discipline**
automatically terminates a run if no improvement has been observed
within a window proportional to the total compute budget. This prevents
wasted compute on runs that have already converged or that have fallen
into a shallow basin. The discipline is inherited from the prior Sobol
project and was refined in the early test runs of the Sloane project
on the smaller cell `(3, 13)`.

The interaction between these four ingredients is non-trivial. A naive
combination of the first three (smoothed-max + Riemannian gradient +
random or Cohn-based warmstart) does not beat the record. The fourth —
refutation discipline — was learned the hard way during earlier projects.
Each ingredient on its own is in the published literature; the
combination, at the specific calibration that makes it work for this
cell, is the proprietary engineering contribution.

---

## 4. Chronology

The days below are given in CEST (Madrid local time, UTC+2).

### May 10, 2026 — opening of the Sloane project

The cell `(4, 64)` was selected as the target after a preliminary
analysis of the *Game of Sloanes* reference table, which identified
it as a *Tier S* cell with no improvement on the upper bound in over
a decade and a substantial gap (approximately 14.5%) to the Levenstein
lower bound. The day was spent on cell selection, bounds verification,
and a transfer of methodology from the just-closed Sobol and Luna
projects.

### May 11, 2026 — pipeline preparation

Pipeline-validation runs were performed on the smaller, easier cell
`(3, 13)` to debug the engine, the verifier, and the sandbox
exploration scripts. Several engineering lessons were learned during
this day, including the critical importance of the
refutation-criterion discipline and the limitations of cold-start
naive optimisation on Tier S cells. The day closed with the engine
compiled, the verifier ready, and a sandbox protocol prepared for
the actual target `(4, 64)`.

### May 12, 2026 (morning) — first record

A sandbox sweep around the Cohn baseline produced a ranked list of
structurally distinct candidate starting points. The top candidate was
selected as the warmstart for a full optimisation run on a Mac M2,
single-threaded, throttled to 25% CPU. The run took approximately
**5.5 hours**, during which the coherence descended from approximately
0.72 (warmstart) through the Cohn threshold (at approximately
step 3,500,000) and finally converged to

> **μ₁ = 0.687040494471422   (record #1, gap vs. Cohn: −1.197 × 10⁻⁴)**

The record was verified byte-exact by the engine's internal four-step
verification protocol (cold rebuild, final-verify, file-roundtrip
re-verify) and then by an independent Python verifier with its own
clean-room kernel. The author was satisfied; the AI assistant was not,
and insisted on a fourth (triple-kernel sandbox) cross-validation
before either of us would call the result a record. All four kernels
agreed byte-exact.

### May 12, 2026 (afternoon and evening) — second record

The author asked: *can we go lower?* A new sandbox exploration was
performed, this time starting from record #1, with a different
perturbation protocol designed to find basins structurally distinct
from the basin of record #1. Approximately ten distinct candidates
were identified, and a second optimisation run was launched.

A subtle error was made initially: the warmstart files supplied to the
engine had been over-processed by the sandbox (already too close to a
local minimum), causing the engine to auto-kill within seconds because
no descent was possible. The error was caught honestly by both the
author and the AI assistant within minutes of the first failed run.
A corrected version of the warmstart files (less processed, leaving
room for the engine to descend) was generated, and a fresh run was
launched. After approximately 5.5 hours, the run converged to

> **μ₂ = 0.687035170223597   (record #2, gap vs. Cohn: −1.250 × 10⁻⁴, i.e. −0.0182%)**

This was deeper than record #1 by `5.32 × 10⁻⁶`, from a structurally
distinct basin (Gram-invariant signature distance ≈ 0.283 to the
basin of record #1). The worst pair indices `(31, 38)` were
**byte-exact preserved** between the two basins — a striking
observation discussed in §6 below.

The second record was verified byte-exact by five independent kernels:
the engine's own final-verify, the independent Python verifier, a
NumPy matmul kernel, a pure-Python double-loop kernel (with no library
involvement at all), and an `np.vdot`-per-pair kernel. All five
reported `0.6870351702235971` to 16 digits, and the worst pair
agreed across all five.

### May 12, 2026 (evening, late) — exploration of further records

After record #2, six additional probes were run in sandbox to determine
whether a *third* record was accessible by local refinement of the
same basin. Each probe was filtered through the *four-criterion check*
before any code was written. The probes are described in §5 below.
**All six probes refuted the existence of an accessible third record
within the basin of record #2.** The session was closed with the second
record consolidated and the open question of where a third record
might come from documented for future work.

---

## 5. The six probes (general description)

The author and the AI assistant adopted a habit during the work of
giving each new exploration probe a metaphorical name in Spanish.
These names are useful here because they convey the **intent** of each
probe without revealing the specific implementation.

In order of execution:

**Probe 1 — "Rats" (ratas).** Random walks around a reference point,
followed by a brief coarse descent. Designed to discover *which
direction the landscape opens up in* on a large scale. The rats were
the probe that, during the morning of May 12, discovered the family
of candidate basins from which record #1 was selected.

**Probe 2 — "Ants" / "Anthill" (hormigas / hormiguero).** A second
sweep, this time using the ranked output of the rats as input,
focused on basins *close to* the reference point but structurally
distinct from it. The ants were the probe that discovered the
warmstart family from which record #2 was selected.

**Probe 3 — "Boomerang" (boomerang).** A short coarse-descent
routine used inside the rats and ants protocols. It takes a perturbed
configuration and runs a small number of fast steps to identify which
basin the perturbation has fallen into, without doing the full
expensive descent.

**Probe 4 — "Termites" (termitas).** Small-scale perturbation
explicitly *targeted* at the worst-pair vectors of the current record.
The hypothesis was that breaking the symmetry of the worst pair would
unlock access to a sub-basin slightly below the current record.
Two variants were tried (one perturbing both worst-pair vectors
simultaneously, one perturbing only one). Both were refuted.

**Probe 5 — "Bat-echo" (murciélago eco-eco).** Profiling rather than
optimisation: a large number of random tangent directions are tested
at several radii, with the coherence change at each radius measured.
The result is an empirical estimate of the local Hessian curvature
of the smoothed objective around the current record. **All radii
returned only ascending directions** — no descending direction was
found, even with a very small radius. The interpretation is that
the second record sits in a *strong local minimum* of the optimisation
landscape: the Hessian is positive-definite in every direction tested.

**Probe 6 — "Mercury" (mercurio).** A Riemannian trust-region
optimisation method (curvature-aware second-order step). Designed to
exploit any narrow descent direction that the local Hessian numerics
might reveal. **The trust-region step never improved beyond record #2**:
when allowed to take a step, it overshot into a shallower basin; when
the trust radius collapsed, it returned to the starting point. This is
the second-order confirmation of the bat-echo finding: the basin is
strongly positive-definite.

A seventh attempt — a vanilla Adam optimiser as a smoke test — was
attempted briefly and abandoned within a few thousand steps when it
became clear that vanilla Adam (without the calibration developed for
the water paradigm) simply ejects the iterate from the basin without
finding a deeper one. This is reported here honestly because the
discipline of the project requires it, not because the smoke test
produced any useful result.

---

## 6. Structural findings

Five structural findings about the basin landscape are reported here.
They are the principal scientific results of the work, separate from
the records themselves.

### Finding 1 — Both records have the same worst pair

In both record #1 and record #2, the worst pair (the two vectors
whose absolute inner product saturates the coherence) consists of
vectors **`v_31` and `v_38`** (zero-indexed). The two records sit in
basins separated by a substantial Gram-invariant signature distance
(approximately 0.283), but the topological role of these two specific
vectors is preserved across the basins. We do not have an explanation
for this; we report it as an observation.

The natural conjecture is that any further coherence record for this
cell, if obtained by methods similar to ours, will continue to have
worst pair `(31, 38)` after a suitable relabelling. We do not have
evidence for this conjecture and we do not assert it as a result.

### Finding 2 — The second record is a strong local minimum

The combination of **bat-echo profiling** (5000 directional probes
returning zero descending directions) and **mercury trust-region
optimisation** (the second-order method finds no descent) provides
strong empirical evidence that record #2 is a **positive-definite
local minimum** of the smoothed-max objective, with a Hessian
condition number that prevents any local refinement from succeeding.
This is a *negative* result in the sense that it forecloses one path
to a third record, but it is a useful negative result: it means
future effort is better spent on basin-distinct exploration or on
non-local algorithms (semidefinite-programming relaxations,
algebraic constructions, branch-and-bound) than on perturbative
refinement of the current best.

### Finding 3 — The basin around record #2 is shallow-walled inward

The rats probe launched *from* record #2 discovered many nearby
basins — but every single one was **shallower** than record #2.
This contrasts sharply with the rats probe launched *from* the
Cohn baseline (which discovered, among others, the basin of
record #1, and another basin from which record #2 was eventually
reached). The interpretation: the *neighbourhood* of record #2 in
the manifold contains no easily accessible deeper basin. The deeper
basin, if it exists, is not in the immediate vicinity.

### Finding 4 — The water paradigm is reproducible across basins

Two independent runs of the engine, started from two structurally
distinct warmstarts, both successfully descended past the Cohn
threshold and converged to distinct local minima, both below the
previous record. This is empirical evidence that the water paradigm
is not a one-shot lucky run but a *reproducible algorithmic
methodology*. Given a structurally distinct starting basin in the
right regime, the engine reliably descends to its local minimum,
and a non-trivial fraction of those local minima are below the
Cohn baseline.

### Finding 5 — Sandbox-first exploration is the leverage

The single most important methodological observation is this:
**the sandbox exploration step that produces the warmstart family
is where the leverage over prior work lives**. The optimisation
engine itself, while carefully calibrated, uses ingredients that
are individually present in the published literature. The
difference between the Cohn record and the new records is, in
practice, the choice of where to *start* the optimisation. The
sandbox produces structurally distinct starting points that the
prior literature does not appear to have systematically explored
for this cell.

---

## 7. Disciplinary lessons

Three doctrinal lessons emerged from the two-day session that the
author considers worth recording, because they may be useful to other
practitioners of computational mathematical optimisation:

### Doctrine 1 — Sandbox-first discipline

Before any expensive (Mac, GPU, cluster) compute is launched, the
intended algorithm should be **smoke-tested in a sandbox** against
the current best result. This is not the same as testing it on a
synthetic problem: it should be tested with the actual current
record as warmstart. Two of the six probes in this work would have
consumed 6+ hours of compute each had they been launched directly
on the Mac without sandbox triage. The sandbox refuted them in
seconds.

### Doctrine 2 — Multi-kernel byte-exact verification

A claimed record is not a record until it has been verified by at
least three code paths written from scratch with no shared
implementation. In this work, five paths were used for record #2.
The cost of running five verifications is trivial. The cost of
publishing a record that turns out to be a verification artefact
is enormous.

### Doctrine 3 — Refutation-criterion-driven kill

Every optimisation run should be launched with an explicit, automatic
termination criterion based on a kill window proportional to the
total budget. Without this discipline, runs that have already
converged (or that have fallen into a shallow basin) waste hours
of compute. With this discipline, the operator can launch many
exploratory runs and let the kill criterion adjudicate which ones
deserve the full budget.

These three doctrines are not novel in isolation. The novelty, if
any, lies in the discipline of applying all three simultaneously
on every probe and every run, without exception, even when the
authors are confident that the probe in question is going to work.

---

## 8. What remains open

The records reported here are the best **known** coherence values for
the cell `(d=4, n=64)` over ℂ⁴. They are not necessarily the **optimal**
values. The Levenstein lower bound is `0.6`, and the current best
upper bound is `0.687035170223597` — a gap of approximately 14.51%
that the lower-bound theory does not close.

The path forward, in our view, is one of:

1. **Basin-distinct exploration.** A larger-scale rats-and-ants sweep
   from the Cohn baseline (or from each of records #1 and #2),
   looking for basins that are far from both records in the
   Gram-invariant signature distance. The Mac compute budget for
   this is moderate (tens of hours per candidate).

2. **Non-local algorithms.** Semidefinite-programming relaxations of
   the coherence-minimisation problem; branch-and-bound on a
   suitably constrained version of the manifold; algebraic
   constructions (Hoggar-type embeddings, MUB-type constructions,
   cyclotomic-field projections). These are computationally
   expensive but they do not have the basin-locality of the
   gradient-flow methods.

3. **Improved lower bounds.** It is possible — though we have no
   evidence for this beyond the strong-local-minimum status of
   record #2 — that an improved lower bound, beyond Levenstein,
   could be derived from the structure of the basins discovered
   here. This would be a project of pure analysis rather than of
   computation.

We have no plans to pursue these immediately. The author intends to
take a short break, archive the records appropriately (PR to the
*Game of Sloanes* repository, formal write-up, notification to the
relevant researchers), and consider next steps. Inquiries about
collaboration on any of the three open directions are welcome.

---

## 9. Acknowledgments

- **Henry Cohn, Abhinav Kumar, Gregory Minton** and collaborators —
  for maintaining the *Game of Sloanes* repository and for the
  body of work on coherence packings that made this comparison
  possible.
- **Dustin Mixon, John Jasper, Joseph Iverson, Emily King** and
  others in the equiangular-tight-frame / Grassmannian-packing
  community — for the literature that taught the author what
  mattered and what didn't.
- **Anthropic** — for building Claude, the AI assistant that
  collaborated on the engineering, the sandbox exploration
  protocols, and the verification pipeline.
- **The Sobol, Luna, and Diamante project communities** (where
  applicable; see the author's GitHub profile for the public
  repositories) — for the prior methodological work that made
  this rapid Sloane result possible.

---

## 10. Reproducibility

The two records, the independent Python verifier, the Mac runtime
logs, and this paper are all included in the repository under MIT
license. Anyone can:

1. Clone the repository.
2. Run `python3 verification/verify_sloane_independent.py records/4x64_record1.txt`.
3. Run `python3 verification/verify_sloane_independent.py records/4x64_record2.txt`.

and obtain the byte-exact coherence values reported in this paper, on
their own machine, in under one minute.

The optimisation engine source code is not included in the public
repository for the reasons described in the editorial note above. It
is available under separate arrangement for research collaboration or
commercial licensing — please open a GitHub issue or contact the author
directly.

---

*Submitted to the public record: May 12, 2026, Madrid.*
*This paper is part of the repository https://github.com/tretoef-estrella/sloane-coherence-records and is licensed under MIT.*
