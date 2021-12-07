import json


def print_map(r):
    for index, i in enumerate(r):
        print(*i)


def map_ls(r):
    return [[x_index != y_index and not y % x for y_index, y in enumerate(r)] for x_index, x in enumerate(r)]


def flat_map(f, xs): return [y for ys in xs for y in f(ys)]


def sliding_window(xs, sz):
    return [xs[i: i + sz] for i in range(len(xs) - sz + 1)]


def solution(l):
    if len(l) < 3:
        return 0

    sorted_list = sorted(l)
    mod_map = map_ls(sorted_list)

    value_map = {}
    for index, i in enumerate(sorted_list):
        value_map.setdefault(i, index)

    def walk(history, index):
        # next_history = {**history, index: True}
        next_history = history.copy()
        next_history[index] = True

        lookup_index = value_map[sorted_list[index]]
        x = 1+lookup_index

        value = mod_map[index][x:]

        l = [[index]]
        if any(value):
            for next, should_proceed in enumerate(value):
                if should_proceed and not next+x in history:
                    w = walk(next_history, next+x)

                    l.extend([[index] + path for path in w])

        return l
    val = flat_map(lambda sub_list: [','.join([str(sorted_list[v]) for v in window]) for window in sliding_window(sub_list, 3)], flat_map(lambda i: walk({i: True}, i), range(len(sorted_list)-2)))

    return len(set(val))


def main():
    # print_map(map_ls([1, 2, 3, 4, 5, 6]))

    print(solution([1, 2, 3, 4, 5, 6]))
    print(solution([1, 1, 1]))


if __name__ == '__main__':
    main()
