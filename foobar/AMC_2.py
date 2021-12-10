from fractions import Fraction
import numpy


def get_data(l):
    primary_matrix = [[i/float(sum(x)) if any(x) else 0 for i in x] for x in l]

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


def reduce_fractions(arr):
    arr = [Fraction(x).limit_denominator() for x in arr]
    v = 1
    for x in arr:
        v = numpy.lcm(v, x.denominator)
    return [x.numerator * (v // x.denominator) for x in arr] + [v]


def solution(m):
    if len(m) < 2:
        return [1, 1]

    non_terminal, primary_matrix, term_index_pushback = get_data(m)

    q = get_q(primary_matrix, non_terminal, term_index_pushback)
    r = get_r(primary_matrix, non_terminal, term_index_pushback)
    i = numpy.identity(len(q))

    imq = numpy.subtract(i, q)
    n = numpy.linalg.inv(imq)

    out = numpy.dot(n, r)

    return reduce_fractions(out[0])


def error(a, b):
    print(a, b)
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
