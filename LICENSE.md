# License

This repository contains two distinct categories of content, governed by
different terms.

---

## 1. Open content (MIT License)

The **records, the independent verifier, the paper, the documentation, and
any auxiliary scripts** in this repository are released under the **MIT
License**, reproduced in full below. The mathematical results are free for
everyone to use, cite, redistribute, modify, and build upon.

### MIT License

> Copyright (c) 2026 Rafael Amichis Luengo
>
> Permission is hereby granted, free of charge, to any person obtaining a copy
> of this software and associated documentation files (the "Software"), to deal
> in the Software without restriction, including without limitation the rights
> to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
> copies of the Software, and to permit persons to whom the Software is
> furnished to do so, subject to the following conditions:
>
> The above copyright notice and this permission notice shall be included in
> all copies or substantial portions of the Software.
>
> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
> IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
> FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
> AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
> LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
> FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
> DEALINGS IN THE SOFTWARE.

### Specifically covered by MIT

- The packing files `records/4x64_record1.txt` and `records/4x64_record2.txt`.
- The Mac runtime logs `records/run_record1.log` and `records/run_record2.log`.
- The independent Python verifier `verification/verify_sloane_independent.py`.
- The technical paper `paper/PAPER_SLOANE_v15.md`.
- All Markdown documentation in the repository root (`README.md`, `GUIDE.md`,
  `RESULTS.md`, `METHODOLOGY.md`, `RECORDS.md`, `PROOF.md`, `CITATION.md`,
  `WITNESS.md`, this `LICENSE.md`, and `CITATION.cff`).

### What this means for users

You can:
- Download and verify the records on any machine.
- Cite the work in academic papers, technical reports, blog posts, etc.
- Reuse the verifier code in your own projects.
- Translate the documentation into other languages.
- Build derivative work (extensions to other cells, alternative verifiers,
  visualisations, etc.).

You only need to retain the copyright notice and the disclaimer in
substantial redistributions.

---

## 2. Engine source code (separate arrangement)

The **source code of the optimisation engine** (the C++ implementation that
produced the records, informally referred to as Engine 9 or
*Aquilestrincaestacasvaaporhectorelresacas*) is **NOT included** in this
repository and is **NOT covered** by the MIT License above.

The engine source code is held under a separate proprietary arrangement by
the author and may be made available under separate terms for:

- **Academic research collaborations** (typically free of charge, subject to
  a usage agreement that protects the author's downstream commercial
  interests).
- **Commercial licensing** (terms to be negotiated).

The high-level methodology is described in [`METHODOLOGY.md`](METHODOLOGY.md)
at the level expected of a research preprint: enough for a peer to understand
the conceptual approach and the engineering choices, but not a turnkey
implementation. A peer with experience in Riemannian manifold optimisation
could reimplement the framework in approximately 300–500 lines of C++ or
Python; the difficulty is not in the implementation but in the calibration
and in the sandbox-exploration protocol that produces the warmstart family,
both of which remain proprietary.

### Inquiries

For engine licensing inquiries, please open a GitHub issue tagged
`engine-licensing` or contact the author directly via the email on the
GitHub profile associated with this repository.

---

## Summary table

| Asset | License | Source |
|:---|:---|:---|
| Record packings (`records/*.txt`) | MIT | This repository |
| Mac runtime logs (`records/*.log`) | MIT | This repository |
| Independent Python verifier (`verification/*.py`) | MIT | This repository |
| Technical paper (`paper/*.md`) | MIT | This repository |
| All Markdown documentation | MIT | This repository |
| Citation metadata (`CITATION.cff`, `CITATION.md`) | MIT | This repository |
| **Engine 9 C++ source code** | **Proprietary** | **Not included; available under separate arrangement** |
| **Warmstart sandbox scripts** | **Proprietary** | **Not included; available under separate arrangement** |

---

## Why this split

The records themselves are a scientific result. Scientific results belong to
humanity and should be freely verifiable, citable, and extendable. That is
why everything you need to **verify** the records is in this repository
under permissive terms.

The engine is engineering. Engineering artefacts that took significant
effort to develop and that have potential commercial value can reasonably be
licensed separately, the same way a research group might publish a paper
describing an algorithm while retaining the patented or proprietary
implementation. The author has chosen to publish the *results* and the
*high-level methodology* openly, while retaining the *implementation* for
potential commercial use or academic collaboration on negotiated terms.

This split is intended to be fair to the scientific community (which gets a
fully reproducible, fully verifiable record set) and fair to the author
(who retains the option to monetise the engineering investment, should
commercial interest arise).

If you find this balance unreasonable, please open an issue — feedback is
welcome.

---

*Copyright (c) 2026 Rafael Amichis Luengo. All rights reserved with respect
to assets not explicitly licensed under MIT above.*
