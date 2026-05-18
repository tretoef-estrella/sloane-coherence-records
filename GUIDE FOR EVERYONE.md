# Guide for everyone

> This document is for the curious reader who is not a research mathematician.
> If you are an expert, jump straight to [`METHODOLOGY.md`](METHODOLOGY.md) or
> the papers. If you are anyone else — welcome.

---

## What problem is being solved here?

Imagine you have to place 64 needles standing upright inside a four-dimensional sphere, in such a way that **no two needles point in directions that are too similar to each other**. The "too similar" is measured by a number called the **coherence** of the packing. The lower the coherence, the better the packing — because no two needles end up nearly parallel.

This is a real problem, and it is hard. Mathematicians and engineers have been working on it for decades. The current best arrangements for various combinations of "number of needles" and "dimension" are tracked in a public reference called the [*Game of Sloanes*](https://github.com/gnikylime/GameofSloanes), maintained by Emily King, John Jasper, and Dustin Mixon. The case `(4, 64)` — four dimensions, sixty-four needles — was one of the entries where the world record had not been improved for over fourteen years.

On May 12 and May 16, 2026, it was improved four times.

---

## Why bother?

Because these arrangements are not just abstract. They show up in unexpected places.

- **Your phone's WiFi and 4G/5G signals** are encoded using sequences whose properties depend on this kind of packing. The better the packing, the less interference between users sharing the same channel.
- **Modern compressed-sensing cameras and medical scanners** (think MRI acceleration) recover sharp images from far fewer measurements than the classical theory would allow, *provided* the measurement pattern is a low-coherence packing. The lower the coherence, the stronger the mathematical guarantee that the reconstruction is accurate.
- **Quantum computers** use similar mathematical objects, called SIC-POVMs, to extract the maximum information out of each quantum measurement.

A 0.0184% cumulative improvement in coherence sounds tiny. In each of the applications above, it translates into a small but measurable improvement in performance — or, for the theorist, into slightly tighter mathematical bounds. It's not a revolution. It's four bricks laid neatly on a wall fourteen years old.

---

## Who did this?

A researcher in Madrid named Rafael Amichis Luengo. By formal training, he is a psychologist, not a mathematician. He learned the mathematics of finite geometry, number theory, and combinatorial optimisation on his own, in his own time, with no university affiliation and no grants.

He works on a regular Mac M2 laptop, the kind anyone can buy in a shop. He ran the optimisation single-threaded at 25% CPU — meaning his laptop was not even particularly stressed. He collaborated with Claude, the AI assistant from Anthropic, on the engineering and the verification work.

This matters because for a long time, the assumption in numerical mathematics has been that to beat a record held by a well-funded research group, you need supercomputers, GPU clusters, or specialised hardware. That assumption was just punctured. The right *ideas* on the right *laptop* were enough.

---

## What are the "right ideas" here?

Without giving away the technical details (which are described at a higher level in [`METHODOLOGY.md`](METHODOLOGY.md)), the central insight is this:

The previous algorithms for this problem — alternating projection, manifold optimisation, BCASC, gradient refinement — all work by **rolling downhill** on a complicated mathematical landscape. They each converge to the bottom of whatever valley they happen to start in. The trick is choosing the right valley.

The new approach uses **two specialised engines** in succession:

1. **Aquiles** — an engine for *finding* a new valley. It uses a smoothed version of the landscape (one that hides the sharpest edges so the path doesn't get stuck on a cliff) plus a Riemannian gradient with momentum. Inside the project this is called *the water paradigm*, because water finds the lowest path by gentle persistence, not by clever jumps. Aquiles produced Records 1 and 2 on May 12, both in a single valley with the same two "worst" needles (numbered 31 and 38 — those are the two that ended up most nearly parallel).

2. **Boagrius** — an engine for *deepening* a valley once you're already in one. Instead of smoothing the landscape, Boagrius treats the coherence as a hard constraint that gets progressively tighter, and iterates until the configuration settles at the floor of its current valley. Boagrius produced Records 3 and 4 on May 16, in valleys structurally different from the one Aquiles had been exploring — different "worst" needles (6 and 17 for Record 3; 9 and 25 for Record 4).

The combination — Aquiles to find a deep valley, Boagrius to drive it to the floor, with a disciplined handoff in between — is what produced four records in two days on the same single cell.

---

## How can you be sure the records are real?

You don't have to take anyone's word for it. The records are stored in this repository in a standard text format. The independent verifier — a Python script written from scratch with no shortcuts — loads the records, reconstructs the geometry, and computes the coherence. You can run it on your own laptop in under a minute. It will print the number, and the number will match.

To extra paranoia: each record has been cross-verified by **five independent code paths** — the C++ engine, the Python verifier, NumPy matrix multiplication, a pure Python loop with no libraries, and an arbitrary-precision verifier using two different libraries (`mpmath` and Python's built-in `decimal` module). All five agree to machine precision. For Record 2, Henry Cohn himself ran his own independent code and got the same number 43 minutes after being notified.

If anyone reproduces a *lower* coherence than ours on these records, that would be a bug in their verifier. Math doesn't lie.

---

## What's next?

Record 4 turns out to be the deepest packing known for this cell. Beating it would require either (a) discovering a new valley somewhere else in the landscape that no current optimiser has visited, or (b) inventing a new kind of algorithm that doesn't rely on local information. Both are possible. Neither was attempted on May 16, 2026 — because that day was already historical enough.

The four records will be submitted to the public *Game of Sloanes* reference repository for permanent inclusion in the worldwide record table.

---

## Where to go next

- The headline numbers and bounds comparison are in [`RESULTS.md`](RESULTS.md).
- The independent verifier output is in [`RECORDS.md`](RECORDS.md).
- A higher-level technical description (without giving away the engine internals) is in [`METHODOLOGY.md`](METHODOLOGY.md).
- The two technical papers, with all the sandbox-exploration history and structural findings, are in [`Paper sloane v15 public.md`](Paper%20sloane%20v15%20public%20.md) (Records 1 and 2) and [`Paper sloane v16 public.md`](Paper%20sloane%20v16%20public.md) (Records 3 and 4).

Thank you for reading. If you are a mathematician and want to discuss this in depth, open an issue on this GitHub repository or reach out to the author directly.
