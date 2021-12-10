
import random
a = [
    [0, 2, 1, 0, 0],  # s0 initial
    [0, 0, 0, 3, 4],  # s1
    [0, 0, 0, 0, 0],  # s2 term
    [0, 0, 0, 0, 0],  # s3 term
    [0, 0, 0, 0, 0]]  # s4 term

a_sol = [7, 6, 8, 21]

a2 = [
    [0, 1, 2, 0, 0],  # s0 initial
    [0, 0, 0, 0, 0],  # s1 term
    [0, 0, 0, 3, 4],  # s2
    [0, 0, 0, 0, 0],  # s3 term
    [0, 0, 0, 0, 0]]  # s4 term


# s1 -- 4/7 --> s4
# s1 -- 3/7 --> s3
# s1 -- 1/1 --> term

# s0 -- 2/3 --> s1
# s0 -- 1/3 --> s2
# s0 -- 1/3 --> term

# p(e of s1) := [0, 3, 4]
# p(e of s0) := [1 * sum(p(s1)), 0, 0] + 2 * p(s1) ++ sum(p(s1))*3

b = [
    [0, 1, 0, 0, 0, 1],  # s0 initial
    [4, 0, 0, 3, 2, 0],  # s1
    [0, 0, 0, 0, 0, 0],  # s2 term
    [0, 0, 0, 0, 0, 0],  # s3 term
    [0, 0, 0, 0, 0, 0],  # s4 term
    [0, 0, 0, 0, 0, 0]]  # s3 term
b_sol = [0, 3, 2, 9, 14]

# s0 -- 1/2 --> s1
# s0 -- 1/2 --> s6
# s0 -- 1/2 --> term

# s1 -- 4/9 --> s0
# s1 -- 3/9 --> s3
# s1 -- 2/9 --> s4
# s1 -- 5/9 --> term

# a * r + a * r^2
# where a = prob to reach state for continuum, r = chance to proceed to term state
#

# p(s0 s0) = p(s0 -> s1) P(s1 -> s0) = 1/2 4/9 = 2/9
# p(s1 s1) = P(s1 -> s0) p(s0 -> s1) = 1/2 4/9 = 2/9


def gen_indexes(s):
    o = []
    for index, i in enumerate(s):
        o += [index]*i
    return o


def approx_sol(m):
    work_matrix = [gen_indexes(i) for i in m]
    is_term = [not any(i) for i in m]

    current_state = [0, 0, 0, 0]

    samples = 1000000
    max_depth = 6

    for i in range(samples):
        d = 0
        state = 0
        while d < max_depth and not is_term[state]:
            state = random.choice(work_matrix[state])

        if is_term[state]:
            current_state[state - 2] += 1

    return [i/samples for i in current_state]


# if __name__ == '__main__':
#     print(*map(lambda x: x[0]-x[1], zip([i/b_sol[-1]
#           for i in b_sol], approx_sol(b))))
