

options = [(2, 1), (1, 2), (2, -1), (-2, 1),
           (-2, -1), (-1, -2), (-2, 1), (-1, 2)]


def get_xy(cord): return (cord % 8, cord // 8)


def check(
    cord): return cord[0] >= 0 and cord[0] < 8 and cord[1] >= 0 and cord[1] < 8


def get_combinations(cord): return set(
    filter(check, map(lambda x: (cord[0] + x[0], cord[1] + x[1]), options)))


def solution(src, dest):
    start = get_xy(src)
    end = get_xy(dest)

    v = 0

    ls = {start}
    while end not in ls:
        new_ls = set()

        for i in ls:
            new_ls |= get_combinations(i)

        ls = new_ls
        v += 1

    return v


if __name__ == '__main__':
    print(solution(19, 36))
    print(solution(0, 1))
