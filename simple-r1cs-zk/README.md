# Simple R1CS Zero Knowledge Proof

## Goal

Demonstrate a zero-knowledge proof using R1CS (Rank-1 Constraint System) and bilinear pairings on elliptic curves.

### Mathematical Problem

Prove knowledge of `x` and `z` that satisfy:

```
x³ + 4x² - xz + 4 = 529
```

## Overview

This implementation showcases the progression from basic arithmetic to elliptic curve-based zero-knowledge proofs:

- **R1CS on normal arithmetic** → **Modular arithmetic** → **Elliptic curve circuits**

## Zero Knowledge Approach

To achieve zero-knowledge properties (while preventing simple guess-and-check attacks), we utilize **elliptic curves** with the same R1CS constraints.

### Key Challenge

Elliptic curve points cannot be multiplied directly, which breaks the standard `OUT = A * B` constraint pattern.

### Solution: Bilinear Pairings

We leverage **bilinear pairings** using elliptic curve points with field extensions:

1. **Dual Witnesses**: Create two witnesses using identical values
   - One multiplied by `G1` point
   - One multiplied by `G2` point

2. **Dot Products**: Compute dot products of witnesses with constraints (as in previous examples)

3. **Pairing Operations**: When "multiplying" `A` and `B`:
   - Take bilinear pairing of the two points
   - Results land in the `G12` group

4. **Verification**: Compare two approaches:
   - **Method 1**: Bilinear pairing of `dot_product(G1_witness, OUT)` with `vector_of_all_G2_points`
   - **Method 2**: Bilinear pairing of `dot_product(G1_witness, A)` with `dot_product(G2_witness, B)`

The result is analogous to multiplying by 1, but operates within the `G12` group, enabling secure comparison.

## Final Verification

We compare the two resulting `G12` points to verify equality, confirming the zero-knowledge proof.

## Acknowledgments

This example is taken from and created by: [https://github.com/zobront/homerolled-zk](https://github.com/zobront/homerolled-zk)
