from fractions import Fraction, gcd
import numpy as np
# def convert_to_markov_parts(m):
#     term_states = []
#     new_matrix = []
#     for (ind, s) in enumerate(m):
#         if sum(s) == 0:
#             term_states.append(ind)
#         else:
#             new_matrix.append(s)

#     m = new_matrix

#     Q = []
#     R = []
#     for s in m:
#         Q_new = []
#         R_new = []
#         for (ind, x) in enumerate(s):
#             if ind in term_states:
#                 R_new.append(x)
#             else:
#                 Q_new.append(x)
#         Q.append(Q_new)
#         R.append(R_new)
#     return (Q, R)


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


def kronecker_delta(a, b): return int(a == b)


def get_q(l, nt, term_index_pushback):
    return [[l[I][J] for J in term_index_pushback if nt[J]]for I in term_index_pushback if nt[I]]


def get_r(l, nt, term_index_pushback):
    return [[l[I][J] for J in term_index_pushback if not nt[J]]for I in term_index_pushback if nt[I]]


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
    if len(m) < 2:
        return [1, 1]

    non_terminal, primary_matrix, term_index_pushback = get_data(m)

    r = np.matrix(get_r(primary_matrix, non_terminal, term_index_pushback))
    q = np.matrix(get_q(primary_matrix, non_terminal, term_index_pushback))

    i = np.matrix([[float(j == i) for j in range(len(q))]
                  for i in range(len(q))])

    return reduce_fractions(np.matmul(np.linalg.inv(np.subtract(i, q)), r).tolist()[0])


if __name__ == '__main__':
    import AMC_shared as amc

    print(solution(amc.b), amc.b_sol)
    # print(solution(amc.a))
    # print(solution(amc.a2))
    # m1 = [[3, 5, -1], [4, 0, 2], [-6, -3, 2]]
    # m2 = [[2, -2, 3, 1], [5, 0, 7, 8], [9, -4, 1, 1]]

    # # print(*m2, sep='\n')
    # print(*matrix_mul(m1, m2), sep='\n
