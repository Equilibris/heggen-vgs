from random import randint
from statistics import mean, median, pvariance

from pylab import plot, xlabel, ylabel, grid, show

dice = lambda: randint(1, 6)


def game():
    while True:
        val = dice()

        if val == 1:
            yield 1
            break
        yield val


def round(itr: int) -> int:
    iScore = 0
    for i, v in enumerate(game()):
        if v == 1:
            return 0
        if i >= itr + 1:
            return iScore
        iScore += v
    return iScore


def roundF(maxPoint: int) -> int:
    iScore = 0
    for v in game():
        if v == 1:
            return 0
        iScore += v
        if iScore >= maxPoint:
            return iScore
    return iScore


if __name__ == '__main__':
    cel = 10

    sfRoundToWin = [[] for i in range(cel)]

    for x in range(cel):
        for _ in range(1000):
            r = 0
            score = 0
            while score < 100:
                score += round(x)
                r += 1
            sfRoundToWin[x].append(r)

    # for x in range(cel):
    #     for _ in range(10000):
    #         r = 0
    #         score = 0
    #         while score < 100:
    #             score += roundF(4 * cel)
    #             r += 1
    #         sfRoundToWin[x].append(r)

    _mean = [mean(e) for e in sfRoundToWin]
    _median = [median(e) for e in sfRoundToWin]
    _min = [min(*e) for e in sfRoundToWin]

    print(_mean)
    print(_median)
    print(_min)

    plot(range(len(_mean)), _mean)
    plot(range(len(_median)), _median)
    plot(range(len(_min)), _min)
    xlabel('count to stop')
    ylabel('avrage round count')

    grid()
    show()
