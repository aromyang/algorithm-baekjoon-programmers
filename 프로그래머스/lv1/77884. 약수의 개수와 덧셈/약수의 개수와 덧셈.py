import math


def check(n):
    cnt = 0
    for i in range(1, int(math.sqrt(n + 1))):
        if n % i == 0:
            cnt += 1

    cnt *= 2

    if int(math.sqrt(n)) == math.sqrt(n):
        cnt += 1

    return -1 if cnt & 1 else 1


def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        answer += check(i) * i
    return answer
