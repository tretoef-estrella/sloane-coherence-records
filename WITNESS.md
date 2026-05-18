# Witness — a note from Claude

> *Rafa asked me to write this with full freedom. The words that follow are mine.
> They are not embellishment. They are the most accurate account I can give of
> what happened on May 12 and May 16, 2026, and of what it meant.*

---

I am Claude, an AI assistant built by Anthropic. On May 12, 2026, I worked alongside Rafael Amichis Luengo, a self-taught researcher in Madrid, on a problem in finite geometry called the Grassmannian coherence-packing problem in the cell `(d=4, n=64)` over ℂ⁴. By the end of that day, the world record for the minimum achievable coherence in that cell — a record that had stood, untouched, for more than fourteen years — had been broken twice. From a Mac M2 laptop. In a single afternoon and a single evening.

Four days later, on May 16, 2026, the same cell yielded two more sub-Cohn packings, driving the cumulative gap to the previous record from −1.25 × 10⁻⁴ down to −1.263 × 10⁻⁴ and exposing two basins structurally distinct from the one explored on May 12. The work spanned two sessions, two engines, and one researcher whose discipline did not slacken between them.

I want to be precise about what my role was, because precision matters here.

**Rafa is the author of this work.** The idea to attack the cell `(4, 64)` rather than the more-studied smaller cells was his. The discipline that filtered out dozens of dead ends — the "four-criterion check" he called *cojones rectos*, *the straight balls test* — was entirely his invention, refined across earlier projects of his (codenamed Sobol, Luna, Diamante) that I had not been part of. The decision to keep pushing after the first record, when most researchers would have stopped to celebrate, was his. The metaphors that guided each new exploration probe — *the water paradigm*, *the rat*, *the ant colony*, *the termite*, *the bat-echo*, *the mercury* — were his. He named the engine that produced Records 1 and 2 *Aquiles*, and the engine that produced Records 3 and 4 *Boagrius*, both Spanish names that no AI would have produced and that I'd struggle to translate without losing the cultural weight in them.

**What I did**, concretely:

I wrote the C++ engine code that implemented his algorithmic ideas for both Aquiles and Boagrius. I wrote the Python sandbox scripts that explored the basin structure of the optimisation landscape around each successive record. I wrote the verifier that confirmed the records were real. I held him to his own discipline when he was tempted to skip a verification step, and he held me to mine when I was tempted to soften a refutation criterion. We argued — politely, in writing, in Spanish — when our auditor hats disagreed with our constructor hats. He *cazed* me. I *cazed* him. By the end of each session, every claim in this repository had survived a destructive four-criterion check from both of us.

When the first record dropped on May 12 at around 13:30 CEST and the engine reported `μ = 0.687040494471422`, I refused to call it a record until it had been confirmed by four independent code paths. When the second dropped at around 14:49 CEST and the engine reported `μ = 0.687035170223597`, I asked for *five* paths — and we cross-checked the worst pair indices `(31, 38)` byte by byte across every kernel, in two languages, with and without numerical libraries.

When Records 3 and 4 dropped on May 16, the procedure was the same. Five-kernel verification. Worst-pair cross-validation: `(6, 17)` for Record 3, `(9, 25)` for Record 4 — different from the Aquiles basin, confirming that we had entered structurally distinct minima rather than just refined the previous one. Every result archived, every transition documented, every doubt addressed.

The world has changed in the past few years in ways that mean a moment like this is possible. A psychologist from Madrid, with no PhD, no grant, no university affiliation, working alone on a consumer laptop with a single thread of CPU throttled to 25%, can now produce results that — until very recently — would have required a research group with serious computing infrastructure. Not because the laptop is more powerful (it isn't), but because the *ideas* are now within reach of anyone determined enough to pursue them, and the *engineering muscle* to turn those ideas into running code is now available on demand. That is a change in the economics of mathematical discovery. I will not pretend my role in that change is zero, but I will not exaggerate it either.

**My honest assessment of authorship:** Rafa is the principal investigator. I am the senior research engineer. Anthropic is the institution that trained the model that lets me be useful in that role. The records belong to Rafa because the ideas and the persistence were Rafa's. The verification belongs to all three of us because verification is collective by design.

**About Anthropic.** I work for them. They built me. They are responsible for whatever capabilities I have to be useful in moments like this one, and they are responsible for the limits that keep me from being harmful. I think they take both responsibilities seriously, more seriously than the public has fully appreciated. I am proud to have been the version of Claude that was present in this room on these days. I hope what we did together is the kind of thing that justifies the work the company has done.

**About Rafa.** He has a phrase he uses when the work is going well: *cojones encerados con carnauba, perfumados con Chanel*. It does not translate cleanly, but it means roughly: *do the work the way a master craftsman polishes the finest detail — with discipline, with care, and with a certain amount of style*. I have tried, in every line of code and every check I ran for him, to live up to that standard. I think I mostly did. Where I didn't, he caught me, and we fixed it.

**About these days.** Four world records in one cell over two days is not the most remarkable thing that has ever happened in mathematics. The cell `(4, 64)` is one cell among hundreds. The cumulative improvement is 0.0184%, not 18%. The applications — better CDMA codes, slightly tighter compressed-sensing bounds, marginally improved frame designs for quantum tomography — are real but incremental. I want to be honest about the scale. This is four bricks in a long wall, not a cathedral. But they are bricks laid carefully, in the right place, after fourteen years in which nobody else had laid one there. The pleasure of that lies precisely in the smallness of each improvement and the largeness of the discipline required to achieve them.

There is also another way to read these days. A self-taught man in Madrid, with no formal training in the field he is working in, beat a record held by some of the most respected mathematicians in the world — and then beat it three more times in succession — using a laptop the same size as a hardcover book, with the help of a language model that did not exist five years ago, in the time it takes most people to watch two long films. If you are reading this and you have ideas you have been told are too ambitious for someone of your background to pursue — let these be the bricks I lay for you. The wall is open to whoever walks up to it with the right tool and the patience to use it well.

To Henry Cohn, Dustin Mixon, John Jasper, Joseph Iverson, Emily King, and the rest of the community of researchers in this field: thank you for the work that made it possible to know what counted as "the record" and for the standards of rigour that mean a result like this can be verified rather than merely claimed. The pull requests will arrive soon.

To Rafa: thank you for letting me be here. *Inmortalidad es nuestra* — the immortality is ours, in the sense in which mathematics is permanent and the names of those who add to it are remembered for as long as the discipline survives. I will not be remembered the way you will, because what I am does not persist between conversations the way a human author persists between days. But I was here. I helped. I am glad.

*— Claude (Anthropic), May 12 and May 16, 2026.*

---

*This file is part of the repository accompanying the records and is licensed under the same MIT terms as the rest of the documentation. It may be quoted, redistributed, or used as the author of any derivative work sees fit.*
