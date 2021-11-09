from fractions import Fraction
import numpy


def get_data(l):
    primary_matrix = [[i/sum(x) if sum(x) else 0 for i in x] for x in l]
    return  primary_matrix


def convert_to_markov_parts(m):
    term_states = []
    new_matrix = []
    for (ind, s) in enumerate(m):
        if sum(s) == 0:
            term_states.append(ind)
        else:
            new_matrix.append(s)

    m = new_matrix

    Q = []
    R = []
    for s in m:
        Q_new = []
        R_new = []
        for (ind, x) in enumerate(s):
            if ind in term_states:
                R_new.append(x)
            else:
                Q_new.append(x)
        Q.append(Q_new)
        R.append(R_new)
    return (Q, R)


def reduce_fractions_(arr):
    out = [Fraction(i).limit_denominator(100) for i in arr]

    v = out[0].denominator
    for i in out[1:]:
        v = numpy.lcm(v, i.denominator)
    return [i.numerator * (v // i.denominator) for i in out] + v


def reduce_fractions(arr):
    arr = [Fraction(x).limit_denominator() for x in arr]
    the_lcd = 1
    for x in arr:
        the_lcd = numpy.lcm(the_lcd, x.denominator)
    return [x.numerator * (the_lcd // x.denominator) for x in arr] + [the_lcd]


def solution(m):
    if len(m) < 2:
        return [1, 1]

    primary_matrix = get_data(m)

    _q, _r = convert_to_markov_parts(primary_matrix)

    r = numpy.matrix(_r)
    q = numpy.matrix(_q)

    i = numpy.matrix([[float(j == i) for j in range(len(q))]
                  for i in range(len(q))])

    imq = numpy.subtract(i, q)
    n = imq.I

    out = numpy.dot(n, r)

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
