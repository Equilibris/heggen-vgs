
from colorama import Back
from functools import reduce

from colorama.ansi import Fore


def _solution(start, length):
    v = 0
    el = start

    l_start = length

    while length > 0:
        for i in range(length):
            v ^= el
            el += 1
        el += l_start - length
        length -= 1

    return v


def __solution(start, length):
    v = 0
    for i in range(length):
        init = start + i * length
        l = length - i
        for k in range(init, init + l):
            print(k, end=' ')
            v ^= k
        print()
    return v


def flat_map(f, xs): return [y for ys in xs for y in f(ys)]


def ___solution(start, length):
    return reduce(lambda acc, current: acc ^ current, flat_map(lambda i: range(start + i * length,
                  start + i * length + length - i), range(length)))


def round(start, length, index):
    if index == length:
        return 0

    v = 0

    for i in range(length - index - 1):
        v ^= i + start

    v ^= round(start + length - 1, length, index + 1)

    return v


def solution(start, length):
    return round(start, length, 0)


def print_justified(*args, justification=5, colour=''):
    out = ''

    for arg in args:
        out += str(arg).rjust(justification)
    # out = out.strip()

    print(colour+out+Back.RESET+Fore.RESET)


def xor_to(b):
    v = 0
    for i in range(b+1):
        v ^= i
    return v


# 0^1^2^...^x
def xor_to(x):
    result = [x, 1, x+1, 0]
    return result[(x) % 4]


def xor_between(a, b):
    # xor is associative
    # n ^ n == 0
    # EXAMPLE if 2 ^ 3 ^ 4 is desired
    #   0 ^ 1 ^ 2 ^ 3 ^ 4
    # ^ 0 ^ 1
    # == (0 ^ 0) ^ (1 ^ 1) ^ 2 ^ 3 ^ 4
    # ==                     2 ^ 3 ^ 4
    return xor_to(a) ^ xor_to(b)


def solution(start, length):
    v = 0
    n = start
    l = length
    for i in range(length):
        v ^= xor_between(n-1, n+l-1)

        n += length
        l -= 1

    return v


if __name__ == '__main__':
    print(solution(0, 3))
    print(solution(17, 4))
