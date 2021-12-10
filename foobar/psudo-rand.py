import math


def sort_string(s, rev=False):
    return "".join(sorted(str(s), key=lambda x: int(x), reverse=rev))


def base(n, b):
    s = ""
    for i in range(math.ceil(math.log(n, b)), 0, -1):
        v = int(b**i)

        s += str(n//v)
        n %= v

    s += str(n)

    return s


def solution(n, b):
    d = {n: 0}

    i = 1

    while True:
        asc = sort_string(n)
        dec = sort_string(n, True)

        n = int(dec, b) - int(asc, b)

        v = base(n, b)

        if n in d:
            return i - d[n]
        else:
            d[n] = 1
            i += 1


if __name__ == "__main__":
    print(solution("21002", 3))


def c_solution(data, n):
    count_map = {}

    for i in data:
        if i in count_map:
            count_map[i] += 1
        else:
            count_map[i] = 1

    print(*[i for i in data if count_map[i] <= n], sep=',')


if __name__ == '__main__':
    c_solution([1, 2, 3], 0)

    c_solution([1, 2, 2, 3, 3, 3, 4, 5, 5], 1)
