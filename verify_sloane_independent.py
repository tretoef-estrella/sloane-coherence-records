#!/usr/bin/env python3
"""
verify_sloane_independent.py — D190 step 4 INDEPENDENT verifier
================================================================
Project Sloane — Game of Sloanes complex projective packings.
Architect: Rafael Amichis Luengo (Madrid).
Constructor: Claude (current session, Sloane Phase 1).

PURPOSE
-------
Clean-room Python re-implementation of the coherence computation for
Game of Sloanes complex projective packings. Independent from any C++
engine kernel. Used as D190 step 4 INDEPENDENT verification.

FORMAT (per github.com/gnikylime/GameofSloanes README, fetched 11 May 2026)
--------------------------------------------------------------------------
- File: dxn_init.txt where d=dimension, n=number of vectors, init=creator tag.
- Content: 2*d*n floats, newline-separated.
- Ordering: ALL real parts first (vector 1 coords 1..d, vector 2 coords 1..d, ...),
  then ALL imag parts (vector 1 coords 1..d, vector 2 coords 1..d, ...).
- Constraint: each vector must satisfy ||v_i||_2 = 1 (unit-norm, within epsilon).

METRIC
------
Coherence: mu(Phi) = max_{1 <= j < k <= n} |<v_j, v_k>|
where <.,.> is the standard Hermitian inner product on C^d.

A new packing beats the current record if coherence is smaller by at least
the 8th decimal place (per GitHub README submission rules).

USAGE
-----
    python3 verify_sloane_independent.py 4x64_hlc.txt
    python3 verify_sloane_independent.py 4x64_hlc.txt --expected 0.68716020

EXIT CODES
----------
    0: file parsed successfully, coherence reported, expected matched (if given).
    1: parse error, structural error (wrong number of floats, non-unit vectors).
    2: expected coherence given but mismatch beyond tolerance.
"""

import sys
import math
import argparse
from typing import List, Tuple


def parse_filename_dxn(filename: str) -> Tuple[int, int, str]:
    """Extract (d, n, creator_tag) from filename pattern dxn_init.txt."""
    import os
    base = os.path.basename(filename)
    name = base.replace(".txt", "")
    # Expected: dxn_init where d and n are integers, init is alphabetic
    if "_" not in name or "x" not in name:
        raise ValueError(f"Filename '{base}' does not match dxn_init.txt pattern.")
    dxn, init = name.rsplit("_", 1)
    d_str, n_str = dxn.split("x", 1)
    return int(d_str), int(n_str), init


def parse_packing_file(filename: str, d: int, n: int) -> List[List[complex]]:
    """
    Parse a Game of Sloanes packing file into a list of n complex d-vectors.

    Format: 2*d*n floats newline-separated. Real parts of all vectors first
    (vector 1 coord 1..d, then vector 2 coord 1..d, ...), then imag parts
    in the same ordering.

    Returns: vectors[i][j] = complex value at coord j of vector i (0-indexed).
    """
    with open(filename, 'r') as f:
        raw_floats = []
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                raw_floats.append(float(line))
            except ValueError as e:
                raise ValueError(f"Cannot parse line as float: '{line}'") from e

    expected_count = 2 * d * n
    if len(raw_floats) != expected_count:
        raise ValueError(
            f"Expected {expected_count} floats (2*d*n = 2*{d}*{n}), "
            f"got {len(raw_floats)}."
        )

    # First d*n floats are real parts, next d*n are imag parts.
    # Within each block, the order is: vec0_coord0, vec0_coord1, ..., vec0_coord(d-1),
    #                                  vec1_coord0, ..., vec(n-1)_coord(d-1).
    real_parts = raw_floats[:d * n]
    imag_parts = raw_floats[d * n:]

    vectors: List[List[complex]] = []
    for i in range(n):
        v: List[complex] = []
        for j in range(d):
            idx = i * d + j
            v.append(complex(real_parts[idx], imag_parts[idx]))
        vectors.append(v)

    return vectors


def vector_norm(v: List[complex]) -> float:
    """L2 norm of a complex vector."""
    s = 0.0
    for c in v:
        # |c|^2 = re^2 + im^2
        s += c.real * c.real + c.imag * c.imag
    return math.sqrt(s)


def verify_unit_norms(vectors: List[List[complex]], tol: float = 1e-10) -> Tuple[bool, float, int]:
    """
    Verify all vectors are unit-norm within tolerance.
    Returns (all_ok, max_deviation, worst_index).
    """
    max_dev = 0.0
    worst_idx = -1
    for i, v in enumerate(vectors):
        norm = vector_norm(v)
        dev = abs(norm - 1.0)
        if dev > max_dev:
            max_dev = dev
            worst_idx = i
    return (max_dev <= tol), max_dev, worst_idx


