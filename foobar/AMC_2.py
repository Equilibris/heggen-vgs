from fractions import Fraction, gcd
import numpy as np

def transpose(m):
    return [list(i)for i in zip(*m)]


def minor(m, i, j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]


def det(m):
    # base case for 2x2 matrix
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]

    d = 0
    for c in range(len(m)):
        d += ((-1)**c)*m[0][c] * \
            det(minor(m, 0, c))
    return d


def inv(m):
    d = det(m)
    # special case for 2x2 matrix:
    if len(m) == 2:
        return [[m[1][1]/d, -1*m[0][1]/d],
                [-1*m[1][0]/d, m[0][0]/d]]

    # find matrix of cofactors
    cof = []
    for r in range(len(m)):
        cof_row = []
        for c in range(len(m)):
            minor = minor(m, r, c)
            cof_row.append(((-1)**(r+c)) * det(minor))
        cof.append(cof_row)
    cof = transpose(cof)
    for r in range(len(cof)):
        for c in range(len(cof)):
            cof[r][c] = cof[r][c]/d
    return cof


def matrix_mul(a, b):
    m = len(a)
    p = len(b[0])

    output = [[0 for i in range(p)] for i in range(m)]

    for inner_index, row in enumerate(transpose(b)):
        for outer_index, i in enumerate(a):
            output[outer_index][inner_index] = (
                sum(map(lambda a: a[0]*a[1], zip(row, i))))

    return output


def transform_primary_matrix_zeroes(m):
    zeroes_index = -1
    for index, el in enumerate(m[::-1]):
        if not any(el):
            # direct progression
            if index == zeroes_index + 1:
                zeroes_index += 1
                continue

            m[-1 - index], m[-1 - zeroes_index] = m[-1 - zeroes_index], m[-1 - index]

            for i in m:
                i[-1 - index], i[-1 - zeroes_index] = \
                    i[-1 - zeroes_index], i[-1 - index]

            zeroes_index += 1


def get_data(l):
    primary_matrix = [[Fraction(i, sum(x)) if sum(x) else Fraction(0)
                       for i in x] for x in l]

    transform_primary_matrix_zeroes(primary_matrix)

    non_terminal = [any(i) for i in l]

    return non_terminal, primary_matrix


def kronecker_delta(a, b): return int(a == b)


def get_imq(l, nt):
    return [[kronecker_delta(J, I) - j for J, j in enumerate(i) if nt[J]] for I, i in enumerate(l) if nt[I]]


def get_r(l, nt):
    return [[j for J, j in enumerate(i) if not nt[J]] for I, i in enumerate(l) if nt[I]]


def lcm(a, b):
    return abs(a*b) // gcd(a, b)


def reduce_fractions(arr):
    arr = [Fraction(x).limit_denominator() for x in arr]
    the_lcd = 1
    for x in arr:
        the_lcd = np.lcm(the_lcd, x.denominator)
    out_arr = [(x.numerator * int(the_lcd / x.denominator)) for x in arr]
    out_arr.append(the_lcd)
    return out_arr


def solution(m):
    non_terminal, primary_matrix = get_data(m)

    r = get_r(primary_matrix, non_terminal)
    imq = get_imq(primary_matrix, non_terminal)
    matrix = inv(imq)
    # print(*imq, sep='\n')
    # print()
    # print(*matrix, sep='\n')
    # print()
    # print(*r, sep='\n')

    out = matrix_mul(matrix, r)[0]

    # v = out[0].denominator
    # for i in out[1:]:
    #     v = lcm(v, i.denominator)
    return reduce_fractions(out)

    # return [i.numerator * v//i.denominator for i in out] + [v]


if __name__ == '__main__':
    import AMC_shared as amc

    print(solution(amc.b))
    # print(solution(amc.a))
    # print(solution(amc.a2))
    # m1 = [[3, 5, -1], [4, 0, 2], [-6, -3, 2]]
    # m2 = [[2, -2, 3, 1], [5, 0, 7, 8], [9, -4, 1, 1]]

    # # print(*m2, sep='\n')
    # print(*matrix_mul(m1, m2), sep='\n
