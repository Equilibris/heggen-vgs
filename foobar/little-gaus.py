
# | 23
# | 17 24
# | 11 18 25
# |  7 12 19 26
# |  4  8 13 20 27
# |  2  5  9 15 21 28
# |  1  3  6 10 16 22 29

def solution(x, y):
    return x + (x + y - 2) * (x + y - 1) // 2


if __name__ == '__main__':
    print(solution(5, 10), 96)
    print(solution(3, 2), 9)