def hermitian_inner_product(v: List[complex], w: List[complex]) -> complex:
    """
    Compute Hermitian inner product <v, w> = sum_j conj(v_j) * w_j.

    Convention: physics-style with conjugate on the LEFT argument.
    Per Game of Sloanes README, coherence is max |<v_j, v_k>|, and the
    standard frame-theory convention is conjugate on the first argument.
    Note: |<v, w>| is the same either way; this convention only matters
    for the complex value, not the magnitude.
    """
    s = complex(0.0, 0.0)
    for a, b in zip(v, w):
        s += a.conjugate() * b
    return s


def compute_coherence(vectors: List[List[complex]]) -> Tuple[float, int, int]:
    """
    Compute coherence mu = max_{i < j} |<v_i, v_j>|.
    Returns (coherence, idx_i, idx_j) where (idx_i, idx_j) is the worst pair.
    """
    n = len(vectors)
    max_abs = 0.0
    max_i, max_j = -1, -1
    for i in range(n):
        for j in range(i + 1, n):
            ip = hermitian_inner_product(vectors[i], vectors[j])
            abs_ip = math.sqrt(ip.real * ip.real + ip.imag * ip.imag)
            if abs_ip > max_abs:
                max_abs = abs_ip
                max_i, max_j = i, j
    return max_abs, max_i, max_j


def welch_bound(d: int, n: int) -> float:
    """
    Welch lower bound for coherence of n unit vectors in C^d.
    welch(d, n) = sqrt( (n - d) / (d * (n - 1)) )    for n > d.
    """
    if n <= d:
        return 0.0
    return math.sqrt((n - d) / (d * (n - 1)))


def main():
    parser = argparse.ArgumentParser(
        description="Verify Game of Sloanes complex projective packing."
    )
    parser.add_argument("filename", help="Path to dxn_init.txt file.")
    parser.add_argument("--expected", type=float, default=None,
                        help="Expected coherence (byte-exact byte-exact comparison to 8 decimals).")
    parser.add_argument("--tol-norm", type=float, default=1e-10,
                        help="Tolerance for unit-norm verification (default 1e-10).")
    parser.add_argument("--tol-expected", type=float, default=1e-8,
                        help="Tolerance for --expected match (default 1e-8 = 8 decimals).")
    args = parser.parse_args()

    print("=" * 70)
    print("VERIFY_SLOANE_INDEPENDENT — D190 step 4 INDEPENDENT verifier")
    print("=" * 70)
    print(f"File: {args.filename}")

    # Extract (d, n, init) from filename
    try:
        d, n, init = parse_filename_dxn(args.filename)
        print(f"Parsed filename: d={d}, n={n}, creator_tag='{init}'")
    except ValueError as e:
        print(f"FILENAME PARSE ERROR: {e}", file=sys.stderr)
        sys.exit(1)

    # Parse the file
    try:
        vectors = parse_packing_file(args.filename, d, n)
        print(f"Parsed {len(vectors)} vectors of dimension {d} (C^{d}).")
    except (ValueError, IOError) as e:
        print(f"FILE PARSE ERROR: {e}", file=sys.stderr)
        sys.exit(1)

    # Verify unit norms (STRUCTURAL check)
    ok_norms, max_dev, worst_idx = verify_unit_norms(vectors, tol=args.tol_norm)
    print(f"Unit-norm check: max deviation = {max_dev:.2e} at vector index {worst_idx}")
    if not ok_norms:
        print(f"STRUCTURAL ERROR: max norm deviation {max_dev:.2e} > tolerance {args.tol_norm:.2e}",
              file=sys.stderr)
        sys.exit(1)
    print(f"Unit-norm check: PASSED (within {args.tol_norm:.0e}).")

    # Compute Welch bound for reference
    wb = welch_bound(d, n)
    print(f"Welch lower bound (d={d}, n={n}): {wb:.10f}")

    # Compute coherence (the main metric)
    coh, idx_i, idx_j = compute_coherence(vectors)
    print(f"Coherence mu(Phi) = {coh:.15f}")
    print(f"Worst pair: vectors ({idx_i}, {idx_j}) with |<v_{idx_i}, v_{idx_j}>| = {coh:.15f}")
    print(f"Coherence / Welch bound ratio: {coh / wb:.6f}")
    print(f"Gap above Welch (absolute): {coh - wb:.10f}")
    print(f"Gap above Welch (percent): {(coh - wb) / wb * 100:.4f}%")

    # Compare against expected value if provided
    if args.expected is not None:
        diff = abs(coh - args.expected)
        print()
        print(f"Expected coherence: {args.expected:.15f}")
        print(f"Computed coherence: {coh:.15f}")
        print(f"Absolute difference: {diff:.2e}")
        print(f"Match tolerance: {args.tol_expected:.2e} (8 decimal places per Game of Sloanes rules)")
        if diff <= args.tol_expected:
            print("EXPECTED MATCH: PASSED byte-exact to 8 decimals.")
            sys.exit(0)
        else:
            print(f"EXPECTED MISMATCH: diff {diff:.2e} > tolerance {args.tol_expected:.2e}",
                  file=sys.stderr)
            sys.exit(2)

    print()
    print("Verification complete.")
    sys.exit(0)


if __name__ == "__main__":
    main()
