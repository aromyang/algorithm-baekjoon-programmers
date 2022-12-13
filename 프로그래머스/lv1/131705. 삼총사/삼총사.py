from itertools import combinations


def solution(number):
    comb = list(combinations(number, 3))
    answer = 0

    for c in comb:
        if sum(c) == 0:
            answer += 1

    return answer