import json


def print_map(r):
    for index, i in enumerate(r):
        print(*i)


def map_ls(r):
    return [[x_index < y_index and not y % x for y_index, y in enumerate(r)] for x_index, x in enumerate(r)]


def flat_map(f, xs): return [y for ys in xs for y in f(ys)]


def sliding_window(xs, sz):
    return [xs[i: i + sz] for i in range(len(xs) - sz + 1)]


def solution(l):
    if len(l) < 3:
        return 0

    sorted_list = l
    mod_map = map_ls(sorted_list)

    print_map(mod_map)

    def walk(index):
        x = 1+index

        value = mod_map[index][x:]

        l = [[index]]
        if any(value):
            for next, should_proceed in enumerate(value):
                if should_proceed:
                    w = walk(next+x)

                    l.extend([[index] + path for path in w])

        return l
    val = flat_map(lambda sub_list: sliding_window(sub_list, 3),
                   flat_map(lambda i: walk(i), range(len(sorted_list)-2)))

    return len(val)

# web solution
def solution(ls):
    c = [0] * len(ls)
    count = 0

    for index, value_at_index in enumerate(ls):
        for j in range(index):
            if not value_at_index % ls[j]:
                c[index] += 1
                count += c[j]
    return count
    # print(f'{index=} {ls[index]=} {j=} {ls[j]=} | {list(zip(ls,c))=} {count=}')


def main():
    # print_map(map_ls([1, 2, 3, 4, 5, 6]))

    # print(solution([1, 4, 6]))

    print(solution([1, 2, 3, 4, 5, 6]))
    print(solution([1, 1, 1]))


if __name__ == '__main__':
    main()
