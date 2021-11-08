from .AMC_shared import *
from fractions import Fraction, gcd


def get_values(matrix):
    '''
        @returns (cycles, terms, sums, actions)
    '''
    sums = [sum(i) for i in matrix]

    cycles = []
    term_states = []
    actions = []
    state_action_map = [[None for i in matrix] for i in sums if i]

    for i in range(len(matrix)):
        if not sums[i]:
            term_states.append(i)

    def iteration(state, prior_states):
        if not sums[state]:
            return
        for index, i in enumerate(matrix[state]):
            if i:
                a = (Fraction(i, sums[state]), state, index)
                state_action_map[state][index] = a
                actions.append(a)
                if index not in prior_states:
                    iteration(index, prior_states + [state])
                else:
                    cycles.append(prior_states + [state])
    iteration(0, [])

    return (cycles, term_states, state_action_map)


def get_cycle_probability(cycle, map):
    frac = Fraction(1)
    for index, i in enumerate(cycle):
        frac *= map[i][cycle[(index + 1) % len(cycle)]][0]

    return frac


def get_cycle_probabilities(cycles, map):
    out = [[] for i in map]

    for cycle in cycles:
        c = get_cycle_probability(cycle, map)

        for i in cycle:
            out[i].append(c)

    return out


def lcm(a, b):
    return abs(a*b) // gcd(a, b)


def solution(matrix):
    cycles, term, map = get_values(matrix)

    fast_term = [i in term for i in range(len(matrix))]

    probability = [Fraction(0, 1) for i in matrix]

    probabilities = get_cycle_probabilities(cycles, map)

    def iteration(actionset, carry, visited):
        for action in actionset:
            if action is not None:

                prob, start, goal = action

                if goal in visited:
                    continue

                if fast_term[goal]:
                    if len(probabilities[start]):
                        for r in probabilities[start]:
                            probability[goal] += (carry*prob / (1-r))
                    else:
                        probability[goal] += carry*prob
                    continue

                iteration(map[goal], carry * prob, visited + [start])
    iteration(map[0], Fraction(1, 1), [])

    out = [probability[i] for i in term]

    v = out[0].denominator
    for i in out[1:]:
        v = lcm(v, i.denominator)

    return [i.numerator * v//i.denominator for i in out] + [v]


if __name__ == '__main__':
    print(solution(b), b_sol)
    print(solution(a), a_sol)
