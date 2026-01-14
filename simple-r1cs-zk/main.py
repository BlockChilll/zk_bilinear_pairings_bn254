from py_ecc.bn128.bn128_curve import G1, G2, add, curve_order, eq, multiply
from py_ecc.bn128.bn128_pairing import pairing


def main():
    # EQUATION TO PROVE: x^3 + 4x^2 - xz + 4 = 529

    # CONSTRAINTS
    # 1) `x_squared = x * x`
    # 2) `x_cubed = x * x_squared`
    # 3) `result - x_cubed - 4 * x_squared - 4 = -xz`

    # OUT gives us the output (left side of equality) of each constraint
    OUT = [
        [0, 0, 1, 0, 0, 0],  # LHS of 1) x^2
        [0, 0, 0, 1, 0, 0],  # LHS of 2) x^3
        [-4, 0, -4, -1, 0, 1],  # LHS of 3) y - x^3 - 4x^2 - 4
    ]

    # A gives us the left argument (right side of equality) of each constraint
    A = [
        [0, 1, 0, 0, 0, 0],  # LHARG of 1) x
        [0, 0, 1, 0, 0, 0],  # LHARG of 2) x^2
        [0, -1, 0, 0, 0, 0],  # LHARG of 3) -x
    ]

    # B give us the right argument (right side of equality) of each constraint
    B = [
        [0, 1, 0, 0, 0, 0],  # RHARG of 1) x
        [0, 1, 0, 0, 0, 0],  # RHARG of 2) x
        [0, 0, 0, 0, 1, 0],  # RHARG of 3) z
    ]

    # SOLUTION
    x = 7
    z = 2
    y = 529

    # CALCULATE WITNESS
    x_squared = x**2
    x_cubed = x**3
    w = [1, x, x_squared, x_cubed, z, y]

    # WITNESSES
    wG1 = [multiply(G1, i) for i in w]
    wG2 = [multiply(G2, i) for i in w]
    allG2 = [G2 for _ in w]

    # HELPER: DOT PRODUCT ON ELIPTIC CURVES
    def dot_ec(constraints, witness, G):
        r = []
        for constraint in constraints:
            sum = None
            for idx, element in enumerate(constraint):
                if element < 0:
                    sum = add(sum, multiply(witness[idx], curve_order + element))
                else:
                    sum = add(sum, multiply(witness[idx], element))
            r.append(sum)
        return r

    # HELPER: ELEMENTWISE MUL ON ELIPTIC CURVES
    def elmul_ec(A, B):
        out = []
        for a, b in zip(A, B):
            # PAY ATTENTION that bn128 expects G2 point as first argument, and G1 as second
            out.append(pairing(b, a))
        return out

    # CHECK CONSTRAINTS
    lhs = elmul_ec(dot_ec(OUT, wG1, G1), allG2)
    rhs = elmul_ec(dot_ec(A, wG1, G1), dot_ec(B, wG2, G2))
    print(all(eq(l, r) for l, r in zip(lhs, rhs)))


if __name__ == "__main__":
    main()
