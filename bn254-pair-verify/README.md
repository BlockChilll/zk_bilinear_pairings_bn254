# ZK Bilinear Pairings on BN254

This project creates ZK verification example using bilinear pairings on the BN254 curve. (EIP 197)
G1 is a simple elliptic curve group.
G2 is an elliptic curve group with field extensions.

## Discrete Log Inputs

| Variable | Value |
|----------|-------|
| a        | 4     |
| b        | 3     |
| c        | 6     |
| d        | 2     |

## Equation to Prove

```
-ab + cd = 0
```

## Bilinear Pairing Equation

Verified by EVM contract:

```
A1*B2 + C1*D2 = e(-aG1, bG2) + e(cG1, dG2) = 0
```

### Point Definitions

| Point | Group | Definition |
|-------|-------|------------|
| A1    | G1(generator)    | -a*G1 (elliptic curve point) |
| B2    | G2(generator)    | b*G2 (elliptic curve point)  |
| C1    | G1(generator)    | c*G1 (elliptic curve point)  |
| D2    | G2(generator)    | d*G2 (elliptic curve point)  |

### Pairing Function

`e(x,y)` is a bilinear pairing function that takes two points on different elliptic curves and returns a value in a finite field Gt.

`e(x1,y1) + e(x2,y2)`: Gt group uses its binary operation here, represented with "+", but sometimes it is called either multiplication or addition.

## Invariant

> The sum of pairings is zero if and only if the sum of the products of the discrete logarithms is zero.
