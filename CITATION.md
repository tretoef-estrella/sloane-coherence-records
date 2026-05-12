# How to cite this work

If you use these records, the methodology, or any of the materials in this
repository in your research, please cite as follows.

---

## Author name — preferred form

The author's preferred name in citations is **Rafael Amichis Luengo**, with
both surnames included. *Amichis* is the first surname; *Luengo* is the
second.

When citation style requires abbreviation of the given name (e.g. ACM, IEEE,
APS, AMS), the preferred abbreviated form is:

> **R. Amichis Luengo**

Please **avoid** abbreviating both surnames (e.g. "R. A. Luengo" or
"R. A.-L.") or dropping the second surname (e.g. "R. Amichis"). The full
double surname matters culturally and is the form under which the author
wishes to be indexed.

For BibTeX, use the `family/given` split shown in the entry below — the
`family` field includes both surnames, separated by a space, which is the
standard way to handle Spanish double surnames in BibTeX.

---

## Plain-text citation

> Amichis Luengo, Rafael (2026). *Two world records in Grassmannian coherence packings (d=4, n=64) hlc.* Independent research, Madrid, Spain. May 12, 2026. Available at: https://github.com/tretoef-estrella/sloane-coherence-records

If using author–year style with abbreviated given name:

> Amichis Luengo, R. (2026). *Two world records in Grassmannian coherence packings (d=4, n=64) hlc.* Independent research, Madrid, Spain. May 12, 2026. Available at: https://github.com/tretoef-estrella/sloane-coherence-records

---

## BibTeX

```bibtex
@misc{amichisluengo2026sloane,
  author       = {Amichis Luengo, Rafael},
  title        = {Two world records in {Grassmannian} coherence packings ($d=4$, $n=64$) hlc},
  year         = {2026},
  month        = {5},
  day          = {12},
  howpublished = {\url{https://github.com/tretoef-estrella/sloane-coherence-records}},
  note         = {Coherence records: $\mu_1 = 0.687040494471422$ (record \#1) and
                  $\mu_2 = 0.687035170223597$ (record \#2). Both records
                  verified byte-exact by five independent kernels.
                  Independent researcher, Madrid, Spain.
                  Author name: please cite as ``Amichis Luengo, R.''
                  with both surnames; avoid abbreviating the second surname.},
  keywords     = {Grassmannian packing, coherence, frame theory, equiangular tight frame,
                  compressed sensing, MIMO precoding, CDMA codes, quantum state tomography}
}
```

**Note for BibTeX users:** the `author` field uses the
`{LastNames, FirstNames}` form. Both surnames *Amichis Luengo* are grouped
together inside the braces, which tells BibTeX to treat them as a single
family name and not to split them. This produces the correct rendering
*Amichis Luengo, R.* in author-year styles and *R. Amichis Luengo* in
numeric styles.

---

## Citation summary

| Field | Value |
|:---|:---|
| Author | Rafael Amichis Luengo |
| Affiliation | Independent researcher, Madrid, Spain |
| Title | Two world records in Grassmannian coherence packings (d=4, n=64) hlc |
| Date | May 12, 2026 |
| Type | Dataset / open-source research artefact |
| Version | 1.0 |
| License | MIT (records, verifier, paper, documentation); engine source code under separate arrangement |
| URL | https://github.com/tretoef-estrella/sloane-coherence-records |
| Record #1 coherence | μ = 0.687040494471422 |
| Record #2 coherence | μ = 0.687035170223597 |
| Previous record (Cohn et al.) | μ = 0.687160201509307 |
| Improvement (record #2 vs. Cohn) | −1.250 × 10⁻⁴ absolute, −0.0182% relative |
| Verification | Byte-exact, 5 independent kernels |

---

## Keywords

`Grassmannian packing` · `coherence` · `frame theory` · `equiangular tight frame` · `compressed sensing` · `MIMO precoding` · `CDMA codes` · `quantum state tomography` · `Mac M2` · `Riemannian gradient flow` · `smoothed-max optimization`

---

## Machine-readable citation

A machine-readable [CITATION.cff](CITATION.cff) file is also included in this repository, conforming to the Citation File Format v1.2.0 standard. GitHub will display a "Cite this repository" button on the repo page using that file.

---

## Acknowledging this work in a paper

If you cite these records in a paper, the author would appreciate (but does not require) a courtesy email so he can track which papers use the work. Contact details are in the [README](README.md).

If you reproduce the records or extend the methodology to other cells `(d, n)`, please consider opening an issue or pull request on this repository to share your results — the community of Grassmannian-packing researchers is small, and collective progress benefits everyone.
