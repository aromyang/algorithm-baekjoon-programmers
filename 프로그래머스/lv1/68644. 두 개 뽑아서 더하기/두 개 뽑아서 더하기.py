from itertools import combinations


def solution(numbers):
    answer = []
    for c in combinations(numbers, 2):
        if sum(c) not in answer:
            answer.append(sum(c))  

    return sorted(answer)
