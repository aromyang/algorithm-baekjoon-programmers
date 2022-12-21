def rank(n):
    if n == 6:
        return 1
    elif n == 5:
        return 2
    elif n == 4:
        return 3
    elif n == 3:
        return 4
    elif n == 2:
        return 5
    else:
        return 6


def solution(lottos, win_nums):
    high = 0
    low = 0

    for l in lottos:
        if l == 0:
            high += 1
        elif l in win_nums:
            high += 1
            low += 1

    return [rank(high), rank(low)]