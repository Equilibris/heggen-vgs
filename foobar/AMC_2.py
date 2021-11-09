from fractions import Fraction
import numpy as np


def get_data(l):
    primary_matrix = [[i/sum(x) if sum(x) else 0 for i in x] for x in l]

    non_terminal = [any(i) for i in l]
    term_index_pushback = []

    zero_counts = 0

    for index, i in enumerate(l):
        if any(i):
            term_index_pushback.insert(
                len(term_index_pushback) - zero_counts, index)
        else:
            term_index_pushback.append(index)
            zero_counts += 1

    return non_terminal, primary_matrix, term_index_pushback


def get_q(l, nt, term_index_pushback):
    return [[l[I][J] for J in term_index_pushback if nt[J]]for I in term_index_pushback if nt[I]]


def get_r(l, nt, term_index_pushback):
    return [[l[I][J] for J in term_index_pushback if not nt[J]]for I in term_index_pushback if nt[I]]


def reduce_fractions_(arr):
    out = [Fraction(i).limit_denominator(100) for i in arr]

    v = out[0].denominator
    for i in out[1:]:
        v = np.lcm(v, i.denominator)
    return [i.numerator * (v // i.denominator) for i in out] + v


def reduce_fractions(arr):
    arr = [Fraction(x).limit_denominator() for x in arr]
    the_lcd = 1
    for x in arr:
        the_lcd = np.lcm(the_lcd, x.denominator)
    return [x.numerator * (the_lcd // x.denominator) for x in arr] + [the_lcd]


def solution(m):
    if len(m) < 2:
        return [1, 1]

    non_terminal, primary_matrix, term_index_pushback = get_data(m)

    r = np.matrix(get_r(primary_matrix, non_terminal, term_index_pushback))
    q = np.matrix(get_q(primary_matrix, non_terminal, term_index_pushback))

    i = np.matrix([[float(j == i) for j in range(len(q))]
                  for i in range(len(q))])

    imq = np.subtract(i, q)
    n = np.linalg.inv(imq)

    out = np.dot(n, r)

    return reduce_fractions(out[0, 0:].flat)


def error(a, b):
    return sum(i-j for i, j in zip(a, b))


if __name__ == '__main__':
    import AMC_shared as amc

    print(error(solution(amc.b), amc.b_sol))
    print(error(solution(amc.a), amc.a_sol))
    print(error(solution(amc.a2), amc.a_sol))
    # print(solution(amc.a))
    # print(solution(amc.a2))
    # m1 = [[3, 5, -1], [4, 0, 2], [-6, -3, 2]]
    # m2 = [[2, -2, 3, 1], [5, 0, 7, 8], [9, -4, 1, 1]]

    # # print(*m2, sep='\n')
    # print(*matrix_mul(m1, m2), sep='\n
