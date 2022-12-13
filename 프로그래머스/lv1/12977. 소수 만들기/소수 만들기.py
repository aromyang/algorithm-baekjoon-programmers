import math
from itertools import combinations


def is_prime(num):
    if num == 2:
        return 1
    elif num == 1:
        return 0
    elif not num & 1:
        return 0
    else:
        for i in range(3, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return 0
    return 1


def solution(nums):
    answer = 0
    for c in combinations(nums, 3):
        answer += is_prime(sum(c))
    return answer
