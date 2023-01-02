import math


def get_power(n):
    power = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            power += 1
    return power * 2 - 1 if int(math.sqrt(n) + 1) == math.sqrt(n) + 1 else power * 2


def solution(number, limit, power):
    answer = 0
    for i in range(1, number + 1):
        p = get_power(i)
        if p > limit:
            answer += power
        else:
            answer += p

    return answer
