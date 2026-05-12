# Guide for everyone

> This document is for the curious reader who is not a research mathematician.
> If you are an expert, jump straight to [`METHODOLOGY.md`](METHODOLOGY.md) or
> the paper. If you are anyone else — welcome.

---

## What problem is being solved here?

Imagine you have to place 64 needles standing upright inside a four-dimensional sphere, in such a way that **no two needles point in directions that are too similar to each other**. The "too similar" is measured by a number called the **coherence** of the packing. The lower the coherence, the better the packing — because no two needles end up nearly parallel.

This is a real problem, and it is hard. Mathematicians and engineers have been working on it for decades. The current best arrangements for various combinations of "number of needles" and "dimension" are tracked in a public reference called the [*Game of Sloanes*](https://github.com/jasonleenaff/GameofSloanes), maintained by Henry Cohn and colleagues. The case `(4, 64)` — four dimensions, sixty-four needles — was one of the entries where the world record had not been improved for over fourteen years.

On May 12, 2026, it was improved twice in one day.

---

## Why bother?

Because these arrangements are not just abstract. They show up in unexpected places.

- **Your phone's WiFi and 4G/5G signals** are encoded using sequences whose properties depend on this kind of packing. The better the packing, the less interference between users sharing the same channel.
- **Modern compressed-sensing cameras and medical scanners** (think MRI acceleration) recover sharp images from far fewer measurements than the classical theory would allow, *provided* the measurement pattern is a low-coherence packing. The lower the coherence, the stronger the mathematical guarantee that the reconstruction is accurate.
- **Quantum computers** use similar mathematical objects, called SIC-POVMs, to extract the maximum information out of each quantum measurement.

A 0.0182% improvement in coherence sounds tiny. In each of the applications above, it translates into a small but measurable improvement in performance — or, for the theorist, into slightly tighter mathematical bounds. It's not a revolution. It's a brick laid neatly on a wall fourteen years old.

---

## Who did this?

A researcher in Madrid named Rafael Amichis Luengo. By formal training, he is a psychologist, not a mathematician. He learned the mathematics of finite geometry, number theory, and combinatorial optimisation on his own, in his own time, with no university affiliation and no grants.

He works on a regular Mac M2 laptop, the kind anyone can buy in a shop. He ran the optimisation single-threaded at 25% CPU — meaning his laptop was not even particularly stressed. He collaborated with Claude, the AI assistant from Anthropic, on the engineering and the verification work.

This matters because for a long time, the assumption in numerical mathematics has been that to beat a record held by a well-funded research group, you need supercomputers, GPU clusters, or specialised hardware. That assumption was just punctured. The right *idea* on the right *laptop* was enough.

---

## What is the "right idea" here?

Without giving away the technical details (which are described at a higher level in [`METHODOLOGY.md`](METHODOLOGY.md)), the central insight was this:

The previous algorithms for this problem — alternating projection, manifold optimisation, BCASC, gradient refinement — all work by **rolling downhill** on a complicated mathematical landscape. They each converge to the bottom of whatever valley they happen to start in. The trick is choosing the right valley.

The new approach combines two ideas:

1. **A different way of rolling downhill** — one that smooths out the sharp peaks of the landscape so the path doesn't get stuck on a cliff edge. Inside the project this approach was nicknamed *the water paradigm*, because water finds the lowest path by gentle persistence, not by clever jumps.
2. **A different way of choosing where to start** — not from random initial conditions, and not from the previous record, but from a carefully selected family of *satellite basins* discovered by a quick sandbox exploration.

The combination, applied with discipline, produced two records on the same day, from two structurally distinct starting basins.

---

## How can I be sure the records are real?

You don't have to take anyone's word for it. The records are stored in this repository in a standard text format. The independent verifier — a Python script written from scratch with no shortcuts — loads the records, reconstructs the geometry, and computes the coherence. You can run it on your own laptop in under a minute. It will print the number, and the number will match. To extra paranoia: the records have been cross-verified by **five independent code paths** (the original C++ engine, the Python verifier, NumPy matrix multiplication, a pure Python loop with no libraries, and a per-pair inner-product calculation). All five agree to machine precision.

If anyone reproduces a *lower* coherence than ours on these records, that would be a bug in their verifier. Math doesn't lie.

---

## What's next?

The second record turns out to be a particularly *stubborn* arrangement — six different probing techniques tried to improve on it and all failed. This is good news, actually: it means the record is robust, sitting at the bottom of a well-defined geometric basin. The mathematical interpretation is that the second record is a *strong local minimum* of the optimisation landscape.

To beat it would require either (a) discovering a completely different basin elsewhere in the landscape, or (b) inventing a new kind of algorithm that doesn't rely on local information. Both are possible. Neither was attempted on May 12, 2026 — because that day was already historical enough.

The records will be submitted to the public *Game of Sloanes* reference repository for permanent inclusion in the worldwide record table.

---

## Where to go next

- The headline numbers and bounds comparison are in [`RESULTS.md`](RESULTS.md).
- The independent verifier output is in [`RECORDS.md`](RECORDS.md).
- A higher-level technical description (without giving away the engine internals) is in [`METHODOLOGY.md`](METHODOLOGY.md).
- The full technical paper, with all the sandbox-exploration history and structural findings, is in [`Paper sloane v15 public .md`](Paper%20sloane%20v15%20public%20.md).

Thank you for reading. If you are a mathematician and want to discuss this in depth, open an issue on this GitHub repository or reach out to the author directly.
