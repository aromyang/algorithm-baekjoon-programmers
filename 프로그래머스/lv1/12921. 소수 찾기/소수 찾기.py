import math


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


def solution(n):
    answer = 0
    for i in range(2, n + 1):
        answer += is_prime(i)
    return answer